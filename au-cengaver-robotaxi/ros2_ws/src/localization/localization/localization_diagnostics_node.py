#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
localization_diagnostics_node.py

Görev:
  Lokalizasyon node'larının sağlık durumunu izler
  /localization/diagnostics topic'ine yayınlar — 1-2Hz

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-9: valid_until_ms eklendi
  - FIX-8: ndt_healthy + ndt_quality izlenir
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
)

from localization_msgs.msg import (
    LocalizationOdometry,
    LocalizationStatus,
    LocalizationDiagnostics
)


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)


class LocalizationDiagnosticsNode(Node):
    """
    Lokalizasyon topic'lerini izler ve diagnostik yayınlar.
    """

    def __init__(self):
        super().__init__('localization_diagnostics_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('publish_hz',     1.0)
        self.declare_parameter('valid_until_ms', 2000)
        self.declare_parameter('odom_timeout_s', 0.1)    # 10Hz beklenir
        self.declare_parameter('status_timeout_s', 0.2)  # 5Hz beklenir

        self.publish_hz       = self.get_parameter('publish_hz').value
        self.valid_until_ms   = self.get_parameter('valid_until_ms').value
        self.odom_timeout_s   = self.get_parameter('odom_timeout_s').value
        self.status_timeout_s = self.get_parameter('status_timeout_s').value

        # ─── İzleme Değişkenleri ───────────────────────────────────────────
        self.last_odom_time   = None
        self.last_status_time = None

        self.odom_msg_count   = 0
        self.status_msg_count = 0
        self.last_count_time  = self.get_clock().now()

        self.odom_hz   = 0.0
        self.status_hz = 0.0

        # Status'tan gelen değerler
        self.ndt_healthy         = False
        self.ndt_quality         = 0.0
        self.map_odom_stable     = False
        self.position_covariance = 99.9
        self.heading_covariance  = 99.9

        # Odometry'den gelen değerler
        self.ekf_latency_ms = 0.0

        # ─── Publisher ─────────────────────────────────────────────────────
        self.diag_pub = self.create_publisher(
            LocalizationDiagnostics,
            '/localization/diagnostics',
            RELIABLE_QOS
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        self.odom_sub = self.create_subscription(
            LocalizationOdometry,
            '/localization/odometry',
            self.odom_callback,
            RELIABLE_QOS
        )

        self.status_sub = self.create_subscription(
            LocalizationStatus,
            '/localization/status',
            self.status_callback,
            RELIABLE_QOS
        )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_diagnostics
        )

        # Hz hesaplama timer — her saniye
        self.hz_timer = self.create_timer(
            1.0,
            self.calculate_hz
        )

        self.get_logger().info('localization_diagnostics_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def odom_callback(self, msg: LocalizationOdometry):
        """Odometry gelince timestamp ve sayaç güncelle."""
        now = self.get_clock().now()

        # Gecikme hesapla
        msg_stamp_ns = msg.header.stamp.sec * 1e9 + msg.header.stamp.nanosec
        now_ns       = now.nanoseconds
        self.ekf_latency_ms = (now_ns - msg_stamp_ns) * 1e-6

        self.last_odom_time = now
        self.odom_msg_count += 1

    def status_callback(self, msg: LocalizationStatus):
        """Status gelince değerleri güncelle."""
        now = self.get_clock().now()
        self.last_status_time = now
        self.status_msg_count += 1

        self.ndt_healthy         = msg.ndt_healthy
        self.ndt_quality         = msg.ndt_quality
        self.map_odom_stable     = msg.map_odom_stable
        self.position_covariance = msg.position_covariance
        self.heading_covariance  = msg.heading_covariance

    # ───────────────────────────────────────────────────────────────────────
    # HZ HESAPLAMA
    # ───────────────────────────────────────────────────────────────────────

    def calculate_hz(self):
        """Her saniye Hz hesapla ve sayaçları sıfırla."""
        self.odom_hz   = float(self.odom_msg_count)
        self.status_hz = float(self.status_msg_count)

        self.odom_msg_count   = 0
        self.status_msg_count = 0

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_diagnostics(self):
        """1-2Hz diagnostik yayını."""
        now = self.get_clock().now()

        msg = LocalizationDiagnostics()
        msg.header.stamp    = now.to_msg()
        msg.age_ms          = 0
        msg.valid_until_ms  = self.valid_until_ms

        # ── Frekans bilgisi ──────────────────────────────────────────────
        msg.ekf_output_hz  = self.odom_hz
        msg.gps_input_hz   = 0.0    # GPS node ayrı izlenir
        msg.imu_input_hz   = 0.0    # IMU node ayrı izlenir
        msg.ndt_output_hz  = 0.0    # NDT stub

        # ── Gecikme ──────────────────────────────────────────────────────
        msg.ekf_latency_ms = self.ekf_latency_ms
        msg.ndt_latency_ms = 0.0    # NDT stub

        # ── Kalite ───────────────────────────────────────────────────────
        msg.position_covariance = self.position_covariance
        msg.heading_covariance  = self.heading_covariance
        msg.ndt_quality         = self.ndt_quality

        # ── Sağlık ───────────────────────────────────────────────────────
        msg.ekf_healthy      = self._check_ekf_healthy(now)
        msg.gps_healthy      = False   # GPS node ayrı izlenir
        msg.imu_healthy      = self._check_ekf_healthy(now)  # EKF üzerinden
        msg.ndt_healthy      = self.ndt_healthy
        msg.map_odom_stable  = self.map_odom_stable

        # ── Warning flags ────────────────────────────────────────────────
        msg.warning_flags = self._collect_warnings(now)

        self.diag_pub.publish(msg)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    def _check_ekf_healthy(self, now) -> bool:
        """EKF sağlıklı mı? — son odom zamanına göre."""
        if self.last_odom_time is None:
            return False
        elapsed = (now - self.last_odom_time).nanoseconds * 1e-9
        return elapsed < self.odom_timeout_s * 3

    def _collect_warnings(self, now) -> list:
        """Uyarı listesi oluştur."""
        warnings = []

        # EKF timeout
        if self.last_odom_time is None:
            warnings.append('EKF_NO_DATA')
        else:
            elapsed = (now - self.last_odom_time).nanoseconds * 1e-9
            if elapsed > self.odom_timeout_s * 3:
                warnings.append('EKF_TIMEOUT')

        # Status timeout
        if self.last_status_time is None:
            warnings.append('STATUS_NO_DATA')
        else:
            elapsed = (now - self.last_status_time).nanoseconds * 1e-9
            if elapsed > self.status_timeout_s * 3:
                warnings.append('STATUS_TIMEOUT')

        # Düşük Hz
        if self.odom_hz > 0 and self.odom_hz < 30.0:
            warnings.append(f'LOW_EKF_HZ:{self.odom_hz:.1f}')

        # Yüksek kovaryans
        if self.position_covariance > 2.0:
            warnings.append('HIGH_POSITION_COV')

        if self.heading_covariance > 0.1:
            warnings.append('HIGH_HEADING_COV')

        # NDT sağlıksız
        if not self.ndt_healthy:
            warnings.append('NDT_UNHEALTHY')

        return warnings


# ───────────────────────────────────────────────────────────────────────────
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