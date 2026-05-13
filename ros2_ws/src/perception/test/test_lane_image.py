# test/test_lane_image.py
#
# Sprint 2 / S2-A2 — Unit tests for lane_image_utils.build_lane_frame.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest cengaver_ws/src/perception/test/test_lane_image.py -v

import types

from perception.lane_image_utils import (
    _BACKGROUND_BGR,
    _LANE_LINE_BGR,
    _LINE_LEFT_FRAC,
    _LINE_RIGHT_FRAC,
    _LINE_WIDTH_PX,
    build_lane_frame,
)

_W, _H = 640, 480
_EXPECTED_LEN = _W * _H * 3

# Threshold above which a BGR channel value is considered "bright" (lane line).
_BRIGHT_THRESHOLD = 200
# Background channels are 80; any value above 150 is "non-background" for the
# blank-scenario test.
_BACKGROUND_MAX = 150


# ------------------------------------------------------------------
# Buffer size
# ------------------------------------------------------------------

def test_straight_frame_correct_size():
    data = build_lane_frame('straight', _W, _H)
    assert len(data) == _EXPECTED_LEN, (
        f'Expected {_EXPECTED_LEN} bytes, got {len(data)}'
    )


def test_blank_frame_correct_size():
    data = build_lane_frame('blank', _W, _H)
    assert len(data) == _EXPECTED_LEN


def test_unknown_scenario_correct_size():
    """Unknown scenario falls back to blank; still returns correct buffer size."""
    data = build_lane_frame('unknown_xyz', _W, _H)
    assert len(data) == _EXPECTED_LEN


def test_small_frame_size():
    """Frame builder works for non-standard dimensions."""
    data = build_lane_frame('straight', 32, 24)
    assert len(data) == 32 * 24 * 3


# ------------------------------------------------------------------
# Straight scenario — lane lines must be present
# ------------------------------------------------------------------

def test_straight_has_bright_pixels():
    """Straight scenario must contain pixel channels at or above the bright threshold."""
    data = build_lane_frame('straight', _W, _H)
    assert max(data) >= _BRIGHT_THRESHOLD, (
        f'Expected at least one channel value >= {_BRIGHT_THRESHOLD} '
        f'in straight scenario; max found: {max(data)}'
    )


def test_straight_lane_line_pixels_at_expected_x():
    """Lane line pixels appear at expected horizontal positions."""
    data = build_lane_frame('straight', _W, _H)
    half = _LINE_WIDTH_PX // 2
    ln_b, ln_g, ln_r = _LANE_LINE_BGR

    for frac in (_LINE_LEFT_FRAC, _LINE_RIGHT_FRAC):
        cx = int(frac * _W)
        # Sample the centre pixel of the lane line in the first row.
        row = 0
        base = (row * _W + cx) * 3
        b, g, r = data[base], data[base + 1], data[base + 2]
        assert (b, g, r) == (ln_b, ln_g, ln_r), (
            f'Expected lane-line BGR {(ln_b, ln_g, ln_r)} at '
            f'x={cx} (frac={frac}), got ({b},{g},{r})'
        )


def test_straight_background_pixels_between_lines():
    """Pixels between the two lane lines retain the background colour."""
    data = build_lane_frame('straight', _W, _H)
    bg_b, bg_g, bg_r = _BACKGROUND_BGR

    # Sample in the middle of the road, between the two lines.
    mid_x = _W // 2
    row = _H // 2
    base = (row * _W + mid_x) * 3
    b, g, r = data[base], data[base + 1], data[base + 2]
    assert (b, g, r) == (bg_b, bg_g, bg_r), (
        f'Expected background BGR {(bg_b, bg_g, bg_r)} at mid-road '
        f'x={mid_x}, row={row}; got ({b},{g},{r})'
    )


# ------------------------------------------------------------------
# Blank scenario — no bright lane pixels
# ------------------------------------------------------------------

def test_blank_has_no_bright_pixels():
    """Blank scenario must contain no pixel channel value above the background max."""
    data = build_lane_frame('blank', _W, _H)
    assert max(data) <= _BACKGROUND_MAX, (
        f'Expected all channel values <= {_BACKGROUND_MAX} in blank scenario; '
        f'max found: {max(data)}'
    )


def test_blank_is_uniform_background():
    """Every pixel in the blank frame equals the background BGR value."""
    data = build_lane_frame('blank', _W, _H)
    bg_b, bg_g, bg_r = _BACKGROUND_BGR
    expected = bytes([bg_b, bg_g, bg_r] * (_W * _H))
    assert data == expected, 'Blank frame contains unexpected non-background pixels'


# ------------------------------------------------------------------
# Unknown / fallback scenario
# ------------------------------------------------------------------

def test_unknown_scenario_falls_back_to_blank():
    """An unrecognised scenario produces the same output as 'blank'."""
    unknown_data = build_lane_frame('does_not_exist', _W, _H)
    blank_data = build_lane_frame('blank', _W, _H)
    assert unknown_data == blank_data, (
        'Unknown scenario did not fall back to blank output'
    )


# ------------------------------------------------------------------
# bgr8 encoding contract
# ------------------------------------------------------------------

def test_straight_frame_is_bytes():
    """build_lane_frame returns bytes (not bytearray), matching Image.data type."""
    data = build_lane_frame('straight', _W, _H)
    assert isinstance(data, bytes)


def test_blank_frame_is_bytes():
    data = build_lane_frame('blank', _W, _H)
    assert isinstance(data, bytes)


# ------------------------------------------------------------------
# ROS-free import check
# ------------------------------------------------------------------

def test_lane_image_utils_has_no_ros_imports():
    """lane_image_utils must not pull in any ROS2 packages at module level."""
    import sys
    import perception.lane_image_utils as utils_mod

    ros_namespaces = ('rclpy', 'sensor_msgs', 'std_msgs', 'geometry_msgs')
    loaded = set(sys.modules.keys())
    # Collect the module's own imports via its __dict__ (only module objects).
    mod_imports = {
        name
        for name, obj in vars(utils_mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'lane_image_utils imported ROS2 namespace {ns!r}'
        )
