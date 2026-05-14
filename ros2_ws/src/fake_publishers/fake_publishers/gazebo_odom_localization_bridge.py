#!/usr/bin/env python3
import math

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
)

from nav_msgs.msg import Odometry
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster

from localization_msgs.msg import (
    LocalizationPose,
    LocalizationOdometry,
    LocalizationStatus,
    MapOrigin,
)


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)

TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1,
)


class GazeboOdomLocalizationBridge(Node):
    """
    Gazebo /odom verisini takımın localization sözleşmesine çevirir.

    Girdi:
      /odom  nav_msgs/Odometry

    Çıktı:
      /localization/pose
      /localization/odometry
      /localization/status
      /localization/map_origin
      TF: map -> odom
    """

    def __init__(self):
        super().__init__('gazebo_odom_localization_bridge')

        self.declare_parameter('odom_topic', '/odom')
        self.declare_parameter('publish_map_origin', True)
        self.declare_parameter('lat_ref', 40.789949)
        self.declare_parameter('lon_ref', 29.508726)
        self.declare_parameter('alt_ref', 85.2)
        self.declare_parameter('yaw_ref', 0.0)
        self.declare_parameter('pose_valid_until_ms', 300)
        self.declare_parameter('odom_valid_until_ms', 200)
        self.declare_parameter('status_valid_until_ms', 300)

        self.odom_topic = str(self.get_parameter('odom_topic').value)
        self.publish_map_origin_enabled = bool(
            self.get_parameter('publish_map_origin').value
        )

        self.lat_ref = float(self.get_parameter('lat_ref').value)
        self.lon_ref = float(self.get_parameter('lon_ref').value)
        self.alt_ref = float(self.get_parameter('alt_ref').value)
        self.yaw_ref = float(self.get_parameter('yaw_ref').value)

        self.pose_valid_until_ms = int(
            self.get_parameter('pose_valid_until_ms').value
        )
        self.odom_valid_until_ms = int(
            self.get_parameter('odom_valid_until_ms').value
        )
        self.status_valid_until_ms = int(
            self.get_parameter('status_valid_until_ms').value
        )

        self.latest_odom = None

        self.pose_pub = self.create_publisher(
            LocalizationPose,
            '/localization/pose',
            RELIABLE_QOS,
        )

        self.loc_odom_pub = self.create_publisher(
            LocalizationOdometry,
            '/localization/odometry',
            RELIABLE_QOS,
        )

        self.status_pub = self.create_publisher(
            LocalizationStatus,
            '/localization/status',
            RELIABLE_QOS,
        )

        self.origin_pub = self.create_publisher(
            MapOrigin,
            '/localization/map_origin',
            TRANSIENT_QOS,
        )

        self.tf_broadcaster = TransformBroadcaster(self)

        self.create_subscription(
            Odometry,
            self.odom_topic,
            self.odom_callback,
            RELIABLE_QOS,
        )

        self.create_timer(1.0 / 30.0, self.publish_pose)
        self.create_timer(1.0 / 50.0, self.publish_localization_odometry)
        self.create_timer(1.0 / 10.0, self.publish_status)
        self.create_timer(1.0, self.publish_map_origin)
        self.create_timer(1.0 / 30.0, self.publish_map_to_odom_tf)

        self.get_logger().info(
            f'gazebo_odom_localization_bridge başladı. '
            f'Girdi: {self.odom_topic}'
        )

    def odom_callback(self, msg: Odometry):
        self.latest_odom = msg

    def publish_pose(self):
        if self.latest_odom is None:
            return

        now = self.get_clock().now()
        odom = self.latest_odom

        x = float(odom.pose.pose.position.x)
        y = float(odom.pose.pose.position.y)
        yaw = self.quaternion_to_yaw(odom.pose.pose.orientation)

        linear_velocity = float(odom.twist.twist.linear.x)
        angular_velocity = float(odom.twist.twist.angular.z)

        msg = LocalizationPose()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.age_ms = 0
        msg.valid_until_ms = self.pose_valid_until_ms

        msg.x = x
        msg.y = y
        msg.yaw = yaw

        msg.linear_velocity = linear_velocity
        msg.angular_velocity = angular_velocity

        msg.source = LocalizationPose.SOURCE_DEAD_RECKONING
        msg.localization_confidence = 0.95

        msg.position_covariance = 0.02
        msg.heading_covariance = 0.01
        msg.velocity_covariance = 0.01
        msg.warning_flags = []

        self.pose_pub.publish(msg)

    def publish_localization_odometry(self):
        if self.latest_odom is None:
            return

        now = self.get_clock().now()
        odom = self.latest_odom

        x = float(odom.pose.pose.position.x)
        y = float(odom.pose.pose.position.y)
        yaw = self.quaternion_to_yaw(odom.pose.pose.orientation)

        linear_velocity = float(odom.twist.twist.linear.x)
        angular_velocity = float(odom.twist.twist.angular.z)

        msg = LocalizationOdometry()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'odom'

        msg.age_ms = 0
        msg.valid_until_ms = self.odom_valid_until_ms

        msg.x = x
        msg.y = y
        msg.yaw = yaw

        msg.linear_velocity = linear_velocity
        msg.angular_velocity = angular_velocity

        msg.position_covariance = 0.02
        msg.heading_covariance = 0.01
        msg.velocity_covariance = 0.01
        msg.warning_flags = []

        self.loc_odom_pub.publish(msg)

    def publish_status(self):
        if self.latest_odom is None:
            return

        now = self.get_clock().now()

        msg = LocalizationStatus()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.age_ms = 0
        msg.valid_until_ms = self.status_valid_until_ms

        msg.status = LocalizationStatus.OK
        msg.localization_confidence = 0.95
        msg.position_covariance = 0.02
        msg.heading_covariance = 0.01

        msg.ndt_healthy = True
        msg.ndt_quality = 1.0

        msg.map_odom_stable = True
        msg.map_odom_drift = 0.0

        msg.gps_available = True
        msg.imu_available = True
        msg.lidar_available = True

        msg.warning_flags = []

        self.status_pub.publish(msg)

    def publish_map_origin(self):
        if not self.publish_map_origin_enabled:
            return

        now = self.get_clock().now()

        msg = MapOrigin()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.lat_ref = self.lat_ref
        msg.lon_ref = self.lon_ref
        msg.alt_ref = self.alt_ref
        msg.yaw_ref = self.yaw_ref
        msg.source = 'gazebo_bridge'
        msg.locked = True

        self.origin_pub.publish(msg)

    def publish_map_to_odom_tf(self):
        """
        Simülasyonun ilk aşamasında map ve odom frame'ini aynı kabul ediyoruz.
        odom -> base_link TF'ini Gazebo diff_drive zaten yayınlıyorsa burada yayınlamıyoruz.
        """
        now = self.get_clock().now()

        tf = TransformStamped()
        tf.header.stamp = now.to_msg()
        tf.header.frame_id = 'map'
        tf.child_frame_id = 'odom'

        tf.transform.translation.x = 0.0
        tf.transform.translation.y = 0.0
        tf.transform.translation.z = 0.0

        tf.transform.rotation.x = 0.0
        tf.transform.rotation.y = 0.0
        tf.transform.rotation.z = 0.0
        tf.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(tf)

    @staticmethod
    def quaternion_to_yaw(q):
        siny_cosp = 2.0 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1.0 - 2.0 * (q.y * q.y + q.z * q.z)
        return math.atan2(siny_cosp, cosy_cosp)


def main(args=None):
    rclpy.init(args=args)
    node = GazeboOdomLocalizationBridge()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
