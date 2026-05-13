# perception/traffic_sign_node.py
#
# Gate B / Milestone 1 / Step 4 — traffic sign node skeleton.
#
# Publishes a contract-shaped *placeholder* perception_msgs/TrafficSigns on
# /perception/traffic_signs at 10 Hz. The wrapper carries only header + signs[]
# (contract §15 raw .msg has no own valid_until_ms / age_ms / warning_flags on
# the wrapper; per-element fields live on TrafficSign nested elements only).
# The dummy publishes an empty signs[] — no fake detections.
#
# Strict scope (see wiki/perception/traffic_sign_node.md, wiki/contracts/message_contracts.md):
#   - No real YOLOv8n, no event-memory state machine, no relevant_to_route
#     classification (planner-derived from /planning/active_route_context).
#   - No driving decisions, no /cmd_vel/control/beemobs publication.
#
# Runtime verification is recorded in wiki/log.md under the 2026-05-11
# per-node perception skeleton split entry.

import rclpy
from rclpy.node import Node

from perception_msgs.msg import TrafficSigns

from perception.dummy_common import (
    BASE_LINK_FRAME_ID,
    RATE_TRAFFIC_SIGNS_HZ,
    make_header,
)


class TrafficSignNode(Node):
    """Skeleton traffic-sign node publishing a dummy empty TrafficSigns at 10 Hz."""

    def __init__(self) -> None:
        super().__init__('traffic_sign_node')
        self._pub = self.create_publisher(
            TrafficSigns, '/perception/traffic_signs', 10)
        self.create_timer(1.0 / RATE_TRAFFIC_SIGNS_HZ, self._tick)
        self.get_logger().info(
            'traffic_sign_node up — publishing dummy empty TrafficSigns on '
            '/perception/traffic_signs. No real sign detection.'
        )

    def _tick(self) -> None:
        msg = TrafficSigns()
        msg.header = make_header(self, BASE_LINK_FRAME_ID)
        msg.signs = []
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = TrafficSignNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
