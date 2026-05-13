# perception/lane_contract.py
#
# Sprint 2 / S2-A4 — ROS-free LaneModel contract helper.
#
# Centralises constants, warning-flag rules, lateral-mapping, and
# forward-point x-value generation for the lane_node MVP.
#
# No rclpy, sensor_msgs, std_msgs, geometry_msgs, or perception_msgs imports.
# Importable by unit tests without a ROS2 installation.
#
# Coordinate convention (base_link evidence, synthetic MVP):
#   x — forward (m), origin at ego front reference
#   y — left positive (m), image column 0 → y > 0, column width-1 → y < 0
#   z — 0.0 (ground-plane approximation)
#
# All values here that mirror timing_and_fallback.md or message_contracts.md
# are kept consistent with dummy_common.py; that file is the ROS-side
# authority and imports std_msgs, so it is NOT imported here.

# ---------------------------------------------------------------------------
# Timing / validity constants
# ---------------------------------------------------------------------------

VALID_UNTIL_LANE_MS: int = 500
NO_IMAGE_AGE_MS: int = 999_999          # sentinel: "no image ever received"

# ---------------------------------------------------------------------------
# Geometry constants for synthetic MVP mapping
# ---------------------------------------------------------------------------

DEFAULT_LANE_WIDTH_M: float = 3.7       # approximate standard road lane width
FORWARD_NEAR_M: float = 1.0            # first forward x value (m)
FORWARD_FAR_M: float = 10.0            # last forward x value (m)
FORWARD_STEP_M: float = 0.1            # point spacing (m)
SPACING_TOLERANCE_M: float = 1e-6      # float tolerance for spacing assertions
MIN_FORWARD_COVERAGE_M: float = 5.0    # minimum required x coverage (m)
MIN_POINT_COUNT: int = 50              # minimum required points per boundary

# ---------------------------------------------------------------------------
# Confidence threshold
# ---------------------------------------------------------------------------

CONFIDENCE_THRESHOLD: float = 0.7
# Below this value LOW_CONFIDENCE must appear in warning_flags.
# At or above this value (and both lanes detected) warning_flags must be [].

# ---------------------------------------------------------------------------
# Warning flag string constants
# ---------------------------------------------------------------------------

FLAG_LOW_CONFIDENCE: str = 'LOW_CONFIDENCE'
FLAG_STALE_MESSAGE: str = 'STALE_MESSAGE'
FLAG_LANE_BOUNDARY_MISSING: str = 'LANE_BOUNDARY_MISSING'
FLAG_NO_INPUT: str = 'NO_INPUT'

# Canonical flag sets — use these in lane_node so the strings are never
# duplicated across the codebase.
FLAGS_VALID_BOTH: list = []
FLAGS_BLANK: list = [FLAG_LOW_CONFIDENCE, FLAG_LANE_BOUNDARY_MISSING]
FLAGS_NO_INPUT: list = [FLAG_LOW_CONFIDENCE, FLAG_NO_INPUT]
FLAGS_STALE: list = [FLAG_LOW_CONFIDENCE, FLAG_STALE_MESSAGE]
FLAGS_PARTIAL: list = [FLAG_LOW_CONFIDENCE, FLAG_LANE_BOUNDARY_MISSING]

# ---------------------------------------------------------------------------
# Warning-flag decision function
# ---------------------------------------------------------------------------

_STATE_FLAG_MAP = {
    'valid_both': FLAGS_VALID_BOTH,
    'blank':      FLAGS_BLANK,
    'no_input':   FLAGS_NO_INPUT,
    'stale':      FLAGS_STALE,
    'partial':    FLAGS_PARTIAL,
}


def compute_warning_flags(state: str) -> list:
    """Return the warning-flag list for a given lane detection state.

    Parameters
    ----------
    state : one of 'valid_both', 'blank', 'no_input', 'stale', 'partial'.
        'valid_both' — both lane boundaries detected, confidence >= CONFIDENCE_THRESHOLD.
        'blank'      — no lanes detected in a fresh image.
        'no_input'   — no image has ever been received.
        'stale'      — image received previously but has now gone stale.
        'partial'    — exactly one boundary detected (confidence < CONFIDENCE_THRESHOLD).

    Returns
    -------
    list of str — warning flag strings (empty list when state == 'valid_both').

    Raises
    ------
    ValueError — if state is not a recognised key.
    """
    if state not in _STATE_FLAG_MAP:
        raise ValueError(
            f'Unknown lane state {state!r}. '
            f'Valid states: {sorted(_STATE_FLAG_MAP)}'
        )
    return list(_STATE_FLAG_MAP[state])

# ---------------------------------------------------------------------------
# Lateral mapping helpers
# ---------------------------------------------------------------------------


def col_to_lateral_m(col: int, width: int) -> float:
    """Map an image column index to a base_link lateral position (y axis).

    col=0            → y = +DEFAULT_LANE_WIDTH_M/2  (left edge)
    col=width-1      → y = -DEFAULT_LANE_WIDTH_M/2  (right edge)
    col=width//2     → y ≈ 0.0                      (image centre)

    MVP approximation: treats the image centre as base_link y=0.
    Real projection requires camera intrinsics + extrinsics + IPM.
    """
    return (0.5 - col / width) * DEFAULT_LANE_WIDTH_M


def compute_centerline_lateral(left_lat: float, right_lat: float) -> float:
    """Return the lateral midpoint between left and right boundaries."""
    return (left_lat + right_lat) / 2.0


def compute_lane_width_estimate(left_lat: float, right_lat: float) -> float:
    """Return the estimated lane width as abs(left_lat - right_lat).

    MVP note: synthetic approximate mapping only.  Real lane width requires
    calibrated IPM or stereo depth.  Future work post-UFLD-v2 integration.
    """
    return abs(left_lat - right_lat)

# ---------------------------------------------------------------------------
# Forward point x-value generator
# ---------------------------------------------------------------------------


def build_forward_x_values() -> list:
    """Return a list of x positions (floats, metres) for forward evidence points.

    Generates x ∈ [FORWARD_NEAR_M, FORWARD_FAR_M] at FORWARD_STEP_M intervals.
    The returned list satisfies all contract requirements:
      - len >= MIN_POINT_COUNT
      - x values are monotonically increasing
      - consecutive spacing <= FORWARD_STEP_M + SPACING_TOLERANCE_M
      - coverage (max − min) >= MIN_FORWARD_COVERAGE_M

    lane_node uses this to build geometry_msgs/Point arrays without re-encoding
    the boundary values here.
    """
    xs = []
    x = FORWARD_NEAR_M
    while x <= FORWARD_FAR_M + 1e-9:
        xs.append(x)
        x = round(x + FORWARD_STEP_M, 10)
    return xs
