#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy
from localization_msgs.msg import LocalizationPose, LocalizationOdometry, LocalizationStatus, MapOrigin

RELIABLE_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.VOLATILE, history=HistoryPolicy.KEEP_LAST, depth=10)
TRANSIENT_QOS = QoSProfile(reliability=ReliabilityPolicy.RELIABLE, durability=DurabilityPolicy.TRANSIENT_LOCAL, history=HistoryPolicy.KEEP_LAST, depth=1)

class FakeLocalization(Node):
    def __init__(self):
        super().__init__('fake_localization')
        self.declare_parameter('speed', 2.0)
        self.declare_parameter('lat_ref', 40.789949)
        self.declare_parameter('lon_ref', 29.508726)
        self.speed = self.get_parameter('speed').value
        self.lat_ref = self.get_parameter('lat_ref').value
        self.lon_ref = self.get_parameter('lon_ref').value
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.pose_pub = self.create_publisher(LocalizationPose, '/localization/pose', RELIABLE_QOS)
        self.odom_pub = self.create_publisher(LocalizationOdometry, '/localization/odometry', RELIABLE_QOS)
        self.status_pub = self.create_publisher(LocalizationStatus, '/localization/status', RELIABLE_QOS)
        self.origin_pub = self.create_publisher(MapOrigin, '/localization/map_origin', TRANSIENT_QOS)
        self.create_timer(1.0/30.0, self.publish_pose)
        self.create_timer(1.0/50.0, self.publish_odometry)
        self.create_timer(1.0/10.0, self.publish_status)
        self.create_timer(1.0, self.publish_origin)
        self.create_timer(1.0/50.0, self.update_position)
        self.get_logger().info(f'fake_localization başlatıldı — hız={self.speed}m/s')

    def update_position(self):
        dt = 1.0/50.0
        self.x += self.speed * math.cos(self.yaw) * dt
        self.y += self.speed * math.sin(self.yaw) * dt

    def publish_pose(self):
        now = self.get_clock().now()
        msg = LocalizationPose()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'
        msg.age_ms = 0
        msg.valid_until_ms = 300
        msg.x = self.x
        msg.y = self.y
        msg.yaw = self.yaw
        msg.linear_velocity = self.speed
        msg.angular_velocity = 0.0
        msg.source = 0
        msg.localization_confidence = 0.95
        msg.position_covariance = 0.05
        msg.heading_covariance = 0.01
        msg.velocity_covariance = 0.01
        self.pose_pub.publish(msg)

    def publish_odometry(self):
        now = self.get_clock().now()
        msg = LocalizationOdometry()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'odom'
        msg.age_ms = 0
        msg.valid_until_ms = 200
        msg.x = self.x
        msg.y = self.y
        msg.yaw = self.yaw
        msg.linear_velocity = self.speed
        msg.angular_velocity = 0.0
        msg.position_covariance = 0.05
        msg.heading_covariance = 0.01
        msg.velocity_covariance = 0.01
        self.odom_pub.publish(msg)

    def publish_status(self):
        now = self.get_clock().now()
        msg = LocalizationStatus()
        msg.header.stamp = now.to_msg()
        msg.age_ms = 0
        msg.valid_until_ms = 300
        msg.status = 0
        msg.localization_confidence = 0.95
        msg.position_covariance = 0.05
        msg.heading_covariance = 0.01
        msg.ndt_healthy = True
        msg.ndt_quality = 0.9
        msg.map_odom_stable = True
        msg.map_odom_drift = 0.0
        msg.gps_available = True
        msg.imu_available = True
        msg.lidar_available = True
        self.status_pub.publish(msg)

    def publish_origin(self):
        now = self.get_clock().now()
        msg = MapOrigin()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'
        msg.lat_ref = self.lat_ref
        msg.lon_ref = self.lon_ref
        msg.alt_ref = 85.2
        msg.yaw_ref = 0.0
        msg.locked = True
        self.origin_pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeLocalization()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
