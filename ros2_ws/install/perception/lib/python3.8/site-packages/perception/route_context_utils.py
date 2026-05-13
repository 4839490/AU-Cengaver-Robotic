# perception/route_context_utils.py
#
# S3-R1 — ROS-free helper for building and validating ActiveRouteContext field dicts.
#
# Used by fake_route_context_pub.py and unit tests. No ROS2 imports.
#
# Contract references:
#   wiki/architecture/active_route_context.md
#   wiki/contracts/message_contracts.md §planning_msgs/ActiveRouteContext
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track R §S3-R1

from __future__ import annotations

from typing import Any, Tuple, List

# Fields that must be present and type-correct for a context dict to be valid.
# ego_speed_mps accepts int or float; route_context_valid must be a strict bool.
_REQUIRED_FIELDS: List[Tuple[str, Any]] = [
    ('ego_speed_mps',       (int, float)),
    ('route_context_valid', bool),
    ('age_ms',              int),
    ('valid_until_ms',      int),
]

# Default values matching ActiveRouteContext.msg contract and S3-R1 spec.
DEFAULTS: dict[str, Any] = {
    'active_waypoint_id':      0,
    'target_x':                0.0,
    'target_y':                0.0,
    'target_heading':          0.0,
    'planner_mode':            0,
    'route_direction':         '',
    'planned_trajectory':      [],
    'lookahead_distance':      0.0,
    'in_stop_zone':            False,
    'distance_to_stop_zone':   0.0,
    'localization_confidence': 1.0,
    'ego_speed_mps':           0.0,
    'route_context_valid':     True,
    'age_ms':                  0,
    'valid_until_ms':          500,
}


def build_route_context_fields(**overrides: Any) -> dict[str, Any]:
    """Return a complete ActiveRouteContext field dict with overrides applied.

    Raises KeyError for any key not in the canonical field set.
    """
    result = dict(DEFAULTS)
    for key, value in overrides.items():
        if key not in result:
            raise KeyError(f"Unknown ActiveRouteContext field: {key!r}")
        result[key] = value
    return result


def validate_route_context(d: dict[str, Any]) -> list[str]:
    """Validate an ActiveRouteContext field dict.

    Returns a list of error strings; empty list means the dict is valid.
    Checks presence and type of required fields; also checks valid_until_ms > 0.
    """
    errors: list[str] = []
    for field, expected in _REQUIRED_FIELDS:
        if field not in d:
            errors.append(f"Missing required field: {field!r}")
            continue
        value = d[field]
        # bool is a subclass of int; guard route_context_valid against plain ints.
        if expected is bool:
            if not isinstance(value, bool):
                errors.append(
                    f"Field {field!r}: expected bool, got {type(value).__name__}"
                )
        else:
            if not isinstance(value, expected):
                if isinstance(expected, tuple):
                    expected_name = ' or '.join(t.__name__ for t in expected)
                else:
                    expected_name = expected.__name__
                errors.append(
                    f"Field {field!r}: expected {expected_name}, "
                    f"got {type(value).__name__}"
                )
    if 'valid_until_ms' in d and isinstance(d['valid_until_ms'], int):
        if d['valid_until_ms'] <= 0:
            errors.append("valid_until_ms must be > 0")
    return errors
