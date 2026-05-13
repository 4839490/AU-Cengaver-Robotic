# test/test_ttc_utils.py
#
# S3-R2/S3-R3 — ROS-free unit tests for ttc_utils.py.
#
# All tests run without a ROS2 environment (no rclpy import).
#
# Test coverage (25 tests):
#
#   is_route_context_fresh [7 tests]:
#     - both criteria fresh → True
#     - both at limit → True
#     - msg age_ms > valid_until_ms (stale message age) → False
#     - wall_delta_ms > valid_until_ms (stale wall clock) → False
#     - both exceed valid_until_ms → False
#     - valid_until_ms=0 (zero validity window) → False
#     - valid_until_ms=-1 (negative validity window) → False
#
#   compute_ttc [9 tests]:
#     - ego 2.7 m/s, obstacle static (vx=0.0), distance 4.59 → ≈1.70 s
#     - ego 2.7 m/s, obstacle moving vx=1.0, distance 4.59 → ≈2.70 s
#     - ego stopped (0.0), obstacle static → 0.0
#     - obstacle moving faster than ego → 0.0
#     - obstacle moving at same speed as ego → 0.0
#     - distance <= 0 → 0.0
#     - closing speed exactly at threshold (0.1) → 0.0
#
#   add_warning_flag_once [5 tests]:  (S3-R3)
#     - add to empty list → flag present
#     - same flag already present → no duplicate
#     - different flag already present → new flag added alongside
#     - multiple calls → only one entry
#     - two different flags → both added
#
#   remove_warning_flag [4 tests]:  (S3-R3 Codex fix)
#     - removes existing flag
#     - no-op when flag absent
#     - preserves other flags
#     - no-op on empty list

import pytest

from perception.ttc_utils import (
    add_warning_flag_once,
    compute_ttc,
    is_route_context_fresh,
    remove_warning_flag,
)


# ---------------------------------------------------------------------------
# is_route_context_fresh
# ---------------------------------------------------------------------------

class TestIsRouteContextFresh:

    def test_both_fresh_returns_true(self):
        """Both message age and wall delta within valid_until_ms → fresh."""
        assert is_route_context_fresh(
            msg_age_ms=0, valid_until_ms=500, wall_delta_ms=0.0
        ) is True

    def test_both_at_limit_returns_true(self):
        """Values exactly equal to valid_until_ms are still considered fresh."""
        assert is_route_context_fresh(
            msg_age_ms=500, valid_until_ms=500, wall_delta_ms=500.0
        ) is True

    def test_stale_msg_age_returns_false(self):
        """msg_age_ms > valid_until_ms → stale even if wall delta is fresh."""
        assert is_route_context_fresh(
            msg_age_ms=600, valid_until_ms=500, wall_delta_ms=0.0
        ) is False

    def test_stale_wall_delta_returns_false(self):
        """wall_delta_ms > valid_until_ms → stale even if msg age is fresh."""
        assert is_route_context_fresh(
            msg_age_ms=0, valid_until_ms=500, wall_delta_ms=600.0
        ) is False

    def test_both_stale_returns_false(self):
        """Both criteria exceeded → stale."""
        assert is_route_context_fresh(
            msg_age_ms=600, valid_until_ms=500, wall_delta_ms=600.0
        ) is False

    def test_zero_valid_until_ms_returns_false(self):
        """valid_until_ms=0 → always False; zero validity window is unusable."""
        assert is_route_context_fresh(
            msg_age_ms=0, valid_until_ms=0, wall_delta_ms=0.0
        ) is False

    def test_negative_valid_until_ms_returns_false(self):
        """valid_until_ms=-1 → always False (invalid validity window)."""
        assert is_route_context_fresh(
            msg_age_ms=0, valid_until_ms=-1, wall_delta_ms=0.0
        ) is False


# ---------------------------------------------------------------------------
# compute_ttc
# ---------------------------------------------------------------------------

class TestComputeTtc:

    def test_static_obstacle_ego_2_7_dist_4_59(self):
        """ego=2.7 m/s, vx=0.0 (static), distance=4.59 → ttc ≈ 1.70 s.

        closing_speed = 2.7 - 0.0 = 2.7
        ttc = 4.59 / 2.7 ≈ 1.7 s
        """
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=2.7, obstacle_velocity_x=0.0)
        assert abs(ttc - 1.7) < 0.01, (
            f'Expected ttc ≈ 1.70 s for static obstacle; got {ttc:.4f}'
        )

    def test_moving_obstacle_vx_1_ego_2_7_dist_4_59(self):
        """ego=2.7 m/s, vx=1.0 (moving away at 1 m/s), distance=4.59 → ttc ≈ 2.70 s.

        closing_speed = 2.7 - 1.0 = 1.7
        ttc = 4.59 / 1.7 ≈ 2.70 s
        """
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=2.7, obstacle_velocity_x=1.0)
        assert abs(ttc - 2.7) < 0.01, (
            f'Expected ttc ≈ 2.70 s for moving obstacle vx=1.0; got {ttc:.4f}'
        )

    def test_ego_stopped_returns_zero(self):
        """ego=0.0, obstacle static → closing_speed=0.0 ≤ 0.1 → ttc=0.0."""
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=0.0, obstacle_velocity_x=0.0)
        assert ttc == 0.0, f'Expected ttc=0.0 when ego stopped; got {ttc}'

    def test_obstacle_moving_faster_than_ego_returns_zero(self):
        """Obstacle outrunning ego → negative closing speed → ttc=0.0."""
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=2.7, obstacle_velocity_x=3.0)
        assert ttc == 0.0, (
            f'Expected ttc=0.0 when obstacle faster than ego; got {ttc}'
        )

    def test_obstacle_same_speed_as_ego_returns_zero(self):
        """Equal speeds → closing_speed=0.0 ≤ 0.1 → ttc=0.0."""
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=2.7, obstacle_velocity_x=2.7)
        assert ttc == 0.0, (
            f'Expected ttc=0.0 when obstacle and ego at same speed; got {ttc}'
        )

    def test_zero_distance_returns_zero(self):
        """distance=0 → ttc=0.0 even with positive closing speed."""
        ttc = compute_ttc(distance_m=0.0, ego_speed_mps=2.7, obstacle_velocity_x=0.0)
        assert ttc == 0.0, f'Expected ttc=0.0 for zero distance; got {ttc}'

    def test_negative_distance_returns_zero(self):
        """distance<0 → ttc=0.0 (degenerate / obstacle behind bumper)."""
        ttc = compute_ttc(distance_m=-1.0, ego_speed_mps=2.7, obstacle_velocity_x=0.0)
        assert ttc == 0.0, f'Expected ttc=0.0 for negative distance; got {ttc}'

    def test_closing_speed_at_threshold_returns_zero(self):
        """closing_speed exactly 0.1 m/s is NOT above threshold → ttc=0.0."""
        ttc = compute_ttc(distance_m=4.59, ego_speed_mps=0.1, obstacle_velocity_x=0.0)
        assert ttc == 0.0, (
            f'Expected ttc=0.0 when closing_speed == 0.1 (not > threshold); got {ttc}'
        )

    def test_positive_ttc_proportional_to_distance(self):
        """Doubling distance doubles TTC — linearity check."""
        ttc1 = compute_ttc(distance_m=4.59, ego_speed_mps=2.7, obstacle_velocity_x=0.0)
        ttc2 = compute_ttc(distance_m=9.18, ego_speed_mps=2.7, obstacle_velocity_x=0.0)
        assert abs(ttc2 - 2 * ttc1) < 0.01, (
            f'TTC should scale linearly with distance; '
            f'ttc1={ttc1:.4f} ttc2={ttc2:.4f}'
        )


# ---------------------------------------------------------------------------
# add_warning_flag_once  (S3-R3)
# ---------------------------------------------------------------------------

class TestAddWarningFlagOnce:

    def test_add_to_empty_list(self):
        """Empty list → flag appended."""
        flags = []
        add_warning_flag_once(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags == ['ROUTE_CONTEXT_MISSING'], (
            f'Expected one entry; got {flags}'
        )

    def test_does_not_duplicate_same_flag(self):
        """Flag already present → list unchanged."""
        flags = ['ROUTE_CONTEXT_MISSING']
        add_warning_flag_once(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags == ['ROUTE_CONTEXT_MISSING'], (
            f'Flag must not be duplicated; got {flags}'
        )

    def test_adds_alongside_different_flag(self):
        """List with a different flag → new flag appended alongside."""
        flags = ['STALE_MESSAGE']
        add_warning_flag_once(flags, 'ROUTE_CONTEXT_MISSING')
        assert 'ROUTE_CONTEXT_MISSING' in flags
        assert 'STALE_MESSAGE' in flags
        assert len(flags) == 2

    def test_multiple_calls_idempotent(self):
        """Calling three times → flag appears exactly once."""
        flags = []
        for _ in range(3):
            add_warning_flag_once(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags.count('ROUTE_CONTEXT_MISSING') == 1, (
            f'Expected exactly 1 entry after 3 calls; got {flags}'
        )

    def test_two_different_flags_both_added(self):
        """Two distinct flags each added once → both present, count=2."""
        flags = []
        add_warning_flag_once(flags, 'ROUTE_CONTEXT_MISSING')
        add_warning_flag_once(flags, 'STALE_MESSAGE')
        assert len(flags) == 2
        assert 'ROUTE_CONTEXT_MISSING' in flags
        assert 'STALE_MESSAGE' in flags


# ---------------------------------------------------------------------------
# remove_warning_flag  (S3-R3 Codex fix)
# ---------------------------------------------------------------------------

class TestRemoveWarningFlag:

    def test_removes_existing_flag(self):
        """Flag present → removed; list is shorter by one."""
        flags = ['ROUTE_CONTEXT_MISSING']
        remove_warning_flag(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags == [], f'Expected empty list after removal; got {flags}'

    def test_noop_when_flag_absent(self):
        """Flag not present → list unchanged; no exception raised."""
        flags = ['STALE_MESSAGE']
        remove_warning_flag(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags == ['STALE_MESSAGE'], (
            f'Other flags must not be altered; got {flags}'
        )

    def test_preserves_other_flags(self):
        """Removes only the target flag; other flags survive."""
        flags = ['STALE_MESSAGE', 'ROUTE_CONTEXT_MISSING', 'TF_MISSING']
        remove_warning_flag(flags, 'ROUTE_CONTEXT_MISSING')
        assert 'ROUTE_CONTEXT_MISSING' not in flags
        assert 'STALE_MESSAGE' in flags
        assert 'TF_MISSING' in flags

    def test_noop_on_empty_list(self):
        """Empty list → no error, still empty."""
        flags = []
        remove_warning_flag(flags, 'ROUTE_CONTEXT_MISSING')
        assert flags == []
