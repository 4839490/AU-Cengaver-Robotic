# perception/lane_image_utils.py
#
# Sprint 2 / S2-A2 — ROS-free helper for building synthetic lane frames.
# Extracted from fake_lane_image_pub.py so unit tests can import this module
# without a ROS2 installation.
#
# No rclpy, sensor_msgs, std_msgs, or geometry_msgs imports here.

# BGR background value — neutral gray road surface.
_BACKGROUND_BGR = (80, 80, 80)

# BGR lane line value — bright white, clearly above any 200-threshold.
_LANE_LINE_BGR = (240, 240, 240)

# Lane line width in pixels and horizontal position as fraction of frame width.
_LINE_WIDTH_PX = 12
_LINE_LEFT_FRAC = 0.25   # centre of left lane line at 25% from left edge
_LINE_RIGHT_FRAC = 0.75  # centre of right lane line at 75% from left edge


def build_lane_frame(scenario: str, width: int, height: int) -> bytes:
    """Build a bgr8 bytearray for the given lane scenario.

    Returns bytes of length width * height * 3 (bgr8 encoding).

    Scenarios:
      straight — gray road background with two bright white vertical lane lines.
      blank    — uniform gray background with no lane lines.
      (any other value falls back to blank)
    """
    bg_b, bg_g, bg_r = _BACKGROUND_BGR
    data = bytearray([bg_b, bg_g, bg_r] * (width * height))

    if scenario == 'straight':
        ln_b, ln_g, ln_r = _LANE_LINE_BGR
        half = _LINE_WIDTH_PX // 2
        for frac in (_LINE_LEFT_FRAC, _LINE_RIGHT_FRAC):
            cx = int(frac * width)
            x0 = max(0, cx - half)
            x1 = min(width, cx + half + (_LINE_WIDTH_PX % 2))
            if x1 <= x0:
                continue
            row_fill = bytes([ln_b, ln_g, ln_r] * (x1 - x0))
            for row in range(height):
                base = row * width * 3 + x0 * 3
                data[base: base + len(row_fill)] = row_fill
    # 'blank' and unknown scenarios: leave data as pure background.

    return bytes(data)
