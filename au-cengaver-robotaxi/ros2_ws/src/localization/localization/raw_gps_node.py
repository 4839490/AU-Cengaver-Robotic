#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
raw_gps_node.py

Görev:
  GPS ham verisini /localization/raw_gps topic'ine yayınlar
  Debug ve rosbag kayıt amaçlıdır

Sözleşme: Localization ↔ Planner Contract v1.2
  - FIX-7: Planner bu topic'i OKUMAZ — sadece debug/rosbag
  - FIX-9: valid_until_ms eklendi
  - Simülasyonda: /fix topic'ini dinler
"""

import math
import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, ReliabilityPolicy, DurabilityPolicy,
    HistoryPolicy, qos_profile_sensor_data
)

from sensor_msgs.msg import NavSatFix
from localization_msgs.msg import RawGps


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)


class RawGpsNode(Node):
    """
    GPS ham verisini RawGps mesajına dönüştürür ve yayınlar.
    PLANNER BU TOPIC'İ OKUMAZ — sadece debug/rosbag içindir.
    """

    def __init__(self):
        super().__init__('raw_gps_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('gps_topic',     '/fix')
        self.declare_parameter('valid_until_ms', 200)

        self.gps_topic      = self.get_parameter('gps_topic').value
        self.valid_until_ms = self.get_parameter('valid_until_ms').value

        # ─── Publisher ─────────────────────────────────────────────────────
        self.raw_gps_pub = self.create_publisher(
            RawGps,
            '/localization/raw_gps',
            RELIABLE_QOS
        )

        # ─── Subscriber ────────────────────────────────────────────────────
        # sensor_data QoS — GPS publisher BEST_EFFORT olabilir
        self.gps_sub = self.create_subscription(
            NavSatFix,
            self.gps_topic,
            self.gps_callback,
            qos_profile_sensor_data
        )

        self.get_logger().info(
            f'raw_gps_node başlatıldı. '
            f'Topic: {self.gps_topic} → /localization/raw_gps'
        )

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ───────────────────────────────────────────────────────────────────────

    def gps_callback(self, msg: NavSatFix):
        """GPS fix gelince RawGps mesajına dönüştür ve yayınla."""
        now = self.get_clock().now()

        raw = RawGps()
        raw.header.stamp    = msg.header.stamp
        raw.header.frame_id = 'gps_frame'
        raw.age_ms          = 0
        raw.valid_until_ms  = self.valid_until_ms

        raw.latitude  = msg.latitude
        raw.longitude = msg.longitude
        raw.altitude  = msg.altitude

        # Hız ve heading — NavSatFix'te yok, 0.0 yayınla
        # Gerçek araçta Xsens MTI-680-DK'dan gelecek
        raw.speed       = 0.0
        raw.heading_deg = 0.0

        # HDOP ve VDOP — NavSatFix'ten kovaryans tipine göre
        if msg.position_covariance_type > 0:
            # Kovaryans matrisinden HDOP tahmini
            hdop = math.sqrt(msg.position_covariance[0]) / 5.0
            raw.hdop = max(0.5, min(hdop, 99.9))
        else:
            raw.hdop = 99.9   # bilinmiyor

        raw.vdop = 99.9   # NavSatFix'ten hesaplanamaz

        # Fix tipi
        raw.fix_type = self._map_fix_type(msg.status.status)

        self.raw_gps_pub.publish(raw)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    def _map_fix_type(self, status: int) -> int:
        """
        NavSatFix status → RawGps fix_type dönüşümü.
        NavSatFix: -1=no fix, 0=fix, 1=sbas, 2=gbas
        RawGps: FIX_NONE=0, FIX_GPS=1, FIX_DGPS=2, FIX_RTK_FLOAT=4, FIX_RTK_FIXED=5
        """
        if status < 0:
            return 0   # FIX_NONE
        elif status == 0:
            return 1   # FIX_GPS
        elif status == 1:
            return 2   # FIX_DGPS
        elif status == 2:
            return 5   # FIX_RTK_FIXED
        else:
            return 1   # FIX_GPS varsayılan


# ───────────────────────────────────────────────────────────────────────────
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