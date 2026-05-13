# Sprint 3 — Perception Integration Kickoff (2026-05-12)

Sources used: `wiki/implementation/perception_sprint_plan.md`, `wiki/perception/stop_target_node.md`, `wiki/perception/lidar_obstacle_node.md`, `wiki/perception/traffic_light_node.md`, `wiki/architecture/active_route_context.md`, `wiki/contracts/message_contracts.md`, `wiki/architecture/tf_standard.md`, `wiki/vehicle/bee1_platform.md`.

Branch: `claude/s3-0-perception-integration-kickoff`
Status: **IN PROGRESS — docs/wiki kickoff only. No runtime code changed.**
Date: 2026-05-12

---

## Context: Sprint 2 is complete

Both Sprint 2 tracks are verified and merged as of 2026-05-12 on Ubuntu 20.04 + ROS2 Foxy:

- **Track A** (`lane_node` synthetic MVP) — 102 tests, PASSED (S2-A5).
- **Track B** (`lidar_obstacle_node` synthetic MVP) — 238 tests, PASSED (S2-B5).

Known Sprint 3 dependencies carried over from Sprint 2:

| Item | Origin | Sprint 3 target |
|---|---|---|
| `ttc = 0.0` placeholder in `ObstacleTrack` | S2-B5 | Track R — wire `ego_speed_mps` from `active_route_context` |
| `/planning/active_route_context` NOT subscribed anywhere | S2-A5, S2-B5 | Track R |
| `relevant_to_route = False` hardcoded in `traffic_light_node` | S1-6 | Track R / Track S |
| `stop_target_node` accepts only dummy inputs | Sprint 0 | Track S |
| No Gazebo sim skeleton | Sprint 0..2 | Track G |

---

## Sprint 3 scope

Sprint 3 delivers **three parallel tracks**. Each track is independent enough to be branched and implemented separately, but all share the same acceptance rule: **no planner/controller/FSM/localization code; no forbidden topics.**

---

## Track G — Gazebo / simulation skeleton

**Goal:** Stand up a Gazebo 11 simulation skeleton for Ubuntu 20.04 + ROS2 Foxy that publishes the sensor topics the perception stack expects, using the BEE1 URDF/xacro as a placeholder vehicle model.

Gazebo is integration support. It does **not** replace or block the synthetic-MVP approach used in Sprints 1–2. The existing `fake_image_pub.py`, `fake_lane_image_pub.py`, and `fake_pointcloud_pub.py` remain the primary test paths for node-level verification.

### Sensor topic targets

| Topic | Message type | Required Hz | Gazebo plugin |
|---|---|---|---|
| `/velodyne_points` | `sensor_msgs/PointCloud2` | ≥ 10 Hz | `libgazebo_ros_velodyne_laser` (or equivalent GPU ray plugin) |
| `/zed2/left/image_raw` | `sensor_msgs/Image` | ≥ 10 Hz | `libgazebo_ros_camera` (bgr8 / rgb8) |
| `/imu/data` | `sensor_msgs/Imu` | ≥ 50 Hz | `libgazebo_ros_imu_sensor` |

### TF rules — ownership per the TF Standard

The full project TF standard requires all four edges (see `wiki/architecture/tf_standard.md`):

```
map → odom → base_link → camera_frame
                       └→ lidar_frame
```

Track G is responsible only for the **static sensor edges**. The dynamic edges are deferred:

| Edge | Owner | Track G status |
|---|---|---|
| `map → odom` | `global_localization_node` (Localization) | **Deferred** — not produced by `static_tf.launch.py` or the Gazebo skeleton launch. Will be provided once localization / sim odometry is implemented. |
| `odom → base_link` | `local_ekf_node` (Localization) | **Deferred** — not produced by `static_tf.launch.py` or the Gazebo skeleton launch. Will be provided once localization / sim odometry is implemented. |
| `base_link → camera_frame` | `static_tf.launch.py` (Bringup/Perception) | ✅ Already published and verified V-B3 (2026-05-11). |
| `base_link → lidar_frame` | `static_tf.launch.py` (Bringup/Perception) | ✅ Already published and verified V-B3 (2026-05-11). |
| `base_link → imu_frame` | `static_tf.launch.py` (non-core) | Published as sensor-support edge. |
| Gazebo internal URDF joint TFs | Gazebo robot_description spawner | Internal (e.g. `base_link → lidar_link`); must not shadow the contract sensor edges. |

> The S3-G3 acceptance check confirms that `static_tf.launch.py` and the Gazebo skeleton launch do **not** incorrectly emit `map → odom` or `odom → base_link` from the wrong owner (static sensor TF must not usurp the localization stack's responsibility). This is a **producer-ownership check**, not a global prohibition on those frames. Once localization / sim odometry nodes are running, `map → odom` and `odom → base_link` will correctly appear from their proper owners.

### BEE1 URDF/xacro placeholder strategy

No final BEE1 CAD/URDF has been provided by the vehicle team. The placeholder approach:

1. Create a minimal `bee1_description` package with a single `bee1.urdf.xacro` that describes the chassis as a box primitive with the documented BEE1 dimensions (2740 × 1060 × 1785 mm).
2. Attach sensor plugins at the extrinsic offsets from `vehicle_params.yaml` (matching `static_tf.launch.py`):
   - VLP-16: x=-0.177 m, y=0.000 m, z=0.620 m from base_link.
   - ZED2: x=-0.205 m, y=0.000 m, z=0.685 m from base_link.
   - Xsens IMU: x=1.440 m, y=0.000 m, z=1.390 m from base_link.
3. When real BEE1 URDF is delivered, replace the box model — sensor plugin attachment points stay the same.
4. World file: `simple_test.world` — flat plane, daylight, no obstacles. Enough to emit sensor data at the required Hz.

### Acceptance gates

| Gate | Description | Verification command |
|---|---|---|
| **S3-G1** | `bee1_description` package created; `bee1.urdf.xacro` parses without errors. | `xacro bee1.urdf.xacro` produces valid XML; `check_urdf` returns 0 errors. |
| **S3-G2** | Gazebo world launches with BEE1 model; `/velodyne_points`, `/zed2/left/image_raw`, `/imu/data` visible. | `ros2 topic list` shows the three sensor topics; `ros2 topic hz /velodyne_points` ≥ 10 Hz. |
| **S3-G3** | Producer-ownership check: `map → odom` and `odom → base_link` are NOT published by `static_tf.launch.py` or the Gazebo skeleton launch (correct — those edges belong to localization / sim odometry, not static sensor TF). | ✅ **PASSED** (2026-05-13) — `static_tf.launch.py`: `map→odom` ABSENT, `odom→base_link` ABSENT; `base_link→{camera,lidar,imu}_frame` PRESENT. `gazebo_sensors.launch.py` (ROS_DOMAIN_ID=63): same result. Source grep: all `map.*odom`/`odom.*base_link` matches are comments only — no publisher/node definitions. Forbidden topics: NONE. No `PlannerMode.msg`, `FSMMode.msg`, or forbidden package dirs found. `git diff --check` clean. |

Forbidden during Track G:
- No planner, controller, FSM, or localization nodes.
- `static_tf.launch.py` must not emit `map → odom` or `odom → base_link` — those are localization-owned edges.
- No `PlannerMode.msg`, `FSMMode.msg`, or any draft-pending message.

---

## Track S — stop_target_node MVP

**Goal:** Replace the dummy `stop_target_node` publisher with a real subscriber skeleton that aggregates existing perception evidence and publishes `StopTarget` evidence only.

### Architecture mandate

`stop_target_node` is an **aggregator, not a decision maker.** It must never:

- Publish `/cmd_vel`, `/control/*`, `/beemobs/*`, or mode changes.
- Set `planner_mode` or modify autonomy mode.
- Compute `in_path` (planner-side).
- Decide whether the vehicle should stop.

It must:

- Subscribe to upstream perception topics.
- Weight and merge evidence according to priority rules.
- Publish a single `StopTarget` with `target_type`, `priority`, `confidence`, `distance_from_front_bumper`, `valid_until_ms`, `source_topic`, and `source` when fresh stop evidence exists.
- When no fresh upstream stop evidence exists: **do not publish a new `StopTarget`.** Consumers rely on the `valid_until_ms=300` expiry of the last published message to discard stale stop evidence. Publishing a message with `target_type=0` (default) on no-evidence would look identical to a real `TRAFFIC_LIGHT_STOP` and must be avoided.

### Inputs

| Topic | Message type | Role |
|---|---|---|
| `/perception/traffic_light_state` | `perception_msgs/TrafficLightState` | Primary light evidence: `state=RED/YELLOW + confirmed=true` → `TRAFFIC_LIGHT_STOP` |
| `/perception/traffic_signs` | `perception_msgs/TrafficSigns` | Sign evidence: `type=STOP + event_status=NEW|TRACKED` → `STOP_SIGN` |
| `/planning/active_route_context` | `planning_msgs/ActiveRouteContext` | Optional: stop-zone gating, `relevant_to_route` cross-check, `in_stop_zone` context. If absent or stale (>500 ms), skip route relevance checks; still publish evidence conservatively. |

GeoJSON PICKUP/DROPOFF waypoints (`target_type = PICKUP | DROPOFF`) are Sprint 3+ or Phase 2 — depend on mission state data that is not yet available. For now, `stop_target_node` only produces `TRAFFIC_LIGHT_STOP` and `STOP_SIGN` targets.

### Output

```
/perception/stop_target    perception_msgs/StopTarget
Hz: 10–20 | valid_until_ms: 300 | frame_id: base_link
```

`StopTarget` canonical fields (no `warning_flags` — contract §15 raw `.msg` does not include this field):

```
target_type                  # TRAFFIC_LIGHT_STOP=0 | STOP_SIGN=1
distance_from_front_bumper   # from upstream ObstacleTrack or TrafficSign.distance
target_x / target_y          # base_link (m); 0.0 when only upstream evidence available
confidence                   # from upstream source; clamp to [0.0, 1.0]
source                       # "perception_only" for S3; "map_plus_perception" when GeoJSON wired
age_ms                       # wall-clock delta from last fresh upstream message
valid_until_ms               # 300 (contract)
waypoint_id                  # -1 (PICKUP/DROPOFF not in S3)
heading_at_stop              # 0.0 placeholder (geometry not computed in S3)
priority                     # see priority rules below
required_stop_duration_ms    # 0 → FSM decides
stop_reason_id               # debug id
source_topic                 # "/perception/traffic_light_state" or "/perception/traffic_signs"
```

### Priority rules

| Condition | target_type | priority |
|---|---|---|
| `RED + confirmed=true + relevant_to_route=true` | `TRAFFIC_LIGHT_STOP` | `CRITICAL=3` |
| `RED + confirmed=true + relevant_to_route=false` | `TRAFFIC_LIGHT_STOP` | `HIGH=2` |
| `YELLOW + confirmed=true` | `TRAFFIC_LIGHT_STOP` | `NORMAL=1` |
| `STOP_SIGN + event_status=NEW/TRACKED` | `STOP_SIGN` | `HIGH=2` |
| Two targets simultaneously | highest priority wins; `source_topic` set to winner |
| No fresh upstream evidence | **Do not publish.** Let `valid_until_ms=300` expiry handle staleness on the consumer side. Publishing with default `target_type=0` would be indistinguishable from a real `TRAFFIC_LIGHT_STOP`. |

### Stale / missing upstream behavior

If `/perception/traffic_light_state` age > 300 ms or `state=STALE/UNKNOWN`: treat as no light evidence for the current cycle.
If `/perception/traffic_signs` is stale or `signs=[]`: treat as no sign evidence.
If `/planning/active_route_context` is absent > 500 ms or `route_context_valid=false`: use `relevant_to_route=false`; still publish light/sign evidence conservatively.

### Forbidden topics

`stop_target_node` must never publish to:
- `/cmd_vel`
- `/control/*`
- `/beemobs/*`
- Any planning, FSM, or localization topic

### Acceptance gates

| Gate | Description | Verification command |
|---|---|---|
| **S3-S1** | ✅ **PASSED** (2026-05-13) — `stop_target_node` subscriber skeleton: subscribes to `/perception/traffic_light_state` and `/perception/traffic_signs`; publishes nothing when no fresh stop evidence is present. `stop_target_policy.py` (ROS-free): `is_fresh()`, `evaluate_light_stop_evidence()`, `has_stop_sign_evidence()` (checks type + event_status + confirmed + age_ms/valid_until_ms per sign), `StopEvidence`; 33 new tests (271 total, 0 failures); smokes A/B/C passed; forbidden topics: NONE. | `ros2 topic info /perception/traffic_light_state -v` shows `stop_target_node` as subscriber; rclpy probe confirms no StopTarget published when upstream evidence is absent or stale. |
| **S3-S2** | ✅ **PASSED** (2026-05-13) — `fake_traffic_light_state_pub` → RED+confirmed+`relevant_to_route=True` → StopTarget `target_type=0 priority=3 confidence=0.850 valid_until_ms=300 source=perception_only frame_id=base_link waypoint_id=-1`; no-publish smokes B/C/D PASS; forbidden topics: NONE; 285 tests (12 new), 0 failures. Geometry placeholder: `distance_from_front_bumper=0.0` until S3-R4 wires route-context geometry. | `ros2 run perception fake_traffic_light_state_pub --ros-args -p state:=red -p confirmed:=true -p confidence:=0.85`; rclpy probe on `/perception/stop_target` → `priority=3`. |
| **S3-S3** | ✅ **PASSED** (2026-05-13) — Forbidden-topic check: no `/cmd_vel`, `/control/*`, `/beemobs/*` published. Also confirmed: (a) no code path publishes empty/zero-filled StopTarget on no-evidence; (b) no `warning_flags` field used on StopTarget anywhere; (c) smokes A–D all PASS with ROS_DOMAIN_ID isolation on Ubuntu 20.04 + ROS2 Foxy. Track S COMPLETE. | `ros2 topic list` (domain 94): /perception/stop_target, /perception/traffic_light_state, /perception/traffic_signs, /parameter_events, /rosout only — no forbidden topics. |

---

## Track R — route context / TTC wiring

**Goal:** Wire `/planning/active_route_context` into the nodes that need it in Sprint 3, according to the contract. All wiring is **evidence-only** — no driving decisions.

### Nodes that need active_route_context

#### lidar_obstacle_node — TTC from ego_speed_mps

Currently `ttc = 0.0` (S2-B5 placeholder). Sprint 3 closes this:

```python
# Perception-side TTC formula (FIX-2.1, contract §6):
ego_speed              = active_route_context.ego_speed_mps
obstacle_v_along_path  = velocity_x  # MVP: forward-axis projection = velocity_x (base_link x = forward)
closing_speed          = ego_speed - obstacle_v_along_path
distance_along_path    = distance_from_front_bumper  # scalar proxy per contract §6

if closing_speed > 0.001:
    ttc = distance_along_path / closing_speed
else:
    ttc = float('inf')  # obstacle moving away or ego stopped

# is_static=True → velocity_x ≈ 0 → closing_speed = ego_speed → ttc = distance / ego_speed
```

**Perception does NOT compute `in_path`.** TTC is scalar evidence. Planner gates on `in_path` from the planned trajectory. Even a small `ttc` is ignored by the planner if `in_path=false`.

Missing / stale `active_route_context` behavior:
- If topic absent > `valid_until_ms` (500 ms) or `route_context_valid=false`: `ttc` remains `0.0` and `ROUTE_CONTEXT_MISSING` warning flag is added to the affected `ObstacleTrack`.
- `age_ms > 500` (exceeds `ActiveRouteContext.valid_until_ms`): same — treat as missing context, safe placeholder.

#### traffic_light_node — relevant_to_route and in_stop_zone

Currently hardcoded `relevant_to_route=False`, `in_stop_zone=False` (Sprint 1 placeholder). Sprint 3 wires:

```python
# ActiveRouteContext.valid_until_ms = 500; use same threshold for route context freshness
if active_route_context and active_route_context.route_context_valid and age_ms <= 500:
    msg.relevant_to_route = True   # set by planner, mirrored
    msg.in_stop_zone      = active_route_context.in_stop_zone
    msg.distance_to_stop  = active_route_context.distance_to_stop_zone
else:
    msg.relevant_to_route = False  # conservative
    msg.in_stop_zone      = False
    msg.distance_to_stop  = 0.0
    # Add ROUTE_CONTEXT_MISSING to warning_flags
```

GREEN gate (FIX-2.2) remains: `state=GREEN + relevant_to_route=true + confirmed=true` only. Conservative by default.

#### stop_target_node — route relevance / stop-zone context

See Track S above. `stop_target_node` uses `active_route_context.in_stop_zone` and `route_context_valid` to set `relevant_to_route` on `StopTarget` and to adjust priority (CRITICAL vs HIGH for RED light).

### Fake publisher for integration testing

A `fake_route_context_pub.py` test helper is needed to exercise Track R without a real planner:

```python
# Publishes planning_msgs/ActiveRouteContext at 10 Hz with configurable ego_speed_mps
# Scenarios:
#   --ego-speed 2.7   → ego moving at 2.7 m/s
#   --ego-speed 0.0   → ego stopped
#   --stale           → publishes with age_ms=600 (forces stale behavior)
#   --invalid         → publishes route_context_valid=False
```

### Acceptance gates

| Gate | Description | Verification command |
|---|---|---|
| **S3-R1** | ✅ **PASSED** (2026-05-13) — `fake_route_context_pub` publishes `ActiveRouteContext` at 10 Hz; `route_context_utils.py` ROS-free helper (DEFAULTS, build, validate); fake node imports `DEFAULTS`/`validate_route_context` (Codex fix); 300 tests, 0 failures; default smoke: `frame_id=base_link`, `ego_speed_mps=0.0`, `route_context_valid=True`, `age_ms=0`, `valid_until_ms=500`; param smoke: `ego_speed_mps=2.70`, `route_context_valid=False`, `age_ms=600`, `in_stop_zone=True`, `distance_to_stop_zone=4.20`; forbidden topics: NONE; `planning_msgs` added to `package.xml exec_depend`. Branch `claude/s3-r1-fake-route-context-publisher` based on current `origin/main` (`9471231`). | `ros2 topic hz /planning/active_route_context` ≥ 8 Hz; `ros2 topic echo` shows `ego_speed_mps`, `route_context_valid`. |
| **S3-R2** | ✅ **PASSED** (2026-05-13) — `lidar_obstacle_node` subscribes to `/planning/active_route_context`; `ttc_utils.py` (`is_route_context_fresh` with `valid_until_ms > 0` guard, `compute_ttc`); per-tick TTC; `ttc=0.0` when context invalid/stale/absent/zero-validity; colcon build 0 errors; 316/316 tests, 0 failures; smoke A: dist=4.590, vx=0.000, ttc=1.7000; smoke B: vx≈1.0 m/s, ttc=dist/1.7 ✓; smokes C–F: ttc=0.0 ✓; forbidden topics: NONE. Branch `claude/s3-r2-lidar-ttc-route-context` based on `origin/main` `f0f0d1c`. | `ros2 run perception lidar_obstacle_node` + `fake_route_context_pub ego_speed_mps:=2.7` + `fake_pointcloud_pub scenario:=simple_obstacle`; echo `/perception/obstacle_tracks` → `ttc≈1.70 s`. |
| **S3-R3** | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy. `add_warning_flag_once` + `remove_warning_flag` in `ttc_utils.py`; `_tick()` adds flag on missing context, removes on recovery; Codex fix: `remove_warning_flag` prevents stale flag persisting across cached-track reuse; 337/337 colcon tests; Smokes A–G PASS. Smoke G = in-process single rclpy publisher: phase-1 (no ctx) all 8 samples `flags=['ROUTE_CONTEXT_MISSING']`; phase-2 (ego=2.7 ctx published) all 10 samples `ttc=1.7000` `flags=[]`; forbidden topics: NONE. Branch `claude/s3-r3-lidar-route-context-missing-flag`. | Kill `fake_route_context_pub.py`; wait 600 ms; echo `/perception/obstacle_tracks` → `ttc=0.0`, `warning_flags` includes `ROUTE_CONTEXT_MISSING`. Then restart `fake_route_context_pub` → flag absent, TTC positive. |
| **S3-R4** | ✅ **PASSED** (2026-05-13) — Ubuntu 20.04 + ROS2 Foxy. `traffic_light_node` subscribes to `/planning/active_route_context`; `route_context_apply_utils.apply_route_context_to_light()` ROS-free helper; wires `relevant_to_route`, `in_stop_zone`, `distance_to_stop`; `ROUTE_CONTEXT_MISSING` flag added on missing/stale/invalid/zero-validity context, removed on recovery; 8 new tests, 345/345 colcon tests, 0 failures; smokes A–F PASS; forbidden topics: NONE. Branch `claude/s3-r4-traffic-light-route-context`. **Track R COMPLETE.** | Smoke A: `fake_image_pub color:=red` + `fake_route_context_pub route_context_valid:=true age_ms:=0 valid_until_ms:=500 in_stop_zone:=true distance_to_stop_zone:=4.2` → `state=RED relevant_to_route=true in_stop_zone=true distance_to_stop=4.20 flags=[]`. Smoke F (recovery, in-process): 16 phase-1 samples `flags=['ROUTE_CONTEXT_MISSING']`; 46 phase-2 samples `relevant=true in_zone=true dist=4.20 flags=[]`. |

### What Track R must NOT do

- Perception must not subscribe to `/controller/feedback` directly. `ego_speed_mps` comes only from `active_route_context`.
- Perception must not compute `in_path`. No trajectory projection.
- Perception must not publish mode changes.

---

## Blocked in Sprint 3

The following are explicitly out of scope for Sprint 3:

| Item | Reason |
|---|---|
| `fsm_msgs`, `localization_msgs` | Owner sign-off pending. See `wiki/contracts/message_contracts.md` § "Pending decisions". |
| Draft `planning_msgs` (`Trajectory`, `TargetSpeed`, etc.) | Same — owner sign-off pending. |
| Planner / controller / FSM implementation | Blocked by above. |
| Real YOLOv8n + TensorRT FP16 | Phase 2. |
| Real UFLD v2 / YOLOP | Phase 2. |
| PCL / RANSAC / PointPillars | Phase 2. |
| Centroid Kalman filter | Phase 2 (current: greedy centroid tracker). |
| Camera fusion (`fusion_node`) | Phase 2. |
| `PlannerMode.msg` / `FSMMode.msg` | Must never be created. |
| Stanley / Pure Pursuit in planner | Controller-side only; not in perception or planner for Sprint 3. |
| GeoJSON PICKUP/DROPOFF targets in `stop_target_node` | Requires `MissionState` / `FSMEvent` schemas — blocked. |
| Dynamic `warning_flags` in `ObstacleTrack` — specifically `LOW_CONFIDENCE`, `CLUSTER_SPLIT`, `TF_MISSING` | Phase 2 enhancement. **`ROUTE_CONTEXT_MISSING` is in Sprint 3 scope** (Track R, S3-R3): added to `ObstacleTrack.warning_flags` when `active_route_context` is absent or stale, to signal that `ttc=0.0` is a safe placeholder rather than a real zero-TTC. |

---

## Sprint 3 acceptance summary

S3-0 (this page) is **wiki-only**. No `colcon` required for this step.

| Gate | Track | Status | Runtime required? |
|---|---|---|---|
| S3-0 | (wiki) | IN PROGRESS (docs only) | No |
| S3-G1 | G | ✅ PASSED (2026-05-12) | `xacro` / `check_urdf` only |
| S3-G2 | G | ✅ PASSED (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy + Gazebo 11 |
| S3-G3 | G | ✅ PASSED (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy + Gazebo 11 |
| S3-S1 | S | ✅ **PASSED** (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy |
| S3-S2 | S | ✅ PASSED (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy |
| S3-S3 | S | ✅ **PASSED** (2026-05-13) — verification + docs only; no code changes. Build OK; 285/285 tests; smokes A–D PASS; no forbidden topics; no warning_flags on StopTarget; no empty StopTarget on no-evidence path. Track S COMPLETE. | Ubuntu 20.04 + ROS2 Foxy |
| S3-R1 | R | ✅ PASSED (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy |
| S3-R2 | R | ✅ PASSED (2026-05-13) | Ubuntu 20.04 + ROS2 Foxy |
| S3-R3 | R | ✅ **PASSED** (2026-05-13) — 337/337 tests; smokes A–G PASS; forbidden: NONE | Ubuntu 20.04 + ROS2 Foxy |
| S3-R4 | R | ✅ **PASSED** (2026-05-13) — 345/345 colcon tests; smokes A–F PASS; forbidden: NONE. **Track R COMPLETE. Sprint 3 COMPLETE.** | Ubuntu 20.04 + ROS2 Foxy |

All future gates require:
- Ubuntu 20.04 + ROS2 Foxy build passing.
- No forbidden topics (`/cmd_vel`, `/control/*`, `/beemobs/*`).
- No forbidden message types (`PlannerMode.msg`, `FSMMode.msg`).
- Static review is provisional only — does not satisfy any runtime gate.

---

## Cross-links

- [Perception Sprint Plan](perception_sprint_plan.md) — overall Sprint 3 entry
- [stop_target_node](../perception/stop_target_node.md) — Track S architecture
- [lidar_obstacle_node](../perception/lidar_obstacle_node.md) — Track R TTC wiring
- [traffic_light_node](../perception/traffic_light_node.md) — Track R route-context wiring
- [Active Route Context](../architecture/active_route_context.md) — source of `ego_speed_mps`, `in_stop_zone`, `route_context_valid`
- [Message Contracts](../contracts/message_contracts.md) — StopTarget canonical schema (no `warning_flags`)
- [TF Standard](../architecture/tf_standard.md) — Track G TF rules
- [BEE1 Platform](../vehicle/bee1_platform.md) — URDF placeholder dimensions and sensor extrinsics
