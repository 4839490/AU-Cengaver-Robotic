# perception/lidar_obstacle_node.py
#
# Sprint 2 Track B (S2-B1..S2-B5) + Sprint 3 Track R S3-R2 + S3-R3.
#
# Subscribes to /velodyne_points (sensor_msgs/PointCloud2), decodes the
# little-endian float32 x/y/z/intensity layout, filters ground points
# (z <= 0.2 m), clusters above-ground points by Euclidean distance, and
# publishes one ObstacleTrack per cluster on /perception/obstacle_tracks.
#
# S3-R2 additions over S2-B5:
#   - Subscribe to /planning/active_route_context (planning_msgs/ActiveRouteContext)
#   - Track latest context and wall-clock receive time
#   - _is_context_usable(): route_context_valid=True AND message age fresh AND
#     wall-clock delta since callback fresh (both within valid_until_ms window)
#   - Per-tick TTC computation: closing_speed = ego_speed_mps - velocity_x;
#     ttc = distance / closing_speed when context usable AND closing_speed > 0.1
#     AND distance > 0; else ttc = 0.0
#   - TTC is re-evaluated every publish tick so ego_speed changes are reflected
#     even when cached tracks are reused between pointcloud messages
#
# S3-R3 additions over S3-R2:
#   - When tracks exist but context is NOT usable: ttc=0.0 AND
#     add "ROUTE_CONTEXT_MISSING" to each track's warning_flags once
#     (add_warning_flag_once prevents duplicates on cached-tick republish)
#   - Usable context + closing_speed<=0.1: ttc=0.0, no flag added
#   - No tracks: no flag (nothing to iterate)
#
# No /cmd_vel, /control/*, /beemobs/* publications — perception evidence only.
#
# Contract references:
#   wiki/contracts/message_contracts.md §ObstacleTrack / §ObstacleTracks
#   wiki/architecture/active_route_context.md §freshness rule
#   wiki/perception/lidar_obstacle_node.md §S3-R2 §S3-R3

import time
from typing import Optional

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

from perception_msgs.msg import ObstacleTrack, ObstacleTracks
from planning_msgs.msg import ActiveRouteContext

from perception.centroid_tracker import CentroidTracker
from perception.dummy_common import BASE_LINK_FRAME_ID, make_header
from perception.lidar_cluster_utils import (
    cluster_summary,
    decode_pointcloud2_data,
    euclidean_cluster,
    filter_ground,
    front_bumper_distance,
)
from perception.ttc_utils import (
    add_warning_flag_once,
    compute_ttc,
    is_route_context_fresh,
    remove_warning_flag,
)

_DEFAULT_POINTCLOUD_TOPIC = '/velodyne_points'
_DEFAULT_ROUTE_CTX_TOPIC = '/planning/active_route_context'
_DEFAULT_PUBLISH_HZ = 20.0
_DEFAULT_STALE_MS = 200
_DEFAULT_GROUND_Z = 0.2           # m — points at or below this are discarded
_DEFAULT_CLUSTER_DIST = 0.5       # m — Euclidean merge threshold
# BEE1 front_overhang_m from vehicle_params.yaml; distance contract §10:
# ObstacleTrack.distance = front-bumper-referenced scalar.
_DEFAULT_FRONT_BUMPER_OFFSET = 0.410  # m
_DEFAULT_MAX_ASSOC_DIST = 1.0     # m — max centroid jump for track association
_DEFAULT_MAX_MISSED = 3           # frames — track removed after this many misses
# ActiveRouteContext contract default: valid_until_ms = 500 ms.
_DEFAULT_ROUTE_CTX_VALID_UNTIL_MS = 500

# PointField.FLOAT32 constant (= 7 in sensor_msgs) — hardcoded to avoid
# importing PointField in the ROS-free helper, kept here for inline check.
_FLOAT32_DATATYPE = 7


def _extract_field_offsets(msg: PointCloud2):
    """Extract field name → byte offset from the PointCloud2 message.

    Returns a dict on success or None if the layout is unsupported
    (missing x/y/z fields or non-FLOAT32 types for x/y/z).
    """
    offsets = {f.name: f.offset for f in msg.fields}

    for req in ('x', 'y', 'z'):
        if req not in offsets:
            return None

    for f in msg.fields:
        if f.name in ('x', 'y', 'z') and f.datatype != _FLOAT32_DATATYPE:
            return None

    return offsets


def _build_obstacle_track(
    track_id: int,
    summary: dict,
    bumper_offset_m: float,
    velocity_x: float = 0.0,
    velocity_y: float = 0.0,
    is_static: bool = True,
) -> ObstacleTrack:
    """Construct one ObstacleTrack from a cluster summary and tracker result."""
    track = ObstacleTrack()
    track.track_id = track_id
    track.class_label = ObstacleTrack.UNKNOWN_OBSTACLE  # 0
    track.confidence = 0.8

    cx = summary['centroid_x']
    cy = summary['centroid_y']
    track.position_x = cx
    track.position_y = cy
    # Contract §10: front-bumper-referenced scalar distance (m).
    track.distance = front_bumper_distance(cx, bumper_offset_m)

    track.velocity_x = velocity_x
    track.velocity_y = velocity_y
    track.ttc = 0.0   # Sprint 3: wire ego_speed_mps for real TTC

    # Bounding box extents — clip to at least 1 cm to avoid degenerate messages.
    track.width = max(summary['max_y'] - summary['min_y'], 0.01)
    track.length = max(summary['max_x'] - summary['min_x'], 0.01)
    track.height = max(summary['max_z'] - summary['min_z'], 0.01)

    track.is_static = is_static
    track.source_sensor = 'lidar_cluster'
    track.semantic_source = 'none'
    track.geometry_source = 'lidar'   # contract-canonical: "lidar" | "fusion" | ""
    track.age_ms = 0
    track.valid_until_ms = 200
    track.warning_flags = []
    return track


class LidarObstacleNode(Node):
    """S3-R3: TTC from active_route_context; ROUTE_CONTEXT_MISSING flag when context unusable."""

    def __init__(self) -> None:
        super().__init__('lidar_obstacle_node')

        self.declare_parameter('pointcloud_topic', _DEFAULT_POINTCLOUD_TOPIC)
        self.declare_parameter('route_context_topic', _DEFAULT_ROUTE_CTX_TOPIC)
        self.declare_parameter('publish_hz', _DEFAULT_PUBLISH_HZ)
        self.declare_parameter('pointcloud_stale_ms', _DEFAULT_STALE_MS)
        self.declare_parameter('ground_z_threshold', _DEFAULT_GROUND_Z)
        self.declare_parameter('cluster_distance_threshold', _DEFAULT_CLUSTER_DIST)
        self.declare_parameter('front_bumper_offset_m', _DEFAULT_FRONT_BUMPER_OFFSET)
        self.declare_parameter('max_association_distance_m', _DEFAULT_MAX_ASSOC_DIST)
        self.declare_parameter('max_missed_frames', _DEFAULT_MAX_MISSED)

        pc_topic: str = (
            self.get_parameter('pointcloud_topic')
            .get_parameter_value().string_value
        )
        ctx_topic: str = (
            self.get_parameter('route_context_topic')
            .get_parameter_value().string_value
        )
        publish_hz: float = (
            self.get_parameter('publish_hz')
            .get_parameter_value().double_value
        )
        self._stale_ms: int = (
            self.get_parameter('pointcloud_stale_ms')
            .get_parameter_value().integer_value
        )
        self._ground_z: float = (
            self.get_parameter('ground_z_threshold')
            .get_parameter_value().double_value
        )
        self._cluster_dist: float = (
            self.get_parameter('cluster_distance_threshold')
            .get_parameter_value().double_value
        )
        self._bumper_offset: float = (
            self.get_parameter('front_bumper_offset_m')
            .get_parameter_value().double_value
        )
        self._max_assoc_dist: float = (
            self.get_parameter('max_association_distance_m')
            .get_parameter_value().double_value
        )
        self._max_missed: int = (
            self.get_parameter('max_missed_frames')
            .get_parameter_value().integer_value
        )

        self._last_pc_wall_sec: Optional[float] = None
        self._latest_msg: Optional[PointCloud2] = None

        # S3-R2: route context state — latest received message and wall-clock
        # receive time. Both must be set for _is_context_usable() to return True.
        self._latest_context: Optional[ActiveRouteContext] = None
        self._context_wall_sec: Optional[float] = None

        # S2-B4: centroid tracker state
        self._tracker = CentroidTracker(
            max_association_distance_m=self._max_assoc_dist,
            max_missed_frames=self._max_missed,
        )
        # Stamp of the last message fed into the tracker (nanoseconds).
        # Used to deduplicate: when the node ticks faster than the publisher,
        # the same message is re-published without re-running the tracker.
        self._last_msg_stamp_ns: int = 0
        self._cached_tracks: list = []

        self._sub = self.create_subscription(
            PointCloud2, pc_topic, self._on_pointcloud, 10)

        # S3-R2: subscribe to route context for ego_speed_mps / TTC computation.
        self._ctx_sub = self.create_subscription(
            ActiveRouteContext, ctx_topic, self._on_route_context, 10)

        self._pub = self.create_publisher(
            ObstacleTracks, '/perception/obstacle_tracks', 10)

        self.create_timer(1.0 / publish_hz, self._tick)

        self.get_logger().info(
            f'lidar_obstacle_node up (S3-R3) — '
            f'subscribing {pc_topic} + {ctx_topic}, '
            f'publishing /perception/obstacle_tracks at {publish_hz} Hz. '
            f'ground_z={self._ground_z} m, cluster_dist={self._cluster_dist} m, '
            f'front_bumper_offset={self._bumper_offset} m, '
            f'max_assoc_dist={self._max_assoc_dist} m, '
            f'max_missed_frames={self._max_missed}'
        )

    def _on_pointcloud(self, msg: PointCloud2) -> None:
        self._last_pc_wall_sec = time.monotonic()
        self._latest_msg = msg

    def _on_route_context(self, msg: ActiveRouteContext) -> None:
        self._latest_context = msg
        self._context_wall_sec = time.monotonic()

    def _is_context_usable(self) -> bool:
        """Return True when route context is present, valid, and fresh.

        Freshness: message's own age_ms <= valid_until_ms AND wall-clock
        elapsed since callback <= valid_until_ms (both must hold).
        When False, _tick() sets ttc=0.0 and adds ROUTE_CONTEXT_MISSING flag.
        """
        if self._latest_context is None or self._context_wall_sec is None:
            return False
        ctx = self._latest_context
        if not ctx.route_context_valid:
            return False
        wall_delta_ms = (time.monotonic() - self._context_wall_sec) * 1000.0
        return is_route_context_fresh(ctx.age_ms, ctx.valid_until_ms, wall_delta_ms)

    def _input_state(self) -> str:
        if self._last_pc_wall_sec is None:
            return 'no_input'
        age_ms = (time.monotonic() - self._last_pc_wall_sec) * 1000.0
        return 'fresh' if age_ms <= self._stale_ms else 'stale'

    def _process_pointcloud(self, msg: PointCloud2, dt_s: float) -> list:
        """Decode, filter, cluster, track. Returns list[ObstacleTrack].

        dt_s: elapsed seconds since last processed message (from header stamp
              delta). Pass 0.0 for the first message or after tracker reset.
        """
        # Validate field layout.
        offsets = _extract_field_offsets(msg)
        if offsets is None:
            self.get_logger().debug(
                'Unsupported PointCloud2 field layout — tracks=[]'
            )
            return []

        if msg.is_bigendian:
            self.get_logger().debug(
                'Big-endian PointCloud2 not supported — tracks=[]'
            )
            return []

        # Decode bytes → list of (x, y, z, intensity).
        points = decode_pointcloud2_data(
            bytes(msg.data), offsets, msg.point_step,
            msg.width, msg.height, msg.row_step)

        # Ground filter.
        above_ground = filter_ground(points, self._ground_z) if points else []

        # Euclidean clustering.
        clusters = euclidean_cluster(above_ground, self._cluster_dist) if above_ground else []

        # Collect summaries for valid clusters.
        summaries = [cluster_summary(c) for c in clusters if c]
        summaries = [s for s in summaries if s]

        # Update tracker with current cluster centroids (empty list ages out tracks).
        cluster_xys = [(s['centroid_x'], s['centroid_y']) for s in summaries]
        track_infos = self._tracker.update(cluster_xys, dt_s)

        # Build one ObstacleTrack per cluster.
        return [
            _build_obstacle_track(
                info['track_id'], s, self._bumper_offset,
                info['velocity_x'], info['velocity_y'], info['is_static']
            )
            for s, info in zip(summaries, track_infos)
        ]

    def _tick(self) -> None:
        state = self._input_state()
        if state != 'fresh':
            self.get_logger().debug(f'point cloud input state: {state}')

        tracks = []
        if state == 'fresh' and self._latest_msg is not None:
            pc_msg = self._latest_msg
            stamp = pc_msg.header.stamp
            stamp_ns = stamp.sec * 10 ** 9 + stamp.nanosec

            # Deduplicate: re-use cached result when the same message arrives
            # again at the next tick (node ticks at 20 Hz, publisher at 10 Hz).
            # A zero stamp is treated as "always new" — safe fallback for
            # misconfigured publishers (make_header always produces nonzero stamps).
            is_new_msg = (stamp_ns == 0) or (stamp_ns != self._last_msg_stamp_ns)

            if is_new_msg:
                # Compute dt from header stamp delta.
                if stamp_ns > 0 and self._last_msg_stamp_ns > 0:
                    dt_s = max((stamp_ns - self._last_msg_stamp_ns) / 1.0e9, 0.0)
                else:
                    dt_s = 0.0  # first message or zero stamp → no velocity
                if stamp_ns != 0:
                    self._last_msg_stamp_ns = stamp_ns

                try:
                    self._cached_tracks = self._process_pointcloud(pc_msg, dt_s)
                except Exception as exc:
                    self.get_logger().debug(
                        f'PointCloud2 processing error (tracks=[]): {exc}'
                    )
                    self._cached_tracks = []

            tracks = self._cached_tracks
        else:
            # Stale or no input — clear cache and reset tracker so stale centroid
            # positions do not contaminate velocity estimates after recovery.
            if self._cached_tracks or self._last_msg_stamp_ns != 0:
                self._cached_tracks = []
                self._last_msg_stamp_ns = 0
                self._tracker.reset()

        # S3-R2/S3-R3: re-evaluate TTC every publish tick so ego_speed changes
        # are reflected even when the point-cloud cache is reused (20 Hz node /
        # 10 Hz pointcloud publisher).
        # S3-R3 Codex fix: when context becomes usable again while the same
        # cached track object is reused, remove any stale ROUTE_CONTEXT_MISSING
        # flag before computing TTC so consumers see a clean flag list.
        context_ok = self._is_context_usable()
        ego_spd = (
            float(self._latest_context.ego_speed_mps)
            if context_ok else 0.0
        )
        for t in tracks:
            if context_ok:
                remove_warning_flag(t.warning_flags, 'ROUTE_CONTEXT_MISSING')
                t.ttc = compute_ttc(t.distance, ego_spd, t.velocity_x)
            else:
                t.ttc = 0.0
                add_warning_flag_once(t.warning_flags, 'ROUTE_CONTEXT_MISSING')

        # Stamp current pointcloud age onto every track before publishing.
        # On the first tick after a new PointCloud2 age_ms ≈ 0; on a cached
        # duplicate tick (20 Hz node / 10 Hz publisher) age_ms ≈ 50 ms.
        # Both values stay well below valid_until_ms=200.
        if tracks and self._last_pc_wall_sec is not None:
            age_ms = int(
                max((time.monotonic() - self._last_pc_wall_sec) * 1000.0, 0.0)
            )
            for track in tracks:
                track.age_ms = age_ms

        out = ObstacleTracks()
        out.header = make_header(self, BASE_LINK_FRAME_ID)
        out.tracks = tracks
        self._pub.publish(out)


def main(args=None) -> None:
    rclpy.init(args=args)
    node = LidarObstacleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
