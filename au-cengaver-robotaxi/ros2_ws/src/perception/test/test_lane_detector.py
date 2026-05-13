# test/test_lane_detector.py
#
# Sprint 2 / S2-A3 — Unit tests for lane_detector_utils.detect_lanes.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest cengaver_ws/src/perception/test/test_lane_detector.py -v

import types

from perception.lane_detector_utils import detect_lanes
from perception.lane_image_utils import (
    _LINE_LEFT_FRAC,
    _LINE_RIGHT_FRAC,
    build_lane_frame,
)

_W, _H = 640, 480


def _add_row_padding(data: bytes, width: int, height: int, padding: int) -> bytes:
    """Insert `padding` zero bytes after each row of tight bgr8 data."""
    tight_row = width * 3
    result = bytearray()
    for r in range(height):
        result.extend(data[r * tight_row: (r + 1) * tight_row])
        result.extend(bytes(padding))
    return bytes(result)


# ------------------------------------------------------------------
# Straight scenario — both lanes detected
# ------------------------------------------------------------------

def test_straight_detects_both_lanes():
    """Straight frame must yield non-None left_col and right_col with confidence=1.0."""
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3, 'bgr8')
    assert result['ok']
    assert result['left_col'] is not None, 'Left lane not detected in straight frame'
    assert result['right_col'] is not None, 'Right lane not detected in straight frame'
    assert result['confidence'] == 1.0


def test_straight_lane_positions_near_expected():
    """Detected columns must be within ±10 px of the lane_image_utils positions."""
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3, 'bgr8')
    expected_left = int(_LINE_LEFT_FRAC * _W)
    expected_right = int(_LINE_RIGHT_FRAC * _W)
    assert abs(result['left_col'] - expected_left) <= 10, (
        f'Left col {result["left_col"]} far from expected {expected_left}'
    )
    assert abs(result['right_col'] - expected_right) <= 10, (
        f'Right col {result["right_col"]} far from expected {expected_right}'
    )


# ------------------------------------------------------------------
# Blank scenario — no lanes detected
# ------------------------------------------------------------------

def test_blank_detects_no_lanes():
    """Blank frame must yield None for both columns and confidence=0.0."""
    data = build_lane_frame('blank', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3, 'bgr8')
    assert result['ok']
    assert result['left_col'] is None, 'Left lane falsely detected in blank frame'
    assert result['right_col'] is None, 'Right lane falsely detected in blank frame'
    assert result['confidence'] == 0.0


# ------------------------------------------------------------------
# Unsupported encoding
# ------------------------------------------------------------------

def test_unsupported_encoding_returns_failure():
    """An unsupported encoding must set ok=False, no columns, confidence=0.0."""
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3, 'rgb8')
    assert not result['ok'], 'Expected ok=False for unsupported encoding'
    assert result['left_col'] is None
    assert result['right_col'] is None
    assert result['confidence'] == 0.0
    assert 'rgb8' in result['error']


def test_mono8_encoding_returns_failure():
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3, 'mono8')
    assert not result['ok']
    assert 'mono8' in result['error']


# ------------------------------------------------------------------
# Padded row step
# ------------------------------------------------------------------

def test_padded_step_detects_lanes():
    """detect_lanes must handle a row stride larger than width*3 (e.g. 4-byte padding)."""
    padding = 4
    step = _W * 3 + padding
    tight = build_lane_frame('straight', _W, _H)
    padded = _add_row_padding(tight, _W, _H, padding)
    result = detect_lanes(padded, _W, _H, step, 'bgr8')
    assert result['ok'], f'Expected ok=True with padded step; got error: {result["error"]}'
    assert result['left_col'] is not None, 'Left lane not detected with padded step'
    assert result['right_col'] is not None, 'Right lane not detected with padded step'


def test_large_padded_step_detects_lanes():
    """Padding of 16 bytes per row must also work correctly."""
    padding = 16
    step = _W * 3 + padding
    tight = build_lane_frame('straight', _W, _H)
    padded = _add_row_padding(tight, _W, _H, padding)
    result = detect_lanes(padded, _W, _H, step, 'bgr8')
    assert result['ok']
    assert result['left_col'] is not None
    assert result['right_col'] is not None


def test_padded_blank_detects_no_lanes():
    """Padded blank frame must still yield no lane detections."""
    padding = 4
    step = _W * 3 + padding
    tight = build_lane_frame('blank', _W, _H)
    padded = _add_row_padding(tight, _W, _H, padding)
    result = detect_lanes(padded, _W, _H, step, 'bgr8')
    assert result['ok']
    assert result['left_col'] is None
    assert result['right_col'] is None


# ------------------------------------------------------------------
# Too-small step
# ------------------------------------------------------------------

def test_too_small_step_rejected():
    """A step smaller than width*3 must set ok=False."""
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, _W * 3 - 1, 'bgr8')
    assert not result['ok'], 'Expected ok=False for step < width*3'
    assert result['left_col'] is None
    assert result['right_col'] is None
    assert result['confidence'] == 0.0
    assert 'step' in result['error']


def test_step_of_zero_rejected():
    data = build_lane_frame('straight', _W, _H)
    result = detect_lanes(data, _W, _H, 0, 'bgr8')
    assert not result['ok']


# ------------------------------------------------------------------
# Short data buffer guard
# ------------------------------------------------------------------

def test_short_data_returns_failure():
    """Data shorter than step*height must set ok=False, no columns, confidence=0.0."""
    result = detect_lanes(b'abc', 640, 480, 640 * 3, 'bgr8')
    assert not result['ok'], 'Expected ok=False for data shorter than step*height'
    assert result['left_col'] is None
    assert result['right_col'] is None
    assert result['confidence'] == 0.0
    assert 'data' in result['error'] or 'length' in result['error'], (
        f'Expected error mentioning data/length; got: {result["error"]!r}'
    )


# ------------------------------------------------------------------
# ROS-free import check
# ------------------------------------------------------------------

def test_lane_detector_utils_has_no_ros_imports():
    """lane_detector_utils must not import any ROS2 namespace at module level."""
    import perception.lane_detector_utils as det_mod

    ros_namespaces = (
        'rclpy',
        'sensor_msgs',
        'std_msgs',
        'geometry_msgs',
        'perception_msgs',
    )
    mod_imports = {
        name
        for name, obj in vars(det_mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'lane_detector_utils imported ROS2 namespace {ns!r}'
        )
