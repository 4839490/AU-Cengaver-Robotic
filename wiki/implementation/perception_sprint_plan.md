# Perception Sprint Plan — 2026-05-12 → 2026-06-23

Sources: `wiki/implementation/milestones.md`, `wiki/perception/perception_overview.md`, `wiki/contracts/message_contracts.md`, `wiki/log.md` (Gate B verification entries).

---

## Sprint 0 — COMPLETE (as of 2026-05-12)

Everything below has been verified on **Ubuntu 20.04 + ROS2 Foxy**. V-B1, V-B2, V-B3 status: **PASSED** (see `wiki/log.md` entries for 2026-05-10 and 2026-05-11).

| Deliverable | Status |
|---|---|
| `common_msgs`, `perception_msgs`, `planning_msgs/ActiveRouteContext` build cleanly (V-B1) | ✅ PASSED |
| `vehicle_params.yaml` present with BEE1 dimensions and sensor extrinsics | ✅ PASSED |
| Static TF: `base_link → camera_frame`, `base_link → lidar_frame`, `base_link → imu_frame` | ✅ PASSED |
| Dummy perception publishers — all seven `/perception/*` topics at contract rates | ✅ PASSED |
| Gate B smoke launch (`gate_b_smoke.launch.py`) — all nodes come up, no ERROR lines (V-B3) | ✅ PASSED |
| Per-node skeletons — one rclpy node per perception responsibility (V-B2) | ✅ PASSED |

---

## Sprint 1 — COMPLETE (2026-05-12, verified on Ubuntu 20.04 + ROS2 Foxy)

**Goal: `traffic_light_node` MVP — replace dummy publisher with real image input pipeline.**

The MVP follows `wiki/perception/traffic_light_node.md` and the MVP order in `wiki/perception/perception_overview.md` §"MVP order" step 6.

### Sprint 1 completion summary

All S1-1 through S1-6 deliverables verified on Ubuntu 20.04 LTS + ROS2 Foxy (Linux 5.15.0-139-generic) on 2026-05-12. No Gazebo required; `fake_image_pub` was used throughout.

| # | Deliverable | Result |
|---|---|---|
| S1-1 | Subscribe to `/zed2/left/image_raw` (sensor_msgs/Image). | ✅ PASSED — `ros2 topic info -v` shows `traffic_light_node` as subscriber. |
| S1-2 | `fake_image_pub.py` — synthetic BGR frames at ≥ 10 Hz. | ✅ PASSED — consecutive timestamp deltas confirm ≈ 10 Hz (bgr8, 640×480). |
| S1-3 | YOLO bbox stub — `model_path` wired; node stays up with model absent. | ✅ PASSED — stub bbox active; `model_path=/dev/null` does not crash node. |
| S1-4 | Pure-Python ROI colour classifier (`colour_classifier.py`). | ✅ PASSED — 16/16 pytest unit tests + RED/GREEN/YELLOW/UNKNOWN runtime checks. |
| S1-5 | 3-frame temporal filter (`temporal_filter.py`). Pre-confirmation publishes observed state with `confirmed=False`. | ✅ PASSED — 28/28 colcon tests; runtime: `confirmed=true` after 3 consistent frames. |
| S1-6 | Real `TrafficLightState` with STALE semantics; `image_stale_ms` clamped to `valid_until_ms=300`. | ✅ PASSED — 42/42 colcon tests; STALE at ~300 ms; clamp WARN logged when > 300. |

A Codex review fix was also applied on 2026-05-12: `image_stale_ms` default changed from 500 → 300 ms; `resolve_stale_ms()` helper extracted to `stale_utils.py` and unit-tested (10 tests). The fix ensures stale evidence never outlives the `valid_until_ms=300` validity window.

**Note:** the MVP uses a pure-Python bbox stub and ROI classifier only. Real YOLOv8n + TensorRT FP16 production inference is NOT part of Sprint 1; it is a Phase 2 item.

### Sprint 1 deliverables (archived test method)

| # | Deliverable | Test method |
|---|---|---|
| S1-1 | Subscribe to `/zed2/left/image_raw` (sensor_msgs/Image). Node log confirms subscription. | `ros2 topic info /zed2/left/image_raw -v` → confirm `traffic_light_node` appears as a subscriber; `ros2 topic echo` may be used only to inspect messages |
| S1-2 | Fake image publisher node (`fake_image_pub.py`) — publishes synthetic BGR frames at 10–30 Hz so the node can be tested without a real camera. | `ros2 topic hz /zed2/left/image_raw` ≥ 10 Hz |
| S1-3 | YOLO bbox stub — model loading path wired from `params/traffic_light_node.yaml`, stub returns no detections if model absent; node does not crash. | Launch with model path set to `/dev/null`; node stays up; `traffic_light_state` still publishes |
| S1-4 | HSV ROI classifier — given a bounding box ROI, classifies dominant hue as `RED`, `YELLOW`, or `GREEN`; falls back to `UNKNOWN` if no box. | Unit test: pass synthetic red/green/yellow image crops, assert expected classification |
| S1-5 | 3-frame temporal filter — `confirmed=True` only after the same non-UNKNOWN classification is seen for ≥ 3 consecutive frames. Before confirmation the current observed state is published as evidence with `confirmed=False` (planner/FSM contract: `confirmed=False → do not act`). See wiki/log.md 2026-05-12 entry for rationale. | Echo topic during early frames (should show classified state + `confirmed=false`), then after 3 consistent frames (`confirmed=true`); assert state transition |
| S1-6 | Publish real `TrafficLightState` — `state`, `confidence`, `confirmed`, `relevant_to_route`, `age_ms`, `valid_until_ms`, `warning_flags` populated from live pipeline, not the dummy constant. | `ros2 topic echo /perception/traffic_light_state` — `state` varies with image input |

**Sprint 1 does NOT require Gazebo.** Testing uses:
- `fake_image_pub.py` for synthetic input.
- `ros2 topic echo` / `ros2 topic hz` for output verification.
- Rosbag replay (if a camera bag is available).

Gazebo sim skeleton is important but is a **parallel track**; it does not block Sprint 1 perception progress. See "Gazebo track" below.

### Sprint 1 out-of-scope

- Lane node, LiDAR obstacle node, stop target node — Sprint 2+.
- Localization, FSM, planner, controller — blocked (see "Blocked work" below).
- UFLD v2, TensorRT FP16, YOLOv8n FP16 production models — Phase 2.

---

## Sprint 2 — IN PROGRESS (2026-05-12 → 2026-06-02)

**Goal: `lane_node` MVP (Track A) + `lidar_obstacle_node` MVP (Track B).**

Track A starts first. Track B begins after Track A reaches a stable publishing state (S2-A3 or later).

See `wiki/implementation/sprint2_perception_kickoff.md` for the full deliverable list, architecture boundaries, test approach, and acceptance gates.

### Track A — lane_node MVP (COMPLETE — synthetic MVP only)

| # | Deliverable | Result |
|---|---|---|
| S2-A1 | Subscribe `/zed2/left/image_raw`; publish empty `LaneModel` skeleton. Node log confirms subscription. | ✅ PASSED — `ros2 topic info -v` shows `lane_node` as subscriber; `NO_INPUT` flag on no-image. |
| S2-A2 | `fake_lane_image_pub.py` — `bgr8` synthetic lane frames (`straight` / `blank`) at ≥ 10 Hz. | ✅ PASSED — consecutive timestamp deltas ≈ 10 Hz; `lane_image_utils.build_lane_frame()` unit-tested. |
| S2-A3 | Column-scoring lane detector — `centerline[]`, `left_boundary[]`, `right_boundary[]` populated; `lane_lost = false` on straight frame. | ✅ PASSED — 67/67 tests; runtime: non-empty arrays, `lane_lost=false` on straight frame. |
| S2-A4 | `lane_contract.py` — all LaneModel fields, warning-flag rules, and point-contract helpers made explicit and testable. `valid_until_ms=500`, `warning_flags` correct in all five states. | ✅ PASSED — 102/102 tests; runtime smoke: straight + blank verified on Ubuntu 20.04 + ROS2 Foxy. |
| S2-A5 | Track A closure: wiki, checklist, sprint plan updated. Final build/test/smoke re-verified. | ✅ COMPLETE — see `wiki/implementation/sprint2_lane_track_a_smoke_checklist.md`. |

### Track A completion summary

All S2-A1 through S2-A5 deliverables verified on **Ubuntu 20.04 + ROS2 Foxy** (Linux 5.15.0-139-generic, 2026-05-12). Track A represents the **synthetic lane MVP** only.

**What IS complete:**
- `fake_lane_image_pub.py` + `lane_node` pipeline — functional end-to-end.
- `bgr8` synthetic lane frame generation (`straight` and `blank` scenarios).
- Column-scoring lane detector — produces `centerline[]`, `left_boundary[]`, `right_boundary[]`.
- Synthetic `base_link` point mapping via `col_to_lateral_m()` (not calibrated IPM).
- All LaneModel contract fields populated: `lane_confidence`, `lane_width_estimate`, `valid_until_ms=500`, `age_ms`, `source_sensor="camera"`, `frame_id="base_link"`, `warning_flags`.
- All five warning-flag states correct and unit-tested.
- 102 tests passing, 0 failures.

**What is NOT complete (Phase 2 / future work):**
- Real UFLD v2 or YOLOP model — Phase 2 only.
- Calibrated camera projection / IPM — requires real camera intrinsics + extrinsics.
- Real curvature estimation — `curvature = 0.0` throughout (`col_to_lateral_m` does not compute curvature).
- Real road / video validation — only synthetic `bgr8` frames tested.
- `/planning/active_route_context` subscriber wiring — Sprint 3 TODO.

**Next:** Track B — `lidar_obstacle_node` MVP (S2-B1..S2-B5). See `wiki/implementation/sprint2_perception_kickoff.md` §"Track B".

**Note:** Production UFLD v2 + TensorRT FP16 is NOT part of Track A. A Hough / polynomial detector is the acceptable MVP path. Gazebo is not required; fake/synthetic image input is sufficient.

### Track B — lidar_obstacle_node MVP

| # | Deliverable | Test method |
|---|---|---|
| S2-B1 | Subscribe `/velodyne_points` (`sensor_msgs/PointCloud2`); publish empty `ObstacleTracks` skeleton. Node log confirms subscription. | ✅ **PASSED** — branch `claude/s2-b1-lidar-obstacle-subscribe`; `ros2 topic info /velodyne_points -v` confirms subscriber; echo shows `frame_id=base_link`, `tracks=[]`; 102 tests pass |
| S2-B2 | Fake PointCloud2 publisher (`fake_pointcloud_pub.py`) — synthetic VLP-16-style clouds at ≥ 10 Hz. Gazebo not required. | ✅ **PASSED** — branch `claude/s2-b2-fake-pointcloud-publisher`; `pointcloud_utils.py` helper (ROS-free); 17 new tests (119 total, 0 failures); `simple_obstacle` (25 pts: width=25, point_step=16, row_step=400, frame_id=lidar_frame) and `empty` (0 pts) verified on Ubuntu 20.04 + ROS2 Foxy; single-instance rate 10.4 Hz ≥ 10 Hz; /velodyne_points pub=1 sub=1; /perception/obstacle_tracks frame_id=base_link tracks=[] |
| S2-B3 | Ground filter + Euclidean clustering — clusters published as `ObstacleTrack[]` entries; `class_label = UNKNOWN_OBSTACLE`, `source_sensor = lidar_cluster`, `geometry_source = lidar`, `distance` = front-bumper-referenced scalar. | ✅ **PASSED** — branch `claude/s2-b3-lidar-clustering-mvp`; `lidar_cluster_utils.py` ROS-free helper (decode / filter / cluster / summary / front_bumper_distance); stale-evidence gating (state != fresh → tracks=[]); 163 tests, 0 failures; verified Ubuntu 20.04 + ROS2 Foxy; simple_obstacle → 1 track (pos_x=5.00, pos_y=0.00, distance=4.59 m); stale-gate verified (publisher stopped → tracks=[]); empty → tracks=[]; no forbidden topics |
| S2-B4 | ✅ **PASSED** — branch `claude/s2-b4-lidar-centroid-tracking`; `centroid_tracker.py` ROS-free helper: nearest-centroid greedy association, persistent `track_id`, `velocity_x/y` from stamp-delta dt, `is_static` threshold 0.1 m/s, tracker reset on stale; stamp deduplication (20 Hz node / 10 Hz publisher); `age_ms` stamped per-publish from wall clock (`~22 ms` fresh, `~72 ms` cached duplicate, all < 200); `moving_obstacle` scenario added to `fake_pointcloud_pub`; 197 tests, 0 failures; verified Ubuntu 20.04 + ROS2 Foxy. | ✅ tracks=1; track_id=1 consistent; vx≈1.0 m/s; is_static=False (moving); age_ms < 200; tracks=0 on stale; no forbidden topics |
| S2-B5 | ✅ **PASSED** — branch `claude/s2-b5-lidar-track-b-closure`; `test_lidar_obstacle_pipeline.py`: 41 contract-field and pipeline integration tests; 238 total tests (colcon test), 0 failures; verified Ubuntu 20.04 + ROS2 Foxy 2026-05-12. Runtime smokes A–E all PASSED. | ✅ 238 tests, 0 failures; simple_obstacle (track_id stable, pos_x=5.000, distance=4.590, all 13 contract fields correct); moving_obstacle (vx≈1.0 m/s, is_static=False); stale→tracks=0; empty→tracks=0; no forbidden topics |

### Track B completion summary (S2-B5 / PASSED)

All S2-B1 through S2-B5 deliverables verified on **Ubuntu 20.04 + ROS2 Foxy** (2026-05-12). Track B is **COMPLETE**.

**What IS complete (synthetic MVP):**
- `/velodyne_points` subscriber + `fake_pointcloud_pub.py` (simple_obstacle / moving_obstacle / empty).
- Pure-Python ground filter (z ≤ 0.2 m) + Euclidean BFS clustering.
- `CentroidTracker`: nearest-centroid greedy association, persistent track_id, velocity_x/y, is_static (|v| < 0.1 m/s), tracker reset on stale.
- All 19 `ObstacleTrack` contract fields populated; `valid_until_ms=200`, `warning_flags=[]`, `geometry_source="lidar"`, `source_sensor="lidar_cluster"`, `semantic_source="none"`, `distance` = front-bumper-referenced scalar.
- Stale-evidence gating (state != fresh → tracks=[]).
- Stamp deduplication (20 Hz node / 10 Hz publisher).
- 238 tests (colcon test), 0 failures (S2-B5 adds 41 contract-field tests).
- Smoke checklist: `wiki/implementation/sprint2_lidar_track_b_smoke_checklist.md`.

**What is NOT complete / Sprint 3+ dependencies:**
- TTC = 0.0 placeholder — Sprint 3 wires `ego_speed_mps` from `/planning/active_route_context`.
- `/planning/active_route_context` NOT subscribed.
- No real VLP-16 hardware or Gazebo Velodyne plugin validation.
- RANSAC, PCL, Centroid Kalman, camera fusion — Phase 2.

**Note:** PointPillars and full camera fusion are NOT part of Track B. Classical RANSAC + Euclidean + Centroid Kalman is the MVP path. Gazebo is not required for Track B either; `fake_pointcloud_pub.py` is sufficient. Gazebo Velodyne plugin is important for Sprint 3+ integration but does not block the Track B MVP.

### Sprint 2 out-of-scope

- `stop_target_node` real inputs — Sprint 3.
- `/planning/active_route_context` subscriber wiring — Sprint 3 (`active_route_context` fields remain placeholder in Sprint 2).
- Localization, FSM, planner, controller — blocked (see "Blocked work" below).
- UFLD v2, TensorRT FP16, YOLOv8n FP16, PointPillars — Phase 2.
- `fsm_msgs`, `localization_msgs`, draft `planning_msgs` schemas — blocked (see "Blocked work" below).

---

## Sprint 3 — ✅ COMPLETE (2026-05-12 → 2026-05-13, verified Ubuntu 20.04 + ROS2 Foxy)

**Goal: Gazebo sim skeleton (Track G) + `stop_target_node` real inputs (Track S) + route context / TTC wiring (Track R).**

See `wiki/implementation/sprint3_perception_integration_kickoff.md` for the full deliverable list, architecture boundaries, TF rules, fake-publisher test approach, and acceptance gates (S3-G1..S3-G3, S3-S1..S3-S3, S3-R1..S3-R4).

**S3-0 kickoff (2026-05-12): wiki-only. No runtime code changed.**

### Track G — Gazebo / simulation skeleton

| Gate | Deliverable | Status |
|---|---|---|
| S3-G1 | `bee1_description` package; `bee1.urdf.xacro` box placeholder with BEE1 dimensions; sensor link placeholders at YAML extrinsics. | ✅ **PASSED** — branch `claude/s3-g1-gazebo-bee1-description`; `colcon build` OK; `xacro` OK; `check_urdf` 0 errors; links: `base_link`, `camera_frame`, `lidar_frame`, `imu_frame`; joints: 3 fixed; forbidden checks: NONE; verified Ubuntu 20.04 + ROS2 Foxy 2026-05-12. |
| S3-G2 | Gazebo 11 world launches; `/velodyne_points`, `/zed2/left/image_raw`, `/imu/data` at ≥ 10 Hz. | ✅ **PASSED** — branch `claude/s3-g2-gazebo-sensor-plugins`; `colcon build` OK; `xacro`/`check_urdf` 0 errors; Gazebo launch OK; `/velodyne_points` **13.8 Hz** `lidar_frame`; `/zed2/left/image_raw` **13.8 Hz** `camera_frame`; `/imu/data` **53.7 Hz** `imu_frame`; forbidden: NONE; `map→odom` and `odom→base_link` ABSENT; base_link→{lidar,camera,imu}_frame PRESENT; verified Ubuntu 20.04 + ROS2 Foxy + Gazebo 11.11.0 2026-05-13. Configured rates: lidar/camera 15 Hz, IMU 60 Hz. Camera requires `DISPLAY` (needs OpenGL rendering context). |
| S3-G3 | Producer-ownership check: `map → odom` and `odom → base_link` not emitted by `static_tf.launch.py` or the Gazebo skeleton launch (those edges are deferred to localization / sim odometry). | ✅ **PASSED** — branch `claude/s3-g3-tf-ownership-closure`; `static_tf.launch.py`: `map→odom` ABSENT, `odom→base_link` ABSENT; `base_link→{camera,lidar,imu}_frame` PRESENT; `gazebo_sensors.launch.py` (ROS_DOMAIN_ID=63): same. Source grep: all `map.*odom`/`odom.*base_link` hits are comments only. Forbidden topics: NONE. No `PlannerMode.msg`, `FSMMode.msg`, or forbidden package dirs. `git diff --check` clean. Verified Ubuntu 20.04 + ROS2 Foxy + Gazebo 11.11.0 2026-05-13. |

TF ownership: `static_tf.launch.py` publishes only `base_link → camera_frame` and `base_link → lidar_frame` (already verified V-B3). `map → odom` and `odom → base_link` are valid required edges in the full system — their producers are localization / sim odometry, not static sensor TF. The Gazebo skeleton must not usurp those edges from the wrong owner.

### Track S — stop_target_node MVP

| Gate | Deliverable | Status |
|---|---|---|
| S3-S1 | `stop_target_node` subscriber skeleton: subscribes to `/perception/traffic_light_state` and `/perception/traffic_signs`; publishes **nothing** when no fresh stop evidence is present (consumers rely on `valid_until_ms=300` expiry of the last real `StopTarget`). | ✅ **PASSED** — branch `claude/s3-s1-stop-target-subscriber-skeleton`; `colcon build` OK; 271 tests (33 new ROS-free in `test_stop_target_policy.py`); smokes A/B/C passed (no StopTarget published, forbidden topics: NONE); verified Ubuntu 20.04 + ROS2 Foxy 2026-05-13. |
| S3-S2 | Priority logic: `fake_traffic_light_state_pub` → RED+confirmed+`relevant_to_route=True` → `target_type=0, priority=3` (CRITICAL). | ✅ **PASSED** (2026-05-13) — `colcon build` OK; 285 tests, 0 failures; smoke A (red+confirmed) PASS; smokes B/C/D (no-publish) PASS; forbidden topics: NONE; geometry placeholder noted. |
| S3-S3 | Forbidden-topic check: no `/cmd_vel`, `/control/*`, `/beemobs/*` published. | ✅ **PASSED** (2026-05-13) — verification + docs only; no code changes. Build OK; 285/285 tests; smokes A–D PASS with ROS_DOMAIN_ID isolation; no forbidden topics; no warning_flags on StopTarget; no empty StopTarget published on no-evidence path. Track S COMPLETE. |

`StopTarget` uses canonical schema (no `warning_flags` — contract §15 raw `.msg` omits it). GeoJSON PICKUP/DROPOFF out of scope for Sprint 3.

### Track R — route context / TTC wiring

| Gate | Deliverable | Status |
|---|---|---|
| S3-R1 | `fake_route_context_pub.py` publishes `ActiveRouteContext` at 10 Hz; `route_context_utils.py` ROS-free helper; fake node imports DEFAULTS + validate_route_context (Codex fix); 300 tests, 0 failures; subscriber smoke PASS; param smoke PASS. | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; branch `claude/s3-r1-fake-route-context-publisher` (based on `origin/main` `9471231`); forbidden topics: NONE. |
| S3-R2 | `lidar_obstacle_node` wires `ego_speed_mps`; `ttc` non-zero when ego moving + obstacle present. | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; branch `claude/s3-r2-lidar-ttc-route-context`; colcon build 0 errors; 316/316 tests; smokes A–F PASS; forbidden topics: NONE. |
| S3-R3 | TTC stale: `ttc=0.0` + `ROUTE_CONTEXT_MISSING` flag when context absent > 500 ms. | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; branch `claude/s3-r3-lidar-route-context-missing-flag`; `add_warning_flag_once` + `remove_warning_flag` (Codex fix: clears stale flag on context recovery from cached tracks); 337/337 colcon tests, 0 failures; smokes A–G PASS (G = in-process recovery test: flag appears when context missing, disappears when context restored, ttc=1.70); forbidden topics: NONE. |
| S3-R4 | `traffic_light_node` wires `relevant_to_route` / `in_stop_zone` / `distance_to_stop` from `active_route_context`; `route_context_apply_utils.py` ROS-free helper; 8 new tests (345 total); `ROUTE_CONTEXT_MISSING` flag behavior. | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy; 345/345 colcon tests, 0 failures; smokes A–F PASS; forbidden topics: NONE. Branch `claude/s3-r4-traffic-light-route-context`. **Track R COMPLETE.** |

Perception must NOT compute `in_path`. TTC is scalar evidence; planner owns path-gating.

---

## Sprint 4 — PLANNED (2026-06-09 → 2026-06-16)

**Goal: Full perception integration in simulation — all nodes on live Gazebo topics.**

All seven `/perception/*` nodes consume Gazebo sensor topics. `perception_diagnostics_node` input_hz and mean_confidence reflect real data. Run T-01..T-05 from `wiki/contracts/test_contract.md`.

---

## Stabilization + Video (2026-06-16 → 2026-06-23)

- 2026-06-16 → 2026-06-21: scenario stabilization, rosbag evidence, warning flag review.
- 2026-06-22 → 2026-06-23: final simulation video ≥ 720p, uninterrupted. Package rosbag + terminal logs + topic plots.
- **2026-06-23: official simulation video upload deadline (teknofest.org).**

---

## Parallel: Gazebo track

Gazebo sim skeleton (Step 3 / V-B4) proceeds in parallel with Sprint 1 perception work. It is important for Sprint 3+ integration and the simulation video, but it does not block:

- `traffic_light_node` MVP (Sprint 1) — uses `fake_image_pub.py`.
- `lane_node` and `lidar_obstacle_node` MVPs (Sprint 2) — use fake publishers and rosbag replay.

Gazebo target: stand up before 2026-06-02 so Sprint 3 has real sensor input available.

---

## Blocked work

**Full system-spine integration remains blocked** until the following owners confirm their message schemas in `wiki/contracts/message_contracts.md` § "Pending decisions":

| Schema group | Blocked by | Impact |
|---|---|---|
| `fsm_msgs` (`CurrentMode`, `MissionState`, `FSMEvent`) | FSM owner sign-off | FSM node (Step 6) cannot start |
| `localization_msgs` | Localization owner sign-off | Localization nodes (Step 5) cannot start |
| `planning_msgs` remainder (`Trajectory`, `TargetSpeed`, `PlanningStatus`, `ControllerFeedback`, `FSMRequest`) | Planner owner sign-off | Planner core (Step 8), controller (Step 9) cannot start |

Perception MVP work in Sprints 1–2 does **not** depend on these schemas. Sprint 3 `stop_target_node` route-context wiring depends on `ActiveRouteContext` only, which is already canonical raw.

---

## Evidence-only mandate

Perception nodes publish evidence. They do not drive.

- Publish: detections, confidence, `valid_until_ms`, `warning_flags`, `relevant_to_route`.
- Do NOT publish: stop commands, speed commands, steering commands, or mode changes.
- Planner and FSM consume perception evidence and decide.

This rule applies in every sprint, including stubs and MVPs. See `CLAUDE.md` § "Core Architecture Rules" and `wiki/perception/perception_overview.md` § "Mandate".
