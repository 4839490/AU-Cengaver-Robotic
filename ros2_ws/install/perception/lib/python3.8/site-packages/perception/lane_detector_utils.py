# perception/lane_detector_utils.py
#
# Sprint 2 / S2-A3 — ROS-free lane detection helper for lane_node.
#
# No rclpy, sensor_msgs, std_msgs, geometry_msgs, or perception_msgs imports.
# Accepts raw image bytes plus width, height, step, encoding.
#
# Detection algorithm:
#   1. Validate encoding (only bgr8 supported).
#   2. Validate step >= width * 3 (reject under-sized stride).
#   3. Build per-column mean brightness score using row-sampled pixels.
#      Using every _ROW_SAMPLE_STRIDE-th row for speed; accuracy is sufficient
#      for synthetic full-column lane lines.
#   4. Find the brightest column above _BRIGHT_THRESHOLD in each image half.
#   5. Return detected column centres (or None) and a confidence score.
#
# The return dict is intentionally plain Python — no ROS types — so lane_node
# can decide how to map columns into geometry_msgs/Point arrays.

# Mean channel brightness above which a column is treated as a lane candidate.
_BRIGHT_THRESHOLD = 200

# Sample every Nth row when scoring columns (trades accuracy for speed).
_ROW_SAMPLE_STRIDE = 4

# Only bgr8 is implemented for the synthetic MVP.
_SUPPORTED_ENCODINGS = frozenset({'bgr8'})


def detect_lanes(
    data: bytes,
    width: int,
    height: int,
    step: int,
    encoding: str,
) -> dict:
    """Detect lane line columns from a raw image buffer.

    Parameters
    ----------
    data     : raw image bytes (length must be >= step * height).
    width    : image width in pixels.
    height   : image height in pixels.
    step     : row stride in bytes (may include end-of-row padding;
               must be >= width * 3).
    encoding : pixel encoding string; only 'bgr8' is supported.

    Returns
    -------
    dict with keys:
        ok        (bool)      – False if encoding is unsupported or step is
                                smaller than width * 3.
        error     (str)       – human-readable reason; empty string when ok=True.
        left_col  (int|None)  – pixel column of left lane line centre, or None.
        right_col (int|None)  – pixel column of right lane line centre, or None.
        confidence (float)    – 0.0 (none), 0.5 (one line), 1.0 (both lines).
    """
    if encoding not in _SUPPORTED_ENCODINGS:
        return {
            'ok': False,
            'error': f'unsupported encoding: {encoding!r}',
            'left_col': None,
            'right_col': None,
            'confidence': 0.0,
        }

    min_step = width * 3
    if step < min_step:
        return {
            'ok': False,
            'error': f'step {step} < width*3 = {min_step}: row stride is too small',
            'left_col': None,
            'right_col': None,
            'confidence': 0.0,
        }

    min_data_len = step * height
    if len(data) < min_data_len:
        return {
            'ok': False,
            'error': (
                f'data length {len(data)} < step*height = {min_data_len}: '
                'image data buffer is too short'
            ),
            'left_col': None,
            'right_col': None,
            'confidence': 0.0,
        }

    # Accumulate per-column mean brightness (B+G+R)/3, sampled across rows.
    col_scores = [0.0] * width
    sampled_rows = range(0, height, _ROW_SAMPLE_STRIDE)
    n_samples = max(len(sampled_rows), 1)

    for r in sampled_rows:
        row_base = r * step
        for c in range(width):
            base = row_base + c * 3
            col_scores[c] += (data[base] + data[base + 1] + data[base + 2]) / 3.0

    col_scores = [s / n_samples for s in col_scores]

    # Find the brightest column above threshold in each image half.
    mid = width // 2
    left_col = _find_peak_col(col_scores, 0, mid)
    right_col = _find_peak_col(col_scores, mid, width)

    if left_col is not None and right_col is not None:
        confidence = 1.0
    elif left_col is not None or right_col is not None:
        confidence = 0.5
    else:
        confidence = 0.0

    return {
        'ok': True,
        'error': '',
        'left_col': left_col,
        'right_col': right_col,
        'confidence': confidence,
    }


def _find_peak_col(scores: list, start: int, end: int):
    """Return the column with the highest score above _BRIGHT_THRESHOLD in [start, end)."""
    best_col = None
    best_score = _BRIGHT_THRESHOLD
    for c in range(start, end):
        if scores[c] > best_score:
            best_score = scores[c]
            best_col = c
    return best_col
