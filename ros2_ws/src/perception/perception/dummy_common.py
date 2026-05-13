# perception/dummy_common.py
#
# Shared helpers and constants for the per-node perception skeleton publishers
# (Gate B / Milestone 1 / Step 4). The original monolithic
# `perception/dummy_publishers.py` carried these as module-level constants; the
# per-node split factors them out so every skeleton produces the same dummy
# field values without each node redeclaring the same numbers.
#
# Strict scope (see wiki/contracts/message_contracts.md, wiki/contracts/timing_and_fallback.md,
# wiki/perception/perception_overview.md):
#   - Constants only mirror the Gate-B-cleared canonical raw `.msg` blocks and
#     the timing/fallback table. No real algorithm logic lives here.
#   - The per-topic frame_id values match the contract: every topic-level
#     perception message uses base_link, except PerceptionDiagnostics which
#     carries no spatial frame and uses "".
#
# Runtime verification is recorded in wiki/log.md under the 2026-05-11
# per-node perception skeleton split entry.

from std_msgs.msg import Header


# --- Publish rates (Hz) ---------------------------------------------------
# Each rate sits at the lower end of the contract band so the dummy stream is
# clearly placeholder evidence rather than real-time perception.
RATE_LANE_HZ = 20.0
RATE_TRAFFIC_LIGHT_HZ = 10.0
RATE_TRAFFIC_SIGNS_HZ = 10.0
RATE_OBSTACLE_TRACKS_HZ = 20.0
RATE_STOP_TARGET_HZ = 10.0
RATE_JUNCTION_HZ = 10.0
RATE_DIAGNOSTICS_HZ = 1.0


# --- valid_until_ms per topic (wiki/contracts/timing_and_fallback.md) -----
VALID_UNTIL_LANE_MS = 500
VALID_UNTIL_LIGHT_MS = 300
VALID_UNTIL_SIGNS_MS = 1000
VALID_UNTIL_TRACKS_MS = 200
VALID_UNTIL_STOP_MS = 300
VALID_UNTIL_JUNCTION_MS = 500


# --- Dummy field defaults --------------------------------------------------
DUMMY_CONFIDENCE = 0.10
DUMMY_WARNING_FLAGS = ['LOW_CONFIDENCE', 'STALE_MESSAGE']

# PerceptionDiagnostics topic uses the standard `warning_flags` set from
# wiki/contracts/timing_and_fallback.md; the dummy advertises NO_INPUT (no
# upstream sensors are wired) plus LOW_CONFIDENCE.
DUMMY_DIAGNOSTICS_WARNING_FLAGS = ['NO_INPUT', 'LOW_CONFIDENCE']

# Frame id for the diagnostics topic (no spatial frame, contract §13).
DIAGNOSTICS_FRAME_ID = ''

# Default base_link source frame id used by every other topic-level message.
BASE_LINK_FRAME_ID = 'base_link'


def make_header(node, frame_id):
    """Build a `std_msgs/Header` stamped with the node's clock.

    Centralizing this avoids each per-node skeleton importing `Header` and
    re-implementing the two-line stamp/frame_id pattern. The node argument is
    any rclpy.Node-like object exposing `get_clock()`.
    """
    h = Header()
    h.stamp = node.get_clock().now().to_msg()
    h.frame_id = frame_id
    return h
