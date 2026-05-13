# perception/ttc_utils.py
#
# S3-R2/S3-R3 — ROS-free helpers for route-context freshness, TTC computation,
# and warning-flag management (add-once, remove).
#
# Used by lidar_obstacle_node and unit tests. No ROS2 imports.
#
# Contract references:
#   wiki/architecture/active_route_context.md §freshness rule
#   wiki/perception/lidar_obstacle_node.md §TTC §S3-R2 §S3-R3
#   wiki/implementation/sprint3_perception_integration_kickoff.md §Track R

from __future__ import annotations

_CLOSING_SPEED_MIN_MPS = 0.1  # m/s — closing speeds at or below this → ttc=0.0


def is_route_context_fresh(
    msg_age_ms: int,
    valid_until_ms: int,
    wall_delta_ms: float,
) -> bool:
    """Return True when the route context message is fresh by both age criteria.

    Freshness requires:
      - msg_age_ms <= valid_until_ms  (message's own declared age within its window)
      - wall_delta_ms <= valid_until_ms  (wall-clock elapsed since callback <= window)

    Both criteria must hold; either alone is insufficient.
    A valid_until_ms <= 0 is always treated as invalid (unusable context).
    """
    if valid_until_ms <= 0:
        return False
    return msg_age_ms <= valid_until_ms and wall_delta_ms <= valid_until_ms


def add_warning_flag_once(flags: list, flag: str) -> None:
    """Append flag to flags in-place if not already present.

    Prevents duplicate entries when the same cached ObstacleTrack is published
    across multiple 20 Hz ticks while route context remains unusable.
    """
    if flag not in flags:
        flags.append(flag)


def remove_warning_flag(flags: list, flag: str) -> None:
    """Remove all occurrences of flag from flags in-place. No-op if absent.

    Called in _tick() when context becomes usable again so that a cached
    ObstacleTrack that previously carried ROUTE_CONTEXT_MISSING no longer
    does once fresh context arrives.
    """
    try:
        while True:
            flags.remove(flag)
    except ValueError:
        pass


def compute_ttc(
    distance_m: float,
    ego_speed_mps: float,
    obstacle_velocity_x: float,
) -> float:
    """Compute scalar TTC evidence (seconds).

    closing_speed = ego_speed_mps - obstacle_velocity_x

    Returns distance_m / closing_speed when:
      - closing_speed > _CLOSING_SPEED_MIN_MPS (0.1 m/s), AND
      - distance_m > 0

    Returns 0.0 otherwise (ego stopped, obstacle moving away/equal speed,
    or zero/negative distance).

    Perception publishes this as evidence only. Planner gates final action
    using in_path and its own path-projected TTC when needed.
    """
    closing_speed = ego_speed_mps - obstacle_velocity_x
    if closing_speed > _CLOSING_SPEED_MIN_MPS and distance_m > 0:
        return distance_m / closing_speed
    return 0.0
