#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
local_ekf_node.py

Görev:
  IMU + tekerlek encoder → /localization/odometry
  TF: odom → base_link
"""

import math

import numpy as np

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
    qos_profile_sensor_data,
)

from sensor_msgs.msg import Imu, JointState
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

from localization_msgs.msg import LocalizationOdometry


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)


class LocalEkfNode(Node):
    """
    IMU + encoder verisiyle kısa vadeli odometri üretir.

    State:
      [x, y, yaw, vx, wz]
    """

    def __init__(self):
        super().__init__('local_ekf_node')

        # ─── Parameters ────────────────────────────────────────────────────
        self.declare_parameter('publish_hz', 50.0)
        self.declare_parameter('imu_topic', '/imu/data')
        self.declare_parameter('joint_states_topic', '/joint_states')
        self.declare_parameter('wheel_radius', 0.3)
        self.declare_parameter('wheelbase', 2.40)
        self.declare_parameter('valid_until_ms', 200)

        self.publish_hz = float(self.get_parameter('publish_hz').value)
        self.imu_topic = str(self.get_parameter('imu_topic').value)
        self.joint_topic = str(self.get_parameter('joint_states_topic').value)
        self.wheel_radius = float(self.get_parameter('wheel_radius').value)
        self.wheelbase = float(self.get_parameter('wheelbase').value)
        self.valid_until_ms = int(self.get_parameter('valid_until_ms').value)

        if self.publish_hz <= 0.0:
            self.get_logger().warn(
                f'Geçersiz publish_hz={self.publish_hz}, 50Hz yapılacak.'
            )
            self.publish_hz = 50.0

        if self.wheel_radius <= 0.0:
            self.get_logger().warn(
                f'Geçersiz wheel_radius={self.wheel_radius}, 0.3m yapılacak.'
            )
            self.wheel_radius = 0.3

        if self.wheelbase <= 0.0:
            self.get_logger().warn(
                f'Geçersiz wheelbase={self.wheelbase}, 2.40m yapılacak.'
            )
            self.wheelbase = 2.40

        if self.valid_until_ms <= 0:
            self.valid_until_ms = 200

        # ─── EKF State ─────────────────────────────────────────────────────
        self.state = np.zeros(5, dtype=float)
        self.P = np.eye(5, dtype=float) * 0.1

        self.Q = np.diag([0.01, 0.01, 0.001, 0.1, 0.01])
        self.R_encoder = np.diag([0.05])

        # ─── Time / Sensor State ───────────────────────────────────────────
        self.last_imu_time = None
        self.last_joint_time = None

        self.latest_speed = 0.0
        self.has_encoder_speed = False

        # ─── TF Broadcaster ────────────────────────────────────────────────
        self.tf_broadcaster = TransformBroadcaster(self)

        # ─── Publisher ─────────────────────────────────────────────────────
        self.odom_pub = self.create_publisher(
            LocalizationOdometry,
            '/localization/odometry',
            RELIABLE_QOS,
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        self.imu_sub = self.create_subscription(
            Imu,
            self.imu_topic,
            self.imu_callback,
            qos_profile_sensor_data,
        )

        self.joint_sub = self.create_subscription(
            JointState,
            self.joint_topic,
            self.joint_callback,
            RELIABLE_QOS,
        )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_odometry,
        )

        self.get_logger().info('local_ekf_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def imu_callback(self, msg: Imu) -> None:
        """IMU angular velocity ile predict adımı."""
        now = self.get_clock().now()

        if self.last_imu_time is None:
            self.last_imu_time = now
            return

        dt = (now.nanoseconds - self.last_imu_time.nanoseconds) / 1e9
        self.last_imu_time = now

        if dt <= 0.0 or dt > 0.5:
            return

        wz = float(msg.angular_velocity.z)

        if not math.isfinite(wz):
            return

        self._ekf_predict(dt=dt, wz=wz)

    def joint_callback(self, msg: JointState) -> None:
        """JointState üzerinden tekerlek hızını hesaplar."""
        self.last_joint_time = self.get_clock().now()

        speed = self._extract_wheel_speed(msg)

        if speed is None:
            return

        self.latest_speed = speed
        self.has_encoder_speed = True

        self._ekf_update_encoder(speed)

    # ───────────────────────────────────────────────────────────────────────
    # EKF
    # ───────────────────────────────────────────────────────────────────────

    def _ekf_predict(self, dt: float, wz: float) -> None:
        """Basit kinematik predict."""
        x, y, yaw, vx, _ = self.state

        yaw = self._normalize_angle(yaw)

        new_x = x + vx * math.cos(yaw) * dt
        new_y = y + vx * math.sin(yaw) * dt
        new_yaw = self._normalize_angle(yaw + wz * dt)
        new_vx = vx
        new_wz = wz

        self.state = np.array(
            [new_x, new_y, new_yaw, new_vx, new_wz],
            dtype=float,
        )

        F = np.eye(5)
        F[0, 2] = -vx * math.sin(yaw) * dt
        F[0, 3] = math.cos(yaw) * dt
        F[1, 2] = vx * math.cos(yaw) * dt
        F[1, 3] = math.sin(yaw) * dt
        F[2, 4] = dt

        self.P = F @ self.P @ F.T + self.Q
        self.P = self._stabilize_covariance(self.P)

    def _ekf_update_encoder(self, measured_vx: float) -> None:
        """Encoder hız ölçümü ile update."""
        if not math.isfinite(measured_vx):
            return

        H = np.array([[0.0, 0.0, 0.0, 1.0, 0.0]])
        z = np.array([measured_vx], dtype=float)

        innovation = z - H @ self.state
        S = H @ self.P @ H.T + self.R_encoder

        try:
            K = self.P @ H.T @ np.linalg.inv(S)
        except np.linalg.LinAlgError:
            self.get_logger().warn(
                'EKF update atlandı: S matrisi singular.',
                throttle_duration_sec=2.0,
            )
            return

        self.state = self.state + (K @ innovation).flatten()
        self.state[2] = self._normalize_angle(self.state[2])

        I = np.eye(5)
        self.P = (I - K @ H) @ self.P
        self.P = self._stabilize_covariance(self.P)

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_odometry(self) -> None:
        """Odometry mesajı ve odom → base_link TF yayınlar."""
        now = self.get_clock().now()

        x, y, yaw, vx, wz = self.state
        yaw = self._normalize_angle(yaw)

        msg = LocalizationOdometry()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'odom'

        msg.x = float(x)
        msg.y = float(y)
        msg.yaw = float(yaw)

        msg.linear_velocity = float(vx)
        msg.angular_velocity = float(wz)

        msg.position_covariance = float(max(self.P[0, 0], self.P[1, 1]))
        msg.heading_covariance = float(self.P[2, 2])
        msg.velocity_covariance = float(self.P[3, 3])

        if hasattr(msg, 'age_ms'):
            msg.age_ms = 0

        if hasattr(msg, 'valid_until_ms'):
            msg.valid_until_ms = int(self.valid_until_ms)

        self.odom_pub.publish(msg)
        self._publish_odom_to_base_link_tf(now, x, y, yaw)

    def _publish_odom_to_base_link_tf(
        self,
        now,
        x: float,
        y: float,
        yaw: float,
    ) -> None:
        """TF: odom → base_link."""
        t = TransformStamped()
        t.header.stamp = now.to_msg()
        t.header.frame_id = 'odom'
        t.child_frame_id = 'base_link'

        t.transform.translation.x = float(x)
        t.transform.translation.y = float(y)
        t.transform.translation.z = 0.0

        qz = math.sin(yaw / 2.0)
        qw = math.cos(yaw / 2.0)

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = qz
        t.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(t)

    # ───────────────────────────────────────────────────────────────────────
    # HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _extract_wheel_speed(self, msg: JointState):
        """JointState içinden sol/sağ arka teker hızını m/s olarak çıkarır."""
        if not msg.name or not msg.velocity:
            return None

        vl = None
        vr = None

        velocity_len = len(msg.velocity)

        for i, name in enumerate(msg.name):
            if i >= velocity_len:
                break

            wheel_angular_speed = float(msg.velocity[i])

            if not math.isfinite(wheel_angular_speed):
                continue

            linear_speed = wheel_angular_speed * self.wheel_radius
            name_l = name.lower()

            if (
                'rear_left' in name_l
                or 'left_rear' in name_l
                or 'left_wheel' in name_l
                or 'rl_wheel' in name_l
            ):
                vl = linear_speed

            elif (
                'rear_right' in name_l
                or 'right_rear' in name_l
                or 'right_wheel' in name_l
                or 'rr_wheel' in name_l
            ):
                vr = linear_speed

        if vl is not None and vr is not None:
            return (vl + vr) / 2.0

        if vl is not None:
            return vl

        if vr is not None:
            return vr

        # Fallback: velocity listesindeki ilk sonlu değeri kullan
        for v in msg.velocity:
            v = float(v)
            if math.isfinite(v):
                return v * self.wheel_radius

        return None

    @staticmethod
    def _stabilize_covariance(P):
        """Kovaryans matrisini simetrik ve pozitif diyagonal yapar."""
        P = 0.5 * (P + P.T)

        for i in range(P.shape[0]):
            if not math.isfinite(float(P[i, i])) or P[i, i] < 1e-9:
                P[i, i] = 1e-9

        return P

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))


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
