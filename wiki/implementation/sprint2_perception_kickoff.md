# Sprint 2 Perception Kickoff

Sources: `wiki/implementation/perception_sprint_plan.md`, `wiki/perception/lane_node.md`, `wiki/perception/lidar_obstacle_node.md`, `wiki/contracts/message_contracts.md`, `wiki/contracts/timing_and_fallback.md`.

> **This page is planning guidance only.** It does not override `wiki/contracts/message_contracts.md`. Any field names or types here are derived from that page; the contract page is authoritative. If they conflict, the contract page wins and this page should be updated.

---

## Sprint goal

Deliver a working `lane_node` MVP (Track A) and a working `lidar_obstacle_node` MVP (Track B), each publishing contract-shaped messages on their respective `/perception/*` topics, testable without Gazebo or physical sensors.

- **Track A starts first.** Track B begins after Track A reaches a stable publishing state (S2-A3 or later, when `lane_node` publishes non-empty `LaneModel` on valid synthetic input).
- Neither track requires Gazebo 11. Fake/synthetic publishers are the intended test input while Gazebo sim skeleton (V-B4) is not yet ready.
- Neither track requires production inference models (UFLD v2 / TensorRT / PointPillars). Simple classical algorithms are the accepted MVP path.

---

## Architecture boundaries (mandatory — applies to every commit in Sprint 2)

| Rule | Rationale |
|---|---|
| Perception publishes **evidence only**: detections, tracks, confidence, `valid_until_ms`, `warning_flags`. | Contract §1 / CLAUDE.md "Core Architecture Rules" |
| Planner/FSM make all driving decisions. | Perception nodes must not publish stop commands, speed commands, steering commands, or mode changes. |
| No `/cmd_vel`, `/control/*`, `/beemobs/*` topics may be published by any perception node. | Forbidden by architecture. Checked via `ros2 topic list` grep after every smoke test. |
| Do **not** create `fsm_msgs`, `localization_msgs`, `planner`, `controller`, `fsm`, or `localization` packages. | Blocked pending owner sign-off — see `wiki/contracts/message_contracts.md` §"Blocked". |
| Do **not** add fields to `.msg` files. | Contract change procedure required for any field addition. |
| Do **not** compute `in_path` in perception. | `in_path` is planner-side, computed against `/planning/active_route_context.planned_trajectory`. |

---

## Track A — lane_node MVP

### Deliverables S2-A1..S2-A5

| # | Deliverable | Acceptance signal |
|---|---|---|
| S2-A1 | Subscribe `/zed2/left/image_raw` (`sensor_msgs/Image`). Node log confirms subscription on startup. | `ros2 topic info /zed2/left/image_raw -v` shows `lane_node` as subscriber |
| S2-A2 | Fake image publisher — synthetic lane-on-road frames (`bgr8`, ≥ 10 Hz). Reuse or extend `fake_image_pub.py`. Gazebo not required. | Consecutive timestamp deltas confirm ≥ 10 Hz |
| S2-A3 | Simple lane detector (Hough lines or polynomial fit on thresholded image). Populate `centerline[]`, `left_boundary[]`, `right_boundary[]`, `curvature`. `lane_lost = false` when lines are detected in the frame. | `ros2 topic echo /perception/lane_model` — arrays non-empty; `lane_lost = false` on a frame that contains detectable lane lines |
| S2-A4 | All contract fields populated: `lane_confidence ∈ [0,1]`, `lane_width_estimate`, `valid_until_ms = 500`, `age_ms`, `source_sensor = "camera"`, `warning_flags` (subset of `LOW_CONFIDENCE \| STALE_MESSAGE \| LANE_BOUNDARY_MISSING`). | Echo confirms field completeness; `LOW_CONFIDENCE` flag set when `lane_confidence < 0.7` |
| S2-A5 | Unit tests: contract field compliance; `lane_lost` triggers on blank / no-line frame; `LOW_CONFIDENCE` and `LANE_BOUNDARY_MISSING` flags set correctly; `valid_until_ms` is exactly 500. | `colcon test --packages-select perception` — all Track A tests pass |

### LaneModel required fields (from `wiki/contracts/message_contracts.md` §LaneModel)

```
std_msgs/Header header           # stamp + frame_id = "base_link"
geometry_msgs/Point[] centerline # base_link; ≥5 m forward; spacing ≤ 0.1 m when lane detected
geometry_msgs/Point[] left_boundary
geometry_msgs/Point[] right_boundary
float32 lane_confidence          # 0.0–1.0
bool    lane_lost                # true → planner reduces speed immediately
float32 curvature                # 1/m (straight ≈ 2.5 m, sharp turn ≈ 0.8 m)
float32 lane_width_estimate      # m
uint32  age_ms
uint32  valid_until_ms           # must be 500
string  source_sensor            # "camera"
string[] warning_flags           # LOW_CONFIDENCE | STALE_MESSAGE | LANE_BOUNDARY_MISSING
```

Do not add, remove, or rename any of these fields. If a field is ambiguous, raise it in the team before changing the contract.

### Track A acceptance gate

All of the following must be true before Track A is declared complete:

1. `colcon build --packages-select perception` exits 0.
2. `colcon test --packages-select perception` — all Track A tests pass (no failures, no errors).
3. `ros2 topic echo /perception/lane_model` with fake image input shows non-empty `centerline[]` and `lane_lost = false`.
4. `ros2 topic echo /perception/lane_model` with blank / no-line input shows `lane_lost = true` and `LANE_BOUNDARY_MISSING` in `warning_flags`.
5. `ros2 topic hz /perception/lane_model` shows ≥ 15 Hz sustained.
6. `ros2 topic list | grep -E '^(/cmd_vel|/control|/beemobs)'` → no matches.

---

## Track B — lidar_obstacle_node MVP

Track B begins after Track A reaches S2-A3 (stable non-empty `LaneModel` publishing).

### Deliverables S2-B1..S2-B5

| # | Deliverable | Acceptance signal |
|---|---|---|
| S2-B1 | Subscribe `/velodyne_points` (`sensor_msgs/PointCloud2`). Node log confirms subscription on startup. | `ros2 topic info /velodyne_points -v` shows `lidar_obstacle_node` as subscriber |
| S2-B2 | Fake PointCloud2 publisher (`fake_pointcloud_pub.py`) — synthetic VLP-16-style 360° point clouds at ≥ 10 Hz. Gazebo not required. | `ros2 topic hz /velodyne_points` ≥ 10 Hz (or timestamp-delta confirmation for large messages) |
| S2-B3 | RANSAC ground plane removal + PCL Euclidean clustering. Non-ground clusters published as `ObstacleTrack[]` entries with `class_label = UNKNOWN_OBSTACLE (0)`, `source_sensor = "lidar_cluster"`. | `ros2 topic echo /perception/obstacle_tracks` — `tracks[]` non-empty on synthetic cloud with above-ground points |
| S2-B4 | Centroid Kalman tracker (constant-velocity). `track_id`, `velocity_x/y`, `is_static` (`\|v\| < 0.1 m/s`), `width/length/height` from cluster geometry populated. Scalar TTC computed via `distance / max(ego_speed, 0.001)` using `ego_speed_mps = 0.0` placeholder; `active_route_context` subscriber wired as a Sprint 3 TODO comment. | Echo confirms `ttc` field present; `is_static = true` on stationary cluster; `track_id` stable across consecutive messages for the same object |
| S2-B5 | Unit tests: cluster → track pipeline; `is_static` threshold; `valid_until_ms = 200`; `warning_flags` (`LOW_CONFIDENCE \| STALE_MESSAGE \| TF_MISSING \| CLUSTER_SPLIT`) set correctly. | `colcon test --packages-select perception` — all Track B tests pass |

### ObstacleTrack and ObstacleTracks required fields (from `wiki/contracts/message_contracts.md` §ObstacleTrack)

**ObstacleTracks (topic-level):**
```
std_msgs/Header header           # stamp + frame_id = "base_link"
perception_msgs/ObstacleTrack[] tracks
```
`valid_until_ms` and `age_ms` are carried per-track (not at the topic level for `ObstacleTracks`).

**ObstacleTrack (nested element — NO own header):**
```
uint32  track_id                 # Centroid Kalman persistent id
uint8   class_label              # UNKNOWN_OBSTACLE=0 for MVP (no camera fusion yet)
float32 confidence
float32 position_x               # base_link (m)
float32 position_y               # base_link (m)
float32 distance                 # front_bumper-referenced scalar (m)
float32 velocity_x               # base_link (m/s)
float32 velocity_y               # base_link (m/s)
float32 ttc                      # s — perception scalar evidence (planner gates on in_path)
float32 width  / length / height # m
bool    is_static                # |v| < 0.1 m/s → true
string  source_sensor            # "lidar_cluster"
string  semantic_source          # "" or "none" → class_label stays UNKNOWN_OBSTACLE
string  geometry_source          # "lidar"
uint32  age_ms
uint32  valid_until_ms           # must be 200
string[] warning_flags           # LOW_CONFIDENCE | STALE_MESSAGE | TF_MISSING | CLUSTER_SPLIT
```

**Important:** `in_path` is NOT a field in `ObstacleTrack`. Path-membership is computed planner-side against `/planning/active_route_context.planned_trajectory`. Do not add it.

### TTC computation for Sprint 2 MVP

```python
# ego_speed_mps = 0.0 (placeholder until Sprint 3 active_route_context subscriber)
closing_speed = ego_speed_mps - obstacle_v_along_path   # obstacle_v_along_path from Kalman
if closing_speed <= 0:
    ttc = float('inf')  # obstacle moving away or ego stopped
else:
    ttc = distance_from_front_bumper / max(closing_speed, 0.001)
# is_static=True → obstacle_v_along_path = 0 → closing_speed = ego_speed
#               → ttc = distance / ego_speed (FINITE when ego_speed > 0; inf when ego_speed = 0)
```

With `ego_speed_mps = 0.0`, all tracks will publish `ttc = inf` until Sprint 3 wires `active_route_context`. This is correct and safe — the planner must not act on `ttc = inf`.

### Track B acceptance gate

All of the following must be true before Track B is declared complete:

1. `colcon build --packages-select perception` exits 0.
2. `colcon test --packages-select perception` — all Track B tests pass (no failures, no errors).
3. `ros2 topic echo /perception/obstacle_tracks` with fake cloud (above-ground points) shows non-empty `tracks[]`.
4. `ros2 topic echo /perception/obstacle_tracks` with ground-only cloud shows empty `tracks[]`.
5. `ros2 topic hz /perception/obstacle_tracks` shows ≥ 15 Hz sustained.
6. `ros2 topic list | grep -E '^(/cmd_vel|/control|/beemobs)'` → no matches.

---

## Test approach while Gazebo is not ready

Gazebo sim skeleton (V-B4, target: before 2026-06-02) does not block Sprint 2. Both tracks test entirely with fake/synthetic publishers:

| Need | Solution |
|---|---|
| Camera input for lane_node | `fake_image_pub.py` (extended for lane scenarios) — synthetic `bgr8` frames with painted lane lines |
| LiDAR input for lidar_obstacle_node | `fake_pointcloud_pub.py` (new) — synthetic `PointCloud2` clouds with configurable above-ground point clusters |
| Rate verification | `ros2 topic hz <topic>` or consecutive timestamp deltas for large message types |
| Field verification | `ros2 topic echo <topic>` |
| Build verification | `colcon build --packages-select perception` |
| Test verification | `colcon test --packages-select perception && colcon test-result --verbose` |
| Forbidden-topic check | `ros2 topic list \| grep -E '^(/cmd_vel\|/control\|/beemobs)'` → no matches |

Later Gazebo validation (Sprint 3+) will replay these same nodes on Velodyne/ZED2 Gazebo plugin output. The fake publisher approach does not conflict with that; it is the standard pattern already proven in Sprint 1 (`fake_image_pub.py` + `traffic_light_node`).

---

## What Sprint 2 does NOT include

- Do not wire `/planning/active_route_context` subscriber in Sprint 2. Leave `ego_speed_mps = 0.0` and `route_context_valid = false` as placeholders with Sprint 3 TODO comments.
- Do not implement `stop_target_node` real inputs — Sprint 3.
- Do not implement Gazebo sim skeleton — parallel Gazebo track, targeting readiness before Sprint 3.
- Do not create launch files for the full perception stack — Sprint 3+.
- Do not create `fsm_msgs`, `localization_msgs`, `planner`, `controller`, `fsm`, or `localization` packages.
- Do not modify any `.msg` file.
- Do not add UFLD v2, TensorRT FP16, YOLOv8n FP16, or PointPillars — Phase 2.
- Do not compute `in_path` — planner-side only.

---

## Rosbag template (optional, end of Sprint 2)

Once both tracks are publishing, capture a reference bag for regression replay:

```bash
ros2 bag record \
  /perception/lane_model \
  /perception/obstacle_tracks \
  /perception/traffic_light_state \
  /perception/diagnostics \
  /zed2/left/image_raw \
  /velodyne_points \
  -o sprint2_reference
```

This bag is not a Sprint 2 acceptance gate, but it makes Sprint 3 Gazebo validation easier.
