# perception/centroid_tracker.py
#
# Sprint 2 / S2-B4 — ROS-free nearest-centroid tracker.
# No rclpy, sensor_msgs, std_msgs, geometry_msgs, PCL, or numpy.
# Importable without a ROS2 installation.
#
# Public API:
#   CentroidTracker(max_association_distance_m=1.0, max_missed_frames=3)
#       .update(cluster_xys, dt_s) -> list[dict]
#       .reset()
#       .active_track_count  (property)
#       .next_id             (property)

import math as _math

# Obstacles with speed below this threshold (m/s) are considered static.
_STATIC_SPEED_THRESHOLD: float = 0.1


class CentroidTracker:
    """Nearest-centroid greedy tracker for 2-D obstacle centroids.

    Tracks persist across frames via nearest-centroid greedy association.
    Unmatched tracks age out after max_missed_frames consecutive misses.
    Track IDs are monotonically increasing integers starting at 1 and
    never reset across update() calls (reset() clears tracks but not the
    next-ID counter, so IDs remain globally unique in the session).

    Velocity is estimated from centroid displacement divided by dt_s.
    is_static is True when the speed magnitude is strictly below 0.1 m/s.

    dt source (S2-B4 decision): the caller supplies dt_s, computed from the
    PointCloud2 header.stamp delta when the stamp is nonzero, otherwise 0.0
    for the first message.  This prevents double-processing the same message
    when the node tick rate exceeds the publisher rate.  See
    wiki/perception/lidar_obstacle_node.md §S2-B4 for the full rationale.
    """

    def __init__(
        self,
        max_association_distance_m: float = 1.0,
        max_missed_frames: int = 3,
    ) -> None:
        self._max_dist_sq: float = max_association_distance_m ** 2
        self._max_missed: int = max_missed_frames
        self._next_id: int = 1
        # track_id -> {'cx': float, 'cy': float,
        #               'vx': float, 'vy': float, 'missed': int}
        self._tracks: dict = {}

    # ------------------------------------------------------------------
    # Public interface

    def update(self, cluster_xys: list, dt_s: float) -> list:
        """Associate clusters, update velocities, return one dict per cluster.

        cluster_xys: list of (cx, cy) tuples — one per cluster this frame.
        dt_s:        elapsed seconds since the previous update() call.
                     Pass 0.0 on the first call or after reset().
                     When dt_s <= 0.0 the velocity is kept at its previous
                     value (or 0.0 for newly created tracks) — no division
                     by zero occurs.

        Returns a list[dict] in the same order as cluster_xys:
            {
              'track_id':   int,
              'velocity_x': float,  # m/s, +x = forward in base_link
              'velocity_y': float,  # m/s, +y = left in base_link
              'is_static':  bool,   # True when |v| < 0.1 m/s
            }

        Side effects: unmatched tracks are aged; tracks exceeding
        max_missed_frames are removed from the internal state.
        """
        track_ids = list(self._tracks.keys())

        # Build greedy association candidates within max_association_distance.
        candidates = []
        for ci, (cx, cy) in enumerate(cluster_xys):
            for tid in track_ids:
                t = self._tracks[tid]
                dx = cx - t['cx']
                dy = cy - t['cy']
                d_sq = dx * dx + dy * dy
                if d_sq <= self._max_dist_sq:
                    candidates.append((d_sq, ci, tid))
        # Sort ascending by distance — closest pairs are assigned first.
        candidates.sort(key=lambda item: item[0])

        matched_clusters: set = set()
        matched_tracks: set = set()
        cluster_to_track: dict = {}

        for _, ci, tid in candidates:
            if ci in matched_clusters or tid in matched_tracks:
                continue
            matched_clusters.add(ci)
            matched_tracks.add(tid)
            cluster_to_track[ci] = tid

        # Update matched tracks: velocity from centroid delta / dt.
        use_velocity = dt_s > 0.0
        for ci, (cx, cy) in enumerate(cluster_xys):
            if ci not in cluster_to_track:
                continue
            tid = cluster_to_track[ci]
            t = self._tracks[tid]
            if use_velocity:
                t['vx'] = (cx - t['cx']) / dt_s
                t['vy'] = (cy - t['cy']) / dt_s
            t['cx'] = cx
            t['cy'] = cy
            t['missed'] = 0

        # Age unmatched existing tracks.
        for tid in track_ids:
            if tid not in matched_tracks:
                self._tracks[tid]['missed'] += 1

        # Remove tracks that exceeded max_missed_frames.
        stale_ids = [
            tid for tid, t in self._tracks.items()
            if t['missed'] > self._max_missed
        ]
        for tid in stale_ids:
            del self._tracks[tid]

        # Create new tracks for unmatched clusters (vx=vy=0, missed=0).
        for ci in range(len(cluster_xys)):
            if ci not in cluster_to_track:
                new_id = self._next_id
                self._next_id += 1
                cx, cy = cluster_xys[ci]
                self._tracks[new_id] = {
                    'cx': cx, 'cy': cy,
                    'vx': 0.0, 'vy': 0.0,
                    'missed': 0,
                }
                cluster_to_track[ci] = new_id

        # Build result list in the same order as cluster_xys.
        result = []
        for ci in range(len(cluster_xys)):
            tid = cluster_to_track[ci]
            t = self._tracks[tid]
            vx = t['vx']
            vy = t['vy']
            speed = _math.sqrt(vx * vx + vy * vy)
            result.append({
                'track_id':   tid,
                'velocity_x': vx,
                'velocity_y': vy,
                'is_static':  speed < _STATIC_SPEED_THRESHOLD,
            })

        return result

    def reset(self) -> None:
        """Remove all active tracks.  The next-ID counter is NOT reset.

        Used when the input becomes stale so new tracks after recovery do
        not inherit stale centroid positions and compute spurious velocities.
        """
        self._tracks.clear()

    # ------------------------------------------------------------------
    # Inspection helpers (primarily for tests)

    @property
    def active_track_count(self) -> int:
        """Number of currently active (non-removed) tracks."""
        return len(self._tracks)

    @property
    def next_id(self) -> int:
        """The ID that will be assigned to the next new track."""
        return self._next_id
