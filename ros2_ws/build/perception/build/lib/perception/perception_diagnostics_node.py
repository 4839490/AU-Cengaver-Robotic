# perception/perception_diagnostics_node.py
#
# Gate B / Milestone 1 / Step 4 — perception diagnostics node skeleton.
#
# Publishes a contract-shaped *placeholder* perception_msgs/PerceptionDiagnostics
# on /perception/diagnostics at 1 Hz. The dummy advertises NO_INPUT and
# LOW_CONFIDENCE flags because no real perception nodes are wired upstream
# yet (this skeleton predates traffic_light/lane/lidar real algorithms).
#
# Strict scope (see wiki/perception/perception_diagnostics_node.md, wiki/contracts/message_contracts.md):
#   - PerceptionDiagnostics carries no spatial frame: header.frame_id = "".
#   - PerceptionDiagnostics has NO `valid_until_ms` field per contract §13;
#     freshness is encoded via `last_msg_age_ms`.
#   - This node does not aggregate real per-node Hz/latency yet — it just
#     publishes a heartbeat row at the contract topic rate.
#
# Runtime verification is recorded in wiki/log.md under the 2026-05-11
# per-node perception skeleton split entry.

import rclpy
from rclpy.node import Node

from perception_msgs.msg import PerceptionDiagnostics

from perception.dummy_common import (
    DIAGNOSTICS_FRAME_ID,
    DUMMY_CONFIDENCE,
    DUMMY_DIAGNOSTICS_WARNING_FLAGS,
    RATE_DIAGNOSTICS_HZ,
    make_header,
)


class PerceptionDiagnosticsNode(Node):
    """Skeleton perception diagnostics node publishing a heartbeat at 1 Hz."""

    def __init__(self) -> None:
        super().__init__('perception_diagnostics_node')
        self._pub = self.create_publisher(
            PerceptionDiagnostics, '/perception/diagnostics', 10)
        self.create_timer(1.0 / RATE_DIAGNOSTICS_HZ, self._tick)
        self.get_logger().info(
            'perception_diagnostics_node up — publishing dummy '
            'PerceptionDiagnostics heartbeat on /perception/diagnostics.'
        )

    def _tick(self) -> None:
        msg = PerceptionDiagnostics()
        msg.header = make_header(self, DIAGNOSTICS_FRAME_ID)
        msg.node_name = 'perception_diagnostics_node'
        msg.input_hz = 0.0
        msg.output_hz = float(RATE_DIAGNOSTICS_HZ)
        msg.latency_ms = 0.0
        msg.last_msg_age_ms = 0
        msg.mean_confidence = DUMMY_CONFIDENCE
        msg.num_outputs = 0
        msg.gpu_utilization = 0.0
        msg.warning_flags = list(DUMMY_DIAGNOSTICS_WARNING_FLAGS)
        self._pub.publish(msg)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = PerceptionDiagnosticsNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
