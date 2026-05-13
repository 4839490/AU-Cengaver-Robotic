# test/test_stale_threshold.py
#
# Sprint 1 / S1-6 Codex fix — Unit tests for stale threshold resolution.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone:
#   pytest cengaver_ws/src/perception/test/test_stale_threshold.py -v

from perception.stale_utils import resolve_stale_ms

_VALID_UNTIL_MS = 300  # matches VALID_UNTIL_LIGHT_MS


# ------------------------------------------------------------------
# Required cases
# ------------------------------------------------------------------

def test_configured_500_clamped_to_300():
    """Configured 500 ms > valid_until_ms=300 → effective 300."""
    assert resolve_stale_ms(500, _VALID_UNTIL_MS) == 300


def test_configured_300_stays_300():
    """Configured 300 ms == valid_until_ms=300 → effective 300 (no clamp)."""
    assert resolve_stale_ms(300, _VALID_UNTIL_MS) == 300


def test_configured_100_stays_100():
    """Configured 100 ms < valid_until_ms=300 → effective 100 (tighter than validity)."""
    assert resolve_stale_ms(100, _VALID_UNTIL_MS) == 100


def test_configured_0_defaults_to_valid_until():
    """Configured 0 (invalid) → effective valid_until_ms=300."""
    assert resolve_stale_ms(0, _VALID_UNTIL_MS) == _VALID_UNTIL_MS


def test_configured_negative_defaults_to_valid_until():
    """Configured negative (invalid) → effective valid_until_ms=300."""
    assert resolve_stale_ms(-1, _VALID_UNTIL_MS) == _VALID_UNTIL_MS
    assert resolve_stale_ms(-999, _VALID_UNTIL_MS) == _VALID_UNTIL_MS


# ------------------------------------------------------------------
# Boundary conditions
# ------------------------------------------------------------------

def test_configured_1_stays_1():
    """Minimum positive value passes through unchanged."""
    assert resolve_stale_ms(1, _VALID_UNTIL_MS) == 1


def test_configured_299_stays_299():
    """One below valid_until_ms passes through unchanged."""
    assert resolve_stale_ms(299, _VALID_UNTIL_MS) == 299


def test_configured_301_clamped_to_300():
    """One above valid_until_ms is clamped."""
    assert resolve_stale_ms(301, _VALID_UNTIL_MS) == 300


def test_large_configured_clamped():
    """Very large configured value is clamped to valid_until_ms."""
    assert resolve_stale_ms(999_999, _VALID_UNTIL_MS) == _VALID_UNTIL_MS


def test_valid_until_200_clamps_to_200():
    """Clamping works for any valid_until_ms value (e.g. obstacle_tracks=200)."""
    assert resolve_stale_ms(500, 200) == 200
    assert resolve_stale_ms(200, 200) == 200
    assert resolve_stale_ms(100, 200) == 100
    assert resolve_stale_ms(0, 200) == 200
