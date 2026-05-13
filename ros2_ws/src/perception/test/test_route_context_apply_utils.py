# test/test_route_context_apply_utils.py
#
# S3-R4 — ROS-free unit tests for route_context_apply_utils.py.
#
# All tests run without a ROS2 environment (plain pytest, no rclpy).
#
# Test coverage (8 tests):
#
#   apply_route_context_to_light:
#     1. missing context (None) → relevant_to_route=False, in_stop_zone=False,
#        distance_to_stop=0.0, ROUTE_CONTEXT_MISSING in flags
#     2. route_context_valid=False → same outcome
#     3. stale age_ms > valid_until_ms → same outcome
#     4. valid_until_ms=0 → same outcome (zero validity window always unusable)
#     5. usable context, in_stop_zone=True, distance_to_stop_zone=4.2 →
#        relevant_to_route=True, in_stop_zone=True, distance_to_stop≈4.2,
#        ROUTE_CONTEXT_MISSING NOT in flags
#     6. recovery: ROUTE_CONTEXT_MISSING added then removed on valid context;
#        unrelated warning flags (LOW_CONFIDENCE) are preserved throughout
#     7. existing warning flags preserved when adding ROUTE_CONTEXT_MISSING
#     8. duplicate ROUTE_CONTEXT_MISSING not added on repeated unusable ticks

import pytest

from perception.route_context_apply_utils import apply_route_context_to_light


# ---------------------------------------------------------------------------
# Minimal stub — mimics the fields used from planning_msgs/ActiveRouteContext
# ---------------------------------------------------------------------------

class _FakeCtx:
    def __init__(
        self,
        route_context_valid: bool = True,
        age_ms: int = 0,
        valid_until_ms: int = 500,
        in_stop_zone: bool = False,
        distance_to_stop_zone: float = 0.0,
    ) -> None:
        self.route_context_valid = route_context_valid
        self.age_ms = age_ms
        self.valid_until_ms = valid_until_ms
        self.in_stop_zone = in_stop_zone
        self.distance_to_stop_zone = distance_to_stop_zone


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

class TestApplyRouteContextToLight:

    def test_missing_context_sets_defaults_and_adds_flag(self):
        """context=None → conservative defaults + ROUTE_CONTEXT_MISSING in flags."""
        flags = []
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=None, wall_delta_ms=0.0
        )
        assert relevant is False
        assert in_zone is False
        assert dist == 0.0
        assert 'ROUTE_CONTEXT_MISSING' in flags

    def test_invalid_route_context_valid_false_adds_flag(self):
        """route_context_valid=False → same conservative result as missing context."""
        flags = []
        ctx = _FakeCtx(route_context_valid=False, age_ms=0, valid_until_ms=500)
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=ctx, wall_delta_ms=0.0
        )
        assert relevant is False
        assert in_zone is False
        assert dist == 0.0
        assert 'ROUTE_CONTEXT_MISSING' in flags

    def test_stale_age_ms_exceeds_valid_until_ms_adds_flag(self):
        """age_ms > valid_until_ms → stale; same conservative result."""
        flags = []
        ctx = _FakeCtx(route_context_valid=True, age_ms=600, valid_until_ms=500)
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=ctx, wall_delta_ms=0.0
        )
        assert relevant is False
        assert in_zone is False
        assert dist == 0.0
        assert 'ROUTE_CONTEXT_MISSING' in flags

    def test_zero_valid_until_ms_adds_flag(self):
        """valid_until_ms=0 → zero validity window is always unusable."""
        flags = []
        ctx = _FakeCtx(route_context_valid=True, age_ms=0, valid_until_ms=0)
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=ctx, wall_delta_ms=0.0
        )
        assert relevant is False
        assert in_zone is False
        assert dist == 0.0
        assert 'ROUTE_CONTEXT_MISSING' in flags

    def test_usable_context_sets_route_fields_and_removes_flag(self):
        """Fresh valid context → relevant_to_route=True, fields set, no flag."""
        flags = []
        ctx = _FakeCtx(
            route_context_valid=True,
            age_ms=0,
            valid_until_ms=500,
            in_stop_zone=True,
            distance_to_stop_zone=4.2,
        )
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=ctx, wall_delta_ms=0.0
        )
        assert relevant is True
        assert in_zone is True
        assert abs(dist - 4.2) < 1e-6
        assert 'ROUTE_CONTEXT_MISSING' not in flags

    def test_recovery_removes_flag_and_preserves_unrelated_flags(self):
        """After unusable context adds flag, usable context removes it; LOW_CONFIDENCE survives."""
        # Phase 1 — unusable context adds ROUTE_CONTEXT_MISSING.
        flags = ['LOW_CONFIDENCE']
        apply_route_context_to_light(flags, context=None, wall_delta_ms=0.0)
        assert 'ROUTE_CONTEXT_MISSING' in flags
        assert 'LOW_CONFIDENCE' in flags  # unrelated flag preserved

        # Phase 2 — usable context removes ROUTE_CONTEXT_MISSING.
        ctx = _FakeCtx(
            route_context_valid=True,
            age_ms=0,
            valid_until_ms=500,
            in_stop_zone=True,
            distance_to_stop_zone=4.2,
        )
        relevant, in_zone, dist = apply_route_context_to_light(
            flags, context=ctx, wall_delta_ms=0.0
        )
        assert 'ROUTE_CONTEXT_MISSING' not in flags
        assert 'LOW_CONFIDENCE' in flags  # must survive route-context removal
        assert relevant is True
        assert in_zone is True
        assert abs(dist - 4.2) < 1e-6

    def test_existing_warning_flags_preserved_when_adding_route_flag(self):
        """STALE_MESSAGE already present → ROUTE_CONTEXT_MISSING added alongside it."""
        flags = ['STALE_MESSAGE', 'LOW_CONFIDENCE']
        apply_route_context_to_light(flags, context=None, wall_delta_ms=0.0)
        assert 'ROUTE_CONTEXT_MISSING' in flags
        assert 'STALE_MESSAGE' in flags
        assert 'LOW_CONFIDENCE' in flags
        assert len(flags) == 3

    def test_duplicate_route_context_missing_not_added(self):
        """Calling with unusable context twice does not duplicate the flag."""
        flags = []
        for _ in range(3):
            apply_route_context_to_light(flags, context=None, wall_delta_ms=0.0)
        assert flags.count('ROUTE_CONTEXT_MISSING') == 1, (
            f'Expected exactly 1 entry; got {flags}'
        )
