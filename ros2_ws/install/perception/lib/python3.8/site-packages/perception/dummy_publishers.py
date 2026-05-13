# perception/dummy_publishers.py
#
# Backward-compatibility thin wrapper for the original monolithic
# `dummy_perception_publishers` console script. Gate B / Step 4 has been
# split into one rclpy node per perception responsibility (lane,
# traffic_light, traffic_sign, lidar_obstacle, stop_target,
# perception_diagnostics, junction). This wrapper keeps the legacy
# entry point alive — it constructs every per-node skeleton in a single
# process and spins them under one executor — so any existing tooling
# that still launches `dummy_perception_publishers` keeps the same
# observable /perception/* output.
#
# No publish logic lives here. Every per-tick payload comes from the
# matching `perception/<thing>_node.py` skeleton, which keeps the dummy
# behaviour single-sourced.
#
# Strict scope (see wiki/perception/perception_overview.md, wiki/contracts/message_contracts.md):
#   - No real algorithms, no driving decisions.
#   - No /cmd_vel, /control/*, /beemobs/*, no controller subscription.
#   - No JUNCTION/TUNNEL as autonomy modes.
#
# Runtime verification is recorded in wiki/log.md under the 2026-05-11
# per-node perception skeleton split entry.

import rclpy
from rclpy.executors import SingleThreadedExecutor

from perception.junction_node import JunctionNode
from perception.lane_node import LaneNode
from perception.lidar_obstacle_node import LidarObstacleNode
from perception.perception_diagnostics_node import PerceptionDiagnosticsNode
from perception.stop_target_node import StopTargetNode
from perception.traffic_light_node import TrafficLightNode
from perception.traffic_sign_node import TrafficSignNode


# The order is presentation-only; rclpy timers run independently per node.
_NODE_CLASSES = (
    LaneNode,
    TrafficLightNode,
    TrafficSignNode,
    LidarObstacleNode,
    StopTargetNode,
    JunctionNode,
    PerceptionDiagnosticsNode,
)


def main(args=None) -> None:
    rclpy.init(args=args)
    nodes = [cls() for cls in _NODE_CLASSES]
    executor = SingleThreadedExecutor()
    for n in nodes:
        executor.add_node(n)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        for n in nodes:
            n.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
