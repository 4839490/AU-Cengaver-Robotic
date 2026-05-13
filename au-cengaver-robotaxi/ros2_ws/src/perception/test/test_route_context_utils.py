# test/test_route_context_utils.py
#
# S3-R1 — ROS-free unit tests for route_context_utils.py.
#
# All tests run without a ROS2 environment (no rclpy import).
#
# Test coverage (15 tests):
#
#   DEFAULTS and build_route_context_fields [9 tests]:
#     - build returns dict containing all canonical field keys
#     - default ego_speed_mps is 0.0
#     - default route_context_valid is True
#     - default valid_until_ms is 500
#     - default planned_trajectory is an empty list
#     - default route_direction is empty string
#     - build with no overrides matches DEFAULTS
#     - build with ego_speed_mps override reflects new value
#     - unknown field raises KeyError
#
#   validate_route_context [6 tests]:
#     - valid dict returns no errors
#     - missing ego_speed_mps returns error
#     - missing route_context_valid returns error
#     - wrong type for route_context_valid (int instead of bool) returns error
#     - valid_until_ms = 0 returns error
#     - valid_until_ms = -1 returns error

import pytest

from perception.route_context_utils import (
    DEFAULTS,
    build_route_context_fields,
    validate_route_context,
)

_EXPECTED_KEYS = {
    'active_waypoint_id',
    'target_x',
    'target_y',
    'target_heading',
    'planner_mode',
    'route_direction',
    'planned_trajectory',
    'lookahead_distance',
    'in_stop_zone',
    'distance_to_stop_zone',
    'localization_confidence',
    'ego_speed_mps',
    'route_context_valid',
    'age_ms',
    'valid_until_ms',
}


# ---------------------------------------------------------------------------
# DEFAULTS and build_route_context_fields
# ---------------------------------------------------------------------------

def test_build_returns_all_canonical_keys():
    result = build_route_context_fields()
    assert set(result.keys()) == _EXPECTED_KEYS


def test_default_ego_speed_mps_is_zero():
    result = build_route_context_fields()
    assert result['ego_speed_mps'] == 0.0


def test_default_route_context_valid_is_true():
    result = build_route_context_fields()
    assert result['route_context_valid'] is True


def test_default_valid_until_ms_is_500():
    result = build_route_context_fields()
    assert result['valid_until_ms'] == 500


def test_default_planned_trajectory_is_empty_list():
    result = build_route_context_fields()
    assert result['planned_trajectory'] == []


def test_default_route_direction_is_empty_string():
    result = build_route_context_fields()
    assert result['route_direction'] == ''


def test_build_no_overrides_matches_defaults():
    result = build_route_context_fields()
    for key, value in DEFAULTS.items():
        assert result[key] == value, f"Mismatch on {key!r}"


def test_build_override_ego_speed_mps():
    result = build_route_context_fields(ego_speed_mps=2.7)
    assert result['ego_speed_mps'] == 2.7


def test_build_unknown_field_raises_key_error():
    with pytest.raises(KeyError, match='not_a_field'):
        build_route_context_fields(not_a_field=99)


# ---------------------------------------------------------------------------
# validate_route_context
# ---------------------------------------------------------------------------

def _valid_dict() -> dict:
    return {
        'ego_speed_mps':       0.0,
        'route_context_valid': True,
        'age_ms':              0,
        'valid_until_ms':      500,
    }


def test_validate_returns_no_errors_for_valid_dict():
    errors = validate_route_context(_valid_dict())
    assert errors == []


def test_validate_missing_ego_speed_returns_error():
    d = _valid_dict()
    del d['ego_speed_mps']
    errors = validate_route_context(d)
    assert any('ego_speed_mps' in e for e in errors)


def test_validate_missing_route_context_valid_returns_error():
    d = _valid_dict()
    del d['route_context_valid']
    errors = validate_route_context(d)
    assert any('route_context_valid' in e for e in errors)


def test_validate_int_for_route_context_valid_returns_error():
    d = _valid_dict()
    d['route_context_valid'] = 1  # int, not bool
    errors = validate_route_context(d)
    assert any('route_context_valid' in e for e in errors)


def test_validate_zero_valid_until_ms_returns_error():
    d = _valid_dict()
    d['valid_until_ms'] = 0
    errors = validate_route_context(d)
    assert any('valid_until_ms' in e for e in errors)


def test_validate_negative_valid_until_ms_returns_error():
    d = _valid_dict()
    d['valid_until_ms'] = -1
    errors = validate_route_context(d)
    assert any('valid_until_ms' in e for e in errors)
