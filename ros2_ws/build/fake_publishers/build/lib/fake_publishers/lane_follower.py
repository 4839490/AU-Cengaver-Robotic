#!/usr/bin/env python3
"""
Direkt şerit takibi — perception/lane_model → cmd_vel
Base_link frame'de çalışır — lokalizasyon gerekmez
"""
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from geometry_msgs.msg import Twist
from perception_msgs.msg import LaneModel

RELIABLE_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)

class LaneFollower(Node):
    def __init__(self):
        super().__init__('lane_follower')
        self.declare_parameter('max_speed', 1.5)
        self.declare_parameter('k_stanley', 0.3)
        self.max_speed = self.get_parameter('max_speed').value
        self.k_stanley = self.get_parameter('k_stanley').value

        self.centerline = []
        self.lane_lost  = False

        self.create_subscription(LaneModel, '/perception/lane_model', self.lane_cb, RELIABLE_QOS)
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', RELIABLE_QOS)
        self.create_timer(0.05, self.publish_cmd)
        self.get_logger().info(f'lane_follower başlatıldı — max_speed={self.max_speed}m/s')

    def lane_cb(self, msg):
        self.lane_lost  = msg.lane_lost
        self.centerline = msg.centerline

    def publish_cmd(self):
        msg = Twist()

        if self.lane_lost or not self.centerline:
            self.cmd_pub.publish(msg)
            return

        # Lookahead noktası — 5. nokta (~2.5m ileride)
        lookahead_idx = min(5, len(self.centerline) - 1)
        target = self.centerline[lookahead_idx]

        # Base_link frame'de araç x ekseninde — hedef yönü
        desired_yaw = math.atan2(target.y, target.x)

        # Cross-track error — y sapması
        cte = target.y

        # Stanley
        speed       = max(self.max_speed, 0.1)
        stanley_ang = desired_yaw + math.atan2(self.k_stanley * cte, speed)
        stanley_ang = self._normalize_angle(stanley_ang)
        stanley_ang = max(-1.0, min(1.0, stanley_ang))

        msg.linear.x  = float(self.max_speed)
        msg.angular.z = float(stanley_ang)
        self.cmd_pub.publish(msg)

    @staticmethod
    def _normalize_angle(angle):
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle

def main(args=None):
    rclpy.init(args=args)
    node = LaneFollower()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
