#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
local_ekf_node.py

Görev:
  IMU (400Hz) + tekerlek encoder → /localization/odometry (50Hz)
  TF: odom → base_link

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-1: Bu node odom→base_link TF üretir (Controller değil)
  - FIX-5: yaw standardı ENU — yaw=0 +x(Doğu), pozitif CCW, [-π,π]
  - Simülasyonda: /imu/data + /joint_states kullanılır
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

import math
import numpy as np

from std_msgs.msg import Header
from sensor_msgs.msg import Imu, JointState
from geometry_msgs.msg import TransformStamped

from tf2_ros import TransformBroadcaster

from localization_msgs.msg import LocalizationOdometry


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)


class LocalEkfNode(Node):
    """
    IMU + encoder verisiyle kısa vadeli odometri üretir.
    EKF predict: IMU ile, update: encoder ile.
    """

    def __init__(self):
        super().__init__('local_ekf_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('publish_hz', 50.0)
        self.declare_parameter('imu_topic', '/imu/data')
        self.declare_parameter('joint_states_topic', '/joint_states')
        self.declare_parameter('wheel_radius', 0.3)       # metre (TBD kalibrasyon)
        self.declare_parameter('wheelbase', 2.40)         # metre — vehicle_params.yaml
        self.declare_parameter('valid_until_ms', 200)

        self.publish_hz     = self.get_parameter('publish_hz').value
        self.imu_topic      = self.get_parameter('imu_topic').value
        self.joint_topic    = self.get_parameter('joint_states_topic').value
        self.wheel_radius   = self.get_parameter('wheel_radius').value
        self.wheelbase      = self.get_parameter('wheelbase').value
        self.valid_until_ms = self.get_parameter('valid_until_ms').value

        # ─── EKF Durum Vektörü: [x, y, yaw, vx, wz] ───────────────────────
        self.state = np.zeros(5)   # [x, y, yaw, vx, wz]
        self.P     = np.eye(5) * 0.1  # kovaryans matrisi

        # Proses gürültüsü
        self.Q = np.diag([0.01, 0.01, 0.001, 0.1, 0.01])
        # Ölçüm gürültüsü
        self.R_imu     = np.diag([0.01, 0.01])   # [ax, wz]
        self.R_encoder = np.diag([0.05])           # [vx]

        # ─── Zaman ─────────────────────────────────────────────────────────
        self.last_time       = self.get_clock().now()
        self.last_imu_time   = None
        self.last_joint_time = None

        # ─── Sensor verisi ─────────────────────────────────────────────────
        self.latest_imu   = None
        self.latest_speed = 0.0   # encoder'dan hesaplanan hız

        # ─── TF Broadcaster ────────────────────────────────────────────────
        self.tf_broadcaster = TransformBroadcaster(self)

        # ─── Publisher ─────────────────────────────────────────────────────
        self.odom_pub = self.create_publisher(
            LocalizationOdometry,
            '/localization/odometry',
            RELIABLE_QOS
        )

        # ─── Subscriber ────────────────────────────────────────────────────
        self.imu_sub = self.create_subscription(
            Imu,
            self.imu_topic,
            self.imu_callback,
            RELIABLE_QOS
        )

        self.joint_sub = self.create_subscription(
            JointState,
            self.joint_topic,
            self.joint_callback,
            RELIABLE_QOS
        )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_odometry
        )

        self.get_logger().info('local_ekf_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def imu_callback(self, msg: Imu):
        """IMU verisi gelince EKF predict adımı."""
        now = self.get_clock().now()

        if self.last_imu_time is None:
            self.last_imu_time = now
            self.latest_imu = msg
            return

        dt = (now - self.last_imu_time).nanoseconds * 1e-9
        self.last_imu_time = now
        self.latest_imu = msg

        if dt <= 0 or dt > 0.5:
            return

        # IMU'dan angular velocity (yaw rate)
        wz = msg.angular_velocity.z

        # EKF Predict
        self._ekf_predict(dt, wz)

    def joint_callback(self, msg: JointState):
        """
        Encoder verisi: /joint_states üzerinden tekerlek hızı.
        Simülasyonda rear wheel velocity kullanılır.
        """
        now = self.get_clock().now()
        self.last_joint_time = now

        # Tekerlek isimlerini bul
        try:
            # Simülasyonda wheel joint isimleri değişebilir
            # 'rear_left_wheel' veya 'rear_right_wheel' aranır
            vl = vr = None
            for i, name in enumerate(msg.name):
                if 'rear_left' in name or 'left_wheel' in name:
                    vl = msg.velocity[i] * self.wheel_radius
                elif 'rear_right' in name or 'right_wheel' in name:
                    vr = msg.velocity[i] * self.wheel_radius

            if vl is not None and vr is not None:
                self.latest_speed = (vl + vr) / 2.0
            elif vl is not None:
                self.latest_speed = vl
            elif vr is not None:
                self.latest_speed = vr

        except (IndexError, AttributeError):
            pass

        # EKF Update — encoder
        self._ekf_update_encoder(self.latest_speed)

    # ───────────────────────────────────────────────────────────────────────
    # EKF
    # ───────────────────────────────────────────────────────────────────────

    def _ekf_predict(self, dt: float, wz: float):
        """EKF tahmin adımı — kinematik model."""
        x, y, yaw, vx, _ = self.state

        # Durum geçiş
        new_x   = x   + vx * math.cos(yaw) * dt
        new_y   = y   + vx * math.sin(yaw) * dt
        new_yaw = self._normalize_angle(yaw + wz * dt)
        new_vx  = vx   # sabit hız modeli
        new_wz  = wz

        self.state = np.array([new_x, new_y, new_yaw, new_vx, new_wz])

        # Jacobian
        F = np.eye(5)
        F[0, 2] = -vx * math.sin(yaw) * dt
        F[0, 3] =  math.cos(yaw) * dt
        F[1, 2] =  vx * math.cos(yaw) * dt
        F[1, 3] =  math.sin(yaw) * dt
        F[2, 4] =  dt

        # Kovaryans güncelle
        self.P = F @ self.P @ F.T + self.Q

    def _ekf_update_encoder(self, measured_vx: float):
        """EKF güncelleme adımı — encoder hızı."""
        # Ölçüm modeli: H = [0, 0, 0, 1, 0]
        H = np.array([[0, 0, 0, 1, 0]])
        z = np.array([measured_vx])
        y = z - H @ self.state
        S = H @ self.P @ H.T + self.R_encoder
        K = self.P @ H.T @ np.linalg.inv(S)

        self.state = self.state + K.flatten() * y[0]
        self.state[2] = self._normalize_angle(self.state[2])
        self.P = (np.eye(5) - K @ H) @ self.P

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_odometry(self):
        """50Hz odometri yayını + TF."""
        now = self.get_clock().now()

        x, y, yaw, vx, wz = self.state

        # ── Odometry mesajı ─────────────────────────────────────────────
        msg = LocalizationOdometry()
        msg.header.stamp    = now.to_msg()
        msg.header.frame_id = 'odom'
        msg.age_ms          = 0
        msg.valid_until_ms  = self.valid_until_ms

        msg.x                = x
        msg.y                = y
        msg.yaw              = yaw
        msg.linear_velocity  = vx
        msg.angular_velocity = wz

        msg.position_covariance = float(self.P[0, 0])
        msg.heading_covariance  = float(self.P[2, 2])
        msg.velocity_covariance = float(self.P[3, 3])

        self.odom_pub.publish(msg)

        # ── TF: odom → base_link ────────────────────────────────────────
        # FIX-1: Bu TF'yi local_ekf_node üretir
        t = TransformStamped()
        t.header.stamp    = now.to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id  = 'base_link'

        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0

        # yaw → quaternion
        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(t)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle


# ───────────────────────────────────────────────────────────────────────────
def main(args=None):
    rclpy.init(args=args)
    node = LocalEkfNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()