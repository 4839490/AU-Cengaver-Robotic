#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from planning_msgs.msg import ControllerFeedback

RELIABLE_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)

class FakeControllerFeedback(Node):
    def __init__(self):
        super().__init__('fake_controller_feedback')
        self.declare_parameter('speed', 2.0)
        self.speed = self.get_parameter('speed').value

        self.pub = self.create_publisher(ControllerFeedback, '/controller/feedback', RELIABLE_QOS)
        self.create_timer(1.0/20.0, self.publish_feedback)
        self.get_logger().info('fake_controller_feedback başlatıldı')

    def publish_feedback(self):
        now = self.get_clock().now()
        msg = ControllerFeedback()
        msg.header.stamp = now.to_msg()
        msg.actual_speed = self.speed
        msg.actual_steering_deg = 0.0
        msg.cross_track_error = 0.0
        msg.heading_error = 0.0
        msg.brake_active = False
        msg.full_brake_active = False
        msg.valid_until_ms = 500
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeControllerFeedback()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
