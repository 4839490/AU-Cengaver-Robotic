# Message Contracts (`.msg` files)

Sources (verified against raw PDFs):
- `raw/final_contracts/Perception_Planner_FSM_v1.4_FINAL_DUZELTILMIS.pdf`
  - §1 "Temel Prensip ve Ortak Kurallar" (mandatory header rule, FIX-2.6, FIX-3, warning flag set) — pp. 1–2
  - §4 "Planner → Perception: /planning/active_route_context" — p. 2 (field table) and p. 3 (raw .msg block)
  - §7 "/perception/lane_model" — p. 4 (table + sample)
  - §8 "/perception/traffic_light_state" — pp. 4–5 (table + behavior table + sample)
  - §9 "/perception/traffic_signs" — p. 5 (table + sample)
  - §10 "/perception/obstacle_tracks" — pp. 6–7 (table + behavior table + sample)
  - §11 "/perception/stop_target" — p. 7 (table + sample)
  - §12 "/perception/junction" — p. 7 (table)
  - §13 "/perception/diagnostics" — p. 8 (table + sample)
  - §15 "Custom .msg Dosyaları — perception_msgs Package" — pp. 9–11 (canonical .msg blocks)
- `raw/final_contracts/AU_Cengaver_GANG_Yol_Haritasi_DUZELTILMIS.pdf` (v1.1 revize)
  - §5 "ROS2 Çalışma Alanı & Dosya Yapısı" — pp. 3–4 (msg package roster + per-file content notes)

This page is the canonical implementable schema. Field types here are ROS2 Foxy `.msg` syntax. Do not invent fields that are not in the contract; do not silently drop fields that are.

## Mandatory-fields rule (resolves prior contradiction)

The contract §1 line *"Tüm topic'lerde zorunlu: header.stamp, header.frame_id, confidence, valid_until_ms"* applies to **topic-level (top-level published) messages**, not to nested element types that travel inside arrays.

| Concept | Rule |
|---|---|
| Topic-level message | MUST have `std_msgs/Header header`. MUST have `uint32 valid_until_ms`. SHOULD have `uint32 age_ms`. SHOULD have `string[] warning_flags`. SHOULD have `float32 confidence` if the message represents a detection / state estimate (not for diagnostics or pure-command messages). |
| Nested element message (e.g. `TrafficSign`, `ObstacleTrack`, `TrajectoryPoint`) | NO own `header` (use parent's `header.stamp` / `frame_id`). MAY include its own `confidence`, `age_ms`, `valid_until_ms`, `warning_flags`, `event_memory_ttl_ms` when the contract specifies them per-element (perception elements do). Geometry-only elements (e.g. `TrajectoryPoint`) carry only geometry. |
| Command / target / mode messages from planner / FSM (`ControllerFeedback`, `TargetSpeed`, `FSMRequest`, `MapOrigin`, `MissionState`, `FSMEvent`) | MUST have `std_msgs/Header header`. `confidence` not required (these are not detections). `valid_until_ms` required where the contract names it (planner-side topics — see roadmap §5.1). |

`PlannerMode.msg` and `FSMMode.msg` MUST NOT be created. The only autonomy mode enum is `common_msgs/AutonomyMode` (FIX-3, contract §1 + roadmap §11). `JUNCTION`, `TUNNEL`, and `ROUNDABOUT` MUST NOT be added as autonomy modes; they live in `TargetSpeed.reason` and `ActiveRouteContext.route_direction` only.

## Status labels (read this before implementing)

Every `.msg` block below is tagged with one of:

- **canonical raw** — field names, types, and enum values come directly from `Perception_Planner_FSM_v1.4_FINAL_DUZELTILMIS.pdf` (contract §4 / §15) or `AU_Cengaver_GANG_Yol_Haritasi_DUZELTILMIS.pdf` §5.1 raw `.msg` blocks. Implementable for Milestone 1 as written.
- **team-approved extension** — additions on top of a canonical raw block that the team has explicitly approved (recorded in `wiki/log.md`). Implementable.
- **draft pending owner confirmation** — the raw documents name the message but do not enumerate every type / constant. Field types and enum values are project-decided and need owner sign-off (planner, FSM, or localization owner) before being generated. **Do NOT generate these for Milestone 1.**

The Milestone 1 readiness rules are defined at the bottom of this page.

---

## `common_msgs/`

### `common_msgs/msg/AutonomyMode.msg` — **status: canonical raw**

Source: roadmap §5.1 p. 3 (`uint8 LANE_FOLLOW=0 … uint8 MISSION_COMPLETE=7`).

```
# common_msgs/msg/AutonomyMode.msg
# Single autonomy mode enum for the whole stack — constants only.
# DO NOT add JUNCTION, TUNNEL, ROUNDABOUT here — those are TargetSpeed.reason / route_direction.

uint8 LANE_FOLLOW=0
uint8 STOP_APPROACH=1
uint8 PICKUP_APPROACH=2
uint8 DROPOFF_APPROACH=3
uint8 OBSTACLE_AVOID=4
uint8 PARK_APPROACH=5
uint8 PARK_MANEUVER=6
uint8 MISSION_COMPLETE=7
```

> Constants-only `.msg` files are valid in ROS2 (and in ROS2 Foxy specifically) — `rosidl` does **not** require at least one non-constant field. The earlier claim that a carrier field was required was incorrect and has been removed.
>
> The mode value travels embedded in other messages' `uint8 planner_mode` / `uint8 mode` fields (see `ActiveRouteContext`, `Trajectory`, `CurrentMode`, `FSMRequest`). Adding a carrier field here would give `AutonomyMode` two reasons to exist; until the team explicitly approves one, this stays constants-only.

---

## `perception_msgs/`

All topic-level perception messages live in this package. Source for raw .msg blocks: contract §15 pp. 9–11.

### `perception_msgs/msg/LaneModel.msg` — **status: canonical raw**

Source: contract §7 p. 4 (table) + §15 p. 9 (raw .msg).

```
# perception_msgs/msg/LaneModel.msg
# Topic: /perception/lane_model | 20–30 Hz | frame_id: base_link | valid_until_ms: 500

std_msgs/Header header
geometry_msgs/Point[] centerline       # base_link, ≥5 m forward, spacing ≤ 0.1 m
geometry_msgs/Point[] left_boundary    # base_link
geometry_msgs/Point[] right_boundary   # base_link
float32 lane_confidence                # 0.0–1.0
bool    lane_lost
float32 curvature                      # 1/m (lookahead-style: straight ≈ 2.5 m, sharp turn ≈ 0.8 m)
float32 lane_width_estimate            # m
uint32  age_ms
uint32  valid_until_ms                 # contract: 500
string  source_sensor                  # "camera"
string[] warning_flags                 # subset of standard set: LOW_CONFIDENCE | STALE_MESSAGE | LANE_BOUNDARY_MISSING
```

### `perception_msgs/msg/TrafficLightState.msg` — **status: canonical raw**

Source: contract §8 pp. 4–5 + §15 p. 9.

```
# perception_msgs/msg/TrafficLightState.msg
# Topic: /perception/traffic_light_state | 10–30 Hz | frame_id: base_link | valid_until_ms: 300

uint8 UNKNOWN=0
uint8 RED=1
uint8 YELLOW=2
uint8 GREEN=3
uint8 STALE=4
uint8 CONFLICT=5

std_msgs/Header header
uint8   state
float32 confidence                     # < 0.7 → publish UNKNOWN
bool    relevant_to_route
float32 distance_to_stop               # front_bumper-referenced scalar (m)
bool    confirmed                      # true after 3 consecutive frames
bool    in_stop_zone                   # mirrors active_route_context.in_stop_zone — critical for STALE behavior
float32 bbox_x                         # px (debug)
float32 bbox_y                         # px (debug)
float32 bbox_w                         # px (debug)
float32 bbox_h                         # px (debug)
uint32  age_ms
uint32  valid_until_ms                 # contract: 300
string  source_sensor                  # "camera"
string[] warning_flags                 # LOW_CONFIDENCE | STALE_MESSAGE | CONFLICT_STATE | SYNC_MISMATCH
```

### `perception_msgs/msg/TrafficSign.msg` — nested element of `TrafficSigns.signs[]` — **status: canonical raw**

Source: contract §9 p. 5 + §15 p. 10.

```
# perception_msgs/msg/TrafficSign.msg
# Nested element of /perception/traffic_signs. NO own header; uses parent header.

uint8 UNKNOWN_SIGN=0
uint8 STOP=1
uint8 SPEED_LIMIT=2
uint8 NO_ENTRY=3
uint8 MANDATORY_LEFT=4
uint8 MANDATORY_RIGHT=5
uint8 MANDATORY_STRAIGHT=6
uint8 MANDATORY_LEFT_STRAIGHT=7
uint8 MANDATORY_RIGHT_STRAIGHT=8
uint8 ROUNDABOUT=9
uint8 PARKING=10
uint8 NO_PARKING=11
uint8 TUNNEL=12
uint8 PEDESTRIAN_CROSSING=13

uint8 NEW=0
uint8 TRACKED=1
uint8 ALREADY_HANDLED=2
uint8 STALE=3

uint32  sign_id                        # event-memory persistent id
uint8   type                           # one of the type constants above
float32 confidence                     # 0.0–1.0
bool    relevant_to_route              # planner-derived from /planning/active_route_context
float32 distance                       # front_bumper-referenced scalar (m)
uint8   event_status                   # NEW | TRACKED | ALREADY_HANDLED | STALE
bool    confirmed                      # true after 3 consecutive frames
float32 bbox_x                         # px (debug)
float32 bbox_y                         # px (debug)
float32 bbox_w                         # px (debug)
float32 bbox_h                         # px (debug)
uint32  age_ms
uint32  valid_until_ms                 # contract: 1000
uint32  event_memory_ttl_ms            # contract: default 5000
string  source_sensor                  # "camera"
string[] warning_flags                 # LOW_CONFIDENCE | STALE_MESSAGE | BBOX_MISSING
```

> Contract §9 prose enum table (p. 5) lists a partial set (skips 2/7/8/10/13). Contract §15 raw `.msg` (p. 10) carries the full set. The full set is canonical.

### `perception_msgs/msg/TrafficSigns.msg` — topic-level — **status: canonical raw**

Source: contract §15 p. 10.

```
# perception_msgs/msg/TrafficSigns.msg
# Topic: /perception/traffic_signs | 10–30 Hz | frame_id: base_link | valid_until_ms: 1000

std_msgs/Header header
perception_msgs/TrafficSign[] signs
```

### `perception_msgs/msg/ObstacleTrack.msg` — nested element of `ObstacleTracks.tracks[]` — **status: canonical raw**

Source: contract §10 pp. 6–7 + §15 pp. 10–11.

```
# perception_msgs/msg/ObstacleTrack.msg
# Nested element of /perception/obstacle_tracks. NO own header; uses parent header.
# IMPORTANT: NO `in_path` field. Path-membership is computed planner-side using
#            /planning/active_route_context.planned_trajectory.

uint8 UNKNOWN_OBSTACLE=0
uint8 VEHICLE=1
uint8 PEDESTRIAN=2
uint8 CONE=3
uint8 BARRIER=4
uint8 SIGN_POLE=5

uint32  track_id                       # Centroid Kalman persistent id
uint8   class_label                    # one of the class constants above
float32 confidence                     # 0.0–1.0
float32 position_x                     # base_link (m), obstacle center x
float32 position_y                     # base_link (m), obstacle center y
float32 distance                       # front_bumper-referenced scalar (m)
float32 velocity_x                     # base_link (m/s), Centroid Kalman estimate
float32 velocity_y                     # base_link (m/s), Centroid Kalman estimate
float32 ttc                            # s — see §"TTC ownership and computation" below
float32 width                          # m
float32 length                         # m
float32 height                         # m
bool    is_static                      # |v| < 0.1 m/s → true
string  source_sensor                  # "lidar_cluster" | "camera_fusion" | "lidar_only"
string  semantic_source                # "" or "none" → class_label kept as UNKNOWN_OBSTACLE
string  geometry_source                # "lidar" | "fusion" | ""
uint32  age_ms
uint32  valid_until_ms                 # contract: 200
string[] warning_flags                 # LOW_CONFIDENCE | STALE_MESSAGE | TF_MISSING | CLUSTER_SPLIT
```

### `perception_msgs/msg/ObstacleTracks.msg` — topic-level — **status: canonical raw**

```
# perception_msgs/msg/ObstacleTracks.msg
# Topic: /perception/obstacle_tracks | 20 Hz | frame_id: base_link | valid_until_ms: 200

std_msgs/Header header
perception_msgs/ObstacleTrack[] tracks
```

#### TTC ownership and computation (resolves prior ambiguity)

Contract: §1 (FIX-2.1) p. 1, §6 p. 3 ("Hız Bağımlı Fren Mesafesi"), §10 p. 6 (`ObstacleTrack.ttc` definition).

- **Perception** (`lidar_obstacle_node` / `fusion_node`) computes the per-track `ttc` as evidence using the FIX-2.1 closing-speed formula:
  ```
  ego_speed              = active_route_context.ego_speed_mps         # subscribed by perception
  obstacle_v_along_path  = projection of (velocity_x, velocity_y) onto the ego forward axis
  closing_speed          = ego_speed - obstacle_v_along_path
  distance_along_path    = distance_from_front_bumper                  # MVP: scalar proxy (contract §6)
  ttc                    = distance_along_path / max(closing_speed, 0.001)
  # is_static=true is treated as obstacle_v_along_path = 0, so closing_speed = ego_speed
  # → ttc = distance / ego_speed (FINITE, NOT inf)
  # closing_speed ≤ 0  → ttc = inf  (obstacle moving away or stationary while ego is stopped)
  ```
- **Perception does NOT compute `in_path`.** It does not own the planned trajectory.
- **Planner** (`planner_node` / `obstacle_avoidance.py` per roadmap §6.3 p. 5) owns:
  - `in_path` boolean, computed against `/planning/active_route_context.planned_trajectory` (and the planner's own current `/planning/trajectory` in `map` frame).
  - `bypass_possible`, `collision_risk`.
  - Final action gating. If `in_path=false`, the planner ignores or downgrades perception's `ttc` regardless of its numeric value.
  - The planner MAY recompute a path-projected TTC using `planned_trajectory` if straight-line `distance_from_front_bumper` is a poor proxy on that segment. That recomputation is planner-internal; perception keeps publishing the scalar form.
- **MVP simplification (contract §6 p. 3)**: `distance_along_path = distance_from_front_bumper`. The planner accepts this as the perception-side TTC for planning, and refines only when its own path geometry shows a meaningful difference (curved segments, lateral offset).

### `perception_msgs/msg/StopTarget.msg` — topic-level — **status: canonical raw**

Source: contract §11 p. 7 + §15 p. 11. Field set matches the raw `.msg` block exactly — no `warning_flags` field, since the raw contract omits it.

```
# perception_msgs/msg/StopTarget.msg
# Topic: /perception/stop_target | 10–20 Hz | frame_id: base_link | valid_until_ms: 300

uint8 TRAFFIC_LIGHT_STOP=0
uint8 STOP_SIGN=1
uint8 PICKUP=2
uint8 DROPOFF=3

uint8 LOW=0
uint8 NORMAL=1
uint8 HIGH=2
uint8 CRITICAL=3

std_msgs/Header header
uint8   target_type                    # one of TRAFFIC_LIGHT_STOP..DROPOFF
float32 distance_from_front_bumper     # m (front_bumper-referenced scalar)
float32 target_x                       # base_link (m)
float32 target_y                       # base_link (m)
float32 confidence                     # 0.0–1.0
string  source                         # "map_plus_perception" | "perception_only"
uint32  age_ms
uint32  valid_until_ms                 # contract: 300
int32   waypoint_id                    # PICKUP/DROPOFF GeoJSON node id (-1 if N/A)
float32 heading_at_stop                # rad — ±10° tolerance
uint8   priority                       # one of LOW..CRITICAL
uint32  required_stop_duration_ms      # 0 → wait for FSM signal (e.g. PICKUP_COMPLETE)
uint32  stop_reason_id                 # debug id, used to correlate with FSM stop_reason
string  source_topic                   # e.g. "/perception/traffic_light_state"
```

> **Pending team extension (NOT in the implementable block above).** A `string[] warning_flags` field would line up with the topic-level header rule and the standard warning flag set used elsewhere. The earlier draft of this page included it, but contract §15 raw `.msg` for `StopTarget` does not list it, so it has been removed from the canonical block. If the team decides to add `warning_flags`, propose it through the normal contract change procedure (topic name / field type → MAJOR; field addition → MINOR), get explicit approval, and update both this page and the contract document. Do not generate the field for Milestone 1.

### `perception_msgs/msg/Junction.msg` — topic-level (OPTIONAL, Phase-2) — **status: canonical raw**

Source: contract §12 p. 7 + §15 p. 11.

```
# perception_msgs/msg/Junction.msg
# Topic: /perception/junction | 10 Hz | frame_id: base_link | valid_until_ms: 500
# OPTIONAL in MVP — when not published, planner uses active_route_context.route_direction.

uint8 NORMAL=0
uint8 ROUNDABOUT=1

std_msgs/Header header
bool    detected                       # true → visual junction perceived ahead
uint8   junction_type                  # NORMAL | ROUNDABOUT
uint8   arm_count                      # number of intersection arms
float32 distance_to_entry              # front_bumper-referenced scalar (m)
float32 confidence                     # 0.0–1.0
uint32  age_ms
uint32  valid_until_ms                 # contract: 500
string  source_sensor                  # "camera"
string[] warning_flags                 # LOW_CONFIDENCE | STALE_MESSAGE
```

### `perception_msgs/msg/PerceptionDiagnostics.msg` — topic-level — **status: canonical raw**

Source: contract §13 p. 8 + §15 p. 11.

```
# perception_msgs/msg/PerceptionDiagnostics.msg
# Topic: /perception/diagnostics | 1–2 Hz | frame_id: "" (no spatial frame)
# Each perception node publishes its own row under this single topic.

std_msgs/Header header
string  node_name                      # "traffic_light_node" | "lane_node" | "lidar_obstacle_node" |
                                       # "traffic_sign_node" | "stop_target_node" | "junction_node" | "fusion_node"
float32 input_hz
float32 output_hz
float32 latency_ms
uint32  last_msg_age_ms                # plays the role of age_ms for diagnostics
float32 mean_confidence
uint32  num_outputs
float32 gpu_utilization                # 0.0–1.0 (RTX 3060)
string[] warning_flags                 # standard set: NO_INPUT | LOW_OUTPUT_HZ | HIGH_LATENCY | LOW_CONFIDENCE |
                                       # STALE_MESSAGE | TF_MISSING | SYNC_MISMATCH | MODEL_ERROR | CONFLICT_STATE | CLUSTER_SPLIT
```

> The contract `.msg` for diagnostics does not include `valid_until_ms` (the §14 timing table assigns 2000 ms as a fallback heuristic, not a field). Per the topic-level rule, this is acceptable: diagnostics is a heartbeat with `last_msg_age_ms` already encoding freshness.

---

## `planning_msgs/`

Source: roadmap §5 pp. 3–4 (package roster), §5.1 pp. 3–4 (per-file content notes), and contract §4 pp. 2–3 (ActiveRouteContext canonical block).

### `planning_msgs/msg/ActiveRouteContext.msg` — **status: canonical raw**

Canonical raw block: contract §4 p. 3.

```
# planning_msgs/msg/ActiveRouteContext.msg
# Topic: /planning/active_route_context | 10 Hz | frame_id: base_link | valid_until_ms: 500
# All coordinates in base_link.

std_msgs/Header header
uint32  active_waypoint_id
float32 target_x                       # base_link (m)
float32 target_y                       # base_link (m)
float32 target_heading                 # rad
uint8   planner_mode                   # common_msgs/AutonomyMode constant — NEVER a string (FIX-3)
string  route_direction                # "STRAIGHT" | "LEFT" | "RIGHT" | "ROUNDABOUT" | "UNKNOWN"
geometry_msgs/Point[] planned_trajectory  # base_link — used by planner-side in_path calc and shared with perception
float32 lookahead_distance             # m
bool    in_stop_zone                   # vehicle currently inside an active stop zone
float32 distance_to_stop_zone          # m
float32 localization_confidence        # EKF confidence 0.0–1.0
float32 ego_speed_mps                  # source: /controller/feedback.actual_speed → planner — TTC source
bool    route_context_valid            # localization OK + waypoint active + planner ACTIVE → true
                                       # false → perception relevant_to_route=false + ROUTE_CONTEXT_MISSING flag
uint32  age_ms                         # >200 → relevant_to_route=false
uint32  valid_until_ms                 # contract: 500
```

### `planning_msgs/msg/TrajectoryPoint.msg` — nested element — **status: draft pending owner confirmation**

The roadmap §5.1 names `points[]: (x, y, yaw, speed, curvature)` but does not specify a separate nested `.msg`. Splitting into `TrajectoryPoint.msg` is a project-side structuring choice for ROS2 `.msg` syntax — confirm with planner owner before generating.

```
# planning_msgs/msg/TrajectoryPoint.msg
# Nested element of Trajectory.points[]. NO own header.

float32 x                              # map frame (m)
float32 y                              # map frame (m)
float32 yaw                            # rad
float32 speed                          # m/s — planner's recommended speed at this point
float32 curvature                      # 1/m
```

### `planning_msgs/msg/Trajectory.msg` — **status: draft pending owner confirmation**

Source: roadmap §5.1 p. 4 ("points[] (x,y,yaw,speed,curvature), planner_mode, valid_until_ms — frame: map"). Field names are from the raw doc; depends on `TrajectoryPoint.msg` (also draft). Confirm with planner owner.

```
# planning_msgs/msg/Trajectory.msg
# Topic: /planning/trajectory | 20 Hz | frame_id: map | valid_until_ms: ~500

std_msgs/Header header
planning_msgs/TrajectoryPoint[] points
uint8  planner_mode                    # common_msgs/AutonomyMode constant
uint32 valid_until_ms
```

### `planning_msgs/msg/TargetSpeed.msg` — **status: draft pending owner confirmation**

Source: roadmap §5.1 p. 4. The raw doc names the field `reason` and the range `LANE_FOLLOW=0 … EMERGENCY_STOP=8` but **does not enumerate** values 1..7. A draft proposal is captured under [Pending decisions](#pending-decisions). The implementable `.msg` has only the two values that come directly from the raw range:

```
# planning_msgs/msg/TargetSpeed.msg
# Topic: /planning/target_speed | 20 Hz | frame_id: "" | valid_until_ms: ~500
# DRAFT — DO NOT GENERATE FOR MILESTONE 1 UNTIL PLANNER OWNER CONFIRMS THE 1..7 reason CONSTANTS.

uint8 LANE_FOLLOW=0
uint8 EMERGENCY_STOP=8

std_msgs/Header header
float32 speed                          # m/s
float32 jerk_limit                     # m/s^3
uint8   reason                         # one of the constants above (1..7 pending)
uint32  valid_until_ms
```

### `planning_msgs/msg/PlanningStatus.msg` — **status: draft pending owner confirmation**

Source: roadmap §5 p. 3 names this in the package roster only — no field list, no enum values. Implementable `.msg` is therefore not yet defined. Draft proposal under [Pending decisions](#pending-decisions). **DO NOT GENERATE FOR MILESTONE 1.**

### `planning_msgs/msg/ControllerFeedback.msg` — **status: draft pending owner confirmation**

Source: roadmap §5.1 p. 4 (`actual_speed, actual_steering_deg, cross_track_error, heading_error, full_brake_active`). Field names come from the raw doc but ROS2 types and units below are project-decided; confirm with controller owner.

```
# planning_msgs/msg/ControllerFeedback.msg
# Topic: /controller/feedback | 20 Hz | frame_id: base_link
# DRAFT — confirm field types / units with controller owner before generating.

std_msgs/Header header
float32 actual_speed                   # m/s — fed from /beemobs/FB_VehicleSpeed.FB_ReelVehicleSpeed_Ms
float32 actual_steering_deg            # deg
float32 cross_track_error              # m
float32 heading_error                  # rad
bool    full_brake_active
```

### `planning_msgs/msg/FSMRequest.msg` — **status: draft pending owner confirmation**

Source: roadmap §5.1 p. 3. Raw range `MODE_CHANGE=0 … PARK_READY=5`; values 1..4 are not enumerated in the raw doc. Draft proposal under [Pending decisions](#pending-decisions). **DO NOT GENERATE FOR MILESTONE 1.**

---

## `fsm_msgs/`

Source: roadmap §5.1 pp. 3–4. Field names appear in the raw doc, but several enum value sets are not enumerated 1..N. All three messages are therefore **draft pending owner confirmation** until the FSM owner sign-off — draft proposals live under [Pending decisions](#pending-decisions). **DO NOT GENERATE THESE FOR MILESTONE 1.**

### `fsm_msgs/msg/CurrentMode.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 3 (`mode, previous_mode, stop_reason (NONE/RED_LIGHT/STOP_SIGN/OBSTACLE_TTC/LOK_LOST/STALE_SENSOR/MISSION_ABORT/PEDESTRIAN), waypoint_id, valid_until_ms, warning_flags[]`). The raw doc lists `stop_reason` symbolic names but does not assign integer values; that mapping is project-decided. Draft proposal under [Pending decisions](#pending-decisions).

### `fsm_msgs/msg/MissionState.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 3 (`mission_active, total_waypoints, completed_waypoints, current_waypoint_id/type, next_waypoint_id/type`). Waypoint-type enum is not in any raw doc. Draft proposal under [Pending decisions](#pending-decisions).

### `fsm_msgs/msg/FSMEvent.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 3. Raw range `event_type (PICKUP_COMPLETE=0 … EMERGENCY_STOP_REQUEST=7)`; values 1..6 are not enumerated in the raw doc. Draft proposal under [Pending decisions](#pending-decisions).

---

## `localization_msgs/`

Source: roadmap §5 p. 3 (package roster) and §5.1 p. 3 (per-file content notes). Field names appear in the raw doc but ROS2 types and several enum values are project-decided. All localization messages are **draft pending owner confirmation**. Draft proposals live under [Pending decisions](#pending-decisions). **DO NOT GENERATE THESE FOR MILESTONE 1.**

### `localization_msgs/msg/LocalizationPose.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 3 (`x, y, yaw (ENU), linear_velocity, source, localization_confidence, position_covariance, heading_covariance, valid_until_ms`). ROS2 types and covariance representation (single float vs flat array) are project-decided.

### `localization_msgs/msg/LocalizationStatus.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 3 (`status (OK=0…LOST=6), ndt_healthy, ndt_quality, map_odom_stable, warning_flags[]`). Status values 1..5 are not enumerated.

### `localization_msgs/msg/Odometry.msg` — **status: draft pending owner confirmation**

Roadmap §5 p. 3 names `Odometry` in the package roster, but does not specify whether to define a project-local message or simply reuse `nav_msgs/Odometry`. This is an open decision for the localization owner — see [Pending decisions](#pending-decisions). The recommended baseline (reuse `nav_msgs/Odometry`) avoids duplicating ROS2-standard types and makes integration with off-the-shelf packages easier; a project-local wrapper would only be justified if the team needs additional fields like `valid_until_ms` or `localization_confidence` exposed alongside the standard pose+twist.

### `localization_msgs/msg/MapOrigin.msg` — **status: draft pending owner confirmation**

Field names from roadmap §5.1 p. 4 (`lat_ref, lon_ref, yaw_ref, locked — planner locked=true olana kadar waypoint işlemez`). ROS2 types are project-decided.

### `localization_msgs/msg/RawGPS.msg` — **status: draft pending owner confirmation**

Roadmap §5 p. 3 names `RawGPS` in the package roster — debug/rosbag only; planner MUST NOT consume this (roadmap §11 p. 12). Field set is otherwise unspecified in the raw doc.

---

## Pending decisions

This section captures the draft proposals that the team has **not yet approved**. They are reproduced here so the owners (planner, FSM, controller, localization) have a concrete starting point for the confirmation discussion. None of these are implementable as written.

### TargetSpeed.reason values 1..7

`LANE_FOLLOW=0` and `EMERGENCY_STOP=8` are from the raw doc. The roadmap §11 p. 12 mandates that `JUNCTION` and `TUNNEL` are represented via `TargetSpeed.reason` (not as autonomy modes). A reasonable starting set, to be confirmed by the planner owner:

```
uint8 LANE_FOLLOW=0
uint8 STOP_APPROACH=1                  # speed reduction triggered by approach to a stop point
uint8 JUNCTION=2                       # reduced speed entering a junction
uint8 TUNNEL=3                         # tunnel speed cap
uint8 OBSTACLE_TTC=4                   # speed cut due to TTC pressure
uint8 CURVATURE=5                      # speed shaped by lane curvature
uint8 ROUTE_CONTEXT_INVALID=6          # conservative fallback when active_route_context is stale
uint8 PICKUP_DROPOFF=7                 # creep speed near PICKUP/DROPOFF
uint8 EMERGENCY_STOP=8
```

### PlanningStatus field set

No raw doc enumerates fields. Suggested minimum, to be confirmed by the planner owner:

```
uint8 IDLE=0
uint8 PLANNING=1
uint8 EXECUTING=2
uint8 STOP_REQUESTED=3
uint8 EMERGENCY_STOP=4
uint8 REPLANNING=5
uint8 FAULT=6

std_msgs/Header header
uint8    status
bool     trajectory_valid
bool     target_speed_valid
uint32   valid_until_ms
string[] warning_flags
```

### FSMRequest.request_type values 1..4

`MODE_CHANGE=0` and `PARK_READY=5` are from the raw range. Suggested intermediate values, to be confirmed by the FSM owner:

```
uint8 MODE_CHANGE=0
uint8 STOP_REQUEST=1
uint8 RESUME_REQUEST=2
uint8 EMERGENCY_STOP_REQUEST=3         # software EMERGENCY_STOP — NOT the hardware AUTONOMOUS_EMERGENCY channel
uint8 REPLANNING_REQUEST=4
uint8 PARK_READY=5
```

### CurrentMode.stop_reason integer mapping

Symbolic names are from the raw doc; integer values are project-decided. Suggested mapping, to be confirmed by the FSM owner:

```
uint8 NONE=0
uint8 RED_LIGHT=1
uint8 STOP_SIGN=2
uint8 OBSTACLE_TTC=3
uint8 LOK_LOST=4
uint8 STALE_SENSOR=5
uint8 MISSION_ABORT=6
uint8 PEDESTRIAN=7
```

### MissionState waypoint-type enum

No raw doc names this enum. Suggested set, derived from the GeoJSON tour structure (roadmap §7), to be confirmed by the FSM and planner owners:

```
uint8 WP_START=0
uint8 WP_NORMAL=1
uint8 WP_PICKUP=2
uint8 WP_DROPOFF=3
uint8 WP_PARK=4
uint8 WP_END=5
```

### FSMEvent.event_type values 1..6

`PICKUP_COMPLETE=0` and `EMERGENCY_STOP_REQUEST=7` are from the raw range. Suggested intermediate values, to be confirmed by the FSM owner:

```
uint8 PICKUP_COMPLETE=0
uint8 DROPOFF_COMPLETE=1
uint8 PARK_COMPLETE=2
uint8 STOP_TIMEOUT=3
uint8 OBSTACLE_CLEARED=4
uint8 LIGHT_GREEN_CONFIRMED=5
uint8 SIGN_HANDLED=6
uint8 EMERGENCY_STOP_REQUEST=7
```

### LocalizationStatus.status values 1..5

`OK=0` and `LOST=6` are from the raw range. Suggested intermediate values, to be confirmed by the localization owner:

```
uint8 OK=0
uint8 NDT_DEGRADED=1
uint8 GPS_LOST=2
uint8 IMU_DOMINANT=3
uint8 ENCODER_DOMINANT=4
uint8 STALE=5
uint8 LOST=6
```

### `localization_msgs/Odometry.msg` vs `nav_msgs/Odometry`

Decision required from the localization owner:

- **Option A — reuse `nav_msgs/Odometry`** (recommended baseline). Drop `localization_msgs/Odometry.msg` from the package; subscribers consume the ROS2 standard type. Update roadmap §5 / §5.1 to remove the project-local entry.
- **Option B — define a project-local wrapper** that adds `confidence` and `valid_until_ms` alongside the standard pose+twist. Justified only if the planner or FSM actually needs those fields on the odometry topic.

If Option B is chosen, the suggested minimum is:

```
std_msgs/Header header
string  child_frame_id                 # "base_link"
geometry_msgs/Pose pose
geometry_msgs/Twist twist
float32 confidence                     # 0.0–1.0
uint32  valid_until_ms
```

### LocalizationPose ROS2 types

Roadmap names the fields; types below are project-suggested, to be confirmed by the localization owner. Notably, the covariance representation (single float vs row-major flat array) and `source` enum vs string are open:

```
std_msgs/Header header
float64 x                              # ENU east (m)
float64 y                              # ENU north (m)
float32 yaw                            # ENU heading (rad)
float32 linear_velocity                # m/s (longitudinal)
string  source                         # "ndt+ekf" | "ekf_only" | "imu_dead_reckon" | "gps_only"
float32 localization_confidence        # 0.0–1.0
float32[36] position_covariance        # 6x6 row-major (x,y,z,roll,pitch,yaw)
float32 heading_covariance             # rad^2
uint32  valid_until_ms
```

### `MapOrigin.msg` and `RawGPS.msg` ROS2 types

Field names are present in the raw doc; below are project-suggested types pending localization owner confirmation.

```
# MapOrigin
std_msgs/Header header
float64 lat_ref                        # WGS84 (deg)
float64 lon_ref                        # WGS84 (deg)
float32 yaw_ref                        # ENU base yaw (rad)
bool    locked
```

```
# RawGPS — debug/rosbag only; planner MUST NOT subscribe (roadmap §11 p. 12)
std_msgs/Header header
float64 latitude                       # WGS84 (deg)
float64 longitude                      # WGS84 (deg)
float32 altitude                       # m
float32 horizontal_accuracy            # m
uint8   fix_status                     # vendor-defined raw byte
```

### `TrajectoryPoint.msg` / `Trajectory.msg`

The raw doc writes `points[]: (x, y, yaw, speed, curvature)` but does not specify a separate nested `.msg` file. Splitting into a `TrajectoryPoint` element is a project-side structuring choice for ROS2 `.msg` syntax. Confirm with the planner owner whether the team prefers the nested-element form or a flat representation (e.g. parallel `float32[]` arrays).

### `ControllerFeedback.msg` types and units

Field names are present in the raw doc. Confirm units (`actual_steering_deg` in degrees vs radians; `heading_error` in radians) with the controller owner before generating.

### Pending team extension: `StopTarget.warning_flags`

Adding `string[] warning_flags` to `perception_msgs/msg/StopTarget.msg` would line up with the topic-level header rule and the standard warning flag set. Contract §15 raw `.msg` for `StopTarget` does **not** include this field, so it has been removed from the canonical block. If the team decides to add it, follow the contract change procedure (field addition → MINOR per contract change policy) and update both this page and the contract document.

---

## Milestone 1 readiness

The wiki is **partially cleared** for Milestone 1.

**Allowed for Milestone 1 generation now (`canonical raw` only):**

| Package | Message | Status |
|---|---|---|
| `common_msgs` | `AutonomyMode.msg` | canonical raw |
| `perception_msgs` | `LaneModel.msg` | canonical raw |
| `perception_msgs` | `TrafficLightState.msg` | canonical raw |
| `perception_msgs` | `TrafficSign.msg` | canonical raw |
| `perception_msgs` | `TrafficSigns.msg` | canonical raw |
| `perception_msgs` | `ObstacleTrack.msg` | canonical raw |
| `perception_msgs` | `ObstacleTracks.msg` | canonical raw |
| `perception_msgs` | `StopTarget.msg` | canonical raw |
| `perception_msgs` | `Junction.msg` | canonical raw (Phase-2 optional) |
| `perception_msgs` | `PerceptionDiagnostics.msg` | canonical raw |
| `planning_msgs` | `ActiveRouteContext.msg` | canonical raw |

These can be created today: package skeletons (`package.xml`, `CMakeLists.txt`) for `common_msgs`, `perception_msgs`, `planning_msgs` containing only the messages above, plus `colcon build` and `ros2 interface show` verification.

**Blocked from Milestone 1 generation until owner confirmation (all `draft pending owner confirmation`):**

- `planning_msgs` — `Trajectory.msg`, `TrajectoryPoint.msg`, `TargetSpeed.msg`, `PlanningStatus.msg`, `ControllerFeedback.msg`, `FSMRequest.msg`.
- `fsm_msgs` — entire package (`CurrentMode.msg`, `MissionState.msg`, `FSMEvent.msg`).
- `localization_msgs` — entire package (`LocalizationPose.msg`, `LocalizationStatus.msg`, `Odometry.msg` vs `nav_msgs/Odometry`, `MapOrigin.msg`, `RawGPS.msg`).

The blocked items become unblocked once the corresponding [Pending decisions](#pending-decisions) entries are confirmed by their owners and the page is updated to reclassify them as `canonical raw` or `team-approved extension`.
