# perception/stop_target_node.py
#
# S3-S1/S3-S2 — stop_target_node: subscriber + publish on confirmed RED evidence.
#
# S3-S1 (done): subscriber skeleton — subscribes to upstream topics; publisher
#   available but never called; logs evidence detection without publishing.
#
# S3-S2 (this step): priority logic + publish.
#   - When fresh confirmed RED evidence is received, publishes a
#     perception_msgs/StopTarget on /perception/stop_target.
#   - Priority: CRITICAL (3) when TrafficLightState.relevant_to_route=True,
#     HIGH (2) otherwise (S3-R4 wires relevant_to_route from active_route_context).
#   - When evidence disappears or becomes stale: publishes nothing.
#     Consumers rely on valid_until_ms=300 expiry of the last real StopTarget.
#   - Geometry placeholders: distance_from_front_bumper = TrafficLightState.distance_to_stop
#     (0.0 in current traffic_light_node until route context is wired in S3-R4).
#     target_x = target_y = 0.0. Planner must treat these as evidence placeholders.
#     See wiki/perception/stop_target_node.md §StopTarget field highlights.
#
# Architecture mandate (wiki/perception/stop_target_node.md §Architecture):
#   - stop_target_node is an aggregator, not a decision maker.
#   - MUST NOT publish /cmd_vel, /control/*, /beemobs/*, or mode changes.
#   - Emits stop *evidence* only; planner/FSM make all driving decisions.
#   - If no fresh stop evidence exists: publish nothing.
#     Publishing target_type=0 (default) on no-evidence would look identical
#     to a real TRAFFIC_LIGHT_STOP.
#
# Subscriptions:
#   /perception/traffic_light_state  perception_msgs/TrafficLightState
#   /perception/traffic_signs        perception_msgs/TrafficSigns
#
# Publisher:
#   /perception/stop_target          perception_msgs/StopTarget
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   traffic_light_topic   string   default /perception/traffic_light_state
#   traffic_signs_topic   string   default /perception/traffic_signs
#   tick_hz               double   default 10.0
#   stale_ms              int      default 300  (matches valid_until_ms of light/signs)
#
# Contract references:
#   wiki/perception/stop_target_node.md
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track S §S3-S2
#   wiki/contracts/message_contracts.md §11/§15 — StopTarget (no warning_flags)

import time

import rclpy
from rclpy.node import Node

from perception_msgs.msg import StopTarget, TrafficLightState, TrafficSigns

from perception.stop_target_policy import (
    DEFAULT_STALE_MS,
    STOP_TARGET_VALID_UNTIL_MS,
    build_stop_target_fields,
    evaluate_light_stop_evidence,
    has_stop_sign_evidence,
)
from perception.dummy_common import BASE_LINK_FRAME_ID, make_header

_NEVER_RECEIVED = -1.0  # sentinel: no message callback has fired yet


class StopTargetNode(Node):
    """Stop-target aggregator — S3-S1 subscriber skeleton.

    Subscribes to /perception/traffic_light_state and /perception/traffic_signs.
    Evaluates freshness and stop evidence using stop_target_policy.
    Does NOT publish in S3-S1; S3-S2 adds the publish() call.
    """

    def __init__(self) -> None:
        super().__init__('stop_target_node')

        # --- parameters ---
        self.declare_parameter('traffic_light_topic', '/perception/traffic_light_state')
        self.declare_parameter('traffic_signs_topic', '/perception/traffic_signs')
        self.declare_parameter('tick_hz', 10.0)
        self.declare_parameter('stale_ms', DEFAULT_STALE_MS)

        light_topic: str = (
            self.get_parameter('traffic_light_topic').get_parameter_value().string_value
        )
        signs_topic: str = (
            self.get_parameter('traffic_signs_topic').get_parameter_value().string_value
        )
        tick_hz: float = (
            self.get_parameter('tick_hz').get_parameter_value().double_value
        )
        self._stale_ms: int = (
            self.get_parameter('stale_ms').get_parameter_value().integer_value
        )

        # --- publisher (available but never called in S3-S1) ---
        self._pub = self.create_publisher(StopTarget, '/perception/stop_target', 10)

        # --- subscriptions ---
        self._sub_light = self.create_subscription(
            TrafficLightState, light_topic, self._on_light, 10)
        self._sub_signs = self.create_subscription(
            TrafficSigns, signs_topic, self._on_signs, 10)

        # --- last received state ---
        self._last_light: 'TrafficLightState | None' = None
        self._last_light_wall_s: float = _NEVER_RECEIVED
        self._last_signs: 'TrafficSigns | None' = None
        self._last_signs_wall_s: float = _NEVER_RECEIVED

        # --- input counters for diagnostics ---
        self._light_count: int = 0
        self._signs_count: int = 0

        self.create_timer(1.0 / tick_hz, self._tick)

        self.get_logger().info(
            f'stop_target_node S3-S2 up — publishing on confirmed RED evidence. '
            f'Subscribed to: {light_topic}, {signs_topic}. '
            f'Publisher on /perception/stop_target. '
            f'stale_ms={self._stale_ms}, tick_hz={tick_hz}.'
        )

    # ------------------------------------------------------------------
    # Subscriber callbacks
    # ------------------------------------------------------------------

    def _on_light(self, msg: TrafficLightState) -> None:
        self._last_light = msg
        self._last_light_wall_s = time.monotonic()
        self._light_count += 1

    def _on_signs(self, msg: TrafficSigns) -> None:
        self._last_signs = msg
        self._last_signs_wall_s = time.monotonic()
        self._signs_count += 1

    # ------------------------------------------------------------------
    # Tick loop — evaluate evidence and publish when fresh stop evidence exists
    # ------------------------------------------------------------------

    def _tick(self) -> None:
        now = time.monotonic()

        # Evaluate traffic-light stop evidence via ROS-free policy module.
        light_evidence = None
        node_delta_ms = 0
        if self._last_light is not None:
            light_evidence = evaluate_light_stop_evidence(
                state=self._last_light.state,
                confirmed=self._last_light.confirmed,
                confidence=self._last_light.confidence,
                light_msg_age_ms=self._last_light.age_ms,
                msg_valid_until_ms=self._last_light.valid_until_ms,
                light_received_wall_s=self._last_light_wall_s,
                now_wall_s=now,
                stale_ms=self._stale_ms,
                relevant_to_route=self._last_light.relevant_to_route,
                distance_m=self._last_light.distance_to_stop,
            )
            node_delta_ms = int((now - self._last_light_wall_s) * 1000)

        # Evaluate traffic-sign stop evidence.
        sign_evidence = False
        if self._last_signs is not None:
            sign_evidence = has_stop_sign_evidence(
                signs=self._last_signs.signs,
                signs_received_wall_s=self._last_signs_wall_s,
                now_wall_s=now,
                stale_ms=self._stale_ms,
            )

        if light_evidence is not None:
            # Fresh confirmed RED evidence — build and publish StopTarget.
            # Returns None when combined age (evidence + node delta) exceeds
            # STOP_TARGET_VALID_UNTIL_MS; do not publish stale-combined evidence.
            msg = self._build_stop_target_msg(light_evidence, node_delta_ms)
            if msg is not None:
                self._pub.publish(msg)
                self.get_logger().debug(
                    f'StopTarget published: type={msg.target_type}, '
                    f'priority={msg.priority}, confidence={msg.confidence:.3f}, '
                    f'valid_until_ms={msg.valid_until_ms}, age_ms={msg.age_ms}.'
                )
            else:
                self.get_logger().debug(
                    f'StopTarget combined age expired — not publishing. '
                    f'light_msg_age={light_evidence.age_ms} ms, '
                    f'node_delta={node_delta_ms} ms.'
                )
        elif sign_evidence:
            # Sign evidence present but no light evidence — sign-sourced StopTarget
            # is deferred beyond S3-S2 (requires sign geometry / confirmed field wiring).
            self.get_logger().debug(
                f'Sign evidence detected — sign-sourced StopTarget deferred to S3-S2+. '
                f'signs_msgs={self._signs_count}.'
            )
        else:
            # No fresh stop evidence — publish nothing. Consumers rely on
            # valid_until_ms=300 expiry of the last real StopTarget.
            light_age_str = (
                f'{int((now - self._last_light_wall_s) * 1000)} ms'
                if self._last_light_wall_s > 0 else 'never'
            )
            self.get_logger().debug(
                f'No fresh stop evidence — not publishing. '
                f'light_msgs={self._light_count}, '
                f'signs_msgs={self._signs_count}, '
                f'light_wall_age={light_age_str}.'
            )

    # ------------------------------------------------------------------
    # StopTarget message builder
    # ------------------------------------------------------------------

    def _build_stop_target_msg(self, evidence, node_delta_ms: int):
        """Build a StopTarget message from StopEvidence and wall-clock delta.

        Returns None when combined age (evidence.age_ms + node_delta_ms) exceeds
        STOP_TARGET_VALID_UNTIL_MS — caller must not publish in that case.

        Geometry placeholders (S3-S2): distance_from_front_bumper mirrors
        TrafficLightState.distance_to_stop (0.0 until S3-R4 wires route context).
        target_x = target_y = 0.0. No warning_flags field (contract §15 omits it).
        """
        fields = build_stop_target_fields(evidence, now_age_ms=node_delta_ms)
        if fields is None:
            return None
        msg = StopTarget()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.target_type = fields['target_type']
        msg.distance_from_front_bumper = fields['distance_from_front_bumper']
        msg.target_x = fields['target_x']
        msg.target_y = fields['target_y']
        msg.confidence = fields['confidence']
        msg.source = fields['source']
        msg.age_ms = fields['age_ms']
        msg.valid_until_ms = fields['valid_until_ms']
        msg.waypoint_id = fields['waypoint_id']
        msg.heading_at_stop = fields['heading_at_stop']
        msg.priority = fields['priority']
        msg.required_stop_duration_ms = fields['required_stop_duration_ms']
        msg.stop_reason_id = fields['stop_reason_id']
        msg.source_topic = fields['source_topic']
        return msg


def main(args=None) -> None:
    rclpy.init(args=args)
    node = StopTargetNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
