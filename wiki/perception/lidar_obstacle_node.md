# lidar_obstacle_node (+ fusion_node)

Sources: `Perception_Planner_FSM_v1.4` §10; roadmap §6.5; team notes (`raw/team_notes/meeting_decisions.md`).

## Topic

```
/perception/obstacle_tracks    perception_msgs/ObstacleTracks
Hz: 20 | valid_until_ms: 200 | frame_id: base_link
Producers : lidar_obstacle_node + fusion_node
Consumers : planner_node, fsm_node
```

## Implementation status

| Step | Status | Description |
|---|---|---|
| S2-B1 | **COMPLETE** (branch `claude/s2-b1-lidar-obstacle-subscribe`) | `/velodyne_points` subscriber wired; publishes empty `ObstacleTracks` at 20 Hz; three input states tracked internally (no_input / fresh / stale) for logging only |
| S2-B2 | **COMPLETE** (branch `claude/s2-b2-fake-pointcloud-publisher`) | `fake_pointcloud_pub.py` + `pointcloud_utils.py` — synthetic VLP-16-style PointCloud2 at 10.4 Hz (clean single instance); `simple_obstacle` (25 pts, width=25, point_step=16, row_step=400, frame_id=lidar_frame) and `empty` (0 pts); 17 tests (119 total), 0 failures; verified Ubuntu 20.04 + ROS2 Foxy |
| S2-B3 | **COMPLETE** (branch `claude/s2-b3-lidar-clustering-mvp`) — verified Ubuntu 20.04 + ROS2 Foxy | Pure-Python ground filter (z ≤ 0.2 m) + Euclidean BFS clustering; `lidar_cluster_utils.py` ROS-free helper (decode / filter / cluster / `front_bumper_distance`); `lidar_obstacle_node.py` decodes little-endian float32 x/y/z PointCloud2 with row_step/height iteration, validates field layout (offset bounds, data length, row sanity), filters ground, clusters, publishes one `ObstacleTrack` per cluster; stale-evidence gating (state != fresh → tracks=[]); `geometry_source="lidar"`, distance = `max(pos_x − 0.410, 0.0)` (BEE1 front_bumper_offset_m); 163 tests, 0 failures; `simple_obstacle` → 1 track (pos_x=5.00, pos_y=0.00, distance=4.59 m); stale-gate verified (publisher stopped → tracks=[]); empty → tracks=[] |
| S2-B4 | **COMPLETE** (branch `claude/s2-b4-lidar-centroid-tracking`) — verified Ubuntu 20.04 + ROS2 Foxy | `centroid_tracker.py` ROS-free helper: nearest-centroid greedy association, `max_association_distance_m=1.0`, `max_missed_frames=3`; persistent `track_id` (monotonically increasing, no reset); `velocity_x/y` from centroid delta / dt; dt from `header.stamp` delta (falls back to 0.0 on first msg); stamp deduplication prevents double-processing when node ticks faster than publisher; `age_ms` stamped per-publish from wall clock (fresh tick ≈ 22 ms, cached duplicate ≈ 72 ms, always < valid_until_ms=200); `is_static = True` when `|v| < 0.1 m/s`; tracker reset on stale; `moving_obstacle` scenario in `fake_pointcloud_pub` (1.0 m/s); 197 tests, 0 failures; `simple_obstacle` → tracks=1, track_id=1 persistent, vx=0.0, is_static=True; `moving_obstacle` → track_id=1 persistent, vx≈1.0 m/s, is_static=False; stale → tracks=[]; forbidden topics: none |
| S2-B5 | **COMPLETE** (branch `claude/s2-b5-lidar-track-b-closure`) — verified Ubuntu 20.04 + ROS2 Foxy 2026-05-12 | Contract-field audit: all 19 `ObstacleTrack` fields confirmed populated; `test_lidar_obstacle_pipeline.py` (41 tests): `valid_until_ms=200`, `warning_flags=[]`, `geometry_source="lidar"`, `source_sensor="lidar_cluster"`, `semantic_source="none"`, `distance` uses front_bumper (not Euclidean), `ttc=0.0` placeholder, bounding-box clipping, `is_static` propagation, `_extract_field_offsets` rejection paths, full decode→filter→cluster→track→build pipeline; moving_obstacle `vx>0`, `is_static=False`; stationary `vx≈0`, `is_static=True`; empty→tracks=[]; tracker-reset→tracks=[]; 238 total tests (colcon test), 0 failures. Runtime smokes PASSED: simple_obstacle (track_id=1 stable, pos_x=5.000, distance=4.590, vx=0.000, is_static=True, age_ms<200, valid_until_ms=200, warning_flags=[], geometry_source='lidar', source_sensor='lidar_cluster', semantic_source='none'); moving_obstacle (vx≈0.999–1.001 m/s, is_static=False, pos_x advancing); stale gating (tracks=0 within 510 ms of publisher stop); empty→tracks=0; forbidden topics none. TTC remains 0.0 placeholder — Sprint 3 active_route_context. |
| S3-R2 | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; branch `claude/s3-r2-lidar-ttc-route-context` | Subscribe `/planning/active_route_context`; `ttc_utils.py` ROS-free helper (`is_route_context_fresh`, `compute_ttc`); per-tick TTC: `closing_speed = ego_speed_mps − velocity_x`; `ttc = distance / closing_speed` when context usable AND `closing_speed > 0.1` AND `distance > 0`; else `ttc = 0.0`. Context usable: `route_context_valid=True` AND `valid_until_ms > 0` AND `age_ms <= valid_until_ms` AND wall-clock delta `<= valid_until_ms`. No `ROUTE_CONTEXT_MISSING` flag (S3-R3). colcon build 0 errors; 316/316 tests, 0 failures. Smokes A–F PASS; forbidden topics: NONE. |
| S3-R3 | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; branch `claude/s3-r3-lidar-route-context-missing-flag` | `add_warning_flag_once` + `remove_warning_flag` in `ttc_utils.py`. `_tick()`: context NOT usable → `ttc=0.0` + add flag once; context usable → `remove_warning_flag` (Codex fix: clears stale flag from cached tracks) + `compute_ttc`. No tracks → no iteration. 21 new tests (S3-R3 initial 14 + Codex fix 7): `TestAddWarningFlagOnce` (5), `TestRemoveWarningFlag` (4), `TestWarningFlagBehavior` (12, incl. 3 recovery scenarios); 337/337 colcon tests pass. Smokes A–G all PASS: A (no context → flag present, ttc=0), B (valid context → ttc≈1.70, no flag), C (stopped ego → ttc=0, no flag), D (stale context → flag present), E (ego=0 with valid context → ttc=0, no flag), F (obstacle moving toward ego → ttc computed), G (recovery: flag appears on missing context, disappears on valid context restore, ttc=1.70 in-process pub); forbidden topics: NONE. |

**S2-B5 contract audit summary (S2-B1..B4 + B5 combined):**

| ObstacleTrack field | Implemented? | Value / source |
|---|---|---|
| `track_id` | ✅ | CentroidTracker persistent ID (monotonically increasing, never reset) |
| `class_label` | ✅ | `UNKNOWN_OBSTACLE = 0` (no camera fusion yet) |
| `confidence` | ✅ | 0.8 (MVP constant; real classifier = Phase 2) |
| `position_x` | ✅ | cluster centroid x in base_link |
| `position_y` | ✅ | cluster centroid y in base_link |
| `distance` | ✅ | `max(pos_x − 0.410, 0.0)` — front-bumper-referenced (BEE1) |
| `velocity_x` | ✅ | centroid delta / stamp-delta dt (m/s); 0.0 on first frame |
| `velocity_y` | ✅ | same |
| `ttc` | ✅ | `compute_ttc(distance, ego_speed_mps, velocity_x)` from `ttc_utils.py`; 0.0 when context missing/stale/invalid (S3-R2). S3-R3 adds `ROUTE_CONTEXT_MISSING` flag. |
| `width` | ✅ | cluster y-extent, clipped to ≥ 0.01 m |
| `length` | ✅ | cluster x-extent, clipped to ≥ 0.01 m |
| `height` | ✅ | cluster z-extent, clipped to ≥ 0.01 m |
| `is_static` | ✅ | `True` when `|v| < 0.1 m/s` |
| `source_sensor` | ✅ | `"lidar_cluster"` |
| `semantic_source` | ✅ | `"none"` (UNKNOWN_OBSTACLE; camera fusion = Phase 2) |
| `geometry_source` | ✅ | `"lidar"` |
| `age_ms` | ✅ | wall-clock delta from last received PointCloud2 (fresh ≈ 22 ms, cached ≈ 72 ms) |
| `valid_until_ms` | ✅ | 200 (contract-canonical) |
| `warning_flags` | ✅ | `[]` when context usable; `['ROUTE_CONTEXT_MISSING']` when context missing/stale/invalid (S3-R3). Other dynamic flags (LOW_CONFIDENCE, STALE_MESSAGE, TF_MISSING, CLUSTER_SPLIT) are Phase 2. |

**S3-R3 warning flag status (Codex fix applied):** `ROUTE_CONTEXT_MISSING` added to each `ObstacleTrack.warning_flags` when route context is absent, stale, invalid, or zero-validity; removed by `remove_warning_flag` when context becomes usable again (critical for cached-track reuse: prevents stale flag persisting after recovery). Usable context + ego stopped → `ttc=0.0` but NO flag.

**Phase-2 / future work (NOT in Sprint 2):** RANSAC ground removal, PCL Euclidean clustering, Centroid Kalman filter, camera fusion, dynamic `warning_flags`, real VLP-16 hardware, Gazebo Velodyne plugin, PointPillars.

**S2-B1 contract note:** `ObstacleTracks` has only `header` + `tracks[]` at the wrapper level — no `age_ms`, `valid_until_ms`, or `warning_flags` fields on the wrapper. Per-track fields (`age_ms`, `valid_until_ms`, `warning_flags`) live inside `ObstacleTrack` elements, which are added in S2-B3/B4.

## Algorithm (S3-R3 current implementation)

Pure-Python synthetic MVP verified against `fake_pointcloud_pub` + `fake_route_context_pub`. No real VLP-16 hardware, no RANSAC, no PCL, no IMU undistortion.

1. **Subscribe `/velodyne_points`** (`sensor_msgs/PointCloud2`) — validate `x/y/z` fields are all `FLOAT32` (datatype=7) via `_extract_field_offsets`; reject malformed layouts (returns `None` → tracks=[]).
2. **Subscribe `/planning/active_route_context`** (`planning_msgs/ActiveRouteContext`) — store latest message + wall-clock receive time. (S3-R2)
3. **Decode** little-endian `float32` `x/y/z` from each point using `row_step`/`height` iteration.
4. **Ground filter** — discard points with `z ≤ 0.2 m`.
5. **Euclidean BFS clustering** — pure-Python connected-component clustering on non-ground points; cluster distance threshold 0.5 m.
6. **Cluster summary** → centroid `(x, y)`, bounding-box extents `(width, length, height)` clipped to ≥ 0.01 m.
7. **`CentroidTracker`** — greedy nearest-centroid association (`max_association_distance_m=1.0`, `max_missed_frames=3`); persistent monotonically-increasing `track_id`; `velocity_x/y` from centroid delta / stamp-delta `dt` (0.0 on first frame); tracker reset on stale input.
8. **`is_static`** = `|v| < 0.1 m/s`.
9. **Build `ObstacleTrack`** per cluster: `class_label=UNKNOWN_OBSTACLE`, `confidence=0.8`, `source_sensor='lidar_cluster'`, `geometry_source='lidar'`, `semantic_source='none'`; `distance = max(position_x − 0.410, 0.0)` (BEE1 front-bumper offset); `ttc=0.0` (overwritten in step 10); `valid_until_ms=200`; `warning_flags=[]`.
10. **TTC computation** (S3-R2) — re-evaluated every publish tick:
    - Check `_is_context_usable()`: `route_context_valid=True` AND `age_ms ≤ valid_until_ms` AND wall-clock delta since callback `≤ valid_until_ms`.
    - If usable: `remove_warning_flag(t.warning_flags, 'ROUTE_CONTEXT_MISSING')` (Codex fix: clears stale flag from cached tracks); then `closing_speed = ego_speed_mps − velocity_x`; `ttc = distance / closing_speed` when `closing_speed > 0.1` AND `distance > 0`; else `ttc = 0.0`.
    - If not usable: `ttc = 0.0` and `add_warning_flag_once(t.warning_flags, 'ROUTE_CONTEXT_MISSING')` (S3-R3).
11. **Stale-evidence gating** — if last received PointCloud2 age > `valid_until_ms` (200 ms): publish `tracks=[]`, reset tracker.
12. **Stamp deduplication** — when the 20 Hz node tick arrives before the 10 Hz publisher sends a new cloud, the previous result is reused (no reprocessing); `age_ms` is re-stamped from wall clock on every publish.

## Phase-2 / future target algorithm (NOT in Sprint 2)

The items below are architectural targets for Phase 2 or later sprints. They are **not implemented** in the current codebase.

- `lidar_undistortion.py` — Xsens IMU-based motion compensation for VLP-16 point cloud.
- RANSAC ground plane removal (replacing the z-threshold filter).
- PCL Euclidean clustering (replacing the pure-Python BFS implementation).
- Centroid Kalman tracker (constant-velocity model, ~50 ms prediction step) replacing the greedy nearest-centroid tracker.
- `fusion_node` — adds camera semantic class (`VEHICLE / PEDESTRIAN / CONE / BARRIER / SIGN_POLE`); until fusion is wired, `class_label=UNKNOWN_OBSTACLE` and `semantic_source='none'`.
- PointPillars — Phase-2 / research item per team decisions; not the MVP path.
- Real VLP-16 hardware and Gazebo Velodyne plugin validation — Sprint 3+ integration targets.

## TTC (FIX-2.1) — perception side, scalar-only (S3-R3 implemented)

Perception publishes a scalar closing-speed TTC as **evidence**. It does NOT know `in_path` and does NOT project onto the planned trajectory. The planner gates the final action.

```
ego_speed     = /planning/active_route_context.ego_speed_mps   # subscribed (S3-R2)
closing_speed = ego_speed - track.velocity_x                   # MVP: straight-line proxy

# ttc_utils.compute_ttc(distance_m, ego_speed_mps, obstacle_velocity_x):
if closing_speed > 0.1 and distance > 0:
    ttc = distance / closing_speed
else:
    ttc = 0.0   # ego stopped, obstacle moving away/same, or zero distance

# Freshness gate (ttc_utils.is_route_context_fresh):
# context usable only when route_context_valid=True
#   AND valid_until_ms > 0  (zero/negative validity window → always unusable)
#   AND age_ms <= valid_until_ms
#   AND wall-clock-delta-since-callback <= valid_until_ms
# If context not usable → ttc = 0.0 + ROUTE_CONTEXT_MISSING flag (S3-R3)

# Examples:
# ego=2.7, static obs (vx=0), dist=4.59 → ttc = 4.59/2.7 ≈ 1.70 s
# ego=2.7, obs vx=1.0, dist=4.59        → ttc = 4.59/1.7 ≈ 2.70 s
# ego=0.0 (stopped)                      → ttc = 0.0
# obstacle moving faster than ego        → ttc = 0.0
```

**Path-gating is planner-side.** Even with a small `ttc`, planner consumes it only after determining `in_path=true` against `/planning/active_route_context.planned_trajectory` and the planner's own `/planning/trajectory`. If `in_path=false`, the planner ignores or downgrades this `ttc` regardless of value. The planner may also recompute a path-projected TTC when straight-line distance is a poor proxy (curved segments, lateral offset).

See [Message Contracts § TTC ownership and computation](../contracts/message_contracts.md) and [Active Route Context](../architecture/active_route_context.md).

## Planner / FSM behavior table

| Condition | Action |
|---|---|
| `in_path=false` | log only — low risk |
| `in_path=true + ttc > 3 s` | watch / prepare |
| `in_path=true + 2 < ttc ≤ 3 s` | reduce speed, prepare to evade |
| `in_path=true + 1 < ttc ≤ 2 s` | STOP_APPROACH or evade |
| `in_path=true + ttc ≤ 1 s` | full brake → controller |
| Safety supervisor: full brake insufficient | `AUTONOMOUS_EMERGENCY` (NOT triggered by planner) |
| `is_static=true + in_path=true` example: ego=2.7 m/s, dist=5.4 → ttc≈2 s | STOP_APPROACH |
| `is_static=true + 10 s timeout` | FSM `replanning_request` |
| `class_label=PEDESTRIAN` | TTC thresholds ×2 |
| `class_label=CONE` | bypass-eligible — low cost |
| `valid_until_ms` exceeded | behave as if obstacle still present |

## Warning flags

`LOW_CONFIDENCE | STALE_MESSAGE | TF_MISSING | CLUSTER_SPLIT`

## Cross-links

- Schema: [Message Contracts § ObstacleTrack](../contracts/message_contracts.md)
- TTC source: [Active Route Context](../architecture/active_route_context.md)
- Tests T-08 / T-09 / T-10 in [Test Contract](../contracts/test_contract.md)
