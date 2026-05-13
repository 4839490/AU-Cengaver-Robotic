#!/usr/bin/env python3
from typing import Tuple
"""
AU Cengaver Robotics — TEKNOFEST 2026
global_localization_node.py

Görev:
  GPS + local_ekf odometrisi + NDT stub → /localization/pose
  TF: map → odom
"""

import math

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
    qos_profile_sensor_data,
)

from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import NavSatFix
from tf2_ros import TransformBroadcaster

from localization_msgs.msg import (
    LocalizationPose,
    LocalizationOdometry,
    LocalizationStatus,
    MapOrigin,
)


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)

TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1,
)


# ─── Localization Status Sabitleri ─────────────────────────────────────────
STATUS_OK = 0
STATUS_GNSS_LOST = 1
STATUS_IMU_ONLY = 2
STATUS_LIDAR_ONLY = 3
STATUS_DEGRADED = 4
STATUS_RELOCALIZING = 5
STATUS_LOST = 6

# ─── Pose Source Sabitleri ─────────────────────────────────────────────────
SOURCE_GPS_IMU_LIDAR = 0
SOURCE_IMU_LIDAR = 1
SOURCE_IMU_ONLY = 2
SOURCE_LIDAR_ONLY = 3
SOURCE_DEAD_RECKONING = 4

# ─── Timeout Eşikleri ──────────────────────────────────────────────────────
GPS_TIMEOUT_S = 1.0
ODOM_TIMEOUT_S = 0.5


class GlobalLocalizationNode(Node):
    """
    Global localization node.

    Üretir:
      /localization/pose
      /localization/status
      TF map → odom
    """

    def __init__(self):
        super().__init__('global_localization_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('sim', True)
        self.declare_parameter('publish_hz', 30.0)
        self.declare_parameter('gps_topic', '/fix')
        self.declare_parameter('valid_until_ms', 300)
        self.declare_parameter('ndt_healthy_threshold', 0.5)
        self.declare_parameter('confidence_degraded_threshold', 0.5)

        self.sim = bool(self.get_parameter('sim').value)
        self.publish_hz = float(self.get_parameter('publish_hz').value)
        self.gps_topic = str(self.get_parameter('gps_topic').value)
        self.valid_until_ms = int(self.get_parameter('valid_until_ms').value)
        self.ndt_threshold = float(
            self.get_parameter('ndt_healthy_threshold').value
        )
        self.conf_degraded = float(
            self.get_parameter('confidence_degraded_threshold').value
        )

        if self.publish_hz <= 0.0:
            self.get_logger().warn(
                f'Geçersiz publish_hz={self.publish_hz}, 30Hz yapılacak.'
            )
            self.publish_hz = 30.0

        if self.valid_until_ms <= 0:
            self.valid_until_ms = 300

        # ─── Map Origin ────────────────────────────────────────────────────
        self.map_origin_locked = False
        self.lat_ref = 0.0
        self.lon_ref = 0.0
        self.yaw_ref = 0.0
        self.r_earth = 6371000.0

        # ─── Pose State ────────────────────────────────────────────────────
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0

        self.position_covariance = 10.0
        self.heading_covariance = 10.0
        self.velocity_covariance = 10.0

        self.localization_confidence = 0.0

        self.ndt_healthy = False
        self.ndt_quality = 0.0
        self.gps_available = False
        self.odom_available = False
        self.map_odom_stable = False

        self.last_gps_time = None
        self.last_odom_time = None

        # Dead reckoning için son update zamanı
        self.last_dr_time = self.get_clock().now()

        # ─── TF Broadcaster ────────────────────────────────────────────────
        self.tf_broadcaster = TransformBroadcaster(self)

        # ─── Publishers ────────────────────────────────────────────────────
        self.pose_pub = self.create_publisher(
            LocalizationPose,
            '/localization/pose',
            RELIABLE_QOS,
        )

        self.status_pub = self.create_publisher(
            LocalizationStatus,
            '/localization/status',
            RELIABLE_QOS,
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        # GPS genelde BEST_EFFORT olabilir, bu yüzden sensor_data QoS daha uyumlu.
        self.gps_sub = self.create_subscription(
            NavSatFix,
            self.gps_topic,
            self.gps_callback,
            qos_profile_sensor_data,
        )

        self.odom_sub = self.create_subscription(
            LocalizationOdometry,
            '/localization/odometry',
            self.odom_callback,
            RELIABLE_QOS,
        )

        self.map_origin_sub = self.create_subscription(
            MapOrigin,
            '/localization/map_origin',
            self.map_origin_callback,
            TRANSIENT_QOS,
        )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.pose_timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_pose,
        )

        self.status_timer = self.create_timer(
            0.1,
            self.publish_status,
        )

        self.get_logger().info('global_localization_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def gps_callback(self, msg: NavSatFix) -> None:
        """GPS fix gelince map frame'e dönüştür."""
        now = self.get_clock().now()
        self.last_gps_time = now

        if not self.map_origin_locked:
            self.get_logger().warn(
                'GPS geldi ama map_origin henüz kilitlenmedi.',
                throttle_duration_sec=5.0,
            )
            return

        if msg.status.status < 0:
            self.gps_available = False
            return

        if not math.isfinite(msg.latitude) or not math.isfinite(msg.longitude):
            self.gps_available = False
            self.get_logger().warn(
                'GPS lat/lon geçersiz geldi.',
                throttle_duration_sec=5.0,
            )
            return

        self.gps_available = True

        x, y = self._latlon_to_map(
            lat=float(msg.latitude),
            lon=float(msg.longitude),
        )

        self.x = x
        self.y = y

        if msg.position_covariance_type > 0:
            cov = float(msg.position_covariance[0])
            self.position_covariance = cov if math.isfinite(cov) else 2.0
        else:
            self.position_covariance = 2.0

        self._update_confidence()

    def odom_callback(self, msg: LocalizationOdometry) -> None:
        """local_ekf odometrisi gelince hız/yaw günceller."""
        now = self.get_clock().now()
        self.last_odom_time = now
        self.odom_available = True

        self.yaw = self._normalize_angle(float(getattr(msg, 'yaw', 0.0)))
        self.linear_velocity = float(getattr(msg, 'linear_velocity', 0.0))
        self.angular_velocity = float(getattr(msg, 'angular_velocity', 0.0))

        self.heading_covariance = float(
            getattr(msg, 'heading_covariance', 1.0)
        )
        self.velocity_covariance = float(
            getattr(msg, 'velocity_covariance', 1.0)
        )

        if not math.isfinite(self.linear_velocity):
            self.linear_velocity = 0.0

        if not math.isfinite(self.angular_velocity):
            self.angular_velocity = 0.0

        if not math.isfinite(self.heading_covariance):
            self.heading_covariance = 1.0

        if not math.isfinite(self.velocity_covariance):
            self.velocity_covariance = 1.0

        # GPS yoksa kısa süreli dead reckoning
        if not self.gps_available and self.map_origin_locked:
            dt = self._duration_sec(self.last_dr_time, now)
            self.last_dr_time = now

            dt = max(0.0, min(0.2, dt))

            self.x += self.linear_velocity * math.cos(self.yaw) * dt
            self.y += self.linear_velocity * math.sin(self.yaw) * dt
            self.position_covariance += 0.02 * max(1.0, dt * self.publish_hz)

        self._update_confidence()

    def map_origin_callback(self, msg: MapOrigin) -> None:
        """Map origin gelince referansı kaydeder."""
        if not msg.locked:
            return

        self.lat_ref = float(msg.lat_ref)
        self.lon_ref = float(msg.lon_ref)
        self.yaw_ref = self._normalize_angle(float(msg.yaw_ref))
        self.map_origin_locked = True

        self.get_logger().info(
            f'Map origin kilitlendi: '
            f'lat={self.lat_ref:.6f}, lon={self.lon_ref:.6f}, '
            f'yaw_ref={self.yaw_ref:.3f}'
        )

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_pose(self) -> None:
        """Pose yayını + map→odom TF yayını."""
        self._refresh_availability()

        now = self.get_clock().now()

        msg = LocalizationPose()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.x = float(self.x)
        msg.y = float(self.y)
        msg.yaw = float(self._normalize_angle(self.yaw))

        msg.linear_velocity = float(self.linear_velocity)
        msg.angular_velocity = float(self.angular_velocity)

        msg.position_covariance = float(self.position_covariance)
        msg.heading_covariance = float(self.heading_covariance)
        msg.velocity_covariance = float(self.velocity_covariance)

        msg.source = int(self._determine_source())
        msg.localization_confidence = float(self.localization_confidence)

        if hasattr(msg, 'age_ms'):
            msg.age_ms = 0

        if hasattr(msg, 'valid_until_ms'):
            msg.valid_until_ms = int(self.valid_until_ms)

        self.pose_pub.publish(msg)

        self._publish_map_to_odom_tf(now)

    def publish_status(self) -> None:
        """10Hz localization status yayını."""
        self._refresh_availability()

        now = self.get_clock().now()

        msg = LocalizationStatus()
        msg.header.stamp = now.to_msg()

        if hasattr(msg.header, 'frame_id'):
            msg.header.frame_id = 'map'

        msg.status = int(self._determine_status())

        msg.localization_confidence = float(self.localization_confidence)
        msg.position_covariance = float(self.position_covariance)
        msg.heading_covariance = float(self.heading_covariance)

        msg.ndt_healthy = bool(self.ndt_healthy)
        msg.ndt_quality = float(self.ndt_quality)

        msg.map_odom_stable = bool(self.map_odom_stable)
        msg.map_odom_drift = 0.0

        msg.gps_available = bool(self.gps_available)
        msg.imu_available = bool(self.odom_available)
        msg.lidar_available = bool(self.ndt_healthy)

        if hasattr(msg, 'age_ms'):
            msg.age_ms = 0

        if hasattr(msg, 'valid_until_ms'):
            msg.valid_until_ms = int(self.valid_until_ms)

        self.status_pub.publish(msg)

    def _publish_map_to_odom_tf(self, now) -> None:
        """
        TF: map → odom.

        Bu MVP sürümde odom origin map origin ile çakışıyor kabul edilir.
        Gerçek sistemde global pose ile local odom arasındaki fark burada hesaplanır.
        """
        t = TransformStamped()
        t.header.stamp = now.to_msg()
        t.header.frame_id = 'map'
        t.child_frame_id = 'odom'

        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0

        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(t)

    # ───────────────────────────────────────────────────────────────────────
    # HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _latlon_to_map(self, lat: float, lon: float) -> Tuple[float, float]:
        """
        Lat/lon → map frame ENU x/y.
        """
        dlat = float(lat) - self.lat_ref
        dlon = float(lon) - self.lon_ref

        x = (
            self.r_earth
            * math.cos(math.radians(self.lat_ref))
            * math.radians(dlon)
        )
        y = self.r_earth * math.radians(dlat)

        return x, y

    def _determine_source(self) -> int:
        if self.gps_available and self.ndt_healthy:
            return SOURCE_GPS_IMU_LIDAR

        if self.ndt_healthy:
            return SOURCE_IMU_LIDAR

        if self.gps_available and self.odom_available:
            return SOURCE_GPS_IMU_LIDAR

        if self.odom_available:
            return SOURCE_IMU_ONLY

        return SOURCE_DEAD_RECKONING

    def _determine_status(self) -> int:
        if not self.map_origin_locked:
            return STATUS_RELOCALIZING

        if not self.odom_available and not self.gps_available:
            return STATUS_LOST

        if self.localization_confidence < 0.1:
            return STATUS_LOST

        if self.odom_available and not self.gps_available and not self.ndt_healthy:
            return STATUS_IMU_ONLY

        if self.localization_confidence < self.conf_degraded:
            return STATUS_DEGRADED

        if not self.gps_available:
            return STATUS_GNSS_LOST

        return STATUS_OK

    def _update_confidence(self) -> None:
        cov = float(self.position_covariance)

        if not math.isfinite(cov):
            cov = 10.0
            self.position_covariance = cov

        if cov < 0.1:
            confidence = 1.0
        elif cov < 0.5:
            confidence = 0.8
        elif cov < 1.0:
            confidence = 0.6
        elif cov < 2.0:
            confidence = 0.4
        else:
            confidence = 0.2

        if not self.map_origin_locked:
            confidence = 0.0

        if not self.odom_available and not self.gps_available:
            confidence = 0.0

        self.localization_confidence = max(0.0, min(1.0, confidence))
        self.map_odom_stable = self.localization_confidence >= self.conf_degraded

    def _refresh_availability(self) -> None:
        now = self.get_clock().now()

        if self.last_gps_time is None:
            self.gps_available = False
        else:
            self.gps_available = (
                self._duration_sec(self.last_gps_time, now) <= GPS_TIMEOUT_S
            )

        if self.last_odom_time is None:
            self.odom_available = False
        else:
            self.odom_available = (
                self._duration_sec(self.last_odom_time, now) <= ODOM_TIMEOUT_S
            )

        self._update_confidence()

    @staticmethod
    def _duration_sec(t0, t1) -> float:
        return (t1.nanoseconds - t0.nanoseconds) / 1e9

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))


def main(args=None):
    rclpy.init(args=args)

    node = GlobalLocalizationNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
