# perception/fake_traffic_light_state_pub.py
#
# S3-S2 — fake TrafficLightState publisher for stop_target_node smoke testing.
#
# Publishes perception_msgs/TrafficLightState on /perception/traffic_light_state
# at a configurable rate with configurable state/confirmed/confidence so that
# stop_target_node can be exercised without a real camera or traffic_light_node.
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   state               string   default 'red'   — 'red' | 'yellow' | 'green' |
#                                                   'unknown' | 'stale' | 'conflict'
#   confirmed           bool     default true
#   confidence          double   default 0.85
#   publish_hz          double   default 10.0
#   age_ms              int      default 0
#   valid_until_ms      int      default 300
#   relevant_to_route   bool     default true  (true → CRITICAL priority in stop_target_node)
#
# Strict scope:
#   - Does NOT publish /cmd_vel, /control/*, /beemobs/*, or any non-perception topic.
#   - Evidence-only helper for S3-S2 smoke testing.
#
# Contract references:
#   wiki/perception/stop_target_node.md §Inputs
#   wiki/contracts/message_contracts.md §8 — TrafficLightState field set
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track S §S3-S2

import rclpy
from rclpy.node import Node

from perception_msgs.msg import TrafficLightState

from perception.dummy_common import BASE_LINK_FRAME_ID, make_header

_STATE_MAP = {
    'unknown':  TrafficLightState.UNKNOWN,
    'red':      TrafficLightState.RED,
    'yellow':   TrafficLightState.YELLOW,
    'green':    TrafficLightState.GREEN,
    'stale':    TrafficLightState.STALE,
    'conflict': TrafficLightState.CONFLICT,
}


class FakeTrafficLightStatePub(Node):
    """Publish synthetic TrafficLightState for stop_target_node smoke testing."""

    def __init__(self) -> None:
        super().__init__('fake_traffic_light_state_pub')

        self.declare_parameter('state', 'red')
        self.declare_parameter('confirmed', True)
        self.declare_parameter('confidence', 0.85)
        self.declare_parameter('publish_hz', 10.0)
        self.declare_parameter('age_ms', 0)
        self.declare_parameter('valid_until_ms', 300)
        self.declare_parameter('relevant_to_route', True)

        state_str: str = (
            self.get_parameter('state').get_parameter_value().string_value.lower()
        )
        self._confirmed: bool = (
            self.get_parameter('confirmed').get_parameter_value().bool_value
        )
        self._confidence: float = float(
            self.get_parameter('confidence').get_parameter_value().double_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz').get_parameter_value().double_value
        )
        self._age_ms: int = (
            self.get_parameter('age_ms').get_parameter_value().integer_value
        )
        self._valid_until_ms: int = (
            self.get_parameter('valid_until_ms').get_parameter_value().integer_value
        )
        self._relevant_to_route: bool = (
            self.get_parameter('relevant_to_route').get_parameter_value().bool_value
        )

        if state_str not in _STATE_MAP:
            self.get_logger().warn(
                f"Unknown state={state_str!r}; defaulting to 'unknown'. "
                f"Valid: {list(_STATE_MAP)}"
            )
            state_str = 'unknown'
        self._state: int = _STATE_MAP[state_str]

        self._pub = self.create_publisher(
            TrafficLightState, '/perception/traffic_light_state', 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'fake_traffic_light_state_pub up — '
            f'state={state_str!r} ({self._state}), '
            f'confirmed={self._confirmed}, '
            f'confidence={self._confidence:.2f}, '
            f'relevant_to_route={self._relevant_to_route}, '
            f'age_ms={self._age_ms}, valid_until_ms={self._valid_until_ms}, '
            f'at {publish_hz:.1f} Hz on /perception/traffic_light_state'
        )

    def _tick(self) -> None:
        msg = TrafficLightState()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.state = self._state
        msg.confidence = self._confidence
        msg.confirmed = self._confirmed
        msg.relevant_to_route = self._relevant_to_route
        msg.distance_to_stop = 0.0
        msg.in_stop_zone = False
        msg.bbox_x = 0.0
        msg.bbox_y = 0.0
        msg.bbox_w = 0.0
        msg.bbox_h = 0.0
        msg.age_ms = self._age_ms
        msg.valid_until_ms = self._valid_until_ms
        msg.source_sensor = 'camera'
        msg.warning_flags = []
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FakeTrafficLightStatePub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
