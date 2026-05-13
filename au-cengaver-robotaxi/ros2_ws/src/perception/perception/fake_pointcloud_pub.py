# perception/fake_pointcloud_pub.py
#
# Sprint 2 / S2-B2 — Synthetic VLP-16-style PointCloud2 publisher for testing
# lidar_obstacle_node without a real Velodyne VLP-16 or Gazebo simulator.
#
# Publishes sensor_msgs/PointCloud2 on /velodyne_points.
# No OpenCV, no PCL, no numpy.  Point data is built by pointcloud_utils.py
# using plain Python struct packing.
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   scenario    string  default 'simple_obstacle'  — 'simple_obstacle' | 'empty'
#   publish_hz  double  default 10.0
#
# Scenarios:
#   simple_obstacle — 16 ground-plane points (z=0.0) + 9 above-ground obstacle
#                     points (z ∈ {0.5, 1.0, 1.5}).  Used to verify that
#                     S2-B3 RANSAC + clustering can find the cluster.
#   empty           — zero points.  Verifies lidar_obstacle_node stays up and
#                     publishes tracks=[] with no input.
#
# PointCloud2 field contract:
#   fields: x(offset=0) y(offset=4) z(offset=8) intensity(offset=12) — all FLOAT32
#   point_step = 16 bytes
#   row_step   = point_step × width
#   is_bigendian = False
#   is_dense     = True
#   height = 1  (unorganised cloud, as VLP-16 driver produces)
#   frame_id: lidar_frame
#
# Strict scope:
#   - Does NOT publish /perception/*, /cmd_vel, /control/*, /beemobs/*.
#   - Evidence support only; no driving decisions.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2, PointField

from perception.dummy_common import make_header
from perception.pointcloud_utils import POINT_STEP, build_obstacle_at_x, build_pointcloud_bytes

_TOPIC = '/velodyne_points'
_FRAME_ID = 'lidar_frame'
_KNOWN_SCENARIOS = ('simple_obstacle', 'empty', 'moving_obstacle')

# moving_obstacle: obstacle starts here and advances _OBSTACLE_STEP_X per tick.
# At 10 Hz that gives 1.0 m/s longitudinal velocity (> 0.1 m/s → is_static=False).
_OBSTACLE_START_X: float = 5.0   # m
_OBSTACLE_STEP_X: float = 0.1    # m per tick


def _make_fields():
    """Build the four PointField descriptors matching pointcloud_utils layout."""
    descs = [
        ('x',         0),
        ('y',         4),
        ('z',         8),
        ('intensity', 12),
    ]
    fields = []
    for name, offset in descs:
        f = PointField()
        f.name = name
        f.offset = offset
        f.datatype = PointField.FLOAT32  # = 7
        f.count = 1
        fields.append(f)
    return fields


class FakePointcloudPub(Node):
    """Publish synthetic VLP-16-style PointCloud2 frames for lidar_obstacle_node testing."""

    def __init__(self) -> None:
        super().__init__('fake_pointcloud_pub')

        self.declare_parameter('scenario', 'simple_obstacle')
        self.declare_parameter('publish_hz', 10.0)

        scenario: str = (
            self.get_parameter('scenario').get_parameter_value().string_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz').get_parameter_value().double_value
        )

        if scenario not in _KNOWN_SCENARIOS:
            self.get_logger().warn(
                f"Unknown scenario={scenario!r}; falling back to 'empty'. "
                f"Known: {_KNOWN_SCENARIOS}"
            )
            scenario = 'empty'

        self._scenario = scenario
        self._tick_count: int = 0

        if scenario == 'moving_obstacle':
            # Data changes each tick; precompute nothing.
            self._data = None
            self._num_points = 25  # always 25 pts (16 ground + 9 obstacle)
        else:
            self._data, self._num_points = build_pointcloud_bytes(scenario)

        self._fields = _make_fields()

        self._pub = self.create_publisher(PointCloud2, _TOPIC, 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'fake_pointcloud_pub up — scenario={scenario!r}, '
            f'{self._num_points} points, {publish_hz:.1f} Hz on {_TOPIC}'
        )

    def _tick(self) -> None:
        if self._scenario == 'moving_obstacle':
            obs_x = _OBSTACLE_START_X + self._tick_count * _OBSTACLE_STEP_X
            data, num_points = build_obstacle_at_x(obs_x)
        else:
            data, num_points = self._data, self._num_points
        self._tick_count += 1

        msg = PointCloud2()
        msg.header = make_header(self, _FRAME_ID)
        msg.height = 1
        msg.width = num_points
        msg.fields = self._fields
        msg.is_bigendian = False
        msg.point_step = POINT_STEP
        msg.row_step = POINT_STEP * num_points
        msg.data = data
        msg.is_dense = True
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FakePointcloudPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
