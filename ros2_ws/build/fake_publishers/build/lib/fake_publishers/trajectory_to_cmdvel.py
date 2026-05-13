#!/usr/bin/env python3
"""
Trajectory → cmd_vel bridge — Stanley Controller
/planning/trajectory + /planning/target_speed → /cmd_vel
"""
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from geometry_msgs.msg import Twist
from planning_msgs.msg import Trajectory, TargetSpeed
from localization_msgs.msg import LocalizationPose

RELIABLE_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)

class TrajectoryToCmdvel(Node):
    def __init__(self):
        super().__init__('trajectory_to_cmdvel')

        self.declare_parameter('max_speed', 2.0)    # test için düşük
        self.declare_parameter('k_stanley', 0.5)    # Stanley kazancı
        self.max_speed = self.get_parameter('max_speed').value
        self.k_stanley = self.get_parameter('k_stanley').value

        self.target_speed = 0.0
        self.angular_z    = 0.0
        self.ego_x        = 0.0
        self.ego_y        = 0.0
        self.ego_yaw      = 0.0
        self.trajectory   = []

        self.create_subscription(Trajectory, '/planning/trajectory', self.traj_cb, RELIABLE_QOS)
        self.create_subscription(TargetSpeed, '/planning/target_speed', self.speed_cb, RELIABLE_QOS)
        self.create_subscription(LocalizationPose, '/localization/pose', self.pose_cb, RELIABLE_QOS)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', RELIABLE_QOS)
        self.create_timer(0.05, self.publish_cmd)
        self.get_logger().info(
            f'trajectory_to_cmdvel başlatıldı — max_speed={self.max_speed}m/s'
        )

    def pose_cb(self, msg):
        self.ego_x   = msg.x
        self.ego_y   = msg.y
        self.ego_yaw = msg.yaw

    def speed_cb(self, msg):
        # Test için max_speed ile sınırla
        self.target_speed = min(msg.speed, self.max_speed)

    def traj_cb(self, msg):
        if not msg.points:
            return
        self.trajectory = msg.points

    def publish_cmd(self):
        msg = Twist()

        if not self.trajectory:
            self.cmd_pub.publish(msg)
            return

        # En yakın trajectory noktasını bul
        closest_idx = 0
        min_dist    = float('inf')
        for i, pt in enumerate(self.trajectory):
            dx   = pt.x - self.ego_x
            dy   = pt.y - self.ego_y
            dist = math.sqrt(dx**2 + dy**2)
            if dist < min_dist:
                min_dist    = dist
                closest_idx = i

        # Lookahead — 2 nokta ilerisi
        lookahead_idx = min(closest_idx + 2, len(self.trajectory) - 1)
        target = self.trajectory[lookahead_idx]

        # Hedef yönü
        dx          = target.x - self.ego_x
        dy          = target.y - self.ego_y
        desired_yaw = math.atan2(dy, dx)

        # Heading hatası
        heading_err = self._normalize_angle(desired_yaw - self.ego_yaw)

        # Cross-track error (basit)
        cte = -math.sin(self.ego_yaw) * (target.x - self.ego_x) + \
               math.cos(self.ego_yaw) * (target.y - self.ego_y)

        # Stanley kontrolcü
        speed       = max(self.target_speed, 0.1)
        stanley_ang = heading_err + math.atan2(
            self.k_stanley * cte, speed
        )
        stanley_ang = self._normalize_angle(stanley_ang)
        stanley_ang = max(-1.0, min(1.0, stanley_ang))

        msg.linear.x  = float(self.target_speed)
        msg.angular.z = float(stanley_ang)
        self.cmd_pub.publish(msg)

    @staticmethod
    def _normalize_angle(angle):
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryToCmdvel()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
