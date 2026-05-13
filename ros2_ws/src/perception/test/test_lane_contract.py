# test/test_lane_contract.py
#
# Sprint 2 / S2-A4 — Contract-level unit tests for lane_contract.py helpers.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest \
#       cengaver_ws/src/perception/test/test_lane_contract.py -v

import types

from perception.lane_contract import (
    CONFIDENCE_THRESHOLD,
    DEFAULT_LANE_WIDTH_M,
    FLAG_LANE_BOUNDARY_MISSING,
    FLAG_LOW_CONFIDENCE,
    FLAG_NO_INPUT,
    FLAG_STALE_MESSAGE,
    FORWARD_STEP_M,
    MIN_FORWARD_COVERAGE_M,
    MIN_POINT_COUNT,
    NO_IMAGE_AGE_MS,
    SPACING_TOLERANCE_M,
    VALID_UNTIL_LANE_MS,
    build_forward_x_values,
    col_to_lateral_m,
    compute_centerline_lateral,
    compute_lane_width_estimate,
    compute_warning_flags,
)

# -----------------------------------------------------------------------
# Forward x-value generation — point contract
# -----------------------------------------------------------------------

def test_forward_x_count_at_least_50():
    """Generated x values must satisfy MIN_POINT_COUNT (>= 50)."""
    xs = build_forward_x_values()
    assert len(xs) >= MIN_POINT_COUNT, (
        f'Expected >= {MIN_POINT_COUNT} points, got {len(xs)}'
    )


def test_forward_x_monotonically_increasing():
    """Consecutive x values must be strictly increasing."""
    xs = build_forward_x_values()
    for i in range(len(xs) - 1):
        assert xs[i] < xs[i + 1], (
            f'x not monotonically increasing at index {i}: '
            f'{xs[i]} >= {xs[i+1]}'
        )


def test_forward_x_max_spacing():
    """Consecutive spacing must not exceed FORWARD_STEP_M + SPACING_TOLERANCE_M."""
    xs = build_forward_x_values()
    for i in range(len(xs) - 1):
        spacing = xs[i + 1] - xs[i]
        assert spacing <= FORWARD_STEP_M + SPACING_TOLERANCE_M, (
            f'Spacing {spacing:.9f} > {FORWARD_STEP_M} + {SPACING_TOLERANCE_M} '
            f'at index {i}'
        )


def test_forward_x_coverage_at_least_5m():
    """x range (max − min) must be >= MIN_FORWARD_COVERAGE_M (5.0 m)."""
    xs = build_forward_x_values()
    coverage = max(xs) - min(xs)
    assert coverage >= MIN_FORWARD_COVERAGE_M, (
        f'Forward coverage {coverage:.3f} m < required {MIN_FORWARD_COVERAGE_M} m'
    )


def test_forward_x_starts_at_1m():
    """First x value must be 1.0 m (FORWARD_NEAR_M)."""
    xs = build_forward_x_values()
    assert abs(xs[0] - 1.0) < SPACING_TOLERANCE_M


def test_forward_x_ends_at_10m():
    """Last x value must be approximately 10.0 m (FORWARD_FAR_M)."""
    xs = build_forward_x_values()
    assert abs(xs[-1] - 10.0) < 1e-6


def test_forward_x_deterministic():
    """Repeated calls return identical lists."""
    xs1 = build_forward_x_values()
    xs2 = build_forward_x_values()
    assert xs1 == xs2

# -----------------------------------------------------------------------
# Lateral column mapping
# -----------------------------------------------------------------------

def test_col_to_lateral_left_edge_positive():
    """Column 0 (left image edge) maps to positive y (left in base_link)."""
    lat = col_to_lateral_m(0, 640)
    assert lat > 0.0, f'Expected lat > 0 for column 0, got {lat}'


def test_col_to_lateral_right_edge_negative():
    """Column width-1 (right image edge) maps to negative y."""
    lat = col_to_lateral_m(639, 640)
    assert lat < 0.0, f'Expected lat < 0 for column 639, got {lat}'


def test_col_to_lateral_center_near_zero():
    """Column width//2 maps close to y=0."""
    lat = col_to_lateral_m(320, 640)
    assert abs(lat) < 0.01, f'Expected lat ≈ 0 for center column, got {lat}'


def test_col_to_lateral_range_bounded_by_default_lane_width():
    """Lateral values must stay within ±DEFAULT_LANE_WIDTH_M/2."""
    half = DEFAULT_LANE_WIDTH_M / 2.0
    for col in [0, 160, 320, 480, 639]:
        lat = col_to_lateral_m(col, 640)
        assert -half - 1e-9 <= lat <= half + 1e-9, (
            f'col_to_lateral_m({col}, 640) = {lat} outside ±{half}'
        )


# -----------------------------------------------------------------------
# Lane width estimate
# -----------------------------------------------------------------------

def test_lane_width_estimate_abs_diff():
    """Width estimate equals abs(left_lat - right_lat)."""
    left_lat = 1.85
    right_lat = -1.85
    w = compute_lane_width_estimate(left_lat, right_lat)
    assert abs(w - abs(left_lat - right_lat)) < 1e-9


def test_lane_width_estimate_symmetric():
    """Order of arguments must not affect the result."""
    a, b = 0.9, -0.9
    assert compute_lane_width_estimate(a, b) == compute_lane_width_estimate(b, a)


def test_lane_width_estimate_zero_when_same():
    """Identical lateral positions yield width estimate = 0.0."""
    assert compute_lane_width_estimate(1.0, 1.0) == 0.0


def test_lane_width_estimate_matches_node_synthetic_output():
    """Width for fake_lane_image_pub straight scenario matches synthetic columns.

    left_col  = int(0.25 * 640) = 160
    right_col = int(0.75 * 640) = 480
    Lateral values computed via col_to_lateral_m.
    """
    width = 640
    left_lat = col_to_lateral_m(160, width)
    right_lat = col_to_lateral_m(480, width)
    w = compute_lane_width_estimate(left_lat, right_lat)
    expected = abs(left_lat - right_lat)
    assert abs(w - expected) < 1e-9

# -----------------------------------------------------------------------
# Centerline lateral
# -----------------------------------------------------------------------

def test_centerline_y_is_midpoint_symmetric():
    """Symmetric left/right boundaries → centerline y = 0.0."""
    left_lat = 1.5
    right_lat = -1.5
    center = compute_centerline_lateral(left_lat, right_lat)
    assert abs(center - 0.0) < 1e-9, f'Expected 0.0, got {center}'


def test_centerline_y_is_midpoint_asymmetric():
    """Asymmetric boundaries → midpoint matches arithmetic mean."""
    left_lat = 2.0
    right_lat = 1.0
    center = compute_centerline_lateral(left_lat, right_lat)
    expected = (left_lat + right_lat) / 2.0
    assert abs(center - expected) < 1e-9


def test_centerline_y_between_left_and_right():
    """Centerline y must lie between left and right lateral values."""
    left_lat = 1.2
    right_lat = -0.8
    center = compute_centerline_lateral(left_lat, right_lat)
    lo, hi = min(left_lat, right_lat), max(left_lat, right_lat)
    assert lo <= center <= hi, (
        f'centerline {center} not between {lo} and {hi}'
    )

# -----------------------------------------------------------------------
# Warning flag rules
# -----------------------------------------------------------------------

def test_warning_flags_valid_both_empty():
    """Both lanes detected at confidence >= 0.7 → warning_flags must be []."""
    flags = compute_warning_flags('valid_both')
    assert flags == [], f'Expected [], got {flags}'


def test_warning_flags_blank_contains_low_confidence():
    flags = compute_warning_flags('blank')
    assert FLAG_LOW_CONFIDENCE in flags


def test_warning_flags_blank_contains_boundary_missing():
    flags = compute_warning_flags('blank')
    assert FLAG_LANE_BOUNDARY_MISSING in flags


def test_warning_flags_no_input_contains_low_confidence():
    flags = compute_warning_flags('no_input')
    assert FLAG_LOW_CONFIDENCE in flags


def test_warning_flags_no_input_contains_no_input():
    flags = compute_warning_flags('no_input')
    assert FLAG_NO_INPUT in flags


def test_warning_flags_stale_contains_low_confidence():
    flags = compute_warning_flags('stale')
    assert FLAG_LOW_CONFIDENCE in flags


def test_warning_flags_stale_contains_stale_message():
    flags = compute_warning_flags('stale')
    assert FLAG_STALE_MESSAGE in flags


def test_warning_flags_partial_contains_low_confidence():
    flags = compute_warning_flags('partial')
    assert FLAG_LOW_CONFIDENCE in flags


def test_warning_flags_partial_contains_boundary_missing():
    flags = compute_warning_flags('partial')
    assert FLAG_LANE_BOUNDARY_MISSING in flags


def test_warning_flags_no_input_excludes_stale():
    """NO_INPUT and STALE_MESSAGE must not appear together."""
    flags = compute_warning_flags('no_input')
    assert FLAG_STALE_MESSAGE not in flags


def test_warning_flags_stale_excludes_no_input():
    flags = compute_warning_flags('stale')
    assert FLAG_NO_INPUT not in flags


def test_warning_flags_unknown_state_raises():
    """An unrecognised state string must raise ValueError."""
    try:
        compute_warning_flags('flying')
        assert False, 'Expected ValueError'
    except ValueError:
        pass


def test_warning_flags_returns_new_list():
    """compute_warning_flags must return a new list each call (not a shared reference)."""
    flags_a = compute_warning_flags('blank')
    flags_b = compute_warning_flags('blank')
    flags_a.append('EXTRA')
    assert 'EXTRA' not in flags_b, 'compute_warning_flags returned a shared mutable list'

# -----------------------------------------------------------------------
# Constants
# -----------------------------------------------------------------------

def test_valid_until_lane_ms_is_500():
    assert VALID_UNTIL_LANE_MS == 500


def test_no_image_age_ms_sentinel():
    assert NO_IMAGE_AGE_MS == 999_999


def test_confidence_threshold_is_0_7():
    assert CONFIDENCE_THRESHOLD == 0.7

# -----------------------------------------------------------------------
# ROS-free import check
# -----------------------------------------------------------------------

def test_lane_contract_has_no_ros_imports():
    """lane_contract must not import any ROS2 namespace at module level."""
    import perception.lane_contract as mod

    ros_namespaces = (
        'rclpy',
        'sensor_msgs',
        'std_msgs',
        'geometry_msgs',
        'perception_msgs',
    )
    mod_imports = {
        name
        for name, obj in vars(mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'lane_contract imported ROS2 namespace {ns!r}'
        )
