# perception/junction_node.py
#
# Gate B / Milestone 1 / Step 4 — junction node skeleton (Phase-2 optional).
#
# Publishes a contract-shaped *placeholder* perception_msgs/Junction on
# /perception/junction at 10 Hz. Junction.msg is in the Gate B canonical raw
# scope (wiki/contracts/message_contracts.md), so the dummy stream is wired
# in to keep the integration surface consistent. The dummy advertises
# `detected = false`, `junction_type = NORMAL`, low confidence.
#
# Strict scope (see wiki/perception/junction_node.md, wiki/contracts/message_contracts.md):
#   - JUNCTION is NOT an autonomy mode. It only appears as
#     TargetSpeed.reason or ActiveRouteContext.route_direction. The single
#     autonomy mode enum is common_msgs/AutonomyMode.
#   - In MVP, planner consumes active_route_context.route_direction; this
#     visual junction hint is optional and remains evidence-only.
#   - No driving decisions, no /cmd_vel/control/beemobs publication.
#
# Runtime verification is recorded in wiki/log.md under the 2026-05-11
# per-node perception skeleton split entry.

import rclpy
from rclpy.node import Node

from perception_msgs.msg import Junction

from perception.dummy_common import (
    BASE_LINK_FRAME_ID,
    DUMMY_CONFIDENCE,
    DUMMY_WARNING_FLAGS,
    RATE_JUNCTION_HZ,
    VALID_UNTIL_JUNCTION_MS,
    make_header,
)


class JunctionNode(Node):
    """Skeleton junction node publishing a dummy Junction at 10 Hz."""

    def __init__(self) -> None:
        super().__init__('junction_node')
        self._pub = self.create_publisher(
            Junction, '/perception/junction', 10)
        self.create_timer(1.0 / RATE_JUNCTION_HZ, self._tick)
        self.get_logger().info(
            'junction_node up — publishing dummy Junction on '
            '/perception/junction. JUNCTION is not an autonomy mode.'
        )

    def _tick(self) -> None:
        msg = Junction()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.detected = False
        msg.junction_type = Junction.NORMAL
        msg.arm_count = 0
        msg.distance_to_entry = 0.0
        msg.confidence = DUMMY_CONFIDENCE
        msg.age_ms = 0
        msg.valid_until_ms = VALID_UNTIL_JUNCTION_MS
        msg.source_sensor = 'camera'
        msg.warning_flags = list(DUMMY_WARNING_FLAGS)
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = JunctionNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
