#!/usr/bin/env python3
import math
import time

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
)

from geometry_msgs.msg import Twist
from planning_msgs.msg import Trajectory, TargetSpeed, ControllerFeedback
from localization_msgs.msg import LocalizationPose


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)


class TrajectoryToCmdvel(Node):
    """
    Simülasyon controller bridge.

    Girdi:
      /planning/trajectory
      /planning/target_speed
      /localization/pose

    Çıktı:
      /cmd_vel
      /controller/feedback

    Not:
      Bu node gerçek controller değildir.
      Gazebo diff_drive için geçici simülasyon köprüsüdür.
    """

    def __init__(self):
        super().__init__('trajectory_to_cmdvel')

        self.declare_parameter('max_speed', 2.0)
        self.declare_parameter('max_angular_z', 1.0)
        self.declare_parameter('k_stanley', 0.8)
        self.declare_parameter('lookahead_points', 4)
        self.declare_parameter('stale_timeout_ms', 700)
        self.declare_parameter('min_speed_for_control', 0.15)

        self.max_speed = float(self.get_parameter('max_speed').value)
        self.max_angular_z = float(self.get_parameter('max_angular_z').value)
        self.k_stanley = float(self.get_parameter('k_stanley').value)
        self.lookahead_points = int(self.get_parameter('lookahead_points').value)
        self.stale_timeout_ms = int(self.get_parameter('stale_timeout_ms').value)
        self.min_speed_for_control = float(
            self.get_parameter('min_speed_for_control').value
        )

        self.ego_x = 0.0
        self.ego_y = 0.0
        self.ego_yaw = 0.0
        self.ego_speed = 0.0

        self.trajectory = []
        self.target_speed = 0.0

        self.last_pose_time = None
        self.last_traj_time = None
        self.last_speed_time = None

        self.last_cte = 0.0
        self.last_heading_error = 0.0
        self.last_angular_cmd = 0.0
        self.last_linear_cmd = 0.0

        self.create_subscription(
            Trajectory,
            '/planning/trajectory',
            self.trajectory_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            TargetSpeed,
            '/planning/target_speed',
            self.target_speed_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            LocalizationPose,
            '/localization/pose',
            self.pose_callback,
            RELIABLE_QOS,
        )

        self.cmd_pub = self.create_publisher(
            Twist,
            '/cmd_vel',
            RELIABLE_QOS,
        )

        self.feedback_pub = self.create_publisher(
            ControllerFeedback,
            '/controller/feedback',
            RELIABLE_QOS,
        )

        self.create_timer(1.0 / 20.0, self.control_loop)
        self.create_timer(1.0 / 20.0, self.publish_feedback)

        self.get_logger().info(
            f'trajectory_to_cmdvel başladı. '
            f'max_speed={self.max_speed:.2f}, '
            f'k_stanley={self.k_stanley:.2f}'
        )

    def pose_callback(self, msg: LocalizationPose):
        self.ego_x = float(msg.x)
        self.ego_y = float(msg.y)
        self.ego_yaw = float(msg.yaw)
        self.ego_speed = float(msg.linear_velocity)
        self.last_pose_time = time.monotonic()

    def trajectory_callback(self, msg: Trajectory):
        self.trajectory = list(msg.points)
        self.last_traj_time = time.monotonic()

    def target_speed_callback(self, msg: TargetSpeed):
        self.target_speed = float(msg.speed)
        self.last_speed_time = time.monotonic()

    def control_loop(self):
        cmd = Twist()

        if self.is_stale():
            self.last_linear_cmd = 0.0
            self.last_angular_cmd = 0.0
            self.cmd_pub.publish(cmd)
            return

        if not self.trajectory:
            self.last_linear_cmd = 0.0
            self.last_angular_cmd = 0.0
            self.cmd_pub.publish(cmd)
            return

        closest_idx, closest_dist = self.find_closest_point_index()
        target_idx = min(
            closest_idx + max(1, self.lookahead_points),
            len(self.trajectory) - 1,
        )

        closest = self.trajectory[closest_idx]
        target = self.trajectory[target_idx]

        dx = float(target.x) - self.ego_x
        dy = float(target.y) - self.ego_y

        desired_yaw = math.atan2(dy, dx)
        heading_error = self.normalize_angle(desired_yaw - self.ego_yaw)

        cte = (
            -math.sin(self.ego_yaw) * (float(closest.x) - self.ego_x)
            + math.cos(self.ego_yaw) * (float(closest.y) - self.ego_y)
        )

        trajectory_speed = float(getattr(target, 'speed', self.target_speed))

        # Sözleşmedeki hız öncelik kuralı:
        # final_speed = min(TargetSpeed.speed, TrajectoryPoint.speed)
        final_speed = min(self.target_speed, trajectory_speed, self.max_speed)
        final_speed = max(0.0, final_speed)

        control_speed = max(final_speed, self.min_speed_for_control)

        angular_cmd = heading_error + math.atan2(
            self.k_stanley * cte,
            control_speed,
        )

        angular_cmd = self.normalize_angle(angular_cmd)
        angular_cmd = self.clamp(
            angular_cmd,
            -self.max_angular_z,
            self.max_angular_z,
        )

        cmd.linear.x = float(final_speed)
        cmd.angular.z = float(angular_cmd)

        self.last_cte = float(cte)
        self.last_heading_error = float(heading_error)
        self.last_linear_cmd = float(final_speed)
        self.last_angular_cmd = float(angular_cmd)

        self.cmd_pub.publish(cmd)

    def publish_feedback(self):
        now = self.get_clock().now()

        msg = ControllerFeedback()
        msg.header.stamp = now.to_msg()

        msg.actual_speed = float(self.ego_speed)
        msg.actual_steering_deg = float(
            math.degrees(self.last_angular_cmd)
        )

        msg.cross_track_error = float(self.last_cte)
        msg.heading_error = float(self.last_heading_error)

        msg.brake_active = self.last_linear_cmd <= 0.01
        msg.full_brake_active = False

        msg.age_ms = 0
        msg.valid_until_ms = 500

        self.feedback_pub.publish(msg)

    def is_stale(self):
        now = time.monotonic()

        required_times = [
            self.last_pose_time,
            self.last_traj_time,
            self.last_speed_time,
        ]

        if any(t is None for t in required_times):
            return True

        for t in required_times:
            age_ms = (now - t) * 1000.0
            if age_ms > self.stale_timeout_ms:
                return True

        return False

    def find_closest_point_index(self):
        closest_idx = 0
        min_dist = float('inf')

        for i, pt in enumerate(self.trajectory):
            dx = float(pt.x) - self.ego_x
            dy = float(pt.y) - self.ego_y
            dist = math.hypot(dx, dy)

            if dist < min_dist:
                min_dist = dist
                closest_idx = i

        return closest_idx, min_dist

    @staticmethod
    def normalize_angle(angle):
        return math.atan2(math.sin(angle), math.cos(angle))

    @staticmethod
    def clamp(value, min_value, max_value):
        return max(min_value, min(max_value, value))


def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryToCmdvel()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        zero = Twist()
        node.cmd_pub.publish(zero)
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
