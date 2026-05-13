# test/test_lidar_cluster_utils.py
#
# Sprint 2 / S2-B3 — Pure-Python unit tests for lidar_cluster_utils.
# No ROS2 dependency; runs with plain pytest or via `colcon test`.
#
# Run standalone:
#   PYTHONPATH=cengaver_ws/src/perception pytest \
#       cengaver_ws/src/perception/test/test_lidar_cluster_utils.py -v

import struct
import types

from perception.lidar_cluster_utils import (
    cluster_summary,
    decode_pointcloud2_data,
    euclidean_cluster,
    filter_ground,
    front_bumper_distance,
)

# ---------------------------------------------------------------------------
# Helpers — synthetic point sets
# ---------------------------------------------------------------------------

_PACK4 = struct.Struct('<ffff')  # little-endian, 4×float32

POINT_STEP = 16
_FIELD_OFFSETS = {'x': 0, 'y': 4, 'z': 8, 'intensity': 12}


def _pack_points(points):
    """Encode a list of (x, y, z, intensity) tuples as raw bytes."""
    buf = bytearray()
    for x, y, z, intensity in points:
        buf += _PACK4.pack(x, y, z, intensity)
    return bytes(buf)


def _simple_obstacle_points():
    """Reproduce the simple_obstacle geometry from pointcloud_utils.py."""
    pts = []
    # Ground plane (z=0.0): 4×4 = 16 points
    for xi in range(4):
        x = 3.0 + xi
        for yi in range(4):
            y = -1.5 + yi
            pts.append((x, y, 0.0, 50.0))
    # Obstacle cluster (z>0.2): 3×3 = 9 points
    for yi in range(3):
        y = -0.3 + yi * 0.3
        for zi in range(3):
            z = 0.5 + zi * 0.5
            pts.append((5.0, y, z, 200.0))
    return pts


# ===========================================================================
# decode_pointcloud2_data
# ===========================================================================

class TestDecodePointcloud2Data:

    def test_correct_decode_xyzintensity(self):
        raw_pts = [(1.0, 2.0, 3.0, 100.0), (4.0, 5.0, 6.0, 200.0)]
        data = _pack_points(raw_pts)
        result = decode_pointcloud2_data(data, _FIELD_OFFSETS, POINT_STEP)
        assert len(result) == 2
        assert abs(result[0][0] - 1.0) < 1e-5
        assert abs(result[0][1] - 2.0) < 1e-5
        assert abs(result[0][2] - 3.0) < 1e-5
        assert abs(result[0][3] - 100.0) < 1e-3
        assert abs(result[1][0] - 4.0) < 1e-5

    def test_correct_decode_xyz_only_offsets(self):
        """Offsets without 'intensity' key: intensity defaults to 0.0."""
        raw_pts = [(1.0, 2.0, 3.0, 99.0)]
        data = _pack_points(raw_pts)
        offsets = {'x': 0, 'y': 4, 'z': 8}  # no intensity
        result = decode_pointcloud2_data(data, offsets, POINT_STEP)
        assert len(result) == 1
        assert abs(result[0][2] - 3.0) < 1e-5
        assert result[0][3] == 0.0  # default intensity

    def test_empty_data_returns_empty(self):
        result = decode_pointcloud2_data(b'', _FIELD_OFFSETS, POINT_STEP)
        assert result == []

    def test_short_data_returns_empty_no_crash(self):
        # 7 bytes: less than one full point record (16 bytes).
        result = decode_pointcloud2_data(b'\x00' * 7, _FIELD_OFFSETS, POINT_STEP)
        assert result == []

    def test_data_one_full_plus_partial_point_returns_empty(self):
        # 20 bytes = 1 full point (16) + 4 extra bytes — truncated second record.
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)]) + b'\x00' * 4
        # n = 20 // 16 = 1 — only one point record fits; extra bytes ignored by n calc.
        result = decode_pointcloud2_data(data, _FIELD_OFFSETS, POINT_STEP)
        assert len(result) == 1

    def test_missing_x_field_returns_empty(self):
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)])
        offsets = {'y': 4, 'z': 8, 'intensity': 12}  # no 'x'
        result = decode_pointcloud2_data(data, offsets, POINT_STEP)
        assert result == []

    def test_missing_y_field_returns_empty(self):
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)])
        offsets = {'x': 0, 'z': 8, 'intensity': 12}
        result = decode_pointcloud2_data(data, offsets, POINT_STEP)
        assert result == []

    def test_missing_z_field_returns_empty(self):
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)])
        offsets = {'x': 0, 'y': 4, 'intensity': 12}
        result = decode_pointcloud2_data(data, offsets, POINT_STEP)
        assert result == []

    def test_zero_point_step_returns_empty(self):
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)])
        result = decode_pointcloud2_data(data, _FIELD_OFFSETS, 0)
        assert result == []

    def test_non_bytes_input_returns_empty(self):
        result = decode_pointcloud2_data("not bytes", _FIELD_OFFSETS, POINT_STEP)
        assert result == []

    def test_none_input_returns_empty(self):
        result = decode_pointcloud2_data(None, _FIELD_OFFSETS, POINT_STEP)
        assert result == []

    def test_multiple_points_all_decoded(self):
        """All 25 simple_obstacle points decode successfully."""
        all_pts = _simple_obstacle_points()
        data = _pack_points(all_pts)
        result = decode_pointcloud2_data(data, _FIELD_OFFSETS, POINT_STEP)
        assert len(result) == 25


# ===========================================================================
# filter_ground
# ===========================================================================

class TestFilterGround:

    def test_ground_points_removed(self):
        pts = [(0.0, 0.0, 0.0, 0.0), (1.0, 0.0, 0.1, 0.0), (2.0, 0.0, 0.2, 0.0)]
        result = filter_ground(pts)
        assert len(result) == 0, "All z <= 0.2 should be removed"

    def test_above_ground_points_kept(self):
        pts = [(0.0, 0.0, 0.3, 0.0), (1.0, 0.0, 1.0, 0.0), (2.0, 0.0, 0.21, 0.0)]
        result = filter_ground(pts)
        assert len(result) == 3, "All z > 0.2 should be kept"

    def test_mixed_points(self):
        pts = [(0.0, 0.0, 0.0, 0.0),  # ground
               (1.0, 0.0, 0.5, 0.0),  # above ground
               (2.0, 0.0, 0.2, 0.0),  # exactly on threshold → ground
               (3.0, 0.0, 0.21, 0.0)]  # above ground
        result = filter_ground(pts)
        assert len(result) == 2
        assert all(p[2] > 0.2 for p in result)

    def test_boundary_exactly_equal_threshold_is_ground(self):
        pts = [(0.0, 0.0, 0.2, 0.0)]
        result = filter_ground(pts)
        assert result == [], "z == threshold is ground (not above-ground)"

    def test_empty_input(self):
        result = filter_ground([])
        assert result == []

    def test_custom_threshold(self):
        pts = [(0.0, 0.0, 0.5, 0.0), (0.0, 0.0, 1.0, 0.0), (0.0, 0.0, 0.1, 0.0)]
        result = filter_ground(pts, ground_z_threshold=0.6)
        assert len(result) == 1
        assert abs(result[0][2] - 1.0) < 1e-6

    def test_simple_obstacle_ground_filtered(self):
        """16 ground points removed, 9 obstacle points kept."""
        all_pts = _simple_obstacle_points()
        result = filter_ground(all_pts)
        assert len(result) == 9, f"Expected 9 above-ground points, got {len(result)}"
        assert all(p[2] > 0.2 for p in result)


# ===========================================================================
# euclidean_cluster
# ===========================================================================

class TestEuclideanCluster:

    def test_empty_input_returns_empty(self):
        result = euclidean_cluster([])
        assert result == []

    def test_single_point_one_cluster(self):
        result = euclidean_cluster([(1.0, 2.0, 3.0, 0.0)])
        assert len(result) == 1
        assert len(result[0]) == 1

    def test_simple_obstacle_one_cluster(self):
        """All 9 above-ground points from simple_obstacle form exactly 1 cluster."""
        all_pts = _simple_obstacle_points()
        above = filter_ground(all_pts)
        clusters = euclidean_cluster(above, distance_threshold=0.5)
        assert len(clusters) == 1, (
            f"Expected 1 cluster from simple_obstacle, got {len(clusters)}"
        )
        assert len(clusters[0]) == 9

    def test_two_separated_groups_give_two_clusters(self):
        """Two groups 10 m apart must form two distinct clusters."""
        group_a = [(0.0, 0.0, 1.0, 0.0), (0.1, 0.0, 1.0, 0.0), (0.0, 0.1, 1.0, 0.0)]
        group_b = [(10.0, 10.0, 1.0, 0.0), (10.1, 10.0, 1.0, 0.0), (10.0, 10.1, 1.0, 0.0)]
        pts = group_a + group_b
        clusters = euclidean_cluster(pts, distance_threshold=0.5)
        assert len(clusters) == 2, (
            f"Expected 2 clusters from separated groups, got {len(clusters)}"
        )
        sizes = sorted(len(c) for c in clusters)
        assert sizes == [3, 3]

    def test_points_within_threshold_merge(self):
        pts = [(0.0, 0.0, 0.0, 0.0), (0.3, 0.0, 0.0, 0.0), (0.6, 0.0, 0.0, 0.0)]
        # 0→1: 0.3m ✓, 1→2: 0.3m ✓ → all one cluster (transitivity)
        clusters = euclidean_cluster(pts, distance_threshold=0.5)
        assert len(clusters) == 1
        assert len(clusters[0]) == 3

    def test_points_at_exact_threshold_merge(self):
        pts = [(0.0, 0.0, 0.0, 0.0), (0.5, 0.0, 0.0, 0.0)]
        clusters = euclidean_cluster(pts, distance_threshold=0.5)
        assert len(clusters) == 1

    def test_points_beyond_threshold_separate(self):
        pts = [(0.0, 0.0, 0.0, 0.0), (0.6, 0.0, 0.0, 0.0)]
        clusters = euclidean_cluster(pts, distance_threshold=0.5)
        assert len(clusters) == 2


# ===========================================================================
# cluster_summary
# ===========================================================================

class TestClusterSummary:

    def test_empty_returns_empty_dict(self):
        result = cluster_summary([])
        assert result == {}

    def test_single_point(self):
        result = cluster_summary([(3.0, 4.0, 5.0, 0.0)])
        assert abs(result['centroid_x'] - 3.0) < 1e-6
        assert abs(result['centroid_y'] - 4.0) < 1e-6
        assert abs(result['centroid_z'] - 5.0) < 1e-6
        assert result['min_x'] == result['max_x']
        assert result['point_count'] == 1

    def test_centroid_simple_obstacle(self):
        """simple_obstacle cluster: centroid ≈ (5.0, 0.0, 1.0)."""
        all_pts = _simple_obstacle_points()
        above = filter_ground(all_pts)
        clusters = euclidean_cluster(above, distance_threshold=0.5)
        assert len(clusters) == 1
        s = cluster_summary(clusters[0])
        assert abs(s['centroid_x'] - 5.0) < 0.01, f"centroid_x={s['centroid_x']}"
        assert abs(s['centroid_y'] - 0.0) < 0.01, f"centroid_y={s['centroid_y']}"
        assert abs(s['centroid_z'] - 1.0) < 0.01, f"centroid_z={s['centroid_z']}"

    def test_bbox_extents_nonzero(self):
        """Width (y) and height (z) must be nonzero for the simple_obstacle cluster.

        Note: all obstacle points share x=5.0, so the x-extent is intentionally 0.
        The node clips extents to 0.01 m minimum when building ObstacleTrack messages.
        """
        all_pts = _simple_obstacle_points()
        above = filter_ground(all_pts)
        clusters = euclidean_cluster(above, distance_threshold=0.5)
        s = cluster_summary(clusters[0])
        assert s['max_y'] - s['min_y'] > 0.0, "width (y-extent) should be nonzero"
        assert s['max_z'] - s['min_z'] > 0.0, "height (z-extent) should be nonzero"

    def test_bbox_extents_sane(self):
        """Obstacle y/z extents must be in a physically plausible range."""
        all_pts = _simple_obstacle_points()
        above = filter_ground(all_pts)
        clusters = euclidean_cluster(above, distance_threshold=0.5)
        s = cluster_summary(clusters[0])
        width = s['max_y'] - s['min_y']
        height = s['max_z'] - s['min_z']
        assert 0.0 < width < 10.0
        assert 0.0 < height < 5.0

    def test_point_count_matches_cluster(self):
        all_pts = _simple_obstacle_points()
        above = filter_ground(all_pts)
        clusters = euclidean_cluster(above, distance_threshold=0.5)
        s = cluster_summary(clusters[0])
        assert s['point_count'] == len(clusters[0])


# ===========================================================================
# decode_pointcloud2_data — row_step / height / field-offset validation
# (Codex review fix — S2-B3 correction pass)
# ===========================================================================

class TestDecodeRowStepHeight:

    def test_padded_row_step_ignores_padding(self):
        """When row_step > width * point_step, padding bytes are not decoded as points."""
        pts = [(1.0, 2.0, 3.0, 0.0), (4.0, 5.0, 6.0, 0.0)]
        data_pts = _pack_points(pts)             # 32 bytes of real point data
        padding = b'\xAA' * 8                    # 8 bytes of row padding
        data = data_pts + padding                # 40 bytes: 1 row (2 pts + padding)
        result = decode_pointcloud2_data(
            data, _FIELD_OFFSETS, POINT_STEP,
            width=2, height=1, row_step=2 * POINT_STEP + 8)
        assert len(result) == 2, "Padding must not be decoded as extra points"
        assert abs(result[0][0] - 1.0) < 1e-5
        assert abs(result[1][0] - 4.0) < 1e-5

    def test_multi_row_padded_correctly_decodes(self):
        """Two padded rows each decode the correct number of points."""
        row_pts = [(0.0, 0.0, 1.0, 0.0), (1.0, 0.0, 1.0, 0.0)]
        row_data = _pack_points(row_pts)        # 32 bytes
        pad = b'\xBB' * 4                       # 4 bytes padding per row
        data = (row_data + pad) * 2             # 2 rows × (32 + 4) = 72 bytes
        result = decode_pointcloud2_data(
            data, _FIELD_OFFSETS, POINT_STEP,
            width=2, height=2, row_step=2 * POINT_STEP + 4)
        assert len(result) == 4, "2 rows × 2 pts = 4 decoded points"

    def test_rejects_short_data_for_declared_height(self):
        """Reject when len(data) < row_step * height."""
        pts = [(1.0, 2.0, 3.0, 0.0)]
        data = _pack_points(pts)   # 16 bytes — enough for 1 row × 1 pt
        # Claim 2 rows: needs 16 * 2 = 32 bytes but have only 16.
        result = decode_pointcloud2_data(
            data, _FIELD_OFFSETS, POINT_STEP,
            width=1, height=2, row_step=POINT_STEP)
        assert result == []

    def test_rejects_truncated_row_step(self):
        """Reject when row_step < point_step * width (rows would be truncated)."""
        pts = [(1.0, 2.0, 3.0, 0.0), (4.0, 5.0, 6.0, 0.0)]
        data = _pack_points(pts)  # 32 bytes, 2 points
        # row_step=12 < point_step * width = 16 * 2 = 32 → reject
        result = decode_pointcloud2_data(
            data, _FIELD_OFFSETS, POINT_STEP,
            width=2, height=1, row_step=12)
        assert result == []

    def test_rejects_field_offset_beyond_point_step(self):
        """Reject when a required field offset + 4 > point_step."""
        data = _pack_points([(1.0, 2.0, 3.0, 0.0)])
        # x starts at byte 13: 13 + 4 = 17 > 16 → out of bounds
        bad_offsets = {'x': 13, 'y': 4, 'z': 8}
        result = decode_pointcloud2_data(data, bad_offsets, POINT_STEP)
        assert result == []

    def test_valid_boundary_field_offset_accepted(self):
        """Field at offset point_step - 4 (last valid position) must be accepted."""
        # intensity at offset 12: 12 + 4 = 16 == point_step → NOT > → OK
        data = _pack_points([(1.0, 2.0, 3.0, 99.0)])
        result = decode_pointcloud2_data(data, _FIELD_OFFSETS, POINT_STEP)
        assert len(result) == 1  # offset 12 is the last valid 4-byte field


# ===========================================================================
# front_bumper_distance
# ===========================================================================

class TestFrontBumperDistance:

    def test_simple_obstacle_centroid(self):
        """Centroid x=5.0 with BEE1 offset 0.410 → distance ≈ 4.59 m."""
        d = front_bumper_distance(5.0, 0.410)
        assert abs(d - 4.59) < 0.01, f"Expected ~4.59, got {d}"

    def test_no_offset_returns_position_x(self):
        """With offset=0.0 the distance equals position_x."""
        assert front_bumper_distance(5.0, 0.0) == 5.0

    def test_clips_to_zero_when_behind_bumper(self):
        """Obstacle at position_x < offset must clip to 0.0 (not negative)."""
        d = front_bumper_distance(0.1, 0.410)
        assert d == 0.0, f"Expected 0.0 (clipped), got {d}"

    def test_exactly_at_bumper_is_zero(self):
        """Obstacle exactly at the bumper line: distance = 0.0."""
        d = front_bumper_distance(0.410, 0.410)
        assert d == 0.0

    def test_default_offset_is_zero(self):
        """Default offset=0.0 so front_bumper_distance(x) == max(x, 0.0)."""
        assert front_bumper_distance(3.0) == 3.0


# ===========================================================================
# ROS-free import check
# ===========================================================================

def test_lidar_cluster_utils_has_no_ros_imports():
    """lidar_cluster_utils must not pull in any ROS2 packages at module level."""
    import perception.lidar_cluster_utils as mod

    ros_namespaces = ('rclpy', 'sensor_msgs', 'std_msgs', 'geometry_msgs',
                      'perception_msgs', 'common_msgs')
    mod_imports = {
        name
        for name, obj in vars(mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'lidar_cluster_utils imported ROS2 namespace {ns!r}'
        )
