# test/test_pointcloud_utils.py
#
# Sprint 2 / S2-B2 — Unit tests for pointcloud_utils.build_pointcloud_bytes.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest cengaver_ws/src/perception/test/test_pointcloud_utils.py -v

import struct
import types

from perception.pointcloud_utils import (
    FIELDS,
    POINT_STEP,
    build_obstacle_at_x,
    build_pointcloud_bytes,
)

_UNPACK = struct.Struct('<ffff')


# ---------------------------------------------------------------------------
# Constants / contract
# ---------------------------------------------------------------------------

def test_point_step_is_16():
    assert POINT_STEP == 16


def test_fields_order():
    assert FIELDS == ('x', 'y', 'z', 'intensity')


def test_fields_count():
    assert len(FIELDS) == 4


# ---------------------------------------------------------------------------
# Byte-length invariant: len(data) == count * POINT_STEP always
# ---------------------------------------------------------------------------

def test_empty_byte_length():
    data, count = build_pointcloud_bytes('empty')
    assert len(data) == count * POINT_STEP


def test_simple_obstacle_byte_length():
    data, count = build_pointcloud_bytes('simple_obstacle')
    assert len(data) == count * POINT_STEP


def test_unknown_scenario_byte_length():
    data, count = build_pointcloud_bytes('unknown_xyz')
    assert len(data) == count * POINT_STEP


# ---------------------------------------------------------------------------
# empty scenario
# ---------------------------------------------------------------------------

def test_empty_has_zero_points():
    data, count = build_pointcloud_bytes('empty')
    assert count == 0
    assert data == b''


# ---------------------------------------------------------------------------
# simple_obstacle scenario
# ---------------------------------------------------------------------------

def test_simple_obstacle_nonzero_points():
    _, count = build_pointcloud_bytes('simple_obstacle')
    assert count > 0


def test_simple_obstacle_has_above_ground_points():
    """At least one point with z > 0.2 m (obstacle, not ground plane)."""
    data, count = build_pointcloud_bytes('simple_obstacle')
    z_values = [_UNPACK.unpack_from(data, i * POINT_STEP)[2] for i in range(count)]
    assert any(z > 0.2 for z in z_values), (
        f'simple_obstacle has no above-ground points (z > 0.2); z values: {z_values}'
    )


def test_simple_obstacle_has_ground_points():
    """At least one point with z == 0.0 (ground plane for future RANSAC)."""
    data, count = build_pointcloud_bytes('simple_obstacle')
    z_values = [_UNPACK.unpack_from(data, i * POINT_STEP)[2] for i in range(count)]
    assert any(z == 0.0 for z in z_values), (
        'simple_obstacle has no ground-plane points (z == 0.0)'
    )


def test_simple_obstacle_all_points_unpack_as_floats():
    """Every point unpacks to four Python floats (x, y, z, intensity)."""
    data, count = build_pointcloud_bytes('simple_obstacle')
    for i in range(count):
        vals = _UNPACK.unpack_from(data, i * POINT_STEP)
        assert len(vals) == 4
        assert all(isinstance(v, float) for v in vals), (
            f'Point {i} has non-float values: {vals}'
        )


def test_simple_obstacle_obstacle_points_have_positive_x():
    """All above-ground points should be in front of the vehicle (x > 0)."""
    data, count = build_pointcloud_bytes('simple_obstacle')
    for i in range(count):
        x, y, z, _ = _UNPACK.unpack_from(data, i * POINT_STEP)
        if z > 0.2:
            assert x > 0.0, f'Obstacle point {i} has x={x} (should be positive)'


def test_simple_obstacle_total_points():
    """simple_obstacle must have exactly 25 points: 16 ground + 9 obstacle."""
    _, count = build_pointcloud_bytes('simple_obstacle')
    assert count == 25, f'Expected 25 points, got {count}'


# ---------------------------------------------------------------------------
# Unknown / fallback scenario
# ---------------------------------------------------------------------------

def test_unknown_scenario_falls_back_to_empty():
    data, count = build_pointcloud_bytes('does_not_exist')
    assert data == b''
    assert count == 0


# ---------------------------------------------------------------------------
# Return type
# ---------------------------------------------------------------------------

def test_returns_bytes_not_bytearray():
    data, _ = build_pointcloud_bytes('simple_obstacle')
    assert isinstance(data, bytes)


def test_empty_returns_bytes():
    data, _ = build_pointcloud_bytes('empty')
    assert isinstance(data, bytes)


# ---------------------------------------------------------------------------
# build_obstacle_at_x — moving_obstacle scenario builder (S2-B4)
# ---------------------------------------------------------------------------

class TestBuildObstacleAtX:

    def test_returns_25_points(self):
        """Always returns 25 points (16 ground + 9 obstacle)."""
        _, count = build_obstacle_at_x(5.0)
        assert count == 25

    def test_byte_length_invariant(self):
        data, count = build_obstacle_at_x(7.5)
        assert len(data) == count * POINT_STEP

    def test_returns_bytes_type(self):
        data, _ = build_obstacle_at_x(5.0)
        assert isinstance(data, bytes)

    def test_obstacle_cluster_at_requested_x(self):
        """Above-ground points (z > 0.2) should have x equal to obstacle_x."""
        obs_x = 8.3
        data, count = build_obstacle_at_x(obs_x)
        for i in range(count):
            x, y, z, _ = _UNPACK.unpack_from(data, i * POINT_STEP)
            if z > 0.2:
                assert abs(x - obs_x) < 1e-5, (
                    f'Obstacle point {i} has x={x}, expected {obs_x}'
                )

    def test_ground_points_still_present(self):
        """Ground-plane points (z == 0.0) are unaffected by obstacle_x."""
        data, count = build_obstacle_at_x(20.0)
        z_values = [_UNPACK.unpack_from(data, i * POINT_STEP)[2] for i in range(count)]
        assert any(z == 0.0 for z in z_values)

    def test_different_x_values_give_different_data(self):
        """Moving the obstacle gives different byte buffers."""
        d1, _ = build_obstacle_at_x(5.0)
        d2, _ = build_obstacle_at_x(5.1)
        assert d1 != d2


# ---------------------------------------------------------------------------
# ROS-free import check
# ---------------------------------------------------------------------------

def test_pointcloud_utils_has_no_ros_imports():
    """pointcloud_utils must not pull in any ROS2 packages at module level."""
    import sys
    import perception.pointcloud_utils as utils_mod

    ros_namespaces = ('rclpy', 'sensor_msgs', 'std_msgs', 'geometry_msgs')
    mod_imports = {
        name
        for name, obj in vars(utils_mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'pointcloud_utils imported ROS2 namespace {ns!r}'
        )
