#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from geometry_msgs.msg import Point  # noqa
from perception_msgs.msg import LaneModel, TrafficLightState, ObstacleTracks

RELIABLE_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)

class FakePerception(Node):
    def __init__(self):
        super().__init__('fake_perception')
        self.declare_parameter('lane_width', 3.5)
        self.declare_parameter('light_state', 3)
        self.lane_width = self.get_parameter('lane_width').value
        self.light_state = self.get_parameter('light_state').value
        self.lane_pub = self.create_publisher(LaneModel, '/perception/lane_model', RELIABLE_QOS)
        self.light_pub = self.create_publisher(TrafficLightState, '/perception/traffic_light_state', RELIABLE_QOS)
        self.obstacle_pub = self.create_publisher(ObstacleTracks, '/perception/obstacle_tracks', RELIABLE_QOS)
        self.create_timer(1.0/20.0, self.publish_lane)
        self.create_timer(1.0/10.0, self.publish_light)
        self.create_timer(1.0/20.0, self.publish_obstacles)
        self.get_logger().info('fake_perception başlatıldı — GREEN ışık, düz şerit')

    def publish_lane(self):
        now = self.get_clock().now()
        msg = LaneModel()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'base_link'
        msg.age_ms = 0
        msg.valid_until_ms = 500
        msg.lane_confidence = 0.95
        msg.lane_lost = False
        msg.curvature = 0.0
        msg.lane_width_estimate = self.lane_width
        for i in range(20):
            d = float(i) * 0.5
            c = Point(); c.x = d; c.y = 0.0; c.z = 0.0
            l = Point(); l.x = d; l.y = self.lane_width/2; l.z = 0.0
            r = Point(); r.x = d; r.y = -self.lane_width/2; r.z = 0.0
            msg.centerline.append(c)
            msg.left_boundary.append(l)
            msg.right_boundary.append(r)
        self.lane_pub.publish(msg)

    def publish_light(self):
        now = self.get_clock().now()
        msg = TrafficLightState()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'base_link'
        msg.age_ms = 0
        msg.valid_until_ms = 300
        msg.state = self.light_state
        msg.confidence = 0.95
        msg.relevant_to_route = True
        msg.confirmed = True
        msg.in_stop_zone = False
        msg.distance_to_stop = 50.0
        self.light_pub.publish(msg)

    def publish_obstacles(self):
        now = self.get_clock().now()
        msg = ObstacleTracks()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'base_link'
        self.obstacle_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakePerception()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
