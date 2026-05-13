# perception/colour_classifier.py
from typing import Tuple, List
#
# Sprint 1 / S1-4 — Pure-Python ROI colour classifier for traffic light detection.
# No ROS2, no OpenCV, no external dependencies beyond the Python standard library.
#
# Input:  raw image bytes (bgr8 or rgb8), image dimensions, bounding box.
# Output: (state, confidence, warning_flags)
#   state:          0=UNKNOWN, 1=RED, 2=YELLOW, 3=GREEN
#                   Matches TrafficLightState.UNKNOWN/RED/YELLOW/GREEN constants.
#   confidence:     float 0.0–1.0, capped at _CONFIDENCE_CAP (no temporal filter yet)
#   warning_flags:  list[str] from the standard set in wiki/contracts/timing_and_fallback.md
#
# Classification logic (channel-dominance, no HSV conversion required):
#   Compute per-channel averages over the bbox ROI.
#   YELLOW:  avg_r and avg_g each occupy > 30% of total; avg_b < 25% of total.
#   RED:     avg_r > 50% of total and at least 1.5× both avg_g and avg_b.
#   GREEN:   avg_g > 50% of total and at least 1.5× both avg_r and avg_b.
#   UNKNOWN: near-black ROI, no dominant pattern, or confidence < threshold.
#   Confidence: channel-dominance score, capped conservatively at _CONFIDENCE_CAP.
#   If confidence < 0.7 (contract §8), state is forced to UNKNOWN + LOW_CONFIDENCE.
#
# Contract ref: wiki/contracts/message_contracts.md §8 (TrafficLightState)
#               wiki/contracts/timing_and_fallback.md (standard warning flag set)
#               wiki/perception/traffic_light_node.md (confidence < 0.7 → UNKNOWN)

STATE_UNKNOWN = 0
STATE_RED = 1
STATE_YELLOW = 2
STATE_GREEN = 3

_CONFIDENCE_CAP = 0.85       # stub cap — do not overclaim without temporal confirmation
_MIN_BRIGHTNESS = 10.0       # skip near-black ROIs (total avg < threshold)
_CONFIDENCE_THRESHOLD = 0.7  # contract §8: below this → UNKNOWN
_SUPPORTED_ENCODINGS = frozenset({'bgr8', 'rgb8'})


def classify_roi(data, width, height, encoding, bbox_x, bbox_y, bbox_w, bbox_h, step=0):
    """
    Classify traffic light colour inside a bounding box ROI.

    Parameters
    ----------
    data : bytes-like
        Raw image payload, row-major, 3 bytes per pixel (bgr8 or rgb8).
    width, height : int
        Image dimensions in pixels.
    encoding : str
        'bgr8' or 'rgb8'.
    bbox_x, bbox_y, bbox_w, bbox_h : float
        Bounding box top-left origin and size in pixels.
        Clamped to [0, width) × [0, height) before sampling.
    step : int, optional
        Full row length in bytes (sensor_msgs/Image.step).  0 means
        tightly-packed rows (step == width * 3).  If provided and smaller
        than width * 3, SYNC_MISMATCH is returned.

    Returns
    -------
    Tuple[int, float, List[str]]
        (state, confidence, warning_flags)
    """
    if encoding not in _SUPPORTED_ENCODINGS:
        return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE', 'MODEL_ERROR']

    if encoding == 'bgr8':
        r_off, g_off, b_off = 2, 1, 0
    else:  # rgb8
        r_off, g_off, b_off = 0, 1, 2

    x0 = max(0, int(bbox_x))
    y0 = max(0, int(bbox_y))
    x1 = min(int(width), int(bbox_x + bbox_w))
    y1 = min(int(height), int(bbox_y + bbox_h))

    if x1 <= x0 or y1 <= y0:
        return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE', 'BBOX_MISSING']

    min_step = int(width) * 3
    step = int(step)
    if step <= 0:
        step = min_step
    elif step < min_step:
        return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE', 'SYNC_MISMATCH']

    if not isinstance(data, (bytes, bytearray)):
        data = bytes(data)

    if len(data) < int(height) * step:
        return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE', 'SYNC_MISMATCH']

    sum_r = sum_g = sum_b = 0
    count = (x1 - x0) * (y1 - y0)
    cols = x1 - x0

    for row in range(y0, y1):
        base = row * step + x0 * 3
        row_slice = data[base: base + cols * 3]
        sum_r += sum(row_slice[r_off::3])
        sum_g += sum(row_slice[g_off::3])
        sum_b += sum(row_slice[b_off::3])

    avg_r = sum_r / count
    avg_g = sum_g / count
    avg_b = sum_b / count
    total = avg_r + avg_g + avg_b

    if total < _MIN_BRIGHTNESS:
        return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE']

    r_ratio = avg_r / total
    g_ratio = avg_g / total
    b_ratio = avg_b / total

    # YELLOW: both R and G significant; B is low.
    # Check yellow before red because yellow has r_ratio ≈ 0.5 which would
    # not pass the RED r_ratio > 0.5 check, but safety-first ordering avoids
    # misclassifying warm-yellow as red when the ratios drift.
    if r_ratio > 0.3 and g_ratio > 0.3 and b_ratio < 0.25:
        raw_conf = min(avg_r, avg_g) / 255.0 * (1.0 - b_ratio)
        confidence = min(raw_conf, _CONFIDENCE_CAP)
        if confidence >= _CONFIDENCE_THRESHOLD:
            return STATE_YELLOW, confidence, []
        return STATE_UNKNOWN, confidence, ['LOW_CONFIDENCE']

    # RED: R dominant over both G and B.
    if r_ratio > 0.5 and avg_r > avg_g * 1.5 and avg_r > avg_b * 1.5:
        raw_conf = (avg_r - max(avg_g, avg_b)) / 255.0
        confidence = min(raw_conf, _CONFIDENCE_CAP)
        if confidence >= _CONFIDENCE_THRESHOLD:
            return STATE_RED, confidence, []
        return STATE_UNKNOWN, confidence, ['LOW_CONFIDENCE']

    # GREEN: G dominant over both R and B.
    if g_ratio > 0.5 and avg_g > avg_r * 1.5 and avg_g > avg_b * 1.5:
        raw_conf = (avg_g - max(avg_r, avg_b)) / 255.0
        confidence = min(raw_conf, _CONFIDENCE_CAP)
        if confidence >= _CONFIDENCE_THRESHOLD:
            return STATE_GREEN, confidence, []
        return STATE_UNKNOWN, confidence, ['LOW_CONFIDENCE']

    return STATE_UNKNOWN, 0.0, ['LOW_CONFIDENCE']
