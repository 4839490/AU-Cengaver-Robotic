# perception/pointcloud_utils.py
#
# Sprint 2 / S2-B2 — ROS-free helper for building synthetic VLP-16-style
# PointCloud2 data buffers.  Extracted so unit tests can import this module
# without a ROS2 installation.
#
# No rclpy, sensor_msgs, std_msgs, or geometry_msgs imports here.

import struct as _struct

# PointCloud2 field layout — matches sensor_msgs/PointField FLOAT32 (datatype=7).
# Fields in order: x, y, z, intensity.  Each is 4 bytes (float32 little-endian).
POINT_STEP: int = 16  # 4 fields × 4 bytes
FIELDS: tuple = ('x', 'y', 'z', 'intensity')  # order matches byte offsets 0/4/8/12

_PACK: _struct.Struct = _struct.Struct('<ffff')  # little-endian, 4 × float32


def _pack(x: float, y: float, z: float, intensity: float = 100.0) -> bytes:
    return _PACK.pack(x, y, z, intensity)


# ---------------------------------------------------------------------------
# Scenario builders
# ---------------------------------------------------------------------------

def _empty() -> tuple:
    """Zero-point cloud.  Returns (b'', 0)."""
    return b'', 0


def _simple_obstacle() -> tuple:
    """Synthetic VLP-16-style scene with a ground plane and one obstacle cluster.

    Ground plane (z = 0.0):
        4×4 = 16 points  — x ∈ {3.0, 4.0, 5.0, 6.0}, y ∈ {-1.5, -0.5, 0.5, 1.5}
        intensity = 50.0 (low reflectance, typical asphalt)

    Obstacle cluster (z > 0.2):
        3 × 3 = 9 points — x = 5.0, y ∈ {-0.3, 0.0, 0.3}, z ∈ {0.5, 1.0, 1.5}
        intensity = 200.0 (high reflectance, retroreflective tape / painted surface)

    Total: 25 points, all above-ground points have z ≥ 0.5.
    """
    buf = bytearray()

    # Ground plane
    for xi in range(4):
        x = 3.0 + xi
        for yi in range(4):
            y = -1.5 + yi
            buf += _pack(x, y, 0.0, 50.0)

    # Obstacle cluster
    for yi in range(3):
        y = -0.3 + yi * 0.3
        for zi in range(3):
            z = 0.5 + zi * 0.5
            buf += _pack(5.0, y, z, 200.0)

    data = bytes(buf)
    return data, len(data) // POINT_STEP


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

_SCENARIOS = {
    'empty': _empty,
    'simple_obstacle': _simple_obstacle,
}


def build_pointcloud_bytes(scenario: str) -> tuple:
    """Return (data: bytes, num_points: int) for the requested scenario.

    Known scenarios: 'empty', 'simple_obstacle'.
    Unknown scenario falls back to 'empty' (same as calling with 'empty').

    Invariant: len(data) == num_points * POINT_STEP always holds.
    """
    builder = _SCENARIOS.get(scenario, _empty)
    return builder()


def build_obstacle_at_x(obstacle_x: float) -> tuple:
    """Return (data: bytes, num_points: int) with obstacle cluster at obstacle_x.

    Same geometry as simple_obstacle but the 9-point obstacle cluster is placed
    at the requested x position instead of the fixed x=5.0 m.  Ground plane
    points (z=0.0) remain at x ∈ {3.0, 4.0, 5.0, 6.0}.

    Used by fake_pointcloud_pub for the moving_obstacle scenario: the caller
    increments obstacle_x by a fixed step each tick to simulate longitudinal
    motion.

    Invariant: len(data) == num_points * POINT_STEP always holds.
    Returns 25 points (16 ground + 9 obstacle) regardless of obstacle_x.
    """
    buf = bytearray()
    # Ground plane (fixed)
    for xi in range(4):
        x = 3.0 + xi
        for yi in range(4):
            y = -1.5 + yi
            buf += _pack(x, y, 0.0, 50.0)
    # Obstacle cluster at requested x
    for yi in range(3):
        y = -0.3 + yi * 0.3
        for zi in range(3):
            z = 0.5 + zi * 0.5
            buf += _pack(obstacle_x, y, z, 200.0)
    data = bytes(buf)
    return data, len(data) // POINT_STEP
