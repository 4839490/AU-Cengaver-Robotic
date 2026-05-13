#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
global_localization_node.py

Görev:
  GPS + NDT + local_ekf odometrisi → /localization/pose (30-50Hz)
  TF: map → odom

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-2: Bu node map→odom TF üretir
  - FIX-5: yaw standardı ENU — yaw=0 +x(Doğu), pozitif CCW, [-π,π]
  - FIX-6: Sensör: Xsens MTI-680-DK
  - FIX-8: ndt_healthy (bool) + ndt_quality (float) — ndt_score kaldırıldı
  - Simülasyonda: GPS stub + NDT stub kullanılır
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

import math
import numpy as np

from geometry_msgs.msg import TransformStamped
from sensor_msgs.msg import NavSatFix
from tf2_ros import TransformBroadcaster

from localization_msgs.msg import (
    LocalizationPose,
    LocalizationOdometry,
    LocalizationStatus,
    MapOrigin
)


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)

TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1
)


# ─── Lokalizasyon Status Sabitleri ─────────────────────────────────────────
STATUS_OK               = 0
STATUS_GNSS_LOST        = 1
STATUS_IMU_ONLY         = 2
STATUS_LIDAR_ONLY       = 3
STATUS_DEGRADED         = 4
STATUS_RELOCALIZING     = 5
STATUS_LOST             = 6

# ─── Pose Source Sabitleri ─────────────────────────────────────────────────
SOURCE_GPS_IMU_LIDAR    = 0
SOURCE_IMU_LIDAR        = 1
SOURCE_IMU_ONLY         = 2
SOURCE_LIDAR_ONLY       = 3
SOURCE_DEAD_RECKONING   = 4


class GlobalLocalizationNode(Node):
    """
    GPS + NDT + local_ekf odometrisi ile global konum tahmini üretir.
    Simülasyonda GPS ve NDT stub olarak çalışır.
    """

    def __init__(self):
        super().__init__('global_localization_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('publish_hz', 30.0)
        self.declare_parameter('gps_topic', '/fix')
        self.declare_parameter('valid_until_ms', 300)
        self.declare_parameter('ndt_healthy_threshold', 0.5)
        self.declare_parameter('confidence_degraded_threshold', 0.5)

        self.publish_hz        = self.get_parameter('publish_hz').value
        self.gps_topic         = self.get_parameter('gps_topic').value
        self.valid_until_ms    = self.get_parameter('valid_until_ms').value
        self.ndt_threshold     = self.get_parameter('ndt_healthy_threshold').value
        self.conf_degraded     = self.get_parameter('confidence_degraded_threshold').value

        # ─── Map Origin ────────────────────────────────────────────────────
        self.map_origin_locked = False
        self.lat_ref           = 0.0
        self.lon_ref           = 0.0
        self.yaw_ref           = 0.0
        self.R_earth           = 6371000.0   # metre

        # ─── Durum ─────────────────────────────────────────────────────────
        self.x   = 0.0
        self.y   = 0.0
        self.yaw = 0.0
        self.linear_velocity  = 0.0
        self.angular_velocity = 0.0

        self.position_covariance = 1.0
        self.heading_covariance  = 1.0
        self.velocity_covariance = 1.0
        self.localization_confidence = 0.0

        self.ndt_healthy = False
        self.ndt_quality = 0.0
        self.gps_available = False
        self.map_odom_stable = False

        self.last_gps_time  = None
        self.last_odom_time = None

        # ─── TF Broadcaster ────────────────────────────────────────────────
        self.tf_broadcaster = TransformBroadcaster(self)

        # ─── Publishers ────────────────────────────────────────────────────
        self.pose_pub = self.create_publisher(
            LocalizationPose,
            '/localization/pose',
            RELIABLE_QOS
        )

        self.status_pub = self.create_publisher(
            LocalizationStatus,
            '/localization/status',
            RELIABLE_QOS
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        self.gps_sub = self.create_subscription(
            NavSatFix,
            self.gps_topic,
            self.gps_callback,
            RELIABLE_QOS
        )

        self.odom_sub = self.create_subscription(
            LocalizationOdometry,
            '/localization/odometry',
            self.odom_callback,
            RELIABLE_QOS
        )

        self.map_origin_sub = self.create_subscription(
            MapOrigin,
            '/localization/map_origin',
            self.map_origin_callback,
            TRANSIENT_QOS
        )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.pose_timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_pose
        )

        self.status_timer = self.create_timer(
            0.1,   # 10Hz
            self.publish_status
        )

        self.get_logger().info('global_localization_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def gps_callback(self, msg: NavSatFix):
        """GPS fix gelince map frame'e dönüştür."""
        now = self.get_clock().now()
        self.last_gps_time = now

        if not self.map_origin_locked:
            self.get_logger().warn(
                'GPS geldi ama map_origin henüz kilitlenmedi.',
                throttle_duration_sec=5.0
            )
            return

        # GPS fix kalitesi kontrolü
        if msg.status.status < 0:
            self.gps_available = False
            return

        self.gps_available = True

        # Lat/lon → map(x,y) — Equirectangular projeksiyon (FIX-5)
        x, y = self._latlon_to_map(msg.latitude, msg.longitude)

        # GPS kovaryansı
        if msg.position_covariance_type > 0:
            self.position_covariance = msg.position_covariance[0]
        else:
            self.position_covariance = 2.0   # GPS fix yok → yüksek belirsizlik

        # Konumu güncelle
        self.x = x
        self.y = y
        self._update_confidence()

    def odom_callback(self, msg: LocalizationOdometry):
        """local_ekf odometrisi gelince hız ve yaw güncelle."""
        self.last_odom_time = self.get_clock().now()

        self.yaw              = msg.yaw
        self.linear_velocity  = msg.linear_velocity
        self.angular_velocity = msg.angular_velocity
        self.heading_covariance  = msg.heading_covariance
        self.velocity_covariance = msg.velocity_covariance

        # GPS yoksa dead reckoning ile konum güncelle
        if not self.gps_available and self.map_origin_locked:
            dt = 1.0 / self.publish_hz
            self.x += msg.linear_velocity * math.cos(msg.yaw) * dt
            self.y += msg.linear_velocity * math.sin(msg.yaw) * dt
            self.position_covariance += 0.01   # drift birikimi

        self._update_confidence()

    def map_origin_callback(self, msg: MapOrigin):
        """Map origin gelince referans noktayı kaydet."""
        if msg.locked:
            self.lat_ref           = msg.lat_ref
            self.lon_ref           = msg.lon_ref
            self.yaw_ref           = msg.yaw_ref
            self.map_origin_locked = True
            self.get_logger().info(
                f'Map origin kilitlendi: lat={self.lat_ref:.6f}, '
                f'lon={self.lon_ref:.6f}'
            )

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_pose(self):
        """30-50Hz pose yayını + map→odom TF."""
        now = self.get_clock().now()

        # ── Pose mesajı ─────────────────────────────────────────────────
        msg = LocalizationPose()
        msg.header.stamp    = now.to_msg()
        msg.header.frame_id = 'map'
        msg.age_ms          = 0
        msg.valid_until_ms  = self.valid_until_ms

        msg.x   = self.x
        msg.y   = self.y
        msg.yaw = self.yaw

        msg.linear_velocity  = self.linear_velocity
        msg.angular_velocity = self.angular_velocity

        msg.source = self._determine_source()
        msg.localization_confidence = self.localization_confidence
        msg.position_covariance     = self.position_covariance
        msg.heading_covariance      = self.heading_covariance
        msg.velocity_covariance     = self.velocity_covariance

        self.pose_pub.publish(msg)

        # ── TF: map → odom ──────────────────────────────────────────────
        # FIX-2: Bu TF'yi global_localization_node üretir
        t = TransformStamped()
        t.header.stamp    = now.to_msg()
        t.header.frame_id = 'map'
        t.child_frame_id  = 'odom'

        # map→odom farkı (basit implementasyon: odom origin = map origin)
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        t.transform.rotation.x    = 0.0
        t.transform.rotation.y    = 0.0
        t.transform.rotation.z    = 0.0
        t.transform.rotation.w    = 1.0

        self.tf_broadcaster.sendTransform(t)

    def publish_status(self):
        """10Hz lokalizasyon status yayını."""
        now = self.get_clock().now()

        msg = LocalizationStatus()
        msg.header.stamp   = now.to_msg()
        msg.age_ms         = 0
        msg.valid_until_ms = 300

        msg.status = self._determine_status()
        msg.localization_confidence = self.localization_confidence
        msg.position_covariance     = self.position_covariance
        msg.heading_covariance      = self.heading_covariance

        # FIX-8: ndt_healthy bool + ndt_quality float
        msg.ndt_healthy  = self.ndt_healthy
        msg.ndt_quality  = self.ndt_quality
        msg.map_odom_stable = self.map_odom_stable
        msg.map_odom_drift  = 0.0

        msg.gps_available   = self.gps_available
        msg.imu_available   = self.last_odom_time is not None
        msg.lidar_available = False   # NDT stub

        self.status_pub.publish(msg)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    def _latlon_to_map(self, lat: float, lon: float):
        """
        Lat/lon → map frame (x, y) metre cinsinden.
        Equirectangular projeksiyon — FIX-5 ENU standardı.
        x = R · cos(lat_ref) · Δlon · π/180
        y = R · Δlat · π/180
        """
        dlat = lat - self.lat_ref
        dlon = lon - self.lon_ref

        x = self.R_earth * math.cos(math.radians(self.lat_ref)) \
            * math.radians(dlon)
        y = self.R_earth * math.radians(dlat)

        return x, y

    def _determine_source(self) -> int:
        """Lokalizasyon kaynağını belirle."""
        if self.gps_available and self.ndt_healthy:
            return SOURCE_GPS_IMU_LIDAR
        elif self.ndt_healthy:
            return SOURCE_IMU_LIDAR
        elif self.gps_available:
            return SOURCE_GPS_IMU_LIDAR
        elif self.last_odom_time is not None:
            return SOURCE_IMU_ONLY
        else:
            return SOURCE_DEAD_RECKONING

    def _determine_status(self) -> int:
        """Lokalizasyon durumunu belirle."""
        if not self.map_origin_locked:
            return STATUS_RELOCALIZING

        if self.localization_confidence < 0.1:
            return STATUS_LOST

        if not self.gps_available and not self.ndt_healthy:
            return STATUS_IMU_ONLY

        if self.localization_confidence < self.conf_degraded:
            return STATUS_DEGRADED

        if not self.gps_available:
            return STATUS_GNSS_LOST

        return STATUS_OK

    def _update_confidence(self):
        """Lokalizasyon güvenini güncelle."""
        cov = self.position_covariance

        if cov < 0.1:
            self.localization_confidence = 1.0
        elif cov < 0.5:
            self.localization_confidence = 0.8
        elif cov < 1.0:
            self.localization_confidence = 0.6
        elif cov < 2.0:
            self.localization_confidence = 0.4
        else:
            self.localization_confidence = 0.2

        self.map_odom_stable = cov < 1.0

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle


# ───────────────────────────────────────────────────────────────────────────
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