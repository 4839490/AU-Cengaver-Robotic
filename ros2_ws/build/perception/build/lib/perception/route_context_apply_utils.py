# perception/route_context_apply_utils.py
#
# S3-R4 — ROS-free helper: apply ActiveRouteContext fields to TrafficLightState
# route output fields (relevant_to_route, in_stop_zone, distance_to_stop) and
# the ROUTE_CONTEXT_MISSING warning flag.
#
# Used by traffic_light_node._tick() and unit tests. No ROS2 imports.
#
# Contract references:
#   wiki/perception/traffic_light_node.md §S3-R4
#   wiki/architecture/active_route_context.md §freshness rule
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track R

from __future__ import annotations

from perception.ttc_utils import (
    add_warning_flag_once,
    is_route_context_fresh,
    remove_warning_flag,
)

_ROUTE_CONTEXT_MISSING = 'ROUTE_CONTEXT_MISSING'


def apply_route_context_to_light(
    flags: list,
    context,
    wall_delta_ms: float,
) -> tuple:
    """Apply ActiveRouteContext to TrafficLightState route fields.

    Modifies `flags` in-place:
      - Adds ROUTE_CONTEXT_MISSING once when context is unusable.
      - Removes ROUTE_CONTEXT_MISSING when context becomes usable again.

    Returns (relevant_to_route, in_stop_zone, distance_to_stop).

    Context is usable when all of the following hold:
      - context is not None
      - context.route_context_valid is True
      - context.valid_until_ms > 0  (checked inside is_route_context_fresh)
      - context.age_ms <= context.valid_until_ms
      - wall_delta_ms <= context.valid_until_ms
    """
    usable = False
    if context is not None and context.route_context_valid:
        usable = is_route_context_fresh(
            context.age_ms, context.valid_until_ms, wall_delta_ms
        )

    if usable:
        remove_warning_flag(flags, _ROUTE_CONTEXT_MISSING)
        return True, bool(context.in_stop_zone), float(context.distance_to_stop_zone)

    add_warning_flag_once(flags, _ROUTE_CONTEXT_MISSING)
    return False, False, 0.0
