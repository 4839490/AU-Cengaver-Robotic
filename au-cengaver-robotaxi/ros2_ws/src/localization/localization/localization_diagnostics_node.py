#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
localization_diagnostics_node.py

Görev:
  Localization node sağlık durumunu izler.
  /localization/diagnostics topic'ine yayınlar.
"""

import math

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
)

from localization_msgs.msg import (
    LocalizationOdometry,
    LocalizationStatus,
    LocalizationDiagnostics,
)


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)


class LocalizationDiagnosticsNode(Node):
    """
    /localization/odometry ve /localization/status topic'lerini izler.
    Sağlık, Hz, latency ve warning bilgisi yayınlar.
    """

    def __init__(self):
        super().__init__('localization_diagnostics_node')

        # ─── Parameters ────────────────────────────────────────────────────
        self.declare_parameter('publish_hz', 1.0)
        self.declare_parameter('valid_until_ms', 2000)
        self.declare_parameter('odom_timeout_s', 0.2)
        self.declare_parameter('status_timeout_s', 0.5)
        self.declare_parameter('ndt_required', False)

        self.publish_hz = float(self.get_parameter('publish_hz').value)
        self.valid_until_ms = int(self.get_parameter('valid_until_ms').value)
        self.odom_timeout_s = float(self.get_parameter('odom_timeout_s').value)
        self.status_timeout_s = float(self.get_parameter('status_timeout_s').value)
        self.ndt_required = bool(self.get_parameter('ndt_required').value)

        if self.publish_hz <= 0.0:
            self.get_logger().warn(
                f'Geçersiz publish_hz={self.publish_hz}, 1Hz yapılacak.'
            )
            self.publish_hz = 1.0

        if self.valid_until_ms <= 0:
            self.valid_until_ms = 2000

        if self.odom_timeout_s <= 0.0:
            self.odom_timeout_s = 0.2

        if self.status_timeout_s <= 0.0:
            self.status_timeout_s = 0.5

        # ─── Watch State ───────────────────────────────────────────────────
        self.last_odom_time = None
        self.last_status_time = None

        self.odom_msg_count = 0
        self.status_msg_count = 0

        self.odom_hz = 0.0
        self.status_hz = 0.0

        # LocalizationStatus değerleri
        self.ndt_healthy = False
        self.ndt_quality = 0.0
        self.map_odom_stable = False

        self.position_covariance = 99.9
        self.heading_covariance = 99.9

        self.gps_available = False
        self.imu_available = False
        self.lidar_available = False

        # Odometry latency
        self.ekf_latency_ms = 0.0

        # ─── Publisher ─────────────────────────────────────────────────────
        self.diag_pub = self.create_publisher(
            LocalizationDiagnostics,
            '/localization/diagnostics',
            RELIABLE_QOS,
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        self.odom_sub = self.create_subscription(
            LocalizationOdometry,
            '/localization/odometry',
            self.odom_callback,
            RELIABLE_QOS,
        )

        self.status_sub = self.create_subscription(
            LocalizationStatus,
            '/localization/status',
            self.status_callback,
            RELIABLE_QOS,
        )

        # ─── Timers ────────────────────────────────────────────────────────
        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_diagnostics,
        )

        self.hz_timer = self.create_timer(
            1.0,
            self.calculate_hz,
        )

        self.get_logger().info('localization_diagnostics_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def odom_callback(self, msg: LocalizationOdometry) -> None:
        now = self.get_clock().now()

        self.last_odom_time = now
        self.odom_msg_count += 1

        msg_stamp_ns = (
            int(msg.header.stamp.sec) * 1_000_000_000
            + int(msg.header.stamp.nanosec)
        )

        now_ns = now.nanoseconds

        if msg_stamp_ns > 0:
            latency_ms = (now_ns - msg_stamp_ns) / 1e6
            self.ekf_latency_ms = max(0.0, float(latency_ms))
        else:
            self.ekf_latency_ms = 0.0

    def status_callback(self, msg: LocalizationStatus) -> None:
        now = self.get_clock().now()

        self.last_status_time = now
        self.status_msg_count += 1

        self.ndt_healthy = bool(getattr(msg, 'ndt_healthy', False))
        self.ndt_quality = self._safe_float(getattr(msg, 'ndt_quality', 0.0), 0.0)
        self.map_odom_stable = bool(getattr(msg, 'map_odom_stable', False))

        self.position_covariance = self._safe_float(
            getattr(msg, 'position_covariance', 99.9),
            99.9,
        )

        self.heading_covariance = self._safe_float(
            getattr(msg, 'heading_covariance', 99.9),
            99.9,
        )

        self.gps_available = bool(getattr(msg, 'gps_available', False))
        self.imu_available = bool(getattr(msg, 'imu_available', False))
        self.lidar_available = bool(getattr(msg, 'lidar_available', False))

    # ───────────────────────────────────────────────────────────────────────
    # HZ
    # ───────────────────────────────────────────────────────────────────────

    def calculate_hz(self) -> None:
        self.odom_hz = float(self.odom_msg_count)
        self.status_hz = float(self.status_msg_count)

        self.odom_msg_count = 0
        self.status_msg_count = 0

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_diagnostics(self) -> None:
        now = self.get_clock().now()

        msg = LocalizationDiagnostics()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        # Frekans
        msg.ekf_output_hz = float(self.odom_hz)
        msg.gps_input_hz = 0.0
        msg.imu_input_hz = 0.0
        msg.ndt_output_hz = 0.0

        # Gecikme
        msg.ekf_latency_ms = float(self.ekf_latency_ms)
        msg.ndt_latency_ms = 0.0

        # Kalite
        msg.position_covariance = float(self.position_covariance)
        msg.heading_covariance = float(self.heading_covariance)
        msg.ndt_quality = float(self.ndt_quality)

        # Sağlık
        msg.ekf_healthy = self._check_ekf_healthy(now)
        msg.gps_healthy = bool(self.gps_available)
        msg.imu_healthy = bool(self.imu_available or msg.ekf_healthy)
        msg.ndt_healthy = bool(self.ndt_healthy)
        msg.map_odom_stable = bool(self.map_odom_stable)

        if not self.ndt_required:
            # MVP/sim için NDT zorunlu değilse genel diagnostikte NDT eksikliği kritik sayılmaz.
            msg.ndt_healthy = bool(self.ndt_healthy)

        msg.warning_flags = self._collect_warnings(now)

        if hasattr(msg, 'age_ms'):
            msg.age_ms = 0

        if hasattr(msg, 'valid_until_ms'):
            msg.valid_until_ms = int(self.valid_until_ms)

        self.diag_pub.publish(msg)

    # ───────────────────────────────────────────────────────────────────────
    # HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _check_ekf_healthy(self, now) -> bool:
        if self.last_odom_time is None:
            return False

        elapsed = self._duration_sec(self.last_odom_time, now)
        return elapsed <= self.odom_timeout_s

    def _check_status_healthy(self, now) -> bool:
        if self.last_status_time is None:
            return False

        elapsed = self._duration_sec(self.last_status_time, now)
        return elapsed <= self.status_timeout_s

    def _collect_warnings(self, now) -> list:
        warnings = []

        if self.last_odom_time is None:
            warnings.append('EKF_NO_DATA')
        else:
            elapsed = self._duration_sec(self.last_odom_time, now)
            if elapsed > self.odom_timeout_s:
                warnings.append('EKF_TIMEOUT')

        if self.last_status_time is None:
            warnings.append('STATUS_NO_DATA')
        else:
            elapsed = self._duration_sec(self.last_status_time, now)
            if elapsed > self.status_timeout_s:
                warnings.append('STATUS_TIMEOUT')

        if 0.0 < self.odom_hz < 30.0:
            warnings.append(f'LOW_EKF_HZ:{self.odom_hz:.1f}')

        if 0.0 < self.status_hz < 5.0:
            warnings.append(f'LOW_STATUS_HZ:{self.status_hz:.1f}')

        if self.ekf_latency_ms > 100.0:
            warnings.append(f'HIGH_EKF_LATENCY:{self.ekf_latency_ms:.1f}ms')

        if self.position_covariance > 2.0:
            warnings.append('HIGH_POSITION_COV')

        if self.heading_covariance > 0.1:
            warnings.append('HIGH_HEADING_COV')

        if self.ndt_required and not self.ndt_healthy:
            warnings.append('NDT_UNHEALTHY')

        if not self.map_odom_stable:
            warnings.append('MAP_ODOM_UNSTABLE')

        if not self.gps_available:
            warnings.append('GPS_UNAVAILABLE')

        return warnings

    @staticmethod
    def _duration_sec(t0, t1) -> float:
        return max(0.0, (t1.nanoseconds - t0.nanoseconds) / 1e9)

    @staticmethod
    def _safe_float(value, fallback: float = 0.0) -> float:
        try:
            value = float(value)
        except Exception:
            return fallback

        if not math.isfinite(value):
            return fallback

        return value


def main(args=None):
    rclpy.init(args=args)

    node = LocalizationDiagnosticsNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
