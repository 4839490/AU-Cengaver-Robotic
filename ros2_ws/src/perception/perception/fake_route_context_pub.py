# perception/fake_route_context_pub.py
#
# S3-R1 — fake ActiveRouteContext publisher for Track R smoke testing.
#
# Publishes planning_msgs/ActiveRouteContext on /planning/active_route_context
# at 10 Hz (configurable) so S3-R2/R3/R4 can be exercised without a real planner.
#
# Default parameter values come from route_context_utils.DEFAULTS — single source
# of truth shared with the ROS-free helper and its unit tests.
#
# Parameters (all overridable via --ros-args or launch-time YAML):
#   publish_hz              float   default 10.0
#   ego_speed_mps           float   default DEFAULTS['ego_speed_mps']       (0.0)
#   route_context_valid     bool    default DEFAULTS['route_context_valid']  (True)
#   age_ms                  int     default DEFAULTS['age_ms']               (0)
#   valid_until_ms          int     default DEFAULTS['valid_until_ms']       (500)
#   in_stop_zone            bool    default DEFAULTS['in_stop_zone']         (False)
#   distance_to_stop_zone   float   default DEFAULTS['distance_to_stop_zone'](0.0)
#   localization_confidence float   default DEFAULTS['localization_confidence'](1.0)
#   active_waypoint_id      int     default DEFAULTS['active_waypoint_id']   (0)
#   target_x                float   default DEFAULTS['target_x']             (0.0)
#   target_y                float   default DEFAULTS['target_y']             (0.0)
#   target_heading          float   default DEFAULTS['target_heading']       (0.0)
#   route_direction         string  default DEFAULTS['route_direction']      ("")
#   planner_mode            int     default DEFAULTS['planner_mode']         (0)
#   lookahead_distance      float   default DEFAULTS['lookahead_distance']   (0.0)
#
# Strict scope:
#   - Does NOT subscribe to anything.
#   - Does NOT publish /cmd_vel, /control/*, /beemobs/*, or any non-planning topic.
#   - planned_trajectory always published as empty list (no geometry needed for S3-R1).
#
# Contract references:
#   wiki/architecture/active_route_context.md §"Fake publisher for Sprint 3 Track R"
#   wiki/contracts/message_contracts.md §planning_msgs/ActiveRouteContext
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track R §S3-R1

import rclpy
from rclpy.node import Node

from planning_msgs.msg import ActiveRouteContext

from perception.dummy_common import BASE_LINK_FRAME_ID, make_header
from perception.route_context_utils import DEFAULTS, validate_route_context

_D = DEFAULTS


class FakeRouteContextPub(Node):
    """Publish synthetic ActiveRouteContext for S3 Track R smoke testing."""

    def __init__(self) -> None:
        super().__init__('fake_route_context_pub')

        self.declare_parameter('publish_hz', 10.0)
        self.declare_parameter('ego_speed_mps', float(_D['ego_speed_mps']))
        self.declare_parameter('route_context_valid', bool(_D['route_context_valid']))
        self.declare_parameter('age_ms', int(_D['age_ms']))
        self.declare_parameter('valid_until_ms', int(_D['valid_until_ms']))
        self.declare_parameter('in_stop_zone', bool(_D['in_stop_zone']))
        self.declare_parameter('distance_to_stop_zone', float(_D['distance_to_stop_zone']))
        self.declare_parameter('localization_confidence', float(_D['localization_confidence']))
        self.declare_parameter('active_waypoint_id', int(_D['active_waypoint_id']))
        self.declare_parameter('target_x', float(_D['target_x']))
        self.declare_parameter('target_y', float(_D['target_y']))
        self.declare_parameter('target_heading', float(_D['target_heading']))
        self.declare_parameter('route_direction', str(_D['route_direction']))
        self.declare_parameter('planner_mode', int(_D['planner_mode']))
        self.declare_parameter('lookahead_distance', float(_D['lookahead_distance']))

        p = self.get_parameter
        publish_hz: float = p('publish_hz').get_parameter_value().double_value
        self._ego_speed_mps: float = float(
            p('ego_speed_mps').get_parameter_value().double_value)
        self._route_context_valid: bool = (
            p('route_context_valid').get_parameter_value().bool_value)
        self._age_ms: int = p('age_ms').get_parameter_value().integer_value
        self._valid_until_ms: int = (
            p('valid_until_ms').get_parameter_value().integer_value)
        self._in_stop_zone: bool = (
            p('in_stop_zone').get_parameter_value().bool_value)
        self._distance_to_stop_zone: float = float(
            p('distance_to_stop_zone').get_parameter_value().double_value)
        self._localization_confidence: float = float(
            p('localization_confidence').get_parameter_value().double_value)
        self._active_waypoint_id: int = (
            p('active_waypoint_id').get_parameter_value().integer_value)
        self._target_x: float = float(p('target_x').get_parameter_value().double_value)
        self._target_y: float = float(p('target_y').get_parameter_value().double_value)
        self._target_heading: float = float(
            p('target_heading').get_parameter_value().double_value)
        self._route_direction: str = (
            p('route_direction').get_parameter_value().string_value)
        self._planner_mode: int = (
            p('planner_mode').get_parameter_value().integer_value)
        self._lookahead_distance: float = float(
            p('lookahead_distance').get_parameter_value().double_value)

        # Validate configured field dict at startup — log any type/range errors.
        errors = validate_route_context({
            'ego_speed_mps':       self._ego_speed_mps,
            'route_context_valid': self._route_context_valid,
            'age_ms':              self._age_ms,
            'valid_until_ms':      self._valid_until_ms,
        })
        for err in errors:
            self.get_logger().error(f'route_context_utils validation: {err}')

        self._pub = self.create_publisher(
            ActiveRouteContext, '/planning/active_route_context', 10)
        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'fake_route_context_pub up — '
            f'ego_speed_mps={self._ego_speed_mps:.2f}, '
            f'route_context_valid={self._route_context_valid}, '
            f'age_ms={self._age_ms}, valid_until_ms={self._valid_until_ms}, '
            f'in_stop_zone={self._in_stop_zone}, '
            f'at {publish_hz:.1f} Hz on /planning/active_route_context'
        )

    def _tick(self) -> None:
        msg = ActiveRouteContext()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.ego_speed_mps = self._ego_speed_mps
        msg.route_context_valid = self._route_context_valid
        msg.age_ms = self._age_ms
        msg.valid_until_ms = self._valid_until_ms
        msg.in_stop_zone = self._in_stop_zone
        msg.distance_to_stop_zone = self._distance_to_stop_zone
        msg.localization_confidence = self._localization_confidence
        msg.active_waypoint_id = self._active_waypoint_id
        msg.target_x = self._target_x
        msg.target_y = self._target_y
        msg.target_heading = self._target_heading
        msg.route_direction = self._route_direction
        msg.planner_mode = self._planner_mode
        msg.lookahead_distance = self._lookahead_distance
        msg.planned_trajectory = []
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = FakeRouteContextPub()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
