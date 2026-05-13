# perception/lane_node.py
#
# Sprint 2 / S2-A4 — lane_node with hardened LaneModel contract output.
#
# Subscribes: /zed2/left/image_raw  (sensor_msgs/Image)
# Publishes:  /perception/lane_model (perception_msgs/LaneModel) at 20 Hz
#
# Publish state machine (evaluated each tick):
#   1. No image ever received     → lane_lost=True, LOW_CONFIDENCE + NO_INPUT
#   2. Image stale (age > threshold) → lane_lost=True, LOW_CONFIDENCE + STALE_MESSAGE
#   3. Fresh image — detector runs:
#      a. Both lanes found (confidence=1.0 ≥ 0.7) → full output, warning_flags=[]
#      b. One lane found (confidence=0.5 < 0.7)   → partial, LOW_CONFIDENCE + LANE_BOUNDARY_MISSING
#      c. No lanes / error                         → empty arrays, lane_lost=True,
#                                                     LOW_CONFIDENCE + LANE_BOUNDARY_MISSING
#
# MVP coordinate mapping (NOT real camera calibration):
#   image column → base_link lateral y via lane_contract.col_to_lateral_m
#   Forward points: x ∈ [1.0, 10.0] m at 0.1 m intervals (satisfies ≥5m + ≤0.1m spacing)
#   z = 0 throughout (ground-plane approximation)
#   Real projection requires camera intrinsics + extrinsics + IPM — future work.
#
# Parameters:
#   image_topic    string  default '/zed2/left/image_raw'
#   publish_hz     double  default 20.0
#   image_stale_ms int     default 500 (clamped to VALID_UNTIL_LANE_MS)
#
# Architecture rules:
#   - Publishes evidence only. No driving decisions, no /cmd_vel, /control/*, /beemobs/*.
#   - Output frame_id = base_link.

import time as _time
from typing import Optional

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Point
from sensor_msgs.msg import Image

from perception_msgs.msg import LaneModel

from perception.dummy_common import (
    BASE_LINK_FRAME_ID,
    RATE_LANE_HZ,
    VALID_UNTIL_LANE_MS,
    make_header,
)
from perception.lane_contract import (
    NO_IMAGE_AGE_MS,
    build_forward_x_values,
    col_to_lateral_m,
    compute_centerline_lateral,
    compute_lane_width_estimate,
    compute_warning_flags,
)
from perception.lane_detector_utils import detect_lanes
from perception.stale_utils import resolve_stale_ms

# Forward x values are constant — compute once at import time.
_FORWARD_X_VALUES = build_forward_x_values()


def _build_forward_points(lateral_m: float) -> list:
    """Build a list of geometry_msgs/Point along the forward axis at a fixed lateral.

    Uses the pre-computed x values from lane_contract so the range/step
    constants are not duplicated here.  All points share y=lateral_m, z=0.0.

    MVP note: straight-line vertical lane only.  Curvature-following geometry
    is future work (post-UFLD-v2 integration).
    """
    pts = []
    for x in _FORWARD_X_VALUES:
        pt = Point()
        pt.x = x
        pt.y = lateral_m
        pt.z = 0.0
        pts.append(pt)
    return pts


class LaneNode(Node):
    """Lane node: subscribes to camera image, publishes LaneModel evidence."""

    def __init__(self) -> None:
        super().__init__('lane_node')

        self.declare_parameter('image_topic', '/zed2/left/image_raw')
        self.declare_parameter('publish_hz', RATE_LANE_HZ)
        self.declare_parameter('image_stale_ms', VALID_UNTIL_LANE_MS)

        image_topic: str = (
            self.get_parameter('image_topic').get_parameter_value().string_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz').get_parameter_value().double_value
        )
        configured_stale: int = (
            self.get_parameter('image_stale_ms').get_parameter_value().integer_value
        )

        self._image_stale_ms: int = resolve_stale_ms(configured_stale, VALID_UNTIL_LANE_MS)
        if configured_stale <= 0:
            self.get_logger().warn(
                f'image_stale_ms={configured_stale} is invalid; '
                f'defaulting to {VALID_UNTIL_LANE_MS} ms'
            )
        elif configured_stale > VALID_UNTIL_LANE_MS:
            self.get_logger().warn(
                f'image_stale_ms={configured_stale} exceeds '
                f'valid_until_ms={VALID_UNTIL_LANE_MS}; '
                f'clamped to {VALID_UNTIL_LANE_MS} ms'
            )

        self._last_image_mono: Optional[float] = None
        self._last_image: Optional[Image] = None

        self._sub = self.create_subscription(
            Image, image_topic, self._on_image, 10)
        self._pub = self.create_publisher(
            LaneModel, '/perception/lane_model', 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'lane_node up — subscribing {image_topic} | '
            f'publishing /perception/lane_model at {publish_hz:.1f} Hz | '
            f'image_stale_ms={self._image_stale_ms}. '
            'S2-A4 hardened lane contract active.'
        )

    # ------------------------------------------------------------------
    # Subscriber callback
    # ------------------------------------------------------------------

    def _on_image(self, msg: Image) -> None:
        self._last_image_mono = _time.monotonic()
        self._last_image = msg

    # ------------------------------------------------------------------
    # Publish timer
    # ------------------------------------------------------------------

    def _tick(self) -> None:
        now_mono = _time.monotonic()
        msg = LaneModel()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.valid_until_ms = VALID_UNTIL_LANE_MS
        msg.source_sensor = 'camera'
        msg.curvature = 0.0         # straight MVP; real curvature is future work
        msg.lane_width_estimate = 0.0

        if self._last_image_mono is None:
            # Case 1 — no image ever received.
            msg.centerline = []
            msg.left_boundary = []
            msg.right_boundary = []
            msg.lane_lost = True
            msg.lane_confidence = 0.0
            msg.age_ms = NO_IMAGE_AGE_MS
            msg.warning_flags = compute_warning_flags('no_input')
            self._pub.publish(msg)
            return

        age_ms = int((now_mono - self._last_image_mono) * 1000.0)
        msg.age_ms = age_ms

        if age_ms > self._image_stale_ms:
            # Case 2 — image was flowing but has gone stale.
            msg.centerline = []
            msg.left_boundary = []
            msg.right_boundary = []
            msg.lane_lost = True
            msg.lane_confidence = 0.0
            msg.warning_flags = compute_warning_flags('stale')
            self._pub.publish(msg)
            return

        # Case 3 — fresh image; run detector.
        img = self._last_image
        result = detect_lanes(
            bytes(img.data),
            img.width,
            img.height,
            img.step,
            img.encoding,
        )

        if result['ok'] and result['left_col'] is not None and result['right_col'] is not None:
            # Both lanes detected — full output, confidence=1.0 >= 0.7 → no flags.
            left_col = result['left_col']
            right_col = result['right_col']
            left_lat = col_to_lateral_m(left_col, img.width)
            right_lat = col_to_lateral_m(right_col, img.width)
            center_lat = compute_centerline_lateral(left_lat, right_lat)

            msg.left_boundary = _build_forward_points(left_lat)
            msg.right_boundary = _build_forward_points(right_lat)
            msg.centerline = _build_forward_points(center_lat)
            msg.lane_lost = False
            msg.lane_confidence = result['confidence']   # 1.0
            msg.lane_width_estimate = compute_lane_width_estimate(left_lat, right_lat)
            msg.warning_flags = compute_warning_flags('valid_both')

        elif result['ok'] and (
            result['left_col'] is not None or result['right_col'] is not None
        ):
            # One boundary detected — partial output, confidence=0.5 < 0.7.
            col = result['left_col'] if result['left_col'] is not None else result['right_col']
            lat = col_to_lateral_m(col, img.width)
            left_pts = _build_forward_points(lat) if result['left_col'] is not None else []
            right_pts = _build_forward_points(lat) if result['right_col'] is not None else []

            msg.left_boundary = left_pts
            msg.right_boundary = right_pts
            msg.centerline = _build_forward_points(lat)
            msg.lane_lost = False
            msg.lane_confidence = result['confidence']   # 0.5
            msg.lane_width_estimate = 0.0
            msg.warning_flags = compute_warning_flags('partial')

        else:
            # No lanes detected or unsupported encoding — blank output.
            msg.centerline = []
            msg.left_boundary = []
            msg.right_boundary = []
            msg.lane_lost = True
            msg.lane_confidence = 0.0
            msg.warning_flags = compute_warning_flags('blank')

        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = LaneNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
