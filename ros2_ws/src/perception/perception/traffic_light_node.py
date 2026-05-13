# perception/traffic_light_node.py
#
# Sprint 1 / S1-1..S1-6 — Subscribe to /zed2/left/image_raw, apply a YOLO
# bbox stub (S1-3), classify colour via pure-Python ROI analysis (S1-4),
# apply 3-frame temporal confirmation (S1-5), and publish a fully live-pipeline
# TrafficLightState with correct STALE semantics (S1-6).
#
# S1-3 — YOLO bbox stub layer:
#   model_path parameter wires the future real-model path.  If the path is
#   empty or the file is absent the node logs an INFO message and continues
#   using the stub.  The stub returns the configured bbox rectangle when
#   stub_bbox_enabled=true and a fresh image exists; otherwise no bbox.
#
# S1-4 — ROI colour classifier (pure Python, no OpenCV):
#   classify_roi() samples average channel values inside the bbox and
#   classifies RED / YELLOW / GREEN / UNKNOWN.
#   confidence < 0.7 (contract §8) → UNKNOWN published.
#
# S1-5 — 3-frame temporal confirmation filter:
#   TemporalFilter accumulates per-frame classifications and sets
#   confirmed=True after confirm_frames consecutive non-UNKNOWN observations
#   of the same state.  Before confirmation the current observed state is
#   published as evidence with confirmed=False (planner/FSM must not act on
#   confirmed=False per the contract behavior table).
#
# S1-6 — State semantics finalization:
#   Three image-availability cases are distinguished in the publish loop:
#     Case 1 (no image ever received):  state=UNKNOWN + [LOW_CONFIDENCE, NO_INPUT]
#     Case 2 (images stale > image_stale_ms): state=STALE + [LOW_CONFIDENCE, STALE_MESSAGE]
#     Case 3 (fresh image):             run classifier → temporal filter → publish
#   In all stale/missing-image cases the temporal filter is reset and
#   confirmed=False is guaranteed.
#   image_stale_ms is clamped to valid_until_ms (300 ms) by resolve_stale_ms()
#   so the node never holds non-STALE evidence past the message validity window.
#
# S3-R4 — Route context wiring:
#   Subscribes to /planning/active_route_context (planning_msgs/ActiveRouteContext).
#   Tracks latest context and wall-clock receive time.
#   apply_route_context_to_light() (ROS-free helper) derives:
#     relevant_to_route — True only when context is present, valid, and fresh
#     in_stop_zone      — mirrors active_route_context.in_stop_zone
#     distance_to_stop  — mirrors active_route_context.distance_to_stop_zone
#   When context is missing/stale/invalid: safe conservative defaults (all False/0.0)
#   and ROUTE_CONTEXT_MISSING added to warning_flags once.
#   ROUTE_CONTEXT_MISSING is removed as soon as context becomes usable again.
#   Existing image-pipeline warning flags are never erased.
#
# Parameters (all overridable from --ros-args or launch-time YAML):
#   image_topic         string   default /zed2/left/image_raw
#   publish_hz          double   default 10.0
#   image_stale_ms      int      default VALID_UNTIL_LIGHT_MS (300)
#                                Clamped to VALID_UNTIL_LIGHT_MS if larger.
#                                Defaults to VALID_UNTIL_LIGHT_MS if <= 0.
#   model_path          string   default ''
#   use_yolo_stub       bool     default true
#   stub_bbox_enabled   bool     default true
#   stub_bbox_x         double   default 250.0  (px, top-left)
#   stub_bbox_y         double   default 120.0
#   stub_bbox_w         double   default 140.0
#   stub_bbox_h         double   default 240.0
#   confirm_frames      int      default 3
#   state_memory_ms     int      default 500
#
# Warning flags published (standard set per timing_and_fallback.md):
#   NO_INPUT                — no image has ever been received
#   STALE_MESSAGE           — images were flowing but most recent is older than image_stale_ms
#   LOW_CONFIDENCE          — classifier confidence below threshold or UNKNOWN state
#   BBOX_MISSING            — fresh image but no bbox (stub disabled or no detection)
#   MODEL_ERROR             — unsupported image encoding
#   SYNC_MISMATCH           — image data length inconsistent with declared dimensions
#   ROUTE_CONTEXT_MISSING   — /planning/active_route_context absent, stale, or invalid
#
# Strict scope:
#   - No real YOLO inference; no driving decisions.
#   - Does NOT publish /cmd_vel, /control/*, /beemobs/*.
#   - confirmed=True requires confirm_frames consecutive consistent frames (S1-5).
#
# Contract references:
#   wiki/perception/traffic_light_node.md — state semantics, warning flags, S3-R4
#   wiki/contracts/message_contracts.md §8 — TrafficLightState field set
#   wiki/contracts/timing_and_fallback.md — valid_until_ms=300, standard flags
#   wiki/architecture/active_route_context.md — freshness rule, valid_until_ms=500

import os
import time
from typing import Optional

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

from perception_msgs.msg import TrafficLightState
from planning_msgs.msg import ActiveRouteContext

from perception.colour_classifier import classify_roi
from perception.temporal_filter import TemporalFilter
from perception.stale_utils import resolve_stale_ms
from perception.route_context_apply_utils import apply_route_context_to_light
from perception.dummy_common import (
    BASE_LINK_FRAME_ID,
    RATE_TRAFFIC_LIGHT_HZ,
    VALID_UNTIL_LIGHT_MS,
    make_header,
)

_NO_INPUT = 'NO_INPUT'
_STALE_MESSAGE = 'STALE_MESSAGE'
_LOW_CONFIDENCE = 'LOW_CONFIDENCE'
_BBOX_MISSING = 'BBOX_MISSING'
_NEVER_RECEIVED = 999_999  # age_ms sentinel when no image has ever arrived


class TrafficLightNode(Node):
    """Traffic-light node: image subscriber + YOLO stub + ROI classifier + temporal filter.

    Subscribes to the camera image topic, runs the colour classifier inside the
    stub bounding box, applies a 3-frame temporal confirmation filter, and
    publishes contract-compliant TrafficLightState including STALE semantics.

    Three image-availability cases are handled in the publish loop:
      1. No image ever received:  state=UNKNOWN + [LOW_CONFIDENCE, NO_INPUT]
      2. Image stale:             state=STALE  + [LOW_CONFIDENCE, STALE_MESSAGE]
      3. Fresh image:             run classifier → temporal filter

    S3-R4: also subscribes to /planning/active_route_context and wires
    relevant_to_route, in_stop_zone, and distance_to_stop from the context
    message. ROUTE_CONTEXT_MISSING flag is added when context is unusable.
    """

    def __init__(self) -> None:
        super().__init__('traffic_light_node')

        # --- parameters ---
        self.declare_parameter('image_topic', '/zed2/left/image_raw')
        self.declare_parameter('publish_hz', RATE_TRAFFIC_LIGHT_HZ)
        self.declare_parameter('image_stale_ms', VALID_UNTIL_LIGHT_MS)
        self.declare_parameter('model_path', '')
        self.declare_parameter('use_yolo_stub', True)
        self.declare_parameter('stub_bbox_enabled', True)
        self.declare_parameter('stub_bbox_x', 250.0)
        self.declare_parameter('stub_bbox_y', 120.0)
        self.declare_parameter('stub_bbox_w', 140.0)
        self.declare_parameter('stub_bbox_h', 240.0)
        self.declare_parameter('confirm_frames', 3)
        self.declare_parameter('state_memory_ms', 500)

        image_topic: str = (
            self.get_parameter('image_topic').get_parameter_value().string_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz').get_parameter_value().double_value
        )
        _configured_stale_ms: int = (
            self.get_parameter('image_stale_ms').get_parameter_value().integer_value
        )
        self._image_stale_ms: int = resolve_stale_ms(_configured_stale_ms, VALID_UNTIL_LIGHT_MS)
        if _configured_stale_ms <= 0:
            self.get_logger().warn(
                f'image_stale_ms={_configured_stale_ms} is invalid (must be > 0); '
                f'using VALID_UNTIL_LIGHT_MS={VALID_UNTIL_LIGHT_MS} ms'
            )
        elif self._image_stale_ms < _configured_stale_ms:
            self.get_logger().warn(
                f'image_stale_ms={_configured_stale_ms} exceeds valid_until_ms='
                f'{VALID_UNTIL_LIGHT_MS}; clamped to {self._image_stale_ms} ms '
                f'so evidence never outlives its validity window'
            )
        model_path: str = (
            self.get_parameter('model_path').get_parameter_value().string_value
        )
        self._use_yolo_stub: bool = (
            self.get_parameter('use_yolo_stub').get_parameter_value().bool_value
        )
        self._stub_bbox_enabled: bool = (
            self.get_parameter('stub_bbox_enabled').get_parameter_value().bool_value
        )
        self._stub_bbox_x: float = (
            self.get_parameter('stub_bbox_x').get_parameter_value().double_value
        )
        self._stub_bbox_y: float = (
            self.get_parameter('stub_bbox_y').get_parameter_value().double_value
        )
        self._stub_bbox_w: float = (
            self.get_parameter('stub_bbox_w').get_parameter_value().double_value
        )
        self._stub_bbox_h: float = (
            self.get_parameter('stub_bbox_h').get_parameter_value().double_value
        )
        confirm_frames: int = (
            self.get_parameter('confirm_frames').get_parameter_value().integer_value
        )
        state_memory_ms: int = (
            self.get_parameter('state_memory_ms').get_parameter_value().integer_value
        )

        # S1-3: log model_path status; no actual load in this step.
        if model_path and not os.path.isfile(model_path):
            self.get_logger().info(
                f'model_path={model_path!r} not found — running YOLO stub only'
            )
        elif not model_path:
            self.get_logger().info(
                'model_path empty — running YOLO stub only (S1-3)'
            )

        # S1-5: temporal filter — requires confirm_frames consecutive same-state frames.
        self._filter = TemporalFilter(
            confirm_frames=confirm_frames,
            state_memory_ms=state_memory_ms,
        )
        # Stamp of the last image fed to the temporal filter (sec, nanosec tuple).
        # Prevents the same frame from incrementing the counter when the publish
        # timer fires faster than the image subscription rate.
        self._last_classified_stamp = None

        # wall-clock second of the most recent image callback; negative = none yet.
        self._last_image_wall_s: float = -1.0
        # Latest Image message; None until first callback.
        self._last_image = None  # type: Optional[Image]

        # S3-R4: route context state — latest received message and wall-clock
        # receive time. Both must be set for apply_route_context_to_light() to
        # treat the context as usable.
        self._latest_context: Optional[ActiveRouteContext] = None
        self._context_wall_sec: Optional[float] = None

        self._sub_image = self.create_subscription(
            Image, image_topic, self._on_image, 10)

        # S3-R4: subscribe to route context for relevant_to_route / in_stop_zone.
        self._ctx_sub = self.create_subscription(
            ActiveRouteContext,
            '/planning/active_route_context',
            self._on_route_context,
            10,
        )

        self._pub = self.create_publisher(
            TrafficLightState, '/perception/traffic_light_state', 10)

        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'traffic_light_node up (S3-R4) — subscribing to {image_topic} '
            f'+ /planning/active_route_context, '
            f'use_yolo_stub={self._use_yolo_stub}, '
            f'stub_bbox_enabled={self._stub_bbox_enabled}, '
            f'stub_bbox=({self._stub_bbox_x},{self._stub_bbox_y},'
            f'{self._stub_bbox_w},{self._stub_bbox_h}), '
            f'confirm_frames={confirm_frames}, state_memory_ms={state_memory_ms}.'
        )

    # ------------------------------------------------------------------
    # Subscriber callback
    # ------------------------------------------------------------------

    def _on_image(self, msg: Image) -> None:
        """Store latest image message and update freshness timestamp."""
        self._last_image_wall_s = time.monotonic()
        self._last_image = msg

    def _on_route_context(self, msg: ActiveRouteContext) -> None:
        """Store latest route context message and wall-clock receive time."""
        self._latest_context = msg
        self._context_wall_sec = time.monotonic()

    # ------------------------------------------------------------------
    # YOLO bbox stub (S1-3)
    # ------------------------------------------------------------------

    def _get_stub_bbox(self):
        """Return (x, y, w, h) stub bbox or None when stub or bbox is disabled."""
        if not self._use_yolo_stub or not self._stub_bbox_enabled:
            return None
        return (
            self._stub_bbox_x,
            self._stub_bbox_y,
            self._stub_bbox_w,
            self._stub_bbox_h,
        )

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _age_ms(self) -> int:
        """Wall-clock ms since the last image arrived, or _NEVER_RECEIVED."""
        if self._last_image_wall_s < 0.0:
            return _NEVER_RECEIVED
        elapsed = int((time.monotonic() - self._last_image_wall_s) * 1000.0)
        return min(elapsed, _NEVER_RECEIVED)

    def _reset_filter(self) -> None:
        """Reset temporal filter and stamp cache (called on stale/missing image)."""
        self._filter.reset()
        self._last_classified_stamp = None

    # ------------------------------------------------------------------
    # Publish loop
    # ------------------------------------------------------------------

    def _tick(self) -> None:
        age_ms = self._age_ms()
        bx = by = bw = bh = 0.0
        confirmed = False

        if self._last_image is None:
            # Case 1: no image has ever arrived (fresh start or late subscription).
            self._reset_filter()
            state = TrafficLightState.UNKNOWN
            confidence = 0.0
            flags = [_LOW_CONFIDENCE, _NO_INPUT]

        elif age_ms > self._image_stale_ms:
            # Case 2: images were flowing but the most recent exceeds the stale
            # threshold.  Publish STALE so the planner can be conservative on
            # the last known state (wiki/perception/traffic_light_node.md §STALE).
            self._reset_filter()
            state = TrafficLightState.STALE
            confidence = 0.0
            flags = [_LOW_CONFIDENCE, _STALE_MESSAGE]

        else:
            # Case 3: fresh image — run YOLO bbox stub + colour classifier.
            bbox = self._get_stub_bbox()
            if bbox is None:
                # Fresh image but no bounding box from stub / real detector.
                self._reset_filter()
                state = TrafficLightState.UNKNOWN
                confidence = 0.0
                flags = [_LOW_CONFIDENCE, _BBOX_MISSING]
            else:
                bx, by, bw, bh = bbox
                img = self._last_image

                # classify_roi returns integers matching TrafficLightState constants.
                state, confidence, flags = classify_roi(
                    img.data, img.width, img.height, img.encoding,
                    bx, by, bw, bh,
                    step=img.step,
                )

                # Only advance the temporal filter for genuinely new frames.
                # The publish timer may fire faster than the image subscription.
                img_stamp = (img.header.stamp.sec, img.header.stamp.nanosec)
                if img_stamp != self._last_classified_stamp:
                    self._last_classified_stamp = img_stamp
                    now_ms = int(time.monotonic() * 1000)
                    self._filter.update(state, now_ms)

                confirmed = self._filter.confirmed

        # S3-R4: derive route fields from active_route_context; modifies flags
        # in-place (adds/removes ROUTE_CONTEXT_MISSING without erasing existing flags).
        wall_delta_ms = (
            (time.monotonic() - self._context_wall_sec) * 1000.0
            if self._context_wall_sec is not None else float('inf')
        )
        relevant_to_route, in_stop_zone, distance_to_stop = apply_route_context_to_light(
            flags, self._latest_context, wall_delta_ms
        )

        msg = TrafficLightState()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.state = state
        msg.confidence = confidence
        msg.relevant_to_route = relevant_to_route
        msg.distance_to_stop = distance_to_stop
        msg.in_stop_zone = in_stop_zone

        msg.confirmed = confirmed
        msg.bbox_x = bx
        msg.bbox_y = by
        msg.bbox_w = bw
        msg.bbox_h = bh
        msg.age_ms = age_ms
        msg.valid_until_ms = VALID_UNTIL_LIGHT_MS
        msg.source_sensor = 'camera'
        msg.warning_flags = flags
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TrafficLightNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
