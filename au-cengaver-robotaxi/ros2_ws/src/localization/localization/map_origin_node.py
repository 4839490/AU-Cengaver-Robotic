#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
map_origin_node.py

/localization/map_origin yayınlar.
QoS: TRANSIENT_LOCAL
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

from sensor_msgs.msg import NavSatFix
from localization_msgs.msg import MapOrigin


TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1,
)


class MapOriginNode(Node):
    """
    Map frame referans noktasını yayınlar.

    source:
      config_file → parametrelerden sabit origin
      gps_fix     → ilk geçerli GPS fix origin olur
    """

    def __init__(self):
        super().__init__('map_origin_node')

        self.declare_parameter('source', 'config_file')
        self.declare_parameter('lat_ref', 40.789949)
        self.declare_parameter('lon_ref', 29.508726)
        self.declare_parameter('alt_ref', 85.2)
        self.declare_parameter('yaw_ref', 0.0)
        self.declare_parameter('gps_topic', '/fix')
        self.declare_parameter('publish_hz', 1.0)

        self.source = str(self.get_parameter('source').value)
        self.lat_ref = float(self.get_parameter('lat_ref').value)
        self.lon_ref = float(self.get_parameter('lon_ref').value)
        self.alt_ref = float(self.get_parameter('alt_ref').value)
        self.yaw_ref = self._normalize_angle(
            float(self.get_parameter('yaw_ref').value)
        )
        self.gps_topic = str(self.get_parameter('gps_topic').value)
        self.publish_hz = float(self.get_parameter('publish_hz').value)

        if self.source not in ('config_file', 'gps_fix'):
            self.get_logger().error(
                f'Geçersiz source={self.source}. '
                'Geçerli değerler: config_file, gps_fix'
            )
            raise ValueError(f'Invalid source: {self.source}')

        if self.publish_hz <= 0.0:
            self.get_logger().warn(
                f'Geçersiz publish_hz={self.publish_hz}, 1.0 Hz yapılacak.'
            )
            self.publish_hz = 1.0

        self.locked = False
        self.published_count = 0
        self.slow_timer_started = False
        self.slow_timer = None

        self.origin_pub = self.create_publisher(
            MapOrigin,
            '/localization/map_origin',
            TRANSIENT_QOS,
        )

        if self.source == 'gps_fix':
            self.gps_sub = self.create_subscription(
                NavSatFix,
                self.gps_topic,
                self.gps_callback,
                qos_profile_sensor_data,
            )

            self.get_logger().info(
                f'map_origin_node gps_fix modunda. '
                f'İlk geçerli GPS fix bekleniyor: {self.gps_topic}'
            )

        else:
            self.locked = True

            self.get_logger().info(
                f'map_origin_node config_file modunda: '
                f'lat_ref={self.lat_ref:.6f}, '
                f'lon_ref={self.lon_ref:.6f}, '
                f'alt_ref={self.alt_ref:.2f}, '
                f'yaw_ref={self.yaw_ref:.3f}'
            )

        self.timer = self.create_timer(
            1.0 / self.publish_hz,
            self.publish_origin,
        )

        self.get_logger().info('map_origin_node başlatıldı.')

    def gps_callback(self, msg: NavSatFix) -> None:
        """İlk geçerli GPS fix gelince origin kilitler."""
        if self.locked:
            return

        if msg.status.status < 0:
            self.get_logger().warn(
                'GPS fix yok, map origin için bekleniyor...',
                throttle_duration_sec=5.0,
            )
            return

        if not math.isfinite(msg.latitude) or not math.isfinite(msg.longitude):
            self.get_logger().warn(
                'GPS lat/lon geçersiz, map origin için bekleniyor...',
                throttle_duration_sec=5.0,
            )
            return

        self.lat_ref = float(msg.latitude)
        self.lon_ref = float(msg.longitude)

        if math.isfinite(msg.altitude):
            self.alt_ref = float(msg.altitude)
        else:
            self.get_logger().warn(
                'GPS altitude NaN geldi, mevcut alt_ref korunuyor.',
                throttle_duration_sec=5.0,
            )

        self.locked = True

        self.get_logger().info(
            f'GPS fix alındı, map origin kilitlendi: '
            f'lat_ref={self.lat_ref:.6f}, '
            f'lon_ref={self.lon_ref:.6f}, '
            f'alt_ref={self.alt_ref:.2f}, '
            f'yaw_ref={self.yaw_ref:.3f}'
        )

    def publish_origin(self) -> None:
        """Map origin mesajını yayınlar."""
        if not self.locked:
            self.get_logger().info(
                'Map origin henüz kilitlenmedi, bekleniyor...',
                throttle_duration_sec=5.0,
            )
            return

        now = self.get_clock().now()

        msg = MapOrigin()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.lat_ref = float(self.lat_ref)
        msg.lon_ref = float(self.lon_ref)
        msg.alt_ref = float(self.alt_ref)
        msg.yaw_ref = float(self.yaw_ref)
        msg.source = str(self.source)
        msg.locked = bool(self.locked)

        self.origin_pub.publish(msg)
        self.published_count += 1

        if self.published_count == 1:
            self.get_logger().info(
                f'Map origin yayınlandı: '
                f'lat_ref={self.lat_ref:.6f}, '
                f'lon_ref={self.lon_ref:.6f}, '
                f'alt_ref={self.alt_ref:.2f}, '
                f'yaw_ref={self.yaw_ref:.3f}, '
                f'source={self.source}, '
                f'locked={self.locked}'
            )

        if self.published_count >= 10 and not self.slow_timer_started:
            self.timer.cancel()

            self.slow_timer = self.create_timer(
                10.0,
                self.publish_origin,
            )

            self.slow_timer_started = True

            self.get_logger().info(
                'Map origin ilk yayınları tamamlandı. '
                'Yayın periyodu 10 saniyeye düşürüldü.'
            )

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))


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
