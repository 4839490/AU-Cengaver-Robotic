# test/test_centroid_tracker.py
#
# Sprint 2 / S2-B4 — Pure-Python unit tests for centroid_tracker.CentroidTracker.
# No ROS2 dependency.
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest \
#       cengaver_ws/src/perception/test/test_centroid_tracker.py -v

import math
import types

from perception.centroid_tracker import CentroidTracker


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def _tracker(**kwargs) -> CentroidTracker:
    return CentroidTracker(**kwargs)


# ===========================================================================
# Track-ID persistence
# ===========================================================================

class TestTrackIdPersistence:

    def test_same_centroid_same_track_id(self):
        """Same centroid over multiple frames keeps the same track_id."""
        t = _tracker()
        centroid = [(5.0, 0.0)]
        r0 = t.update(centroid, 0.0)
        r1 = t.update(centroid, 0.1)
        r2 = t.update(centroid, 0.1)
        assert r0[0]['track_id'] == r1[0]['track_id'] == r2[0]['track_id']

    def test_small_movement_within_association_distance_keeps_id(self):
        """Centroid moves 0.3 m (within default 1.0 m limit) → same track_id."""
        t = _tracker()
        r0 = t.update([(0.0, 0.0)], 0.0)
        r1 = t.update([(0.3, 0.0)], 0.1)
        assert r0[0]['track_id'] == r1[0]['track_id']

    def test_far_cluster_gets_new_track_id(self):
        """Cluster > max_association_distance away creates a new track_id."""
        t = _tracker(max_association_distance_m=1.0)
        r0 = t.update([(0.0, 0.0)], 0.0)
        r1 = t.update([(5.0, 5.0)], 0.1)
        assert r1[0]['track_id'] != r0[0]['track_id']

    def test_track_ids_are_monotonically_increasing(self):
        """Each new track gets a strictly higher ID than all previous tracks."""
        t = _tracker(max_association_distance_m=0.1)
        ids = []
        for i in range(5):
            r = t.update([(float(i * 10), 0.0)], 0.1)
            ids.append(r[0]['track_id'])
        assert ids == sorted(ids), f'IDs not monotonically increasing: {ids}'
        assert len(set(ids)) == 5, 'Duplicate track IDs detected'

    def test_id_starts_at_1(self):
        t = _tracker()
        r = t.update([(0.0, 0.0)], 0.0)
        assert r[0]['track_id'] == 1


# ===========================================================================
# Velocity estimation
# ===========================================================================

class TestVelocityEstimation:

    def test_stationary_velocity_near_zero(self):
        """Same centroid over consecutive frames → velocity_x/y ≈ 0.0."""
        t = _tracker()
        t.update([(5.0, 0.0)], 0.0)
        r = t.update([(5.0, 0.0)], 0.1)
        assert abs(r[0]['velocity_x']) < 1e-9
        assert abs(r[0]['velocity_y']) < 1e-9

    def test_positive_x_movement_gives_positive_vx(self):
        """Centroid moves +1 m in x over 1 s → velocity_x = +1.0 m/s."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(1.0, 0.0)], 1.0)
        assert abs(r[0]['velocity_x'] - 1.0) < 1e-6

    def test_positive_y_movement_gives_positive_vy(self):
        """Centroid moves +0.5 m in y over 0.5 s → velocity_y = +1.0 m/s."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(0.0, 0.5)], 0.5)
        assert abs(r[0]['velocity_y'] - 1.0) < 1e-6

    def test_negative_x_movement_gives_negative_vx(self):
        """Centroid moves -2 m in x over 1 s → velocity_x = -2.0 m/s.
        Uses max_association_distance_m=5.0 so the 2 m jump stays within range.
        """
        t = _tracker(max_association_distance_m=5.0)
        t.update([(5.0, 0.0)], 0.0)
        r = t.update([(3.0, 0.0)], 1.0)
        assert abs(r[0]['velocity_x'] - (-2.0)) < 1e-6

    def test_velocity_signs_both_axes(self):
        """Combined movement gives correct signs for both axes.
        Uses max_association_distance_m=5.0 so the diagonal jump stays in range.
        """
        t = _tracker(max_association_distance_m=5.0)
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(2.0, -1.0)], 1.0)
        assert r[0]['velocity_x'] > 0.0
        assert r[0]['velocity_y'] < 0.0

    def test_dt_zero_does_not_crash_velocity_unchanged(self):
        """dt=0 must not raise; velocity stays at previous value (0 for new track)."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(1.0, 0.0)], 0.0)  # dt=0 → no velocity update
        assert r[0]['velocity_x'] == 0.0
        assert r[0]['velocity_y'] == 0.0

    def test_dt_negative_does_not_crash(self):
        """Negative dt (clock rollback) must not raise; treated as dt≤0."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(1.0, 0.0)], -0.1)  # negative dt → velocity not updated
        assert r[0]['velocity_x'] == 0.0

    def test_velocity_at_10hz_dt(self):
        """At 10 Hz (dt=0.1 s), 0.1 m movement gives exactly 1.0 m/s."""
        t = _tracker()
        t.update([(5.0, 0.0)], 0.0)
        r = t.update([(5.1, 0.0)], 0.1)
        assert abs(r[0]['velocity_x'] - 1.0) < 1e-5


# ===========================================================================
# is_static threshold
# ===========================================================================

class TestIsStatic:

    def test_stationary_is_static_true(self):
        t = _tracker()
        t.update([(5.0, 0.0)], 0.0)
        r = t.update([(5.0, 0.0)], 0.1)
        assert r[0]['is_static'] is True

    def test_slow_speed_below_threshold_is_static(self):
        """Speed = 0.05 m/s < 0.1 m/s → is_static=True."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(0.005, 0.0)], 0.1)  # vx = 0.05 m/s
        assert r[0]['is_static'] is True

    def test_speed_at_threshold_is_not_static(self):
        """Speed = 0.15 m/s > 0.1 m/s → is_static=False.
        Uses 0.015/0.1 = 0.15 to avoid IEEE 754 edge cases at the boundary.
        """
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(0.015, 0.0)], 0.1)  # vx = 0.15 m/s > threshold
        assert r[0]['is_static'] is False

    def test_fast_moving_is_not_static(self):
        """Speed = 5 m/s → is_static=False."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(0.5, 0.0)], 0.1)  # vx = 5 m/s
        assert r[0]['is_static'] is False

    def test_diagonal_speed_above_threshold_not_static(self):
        """Speed = sqrt(0.08^2 + 0.07^2) ≈ 0.106 m/s > 0.1 → is_static=False."""
        t = _tracker()
        t.update([(0.0, 0.0)], 0.0)
        r = t.update([(0.008, 0.007)], 0.1)  # vx=0.08, vy=0.07
        speed = math.sqrt(0.08 ** 2 + 0.07 ** 2)
        assert speed > 0.1, 'Pre-condition: speed must exceed threshold'
        assert r[0]['is_static'] is False


# ===========================================================================
# Track lifetime and missed-frame removal
# ===========================================================================

class TestTrackLifetime:

    def test_missing_cluster_removed_after_max_missed_frames_plus_one(self):
        """Track is removed only after missed > max_missed_frames (strict >)."""
        t = _tracker(max_missed_frames=3)
        t.update([(0.0, 0.0)], 0.0)
        assert t.active_track_count == 1

        # 3 misses — track still present (missed == max, not yet removed).
        t.update([], 0.1)
        t.update([], 0.1)
        t.update([], 0.1)
        assert t.active_track_count == 1, 'Track should survive exactly max_missed_frames misses'

        # 4th miss — removed (missed > max).
        t.update([], 0.1)
        assert t.active_track_count == 0, 'Track should be removed after missed > max'

    def test_track_survives_exactly_max_missed_frames(self):
        """Track with missed == max_missed_frames is still alive."""
        t = _tracker(max_missed_frames=2)
        t.update([(0.0, 0.0)], 0.0)
        t.update([], 0.1)  # missed=1
        t.update([], 0.1)  # missed=2
        assert t.active_track_count == 1

    def test_track_resurrected_before_removal(self):
        """Cluster reappears within max_missed_frames → same track_id restored."""
        t = _tracker(max_missed_frames=3)
        r0 = t.update([(0.0, 0.0)], 0.0)
        old_id = r0[0]['track_id']
        t.update([], 0.1)  # missed=1
        t.update([], 0.1)  # missed=2
        r3 = t.update([(0.0, 0.0)], 0.1)  # reappears at missed=2 < max=3
        assert r3[0]['track_id'] == old_id
        assert t.active_track_count == 1

    def test_new_track_id_after_old_track_removed(self):
        """After a track is removed, a new cluster gets a new, higher ID."""
        t = _tracker(max_missed_frames=1)
        r0 = t.update([(0.0, 0.0)], 0.0)
        old_id = r0[0]['track_id']
        t.update([], 0.1)   # missed=1 (still alive)
        t.update([], 0.1)   # missed=2 > max=1 → removed
        assert t.active_track_count == 0
        r2 = t.update([(10.0, 10.0)], 0.1)  # far cluster → new track
        new_id = r2[0]['track_id']
        assert new_id != old_id
        assert new_id > old_id  # monotonically increasing


# ===========================================================================
# Multi-cluster and edge cases
# ===========================================================================

class TestMultiCluster:

    def test_two_clusters_two_distinct_tracks(self):
        """Two clusters far apart produce two distinct track IDs."""
        t = _tracker()
        r = t.update([(0.0, 0.0), (10.0, 0.0)], 0.0)
        assert len(r) == 2
        assert r[0]['track_id'] != r[1]['track_id']

    def test_two_clusters_ids_persist_across_frames(self):
        """Both track IDs are maintained independently over multiple frames."""
        t = _tracker()
        r0 = t.update([(0.0, 0.0), (10.0, 0.0)], 0.0)
        ids0 = {r0[0]['track_id'], r0[1]['track_id']}
        r1 = t.update([(0.0, 0.0), (10.0, 0.0)], 0.1)
        ids1 = {r1[0]['track_id'], r1[1]['track_id']}
        assert ids0 == ids1

    def test_empty_cluster_list_returns_empty(self):
        """No clusters → empty result, no tracks created."""
        t = _tracker()
        r = t.update([], 0.0)
        assert r == []
        assert t.active_track_count == 0

    def test_reset_clears_all_tracks(self):
        t = _tracker()
        t.update([(1.0, 0.0), (2.0, 0.0)], 0.0)
        assert t.active_track_count == 2
        t.reset()
        assert t.active_track_count == 0

    def test_reset_preserves_next_id_counter(self):
        """After reset, new tracks get IDs higher than any previous track."""
        t = _tracker()
        r0 = t.update([(0.0, 0.0)], 0.0)
        first_id = r0[0]['track_id']
        t.reset()
        r1 = t.update([(0.0, 0.0)], 0.0)
        second_id = r1[0]['track_id']
        assert second_id > first_id, (
            f'Expected second_id ({second_id}) > first_id ({first_id}) after reset'
        )


# ===========================================================================
# ROS-free import check
# ===========================================================================

def test_centroid_tracker_has_no_ros_imports():
    """centroid_tracker must not import any ROS2 package at module level."""
    import perception.centroid_tracker as mod

    ros_namespaces = (
        'rclpy', 'sensor_msgs', 'std_msgs', 'geometry_msgs',
        'perception_msgs', 'common_msgs', 'planning_msgs',
    )
    mod_imports = {
        name for name, obj in vars(mod).items()
        if isinstance(obj, types.ModuleType)
    }
    for ns in ros_namespaces:
        assert not any(m == ns or m.startswith(ns + '.') for m in mod_imports), (
            f'centroid_tracker imported ROS2 namespace {ns!r}'
        )
