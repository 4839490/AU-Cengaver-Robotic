# test/test_lidar_obstacle_pipeline.py
#
# Sprint 2 S2-B5 + Sprint 3 S3-R2 + S3-R3 — Contract-level unit tests for
# lidar_obstacle_node helpers.  No ROS2 dependency: all ROS2 packages are
# stubbed in sys.modules before import.
#
# Tests cover:
#   _build_obstacle_track  — all ObstacleTrack contract fields
#   _extract_field_offsets — malformed / unsupported PointCloud2 rejection
#   Full pure-Python pipeline: decode → filter → cluster → track → build_track
#
# Run standalone (no ROS2 needed):
#   PYTHONPATH=cengaver_ws/src/perception pytest \
#       cengaver_ws/src/perception/test/test_lidar_obstacle_pipeline.py -v

import sys
import types

# ---------------------------------------------------------------------------
# Stubs — installed into sys.modules BEFORE lidar_obstacle_node is imported.
# ---------------------------------------------------------------------------

_FLOAT32_DATATYPE = 7  # sensor_msgs/PointField.FLOAT32


class _ObstacleTrackStub:
    """Minimal stand-in for perception_msgs.msg.ObstacleTrack."""

    UNKNOWN_OBSTACLE = 0
    VEHICLE = 1
    PEDESTRIAN = 2
    CONE = 3
    BARRIER = 4
    SIGN_POLE = 5

    def __init__(self):
        self.track_id = 0
        self.class_label = 0
        self.confidence = 0.0
        self.position_x = 0.0
        self.position_y = 0.0
        self.distance = 0.0
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.ttc = 0.0
        self.width = 0.0
        self.length = 0.0
        self.height = 0.0
        self.is_static = False
        self.source_sensor = ''
        self.semantic_source = ''
        self.geometry_source = ''
        self.age_ms = 0
        self.valid_until_ms = 0
        self.warning_flags = []


class _ObstacleTracksStub:
    def __init__(self):
        self.header = None
        self.tracks = []


class _HeaderStub:
    def __init__(self):
        self.stamp = None
        self.frame_id = ''


class _NodeStub:
    pass


class _PointCloud2Stub:
    pass


class _ActiveRouteContextStub:
    def __init__(self):
        self.ego_speed_mps = 0.0
        self.route_context_valid = True
        self.age_ms = 0
        self.valid_until_ms = 500


def _build_module_stubs():
    _perception_msgs = types.ModuleType('perception_msgs')
    _perception_msgs_msg = types.ModuleType('perception_msgs.msg')
    _perception_msgs_msg.ObstacleTrack = _ObstacleTrackStub
    _perception_msgs_msg.ObstacleTracks = _ObstacleTracksStub
    _perception_msgs.msg = _perception_msgs_msg

    # S3-R2: planning_msgs stub so lidar_obstacle_node import succeeds.
    _planning_msgs = types.ModuleType('planning_msgs')
    _planning_msgs_msg = types.ModuleType('planning_msgs.msg')
    _planning_msgs_msg.ActiveRouteContext = _ActiveRouteContextStub
    _planning_msgs.msg = _planning_msgs_msg

    _rclpy = types.ModuleType('rclpy')
    _rclpy.init = lambda args=None: None
    _rclpy.spin = lambda node: None
    _rclpy.shutdown = lambda: None

    _rclpy_node = types.ModuleType('rclpy.node')
    _rclpy_node.Node = _NodeStub

    _sensor_msgs = types.ModuleType('sensor_msgs')
    _sensor_msgs_msg = types.ModuleType('sensor_msgs.msg')
    _sensor_msgs_msg.PointCloud2 = _PointCloud2Stub
    _sensor_msgs.msg = _sensor_msgs_msg

    _std_msgs = types.ModuleType('std_msgs')
    _std_msgs_msg = types.ModuleType('std_msgs.msg')
    _std_msgs_msg.Header = _HeaderStub
    _std_msgs.msg = _std_msgs_msg

    # Stub perception.dummy_common directly so its real std_msgs import is skipped.
    _dummy_common = types.ModuleType('perception.dummy_common')
    _dummy_common.BASE_LINK_FRAME_ID = 'base_link'
    _dummy_common.make_header = lambda node, frame_id: _HeaderStub()

    stubs = {
        'perception_msgs':        _perception_msgs,
        'perception_msgs.msg':    _perception_msgs_msg,
        'planning_msgs':          _planning_msgs,
        'planning_msgs.msg':      _planning_msgs_msg,
        'rclpy':                  _rclpy,
        'rclpy.node':             _rclpy_node,
        'sensor_msgs':            _sensor_msgs,
        'sensor_msgs.msg':        _sensor_msgs_msg,
        'std_msgs':               _std_msgs,
        'std_msgs.msg':           _std_msgs_msg,
        'perception.dummy_common': _dummy_common,
    }
    for name, mod in stubs.items():
        sys.modules.setdefault(name, mod)


_build_module_stubs()

# Now import the functions under test (and the pure-Python helpers).
from perception.lidar_obstacle_node import (  # noqa: E402
    _build_obstacle_track,
    _extract_field_offsets,
)
from perception.ttc_utils import (             # noqa: E402
    add_warning_flag_once,
    compute_ttc,
    is_route_context_fresh,
    remove_warning_flag,
)
from perception.lidar_cluster_utils import (  # noqa: E402
    cluster_summary,
    decode_pointcloud2_data,
    euclidean_cluster,
    filter_ground,
    front_bumper_distance,
)
from perception.centroid_tracker import CentroidTracker  # noqa: E402
from perception.pointcloud_utils import (               # noqa: E402
    POINT_STEP,
    build_obstacle_at_x,
    build_pointcloud_bytes,
)


# ---------------------------------------------------------------------------
# Test helpers
# ---------------------------------------------------------------------------

_FIELD_OFFSETS = {'x': 0, 'y': 4, 'z': 8, 'intensity': 12}
_BUMPER_OFFSET = 0.410  # BEE1 front_overhang_m from vehicle_params.yaml


def _make_summary(
    cx=5.0, cy=0.0,
    min_x=5.0, max_x=5.0,
    min_y=-0.3, max_y=0.3,
    min_z=0.5, max_z=1.5,
):
    """Build a cluster_summary-like dict matching the simple_obstacle geometry."""
    return {
        'centroid_x': cx,
        'centroid_y': cy,
        'centroid_z': (min_z + max_z) / 2.0,
        'min_x': min_x, 'max_x': max_x,
        'min_y': min_y, 'max_y': max_y,
        'min_z': min_z, 'max_z': max_z,
        'point_count': 9,
    }


def _make_pc2_field(name, offset, datatype=_FLOAT32_DATATYPE):
    return types.SimpleNamespace(name=name, offset=offset, datatype=datatype)


def _make_pc2(*fields):
    return types.SimpleNamespace(fields=list(fields))


def _run_pipeline(
    data, offsets, point_step, width, height, row_step,
    tracker, bumper_offset, cluster_dist=0.5, ground_z=0.2, dt_s=0.0,
):
    """Run the pure-Python side of _process_pointcloud without ROS2."""
    points = decode_pointcloud2_data(data, offsets, point_step, width, height, row_step)
    above = filter_ground(points, ground_z) if points else []
    clusters = euclidean_cluster(above, cluster_dist) if above else []
    summaries = [cluster_summary(c) for c in clusters if c]
    summaries = [s for s in summaries if s]
    cluster_xys = [(s['centroid_x'], s['centroid_y']) for s in summaries]
    track_infos = tracker.update(cluster_xys, dt_s)
    return [
        _build_obstacle_track(
            info['track_id'], s, bumper_offset,
            info['velocity_x'], info['velocity_y'], info['is_static'],
        )
        for s, info in zip(summaries, track_infos)
    ]


# ===========================================================================
# _build_obstacle_track — contract field tests
# ===========================================================================

class TestBuildObstacleTrackContractFields:
    """Each test verifies one field of ObstacleTrack against the message contract.

    Contract reference:
        wiki/contracts/message_contracts.md §ObstacleTrack.msg (canonical raw)
    """

    def test_valid_until_ms_is_200(self):
        """Contract: valid_until_ms = 200 for all lidar_obstacle_node tracks."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.valid_until_ms == 200, (
            f'valid_until_ms must be 200; got {track.valid_until_ms}'
        )

    def test_warning_flags_is_empty_list_for_valid_synthetic_track(self):
        """Contract: warning_flags = [] for a valid cluster — no fault flags."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.warning_flags == [], (
            f'warning_flags must be [] for valid track; got {track.warning_flags}'
        )

    def test_geometry_source_is_lidar(self):
        """Contract: geometry_source = "lidar" for all lidar_obstacle_node tracks."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.geometry_source == 'lidar', (
            f'geometry_source must be "lidar"; got {track.geometry_source!r}'
        )

    def test_source_sensor_is_lidar_cluster(self):
        """Contract: source_sensor = "lidar_cluster" for Euclidean cluster output."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.source_sensor == 'lidar_cluster', (
            f'source_sensor must be "lidar_cluster"; got {track.source_sensor!r}'
        )

    def test_semantic_source_is_none_for_unknown_obstacle(self):
        """Contract: semantic_source = "none" when class_label = UNKNOWN_OBSTACLE."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.semantic_source == 'none', (
            f'semantic_source must be "none" for UNKNOWN_OBSTACLE; '
            f'got {track.semantic_source!r}'
        )

    def test_class_label_is_unknown_obstacle_zero(self):
        """Contract: class_label = UNKNOWN_OBSTACLE = 0 (no camera fusion yet)."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.class_label == _ObstacleTrackStub.UNKNOWN_OBSTACLE
        assert track.class_label == 0

    def test_ttc_default_is_zero(self):
        """_build_obstacle_track sets ttc=0.0; node overwrites from route context in _tick()."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert track.ttc == 0.0, (
            f'_build_obstacle_track ttc default must be 0.0; got {track.ttc}'
        )

    def test_track_id_propagated(self):
        """track_id from the centroid tracker is passed through unchanged."""
        for tid in (1, 7, 42, 999):
            track = _build_obstacle_track(tid, _make_summary(), _BUMPER_OFFSET)
            assert track.track_id == tid, f'track_id={tid} not propagated; got {track.track_id}'

    def test_position_x_equals_centroid_x(self):
        summary = _make_summary(cx=7.5)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.position_x - 7.5) < 1e-6, (
            f'position_x must equal centroid_x=7.5; got {track.position_x}'
        )

    def test_position_y_equals_centroid_y(self):
        summary = _make_summary(cy=-1.2)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.position_y - (-1.2)) < 1e-6, (
            f'position_y must equal centroid_y=-1.2; got {track.position_y}'
        )

    def test_distance_uses_front_bumper_not_euclidean(self):
        """distance = max(pos_x - bumper_offset, 0) — NOT sqrt(x²+y²).

        Using cy=2.0 makes Euclidean range (≈5.38) clearly different from
        front-bumper distance (≈4.59) so the test distinguishes the two.
        """
        cx, cy = 5.0, 2.0
        summary = _make_summary(cx=cx, cy=cy)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        expected = front_bumper_distance(cx, _BUMPER_OFFSET)   # 4.59
        euclidean = (cx ** 2 + cy ** 2) ** 0.5                # 5.385
        assert abs(track.distance - expected) < 1e-5, (
            f'distance should use front_bumper ({expected:.4f}) '
            f'not Euclidean ({euclidean:.4f}); got {track.distance:.4f}'
        )

    def test_distance_simple_obstacle_is_4_59(self):
        """simple_obstacle: centroid x=5.0, bumper=0.410 → distance≈4.59 m."""
        summary = _make_summary(cx=5.0)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.distance - 4.59) < 0.01, (
            f'Expected distance≈4.59 m from simple_obstacle; got {track.distance:.4f}'
        )

    def test_velocity_x_propagated(self):
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET, velocity_x=1.23)
        assert abs(track.velocity_x - 1.23) < 1e-6

    def test_velocity_y_propagated(self):
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET, velocity_y=-0.5)
        assert abs(track.velocity_y - (-0.5)) < 1e-6

    def test_is_static_true_propagated(self):
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET, is_static=True)
        assert track.is_static is True

    def test_is_static_false_propagated(self):
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET, is_static=False)
        assert track.is_static is False

    def test_confidence_is_0_8(self):
        """MVP confidence is 0.8 for all synthetic tracks (no real classifier yet)."""
        track = _build_obstacle_track(1, _make_summary(), _BUMPER_OFFSET)
        assert abs(track.confidence - 0.8) < 1e-6, (
            f'Expected confidence=0.8; got {track.confidence}'
        )


class TestBuildObstacleTrackBoundingBox:

    def test_width_from_y_extent(self):
        """width = max_y - min_y for a cluster with nonzero y-spread."""
        summary = _make_summary(min_y=-0.3, max_y=0.3)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.width - 0.6) < 1e-6, f'Expected width=0.6; got {track.width}'

    def test_length_from_x_extent(self):
        """length = max_x - min_x for a cluster with nonzero x-spread."""
        summary = _make_summary(min_x=5.0, max_x=6.0)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.length - 1.0) < 1e-6, f'Expected length=1.0; got {track.length}'

    def test_height_from_z_extent(self):
        """height = max_z - min_z for a cluster with nonzero z-spread."""
        summary = _make_summary(min_z=0.5, max_z=1.5)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.height - 1.0) < 1e-6, f'Expected height=1.0; got {track.height}'

    def test_zero_y_extent_clips_to_0_01(self):
        """Degenerate cluster with zero y-extent → width clipped to 0.01 m minimum."""
        summary = _make_summary(min_y=0.0, max_y=0.0)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.width - 0.01) < 1e-6, (
            f'Zero y-extent must clip to 0.01; got {track.width}'
        )

    def test_zero_x_extent_clips_to_0_01(self):
        """simple_obstacle all cluster points at x=5.0 → length clipped to 0.01."""
        summary = _make_summary(min_x=5.0, max_x=5.0)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.length - 0.01) < 1e-6, (
            f'Zero x-extent must clip to 0.01; got {track.length}'
        )

    def test_zero_z_extent_clips_to_0_01(self):
        """Degenerate cluster with zero z-extent → height clipped to 0.01 m minimum."""
        summary = _make_summary(min_z=1.0, max_z=1.0)
        track = _build_obstacle_track(1, summary, _BUMPER_OFFSET)
        assert abs(track.height - 0.01) < 1e-6, (
            f'Zero z-extent must clip to 0.01; got {track.height}'
        )


# ===========================================================================
# _extract_field_offsets — PointCloud2 layout validation
# ===========================================================================

class TestExtractFieldOffsets:
    """Tests for the PointCloud2 field layout validator."""

    def test_valid_xyz_float32_returns_dict(self):
        """Standard VLP-16 x/y/z FLOAT32 layout is accepted."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0),
            _make_pc2_field('y', 4),
            _make_pc2_field('z', 8),
            _make_pc2_field('intensity', 12),
        )
        result = _extract_field_offsets(pc2)
        assert result is not None
        assert isinstance(result, dict)

    def test_valid_layout_returns_correct_offsets(self):
        """Returned dict maps field names to their byte offsets."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0),
            _make_pc2_field('y', 4),
            _make_pc2_field('z', 8),
        )
        result = _extract_field_offsets(pc2)
        assert result is not None
        assert result['x'] == 0
        assert result['y'] == 4
        assert result['z'] == 8

    def test_missing_x_returns_none(self):
        pc2 = _make_pc2(_make_pc2_field('y', 4), _make_pc2_field('z', 8))
        assert _extract_field_offsets(pc2) is None

    def test_missing_y_returns_none(self):
        pc2 = _make_pc2(_make_pc2_field('x', 0), _make_pc2_field('z', 8))
        assert _extract_field_offsets(pc2) is None

    def test_missing_z_returns_none(self):
        pc2 = _make_pc2(_make_pc2_field('x', 0), _make_pc2_field('y', 4))
        assert _extract_field_offsets(pc2) is None

    def test_non_float32_x_returns_none(self):
        """x with datatype != FLOAT32 (e.g. FLOAT64=8) must be rejected."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0, datatype=8),  # FLOAT64, not FLOAT32
            _make_pc2_field('y', 4),
            _make_pc2_field('z', 8),
        )
        assert _extract_field_offsets(pc2) is None

    def test_non_float32_y_returns_none(self):
        """y with datatype != FLOAT32 must be rejected."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0),
            _make_pc2_field('y', 4, datatype=4),  # UINT16
            _make_pc2_field('z', 8),
        )
        assert _extract_field_offsets(pc2) is None

    def test_non_float32_z_returns_none(self):
        """z with datatype != FLOAT32 must be rejected."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0),
            _make_pc2_field('y', 4),
            _make_pc2_field('z', 8, datatype=6),  # UINT32
        )
        assert _extract_field_offsets(pc2) is None

    def test_extra_non_xyz_fields_do_not_reject(self):
        """Extra fields (intensity, ring, timestamp) beside x/y/z are ignored."""
        pc2 = _make_pc2(
            _make_pc2_field('x', 0),
            _make_pc2_field('y', 4),
            _make_pc2_field('z', 8),
            _make_pc2_field('ring', 12, datatype=4),       # UINT16 — OK
            _make_pc2_field('timestamp', 16, datatype=8),  # FLOAT64 — OK
        )
        result = _extract_field_offsets(pc2)
        assert result is not None

    def test_empty_fields_returns_none(self):
        """No fields at all: missing x/y/z → None."""
        pc2 = _make_pc2()
        assert _extract_field_offsets(pc2) is None


# ===========================================================================
# Full pipeline integration (pure-Python helpers, no ROS2)
# ===========================================================================

class TestPipelineIntegration:
    """End-to-end decode → filter → cluster → track → build_track pipeline.

    These tests exercise the same code path as _process_pointcloud() but
    without instantiating LidarObstacleNode.  They verify that the contract
    fields produced by _build_obstacle_track are correct after real cluster
    summaries are fed through it.
    """

    def _simple_obs_data(self):
        data, n = build_pointcloud_bytes('simple_obstacle')
        row_step = n * POINT_STEP
        return data, n, row_step

    def test_simple_obstacle_produces_one_track(self):
        data, n, row_step = self._simple_obs_data()
        tracker = CentroidTracker()
        tracks = _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET,
        )
        assert len(tracks) == 1, (
            f'Expected 1 track from simple_obstacle; got {len(tracks)}'
        )

    def test_simple_obstacle_contract_fields(self):
        """Pipeline output satisfies all contract-sensitive fields."""
        data, n, row_step = self._simple_obs_data()
        tracker = CentroidTracker()
        tracks = _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET,
        )
        assert len(tracks) == 1
        t = tracks[0]
        assert t.valid_until_ms == 200
        assert t.warning_flags == []
        assert t.geometry_source == 'lidar'
        assert t.source_sensor == 'lidar_cluster'
        assert t.semantic_source == 'none'
        assert abs(t.distance - 4.59) < 0.01, (
            f'Expected distance≈4.59 m; got {t.distance:.4f}'
        )

    def test_empty_scenario_produces_zero_tracks(self):
        """Empty cloud → no clusters → tracks=[]."""
        tracker = CentroidTracker()
        tracks = _run_pipeline(
            b'', _FIELD_OFFSETS, POINT_STEP, 0, 1, 0,
            tracker, _BUMPER_OFFSET,
        )
        assert tracks == [], f'Expected [] from empty cloud; got {tracks}'

    def test_moving_obstacle_velocity_x_positive(self):
        """Obstacle moves +0.1 m in x over 0.1 s → velocity_x ≈ +1.0 m/s."""
        tracker = CentroidTracker()
        data0, n0 = build_obstacle_at_x(5.0)
        _run_pipeline(
            data0, _FIELD_OFFSETS, POINT_STEP, n0, 1, n0 * POINT_STEP,
            tracker, _BUMPER_OFFSET, dt_s=0.0,
        )
        data1, n1 = build_obstacle_at_x(5.1)
        tracks = _run_pipeline(
            data1, _FIELD_OFFSETS, POINT_STEP, n1, 1, n1 * POINT_STEP,
            tracker, _BUMPER_OFFSET, dt_s=0.1,
        )
        assert len(tracks) == 1
        assert tracks[0].velocity_x > 0, (
            f'Expected positive velocity_x; got {tracks[0].velocity_x}'
        )

    def test_moving_obstacle_is_not_static(self):
        """Obstacle at ≈1.0 m/s → is_static=False (speed > 0.1 m/s threshold)."""
        tracker = CentroidTracker()
        data0, n0 = build_obstacle_at_x(5.0)
        _run_pipeline(
            data0, _FIELD_OFFSETS, POINT_STEP, n0, 1, n0 * POINT_STEP,
            tracker, _BUMPER_OFFSET, dt_s=0.0,
        )
        data1, n1 = build_obstacle_at_x(5.1)
        tracks = _run_pipeline(
            data1, _FIELD_OFFSETS, POINT_STEP, n1, 1, n1 * POINT_STEP,
            tracker, _BUMPER_OFFSET, dt_s=0.1,
        )
        assert len(tracks) == 1
        assert tracks[0].is_static is False, (
            f'Expected is_static=False for 1 m/s obstacle; got {tracks[0].is_static}'
        )

    def test_stationary_obstacle_velocity_near_zero(self):
        """Same centroid across two frames → velocity_x/y ≈ 0."""
        tracker = CentroidTracker()
        data, n = build_obstacle_at_x(5.0)
        row_step = n * POINT_STEP
        _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET, dt_s=0.0,
        )
        tracks = _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET, dt_s=0.1,
        )
        assert len(tracks) == 1
        assert abs(tracks[0].velocity_x) < 1e-6
        assert abs(tracks[0].velocity_y) < 1e-6

    def test_stationary_obstacle_is_static_true(self):
        """Same centroid across two frames → is_static=True."""
        tracker = CentroidTracker()
        data, n = build_pointcloud_bytes('simple_obstacle')
        row_step = n * POINT_STEP
        _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET, dt_s=0.0,
        )
        tracks = _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET, dt_s=0.1,
        )
        assert tracks[0].is_static is True

    def test_tracker_reset_then_empty_gives_no_tracks(self):
        """After tracker reset (stale-path simulation), empty cloud → tracks=[]."""
        tracker = CentroidTracker()
        data, n = build_pointcloud_bytes('simple_obstacle')
        row_step = n * POINT_STEP
        _run_pipeline(
            data, _FIELD_OFFSETS, POINT_STEP, n, 1, row_step,
            tracker, _BUMPER_OFFSET,
        )
        tracker.reset()
        empty_tracks = _run_pipeline(
            b'', _FIELD_OFFSETS, POINT_STEP, 0, 1, 0,
            tracker, _BUMPER_OFFSET,
        )
        assert empty_tracks == []


# ===========================================================================
# S3-R3 — ROUTE_CONTEXT_MISSING warning flag behaviour
# ===========================================================================

def _apply_tick_logic(tracks: list, context_ok: bool, ego_spd: float = 0.0) -> None:
    """Replicate the per-tick TTC + flag logic from LidarObstacleNode._tick().

    Mirrors the S3-R3 Codex-fix behaviour: on context recovery, removes any
    stale ROUTE_CONTEXT_MISSING from cached tracks before computing TTC.

    Used by TestWarningFlagBehavior to exercise the S3-R3 logic without
    instantiating the full ROS2 node.
    """
    for t in tracks:
        if context_ok:
            remove_warning_flag(t.warning_flags, 'ROUTE_CONTEXT_MISSING')
            t.ttc = compute_ttc(t.distance, ego_spd, t.velocity_x)
        else:
            t.ttc = 0.0
            add_warning_flag_once(t.warning_flags, 'ROUTE_CONTEXT_MISSING')


class TestWarningFlagBehavior:
    """S3-R3 + Codex fix: ROUTE_CONTEXT_MISSING managed symmetrically.

    Added when context unusable; removed on context recovery from cached tracks.
    All tests are ROS-free: tracks are built via _build_obstacle_track and the
    tick logic is exercised through _apply_tick_logic which mirrors _tick().
    """

    def _one_track(self):
        """Build one fresh ObstacleTrack for a simple_obstacle-style cluster."""
        return _build_obstacle_track(1, _make_summary(cx=5.0), _BUMPER_OFFSET)

    def test_missing_context_adds_route_context_missing_flag(self):
        """context_ok=False + one track → ROUTE_CONTEXT_MISSING in warning_flags."""
        track = self._one_track()
        assert track.warning_flags == [], 'sanity: fresh track has no flags'
        _apply_tick_logic([track], context_ok=False)
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags, (
            f'Expected ROUTE_CONTEXT_MISSING; got {track.warning_flags}'
        )

    def test_missing_context_flag_appears_exactly_once_on_cached_tick(self):
        """Simulated cached duplicate tick: flag added once, not twice.

        Reproduces the 20 Hz / 10 Hz cache reuse scenario: same track object
        published on a second tick while context is still missing.
        """
        track = self._one_track()
        _apply_tick_logic([track], context_ok=False)   # tick 1
        _apply_tick_logic([track], context_ok=False)   # tick 2 (cached)
        assert track.warning_flags.count('ROUTE_CONTEXT_MISSING') == 1, (
            f'Flag must appear exactly once; got {track.warning_flags}'
        )

    def test_stale_context_is_not_usable(self):
        """is_route_context_fresh returns False for stale age → flag present.

        age_ms=600 > valid_until_ms=500 → context not fresh → context_ok=False.
        """
        context_ok = is_route_context_fresh(
            msg_age_ms=600, valid_until_ms=500, wall_delta_ms=0.0
        )
        assert context_ok is False, 'stale context must not be usable'
        track = self._one_track()
        _apply_tick_logic([track], context_ok=context_ok)
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags

    def test_zero_validity_is_not_usable(self):
        """valid_until_ms=0 → is_route_context_fresh=False → flag present."""
        context_ok = is_route_context_fresh(
            msg_age_ms=0, valid_until_ms=0, wall_delta_ms=0.0
        )
        assert context_ok is False
        track = self._one_track()
        _apply_tick_logic([track], context_ok=context_ok)
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags

    def test_invalid_route_context_valid_false_adds_flag(self):
        """route_context_valid=False → context_ok=False (checked before freshness).

        _is_context_usable() short-circuits on route_context_valid=False.
        We replicate that by passing context_ok=False directly.
        """
        track = self._one_track()
        _apply_tick_logic([track], context_ok=False)
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags, (
            f'Expected flag for invalid route_context_valid; got {track.warning_flags}'
        )

    def test_usable_context_ego_stopped_no_flag(self):
        """context_ok=True, ego=0 m/s → ttc=0.0 but NO ROUTE_CONTEXT_MISSING."""
        track = self._one_track()
        _apply_tick_logic([track], context_ok=True, ego_spd=0.0)
        assert 'ROUTE_CONTEXT_MISSING' not in track.warning_flags, (
            f'Must not add flag when context is usable; got {track.warning_flags}'
        )
        assert track.ttc == 0.0

    def test_usable_context_positive_ttc_no_flag(self):
        """context_ok=True, ego=2.7 m/s, dist=4.59 → ttc≈1.70, no flag."""
        track = self._one_track()
        _apply_tick_logic([track], context_ok=True, ego_spd=2.7)
        assert 'ROUTE_CONTEXT_MISSING' not in track.warning_flags, (
            f'Must not add flag when context is usable; got {track.warning_flags}'
        )
        assert track.ttc > 1.0, f'Expected ttc≈1.70 s; got {track.ttc}'

    def test_no_tracks_with_missing_context_no_flag(self):
        """context_ok=False but tracks=[] → nothing to iterate, no error."""
        _apply_tick_logic([], context_ok=False)  # must not raise

    def test_multiple_tracks_all_get_flag(self):
        """context_ok=False + two tracks → both tracks get ROUTE_CONTEXT_MISSING."""
        t1 = _build_obstacle_track(1, _make_summary(cx=5.0), _BUMPER_OFFSET)
        t2 = _build_obstacle_track(2, _make_summary(cx=8.0), _BUMPER_OFFSET)
        _apply_tick_logic([t1, t2], context_ok=False)
        for t in (t1, t2):
            assert 'ROUTE_CONTEXT_MISSING' in t.warning_flags, (
                f'track_id={t.track_id}: expected flag; got {t.warning_flags}'
            )

    # ------------------------------------------------------------------
    # S3-R3 Codex fix — context recovery removes stale flag from cache
    # ------------------------------------------------------------------

    def test_recovery_missing_then_usable_removes_flag_positive_ttc(self):
        """Codex fix: stale flag cleared when context becomes usable (positive TTC).

        Simulates the Codex finding scenario:
          1. Track cached; context missing → ROUTE_CONTEXT_MISSING added.
          2. Same track object reused; context now usable → flag removed, TTC > 0.
        """
        track = self._one_track()
        _apply_tick_logic([track], context_ok=False)          # tick 1: missing
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags
        _apply_tick_logic([track], context_ok=True, ego_spd=2.7)  # tick 2: recovered
        assert 'ROUTE_CONTEXT_MISSING' not in track.warning_flags, (
            f'Flag must be cleared on context recovery; got {track.warning_flags}'
        )
        assert track.ttc > 1.0, (
            f'Expected positive TTC after recovery; got {track.ttc}'
        )

    def test_recovery_missing_then_usable_removes_flag_ego_stopped(self):
        """Codex fix: stale flag cleared on recovery even when ego is stopped.

        ego=0 → ttc=0.0 but the flag must still be removed because context IS usable.
        """
        track = self._one_track()
        _apply_tick_logic([track], context_ok=False)           # tick 1: missing
        assert 'ROUTE_CONTEXT_MISSING' in track.warning_flags
        _apply_tick_logic([track], context_ok=True, ego_spd=0.0)  # tick 2: recovered
        assert 'ROUTE_CONTEXT_MISSING' not in track.warning_flags, (
            f'Flag must be cleared on recovery (ego stopped); got {track.warning_flags}'
        )
        assert track.ttc == 0.0

    def test_recovery_preserves_other_flags(self):
        """Context recovery removes only ROUTE_CONTEXT_MISSING; other flags survive."""
        track = self._one_track()
        track.warning_flags.append('STALE_MESSAGE')
        _apply_tick_logic([track], context_ok=False)           # adds ROUTE_CONTEXT_MISSING
        _apply_tick_logic([track], context_ok=True, ego_spd=2.7)  # removes only it
        assert 'ROUTE_CONTEXT_MISSING' not in track.warning_flags
        assert 'STALE_MESSAGE' in track.warning_flags, (
            f'Other flags must be preserved; got {track.warning_flags}'
        )
