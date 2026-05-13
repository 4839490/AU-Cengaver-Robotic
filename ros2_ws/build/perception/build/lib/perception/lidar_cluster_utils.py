# perception/lidar_cluster_utils.py
#
# Sprint 2 / S2-B3 — ROS-free helper: PointCloud2 byte decoding, ground
# filtering, Euclidean clustering, and distance helpers.
#
# No rclpy, sensor_msgs, std_msgs, geometry_msgs, PCL, or numpy.
# Plain Python only — importable without a ROS2 installation.
#
# Public API:
#   decode_pointcloud2_data(data, field_offsets, point_step,
#                           width, height, row_step)  -> list[(x,y,z,i)]
#   filter_ground(points, ground_z_threshold=0.2)     -> list
#   euclidean_cluster(points, distance_threshold=0.5) -> list[list]
#   cluster_summary(cluster)                          -> dict
#   front_bumper_distance(position_x, front_bumper_offset_m=0.0) -> float

import struct as _struct

_F32 = _struct.Struct('<f')   # little-endian float32, 4 bytes


# ---------------------------------------------------------------------------
# PointCloud2 byte decoding
# ---------------------------------------------------------------------------

def decode_pointcloud2_data(
    data: bytes,
    field_offsets: dict,
    point_step: int,
    width: int = None,
    height: int = 1,
    row_step: int = None,
) -> list:
    """Decode raw PointCloud2 bytes into a list of (x, y, z, intensity) tuples.

    field_offsets: dict mapping field name to byte offset within one point
                   record.  Must contain 'x', 'y', 'z'; 'intensity' optional.
    point_step:    size in bytes of one point record.
    width:         number of valid points per row.  When omitted, inferred
                   as len(data) // point_step (unorganised-cloud shorthand).
    height:        number of rows (1 for unorganised / lidar clouds).
    row_step:      size in bytes of one row including any padding.  When
                   omitted, inferred as width * point_step (no padding).

    Validation — returns [] when any condition holds:
      - data is not bytes/bytearray
      - point_step <= 0
      - required field ('x', 'y', 'z') absent from field_offsets
      - any required field offset + 4 > point_step (field extends past record)
      - row_step < point_step * width  (rows would be truncated)
      - len(data) < row_step * height  (data buffer is shorter than declared)

    Padding at the end of each row is correctly skipped: only 'width' points
    per row are decoded, not row_step // point_step.

    Returns [] on any struct decode error.  Never raises.
    """
    if not isinstance(data, (bytes, bytearray)):
        return []
    if point_step <= 0:
        return []
    for req in ('x', 'y', 'z'):
        if req not in field_offsets:
            return []

    # Validate that required field offsets fit within a point record.
    for req in ('x', 'y', 'z'):
        if field_offsets[req] + 4 > point_step:
            return []

    x_off = field_offsets['x']
    y_off = field_offsets['y']
    z_off = field_offsets['z']
    i_off = field_offsets.get('intensity')
    # Ignore intensity if its offset would extend past the point record.
    if i_off is not None and i_off + 4 > point_step:
        i_off = None

    # Compute defaults for width and row_step.
    if width is None:
        width = len(data) // point_step
    if row_step is None:
        row_step = width * point_step

    # Validate row_step vs width.
    if row_step < point_step * width:
        return []

    # Validate data buffer length.
    if len(data) < row_step * height:
        return []

    if width == 0 or height == 0:
        return []

    result = []
    unpack = _F32.unpack_from
    try:
        for r in range(height):
            row_base = r * row_step
            for c in range(width):
                base = row_base + c * point_step
                x = unpack(data, base + x_off)[0]
                y = unpack(data, base + y_off)[0]
                z = unpack(data, base + z_off)[0]
                intensity = unpack(data, base + i_off)[0] if i_off is not None else 0.0
                result.append((x, y, z, intensity))
    except Exception:
        return []

    return result


# ---------------------------------------------------------------------------
# Ground filtering
# ---------------------------------------------------------------------------

def filter_ground(points: list, ground_z_threshold: float = 0.2) -> list:
    """Return only the points whose z value is strictly above ground_z_threshold.

    Points are expected to be iterables with at least 3 elements: (x, y, z, ...).
    Points with z <= ground_z_threshold are discarded as ground returns.
    """
    return [p for p in points if p[2] > ground_z_threshold]


# ---------------------------------------------------------------------------
# Euclidean clustering
# ---------------------------------------------------------------------------

def euclidean_cluster(points: list, distance_threshold: float = 0.5) -> list:
    """Cluster points by Euclidean distance using BFS flood-fill.

    Two points belong to the same cluster when their 3-D Euclidean distance is
    <= distance_threshold.  Clustering is transitive: if A connects to B and B
    connects to C, all three are in one cluster.

    Points must be iterables with at least 3 elements: (x, y, z, ...).

    Returns a list of clusters; each cluster is a list of points taken directly
    from the input.  Returns [] for empty input.
    """
    if not points:
        return []

    n = len(points)
    assigned = [False] * n
    clusters = []
    thresh_sq = distance_threshold * distance_threshold

    for seed in range(n):
        if assigned[seed]:
            continue
        assigned[seed] = True
        members = [seed]
        queue = [seed]

        while queue:
            cur = queue.pop()
            cx, cy, cz = points[cur][0], points[cur][1], points[cur][2]
            for j in range(n):
                if assigned[j]:
                    continue
                dx = cx - points[j][0]
                dy = cy - points[j][1]
                dz = cz - points[j][2]
                if dx * dx + dy * dy + dz * dz <= thresh_sq:
                    assigned[j] = True
                    members.append(j)
                    queue.append(j)

        clusters.append([points[i] for i in members])

    return clusters


# ---------------------------------------------------------------------------
# Cluster summary
# ---------------------------------------------------------------------------

def cluster_summary(cluster: list) -> dict:
    """Compute centroid and bounding-box statistics for a cluster.

    Each point must have at least 3 elements: (x, y, z, ...).

    Returns a dict:
        centroid_x, centroid_y, centroid_z — arithmetic mean
        min_x, max_x, min_y, max_y, min_z, max_z — axis-aligned bounding box
        point_count — number of points in the cluster

    Returns {} for empty input.
    """
    if not cluster:
        return {}

    xs = [p[0] for p in cluster]
    ys = [p[1] for p in cluster]
    zs = [p[2] for p in cluster]
    n = len(cluster)

    return {
        'centroid_x': sum(xs) / n,
        'centroid_y': sum(ys) / n,
        'centroid_z': sum(zs) / n,
        'min_x': min(xs), 'max_x': max(xs),
        'min_y': min(ys), 'max_y': max(ys),
        'min_z': min(zs), 'max_z': max(zs),
        'point_count': n,
    }


# ---------------------------------------------------------------------------
# Distance helpers
# ---------------------------------------------------------------------------

def front_bumper_distance(position_x: float, front_bumper_offset_m: float = 0.0) -> float:
    """Compute the front-bumper-referenced scalar distance for an obstacle.

    position_x:          obstacle centroid x in base_link (m, +forward).
    front_bumper_offset_m: distance from base_link origin to the front bumper
                           along +x (BEE1 = front_overhang_m = 0.410 m, from
                           vehicle_params.yaml).

    Returns max(position_x - front_bumper_offset_m, 0.0) — clipped to zero
    when the obstacle is at or behind the front bumper.
    """
    return max(position_x - front_bumper_offset_m, 0.0)
