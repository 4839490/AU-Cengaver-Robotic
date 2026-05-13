#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
raw_gps_node.py

Görev:
  GPS ham verisini /localization/raw_gps topic'ine yayınlar.
  Debug ve rosbag kayıt amaçlıdır.

Not:
  Planner bu topic'i okumaz.
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
from localization_msgs.msg import RawGps


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)


class RawGpsNode(Node):
    """
    NavSatFix mesajını localization_msgs/RawGps mesajına dönüştürür.
    """

    def __init__(self):
        super().__init__('raw_gps_node')

        self.declare_parameter('gps_topic', '/fix')
        self.declare_parameter('gps_frame', 'gps_frame')
        self.declare_parameter('valid_until_ms', 200)

        self.gps_topic = str(self.get_parameter('gps_topic').value)
        self.gps_frame = str(self.get_parameter('gps_frame').value)
        self.valid_until_ms = int(self.get_parameter('valid_until_ms').value)

        if self.valid_until_ms <= 0:
            self.valid_until_ms = 200

        self.raw_gps_pub = self.create_publisher(
            RawGps,
            '/localization/raw_gps',
            RELIABLE_QOS,
        )

        self.gps_sub = self.create_subscription(
            NavSatFix,
            self.gps_topic,
            self.gps_callback,
            qos_profile_sensor_data,
        )

        self.get_logger().info(
            f'raw_gps_node başlatıldı: '
            f'{self.gps_topic} → /localization/raw_gps'
        )

    def gps_callback(self, msg: NavSatFix) -> None:
        """GPS fix gelince RawGps mesajına dönüştürür."""
        now = self.get_clock().now()

        raw = RawGps()

        # Eğer gelen GPS stamp geçerliyse onu kullan, değilse node zamanını bas.
        if msg.header.stamp.sec != 0 or msg.header.stamp.nanosec != 0:
            raw.header.stamp = msg.header.stamp
        else:
            raw.header.stamp = now.to_msg()

        raw.header.frame_id = msg.header.frame_id if msg.header.frame_id else self.gps_frame

        raw.latitude = self._safe_float(msg.latitude, 0.0)
        raw.longitude = self._safe_float(msg.longitude, 0.0)
        raw.altitude = self._safe_float(msg.altitude, 0.0)

        raw.speed = 0.0
        raw.heading_deg = 0.0

        raw.hdop = self._estimate_hdop(msg)
        raw.vdop = 99.9

        raw.fix_type = self._map_fix_type(int(msg.status.status))

        if hasattr(raw, 'age_ms'):
            raw.age_ms = 0

        if hasattr(raw, 'valid_until_ms'):
            raw.valid_until_ms = int(self.valid_until_ms)

        self.raw_gps_pub.publish(raw)

    def _estimate_hdop(self, msg: NavSatFix) -> float:
        """
        NavSatFix position_covariance üzerinden yaklaşık HDOP üretir.
        Gerçek GPS sürücüsünde HDOP doğrudan gelirse ayrı alanla beslenebilir.
        """
        if msg.position_covariance_type <= 0:
            return 99.9

        try:
            cov_x = float(msg.position_covariance[0])
            cov_y = float(msg.position_covariance[4])

            if not math.isfinite(cov_x) or not math.isfinite(cov_y):
                return 99.9

            cov_x = max(0.0, cov_x)
            cov_y = max(0.0, cov_y)

            # Basit yaklaşık: yatay std / 5.0
            horizontal_std = math.sqrt((cov_x + cov_y) / 2.0)
            hdop = horizontal_std / 5.0

            return max(0.5, min(hdop, 99.9))

        except Exception:
            return 99.9

    @staticmethod
    def _map_fix_type(status: int) -> int:
        """
        NavSatFix status → RawGps fix_type dönüşümü.

        NavSatFix:
          -1 = no fix
           0 = fix
           1 = SBAS fix
           2 = GBAS fix

        RawGps:
          0 = FIX_NONE
          1 = FIX_GPS
          2 = FIX_DGPS
          4 = FIX_RTK_FLOAT
          5 = FIX_RTK_FIXED
        """
        if status < 0:
            return 0

        if status == 0:
            return 1

        if status == 1:
            return 2

        if status == 2:
            return 5

        return 1

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

    node = RawGpsNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
