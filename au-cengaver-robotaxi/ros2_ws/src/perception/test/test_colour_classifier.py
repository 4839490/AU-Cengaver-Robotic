# test/test_colour_classifier.py
#
# Sprint 1 / S1-4 — Unit tests for the pure-Python ROI colour classifier.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (after `colcon build` + `source install/setup.bash`):
#   pytest cengaver_ws/src/perception/test/test_colour_classifier.py -v
#
# Run through colcon:
#   colcon test --packages-select perception
#   colcon test-result --verbose

from perception.colour_classifier import (
    STATE_GREEN,
    STATE_RED,
    STATE_UNKNOWN,
    STATE_YELLOW,
    classify_roi,
)


def _solid_frame(b, g, r, width=64, height=48):
    """Return a bgr8 bytearray filled with a single BGR colour."""
    return bytes([b, g, r] * (width * height))


def _rgb_solid_frame(r, g, b, width=64, height=48):
    """Return an rgb8 bytearray filled with a single RGB colour."""
    return bytes([r, g, b] * (width * height))


def _padded_frame(b, g, r, width=64, height=48, pad=4):
    """Return a bgr8 frame with `pad` zero bytes of row padding (step = width*3+pad)."""
    row = bytes([b, g, r] * width) + bytes(pad)
    return row * height


# ------------------------------------------------------------------
# Happy-path: bright synthetic colours, bgr8
# ------------------------------------------------------------------

def test_red_bgr8():
    data = _solid_frame(b=0, g=0, r=255)
    state, conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_RED
    assert conf >= 0.7
    assert 'LOW_CONFIDENCE' not in flags


def test_green_bgr8():
    data = _solid_frame(b=0, g=255, r=0)
    state, conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_GREEN
    assert conf >= 0.7
    assert 'LOW_CONFIDENCE' not in flags


def test_yellow_bgr8():
    data = _solid_frame(b=0, g=255, r=255)
    state, conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_YELLOW
    assert conf >= 0.7
    assert 'LOW_CONFIDENCE' not in flags


def test_unknown_gray_bgr8():
    data = _solid_frame(b=128, g=128, r=128)
    state, _conf, _flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_UNKNOWN


# ------------------------------------------------------------------
# Happy-path: rgb8 encoding
# ------------------------------------------------------------------

def test_red_rgb8():
    data = _rgb_solid_frame(r=255, g=0, b=0)
    state, conf, flags = classify_roi(data, 64, 48, 'rgb8', 0, 0, 64, 48)
    assert state == STATE_RED
    assert conf >= 0.7


def test_green_rgb8():
    data = _rgb_solid_frame(r=0, g=255, b=0)
    state, conf, flags = classify_roi(data, 64, 48, 'rgb8', 0, 0, 64, 48)
    assert state == STATE_GREEN
    assert conf >= 0.7


def test_yellow_rgb8():
    data = _rgb_solid_frame(r=255, g=255, b=0)
    state, conf, flags = classify_roi(data, 64, 48, 'rgb8', 0, 0, 64, 48)
    assert state == STATE_YELLOW
    assert conf >= 0.7


# ------------------------------------------------------------------
# Confidence cap
# ------------------------------------------------------------------

def test_confidence_capped_below_1():
    data = _solid_frame(b=0, g=0, r=255)
    _, conf, _ = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert conf <= 0.85


# ------------------------------------------------------------------
# Error / edge cases
# ------------------------------------------------------------------

def test_unsupported_encoding():
    data = b'\x00' * (64 * 48 * 1)
    state, _conf, flags = classify_roi(data, 64, 48, 'mono8', 0, 0, 64, 48)
    assert state == STATE_UNKNOWN
    assert 'MODEL_ERROR' in flags


def test_bbox_completely_out_of_bounds():
    data = _solid_frame(b=0, g=0, r=255)
    # bbox origin beyond image dimensions
    state, _conf, flags = classify_roi(data, 64, 48, 'bgr8', 200, 200, 50, 50)
    assert state == STATE_UNKNOWN
    assert 'BBOX_MISSING' in flags


def test_bbox_clamped_to_partial_overlap():
    # bbox partially outside — clamped portion is still green → GREEN
    data = _solid_frame(b=0, g=255, r=0)
    state, conf, _flags = classify_roi(data, 64, 48, 'bgr8', 50, 40, 30, 20)
    assert state == STATE_GREEN
    assert conf >= 0.7


def test_truncated_data_sync_mismatch():
    data = b'\x00' * 10  # far too short for 64×48×3
    state, _conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 10, 10)
    assert state == STATE_UNKNOWN
    assert 'SYNC_MISMATCH' in flags


def test_near_black_roi_unknown():
    data = _solid_frame(b=1, g=1, r=1)  # total avg = 3 < _MIN_BRIGHTNESS (10)
    state, _conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_UNKNOWN
    assert 'LOW_CONFIDENCE' in flags


def test_bytearray_input():
    # Verify bytearray input (not bytes) is handled
    data = bytearray(_solid_frame(b=0, g=255, r=0))
    state, conf, _ = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48)
    assert state == STATE_GREEN
    assert conf >= 0.7


# ------------------------------------------------------------------
# Row-stride (padded step) support
# ------------------------------------------------------------------

def test_padded_row_step_red():
    # step = width*3 + 4 padding bytes per row; classifier must use step, not width*3
    width, height, pad = 64, 48, 4
    step = width * 3 + pad
    data = _padded_frame(b=0, g=0, r=255, width=width, height=height, pad=pad)
    state, conf, flags = classify_roi(data, width, height, 'bgr8', 0, 0, width, height, step=step)
    assert state == STATE_RED
    assert conf >= 0.7
    assert 'LOW_CONFIDENCE' not in flags


def test_step_too_small_sync_mismatch():
    # Explicitly providing a step smaller than width*3 → SYNC_MISMATCH
    data = _solid_frame(b=0, g=0, r=255)
    state, _conf, flags = classify_roi(data, 64, 48, 'bgr8', 0, 0, 64, 48, step=64 * 3 - 1)
    assert state == STATE_UNKNOWN
    assert 'SYNC_MISMATCH' in flags
