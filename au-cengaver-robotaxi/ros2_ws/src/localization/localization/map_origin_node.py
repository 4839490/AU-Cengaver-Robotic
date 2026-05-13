#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
map_origin_node.py

Görev:
  /localization/map_origin yayınlar — lat_ref, lon_ref, yaw_ref, locked
  TRANSIENT_LOCAL QoS (latching) — bir kez yayınlanır, geç bağlananlar alır

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-3: map_origin topic eklendi
  - FIX-5: yaw standardı ENU — yaw=0 +x(Doğu), pozitif CCW, [-π,π]
  - Planner locked=true olana kadar GeoJSON waypoint işlemez
  - Simülasyonda: config dosyasından sabit değer okunur
"""

import math
import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, ReliabilityPolicy, DurabilityPolicy,
    HistoryPolicy, qos_profile_sensor_data
)

from sensor_msgs.msg import NavSatFix
from localization_msgs.msg import MapOrigin


# ─── QoS ───────────────────────────────────────────────────────────────────
TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1
)


class MapOriginNode(Node):
    """
    Map frame referans noktasını yayınlar.

    İki mod:
      1. config_file: parametre dosyasından sabit lat/lon okur (simülasyon)
      2. gps_fix: ilk GPS fix'i referans alır (gerçek araç)
    """

    def __init__(self):
        super().__init__('map_origin_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('source',    'config_file')
        self.declare_parameter('lat_ref',    40.789949)
        self.declare_parameter('lon_ref',    29.508726)
        self.declare_parameter('alt_ref',    85.2)
        self.declare_parameter('yaw_ref',    0.0)
        self.declare_parameter('gps_topic', '/fix')
        self.declare_parameter('publish_hz', 1.0)

        self.source     = self.get_parameter('source').value
        self.lat_ref    = self.get_parameter('lat_ref').value
        self.lon_ref    = self.get_parameter('lon_ref').value
        self.alt_ref    = self.get_parameter('alt_ref').value
        self.publish_hz = self.get_parameter('publish_hz').value
        self.gps_topic  = self.get_parameter('gps_topic').value

        # FIX-5: yaw_ref normalize et
        self.yaw_ref = self._normalize_angle(
            self.get_parameter('yaw_ref').value
        )

        # source doğrulama
        if self.source not in ['config_file', 'gps_fix']:
            self.get_logger().error(
                f'Geçersiz source parametresi: {self.source}. '
                'Geçerli değerler: config_file, gps_fix'
            )
            raise ValueError(f'Invalid source: {self.source}')

        # ─── Durum ─────────────────────────────────────────────────────────
        self.locked             = False
        self.published_count    = 0
        self.slow_timer_started = False
        self.slow_timer         = None

        # ─── Publisher ─────────────────────────────────────────────────────
        self.origin_pub = self.create_publisher(
            MapOrigin,
            '/localization/map_origin',
            TRANSIENT_QOS
        )

        # ─── GPS Subscriber (gps_fix modu için) ────────────────────────────
        if self.source == 'gps_fix':
            # FIX: sensor_data QoS — GPS publisher BEST_EFFORT olabilir
            self.gps_sub = self.create_subscription(
                NavSatFix,
                self.gps_topic,
                self.gps_callback,
                qos_profile_sensor_data
            )
            self.get_logger().info(
                'map_origin_node GPS modunda — ilk fix bekleniyor.'
            )
        else:
            # config_file modu: hemen kilitle
            self.locked = True
            self.get_logger().info(
                f'map_origin_node config modunda — '
                f'lat={self.lat_ref}, lon={self.lon_ref}'
            )

        # ─── Timer ─────────────────────────────────────────────────────────
        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_origin
        )

        self.get_logger().info('map_origin_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def gps_callback(self, msg: NavSatFix):
        """İlk GPS fix gelince referans noktayı kilitle."""
        if self.locked:
            return

        if msg.status.status < 0:
            self.get_logger().warn(
                'GPS fix kalitesi yetersiz, bekleniyor...',
                throttle_duration_sec=5.0
            )
            return

        self.lat_ref = msg.latitude
        self.lon_ref = msg.longitude
        self.alt_ref = msg.altitude
        self.locked  = True

        self.get_logger().info(
            f'GPS fix alındı, map origin kilitlendi: '
            f'lat={self.lat_ref:.6f}, lon={self.lon_ref:.6f}, '
            f'yaw_ref={self.yaw_ref:.3f} rad (parametreden)'
        )

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def publish_origin(self):
        """Map origin yayınla."""
        if not self.locked:
            self.get_logger().info(
                'Map origin henüz kilitlenmedi, bekleniyor...',
                throttle_duration_sec=5.0
            )
            return

        now = self.get_clock().now()

        msg = MapOrigin()
        msg.header.stamp    = now.to_msg()
        msg.header.frame_id = 'map'

        msg.lat_ref = self.lat_ref
        msg.lon_ref = self.lon_ref
        msg.alt_ref = self.alt_ref
        msg.yaw_ref = self.yaw_ref
        msg.locked  = self.locked

        self.origin_pub.publish(msg)
        self.published_count += 1

        if self.published_count == 1:
            self.get_logger().info(
                f'Map origin yayınlandı: '
                f'lat={self.lat_ref:.6f}, '
                f'lon={self.lon_ref:.6f}, '
                f'locked={self.locked}'
            )

        # FIX: slow_timer_started bayrağı — tekrar timer oluşturma
        if self.published_count >= 10 and not self.slow_timer_started:
            self.timer.cancel()
            self.slow_timer = self.create_timer(
                10.0,
                self.publish_origin
            )
            self.slow_timer_started = True

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
    node = MapOriginNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()