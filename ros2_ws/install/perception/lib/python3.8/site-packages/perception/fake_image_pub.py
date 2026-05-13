# perception/fake_image_pub.py
#
# Sprint 1 / S1-2 + S1-3/S1-4 extension — Synthetic image publisher for testing
# traffic_light_node without a real ZED2 camera.  Publishes sensor_msgs/Image on
# /zed2/left/image_raw using a plain bytearray frame.  No OpenCV dependency.
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   color        string  default 'red'   — 'red' | 'yellow' | 'green' | 'unknown'
#   width        int     default 640
#   height       int     default 480
#   publish_hz   double  default 10.0
#
# Frame layout:
#   encoding: bgr8 (3 bytes per pixel: B, G, R)
#   background: neutral gray (B=100, G=100, R=100) — no channel bias outside bbox
#   rectangle: solid colour overlapping the default stub bbox (x=250, y=120, w=140, h=240)
#     red:     B=0, G=0,   R=255
#     green:   B=0, G=255, R=0
#     yellow:  B=0, G=255, R=255
#     unknown: same as background (gray) — classifier sees no dominant channel
#
# frame_id: camera_frame (matches static TF base_link -> camera_frame)
#
# Strict scope:
#   - Evidence-only helper; does not publish driving topics.
#   - No /cmd_vel, /control/*, /beemobs/*, no /perception/* output topics.

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

from perception.dummy_common import make_header

_FRAME_ID = 'camera_frame'
_ENCODING = 'bgr8'

# Default stub bbox coordinates (must match traffic_light_node defaults).
_BBOX_X, _BBOX_Y, _BBOX_W, _BBOX_H = 250, 120, 140, 240

# BGR values for each synthetic colour.
_COLOUR_PIXELS = {
    'red':     (0,   0,   255),
    'green':   (0,   255, 0),
    'yellow':  (0,   255, 255),
    'unknown': (100, 100, 100),  # gray — same as background; no dominant channel
}
_BACKGROUND_BGR = (100, 100, 100)


def _build_frame(color: str, width: int, height: int) -> bytes:
    """
    Build a bgr8 bytearray with a solid-colour rectangle inside the stub bbox.

    Background is neutral gray so the classifier sees no channel bias outside
    the rectangle area.  The rectangle overlaps the default stub bbox
    (x=250, y=120, w=140, h=240) so traffic_light_node can classify the
    correct colour with default parameters.
    """
    bg_b, bg_g, bg_r = _BACKGROUND_BGR
    data = bytearray([bg_b, bg_g, bg_r] * (width * height))

    rect_b, rect_g, rect_r = _COLOUR_PIXELS.get(color, _BACKGROUND_BGR)

    x0 = max(0, _BBOX_X)
    y0 = max(0, _BBOX_Y)
    x1 = min(width,  _BBOX_X + _BBOX_W)
    y1 = min(height, _BBOX_Y + _BBOX_H)

    if x1 > x0 and y1 > y0:
        row_fill = bytes([rect_b, rect_g, rect_r] * (x1 - x0))
        for row in range(y0, y1):
            base = row * width * 3 + x0 * 3
            data[base: base + len(row_fill)] = row_fill

    return bytes(data)


class FakeImagePub(Node):
    """Publish synthetic bgr8 traffic-light-like frames for node testing."""

    def __init__(self) -> None:
        super().__init__('fake_image_pub')

        self.declare_parameter('color', 'red')
        self.declare_parameter('width', 640)
        self.declare_parameter('height', 480)
        self.declare_parameter('publish_hz', 10.0)

        color: str = (
            self.get_parameter('color').get_parameter_value().string_value
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

        if color not in _COLOUR_PIXELS:
            self.get_logger().warn(
                f"Unknown color={color!r}; defaulting to 'unknown'. "
                f"Valid: {list(_COLOUR_PIXELS)}"
            )
            color = 'unknown'

        self._width = width
        self._height = height
        self._step = width * 3
        self._frame_data = _build_frame(color, width, height)

        self._pub = self.create_publisher(Image, '/zed2/left/image_raw', 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'fake_image_pub up — {width}x{height} {_ENCODING} '
            f'color={color!r} rect at bbox({_BBOX_X},{_BBOX_Y},{_BBOX_W},{_BBOX_H}) '
            f'at {publish_hz:.1f} Hz on /zed2/left/image_raw'
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
    node = FakeImagePub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
