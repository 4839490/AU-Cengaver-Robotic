# perception/fake_lane_image_pub.py
#
# Sprint 2 / S2-A2 — Synthetic lane scene publisher for testing lane_node
# without a real ZED2 camera or Gazebo simulator.
#
# Publishes sensor_msgs/Image on /zed2/left/image_raw.  No OpenCV dependency;
# frames are built with plain bytearray manipulation.
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   scenario    string  default 'straight'  — 'straight' | 'blank'
#   width       int     default 640
#   height      int     default 480
#   publish_hz  double  default 10.0
#
# Scenarios:
#   straight — gray road background with two bright white vertical lane lines
#              at ~25% and ~75% of frame width, each 12 px wide.  The bright
#              pixels are easily detectable by any threshold-based detector.
#   blank    — uniform gray/dark background with no lane lines.  Used to verify
#              that lane_node correctly publishes lane_lost=true +
#              LANE_BOUNDARY_MISSING when the image contains no detectable lane.
#   (any other value falls back to blank and a WARN is logged)
#
# frame_id: camera_frame (matches static TF base_link -> camera_frame).
#
# Strict scope:
#   - Does NOT publish /perception/*, /cmd_vel, /control/*, /beemobs/*.
#   - Evidence support only; no driving decisions.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

from perception.dummy_common import make_header
from perception.lane_image_utils import build_lane_frame

_FRAME_ID = 'camera_frame'
_ENCODING = 'bgr8'


class FakeLaneImagePub(Node):
    """Publish synthetic lane scene frames for lane_node testing."""

    def __init__(self) -> None:
        super().__init__('fake_lane_image_pub')

        self.declare_parameter('scenario', 'straight')
        self.declare_parameter('width', 640)
        self.declare_parameter('height', 480)
        self.declare_parameter('publish_hz', 10.0)

        scenario: str = (
            self.get_parameter('scenario').get_parameter_value().string_value
        )
        width: int = (
            self.get_parameter('width').get_parameter_value().integer_value
        )
        height: int = (
            self.get_parameter('height').get_parameter_value().integer_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz').get_parameter_value().double_value
        )

        _known = ('straight', 'blank')
        if scenario not in _known:
            self.get_logger().warn(
                f"Unknown scenario={scenario!r}; falling back to 'blank'. "
                f"Known: {_known}"
            )
            scenario = 'blank'

        self._width = width
        self._height = height
        self._step = width * 3
        self._frame_data = build_lane_frame(scenario, width, height)

        self._pub = self.create_publisher(Image, '/zed2/left/image_raw', 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'fake_lane_image_pub up — {width}x{height} {_ENCODING} '
            f"scenario={scenario!r} at {publish_hz:.1f} Hz on /zed2/left/image_raw"
        )

    def _tick(self) -> None:
        msg = Image()
        msg.header = make_header(self, _FRAME_ID)
        msg.height = self._height
        msg.width = self._width
        msg.encoding = _ENCODING
        msg.is_bigendian = False
        msg.step = self._step
        msg.data = self._frame_data
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FakeLaneImagePub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
