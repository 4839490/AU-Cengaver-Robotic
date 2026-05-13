# Implementation Milestones

Source: `raw/final_contracts/AU_Cengaver_GANG_Yol_Haritasi_DUZELTILMIS.pdf` (v1.1 revize, 09 Mayıs 2026) §2, §4, §7.

## Strategy

Two parallel tracks (so the simulation video doesn't gate on perception readiness):

- **Track A — System spine**: msg packages → localization → FSM → planner → controller → integration.
- **Track B — Perception & sim**: sim skeleton → perception MVP → rosbag/dataset → perception integration.

## Module dependency order

| # | Module | Depends on | Notes |
|---|---|---|---|
| 1 | `common_msgs` + msg packages | — | Required for every node. |
| 2 | `vehicle_params.yaml` | — | Single source for vehicle constants. |
| 3 | Simulation skeleton | msg packages | URDF, sensor plugins, simple world. |
| 4 | Perception MVP | msg packages + sim/rosbag | Lane / light / obstacle MVP starts in parallel. |
| 5 | Localization | msg packages + sim | EKF + NDT/global. |
| 6 | FSM | msg packages + localization | 8 modes, mode transitions. |
| 7 | Planner core | localization + FSM | Trajectory + speed profile. |
| 8 | Controller core | planner + vehicle params | Stanley/Pure Pursuit, PID, Ackermann. |
| 9 | Integration MVP (Tour 1) | planner + controller + loc + FSM | Minimum viable tour. |
| 10 | Full perception integration | perception MVP + planner/FSM | Light, sign, obstacle, lane_lost wired in. |
| 11 | Full simulation | all modules | Tour 2/3 + video + report. |
| 12 | Real vehicle | sim-passing system | Camp adaptation. |

## Calendar (key absolute dates)

- 2026-05-09 → 2026-05-12 — msg packages, `vehicle_params.yaml`, repo skeleton, sim skeleton.
- 2026-05-12 → 2026-05-18 — localization MVP, FSM skeleton, perception MVP starter.
- 2026-05-18 → 2026-05-25 — planner / controller basic loop, Gazebo straight-road test.
- 2026-05-25 → 2026-06-02 — lane + light + obstacle MVP rosbag tests.
- 2026-06-02 → 2026-06-09 — Tour 1 integration, route context, mission flow.
- 2026-06-09 → 2026-06-16 — Tour 2/3, traffic light, dynamic obstacle, parking.
- 2026-06-16 → 2026-06-21 — stabilization, video scenarios, rosbag evidence.
- 2026-06-22 → 2026-06-23 — final simulation video and report packaging.
- **2026-06-23 — official simulation video upload deadline (teknofest.org)**.
- 2026-07 → 2026-08 — Real-vehicle camp at Bilişim Vadisi.

## Step list (numbered like the roadmap)

1. **Message packages — partial scope (Gate B).** Generate ONLY the canonical raw messages currently cleared by `wiki/contracts/message_contracts.md`. Full five-package generation is **NOT allowed yet** — `fsm_msgs`, `localization_msgs`, and the draft `planning_msgs` schemas remain blocked until owner confirmation.

   **Cleared now (canonical raw):**
   - `common_msgs/msg/AutonomyMode.msg` — 8 autonomy constants only, no carrier field. `PlannerMode.msg` and `FSMMode.msg` MUST NOT be created.
   - `perception_msgs/msg/`: `LaneModel.msg`, `TrafficLightState.msg`, `TrafficSign.msg`, `TrafficSigns.msg`, `ObstacleTrack.msg`, `ObstacleTracks.msg`, `StopTarget.msg` (no `warning_flags` until team-approved), `Junction.msg` (Phase-2 optional), `PerceptionDiagnostics.msg`.
   - `planning_msgs/msg/ActiveRouteContext.msg` — and **only** `ActiveRouteContext.msg` in `planning_msgs` for now.

   **Blocked until owner confirmation (do NOT create):**
   - Rest of `planning_msgs`: `Trajectory.msg`, `TrajectoryPoint.msg`, `TargetSpeed.msg`, `PlanningStatus.msg`, `ControllerFeedback.msg`, `FSMRequest.msg`.
   - All of `fsm_msgs` (`CurrentMode.msg`, `MissionState.msg`, `FSMEvent.msg`).
   - All of `localization_msgs` (`LocalizationPose.msg`, `LocalizationStatus.msg`, `Odometry.msg` vs `nav_msgs/Odometry`, `MapOrigin.msg`, `RawGPS.msg`).

   See `wiki/contracts/message_contracts.md` § "Pending decisions" for the draft proposals each owner must confirm.

   **Verification:** `colcon build --packages-select common_msgs perception_msgs planning_msgs` runs cleanly. `ros2 interface show <pkg>/msg/<Type>` succeeds for every message in the cleared scope.
2. **`vehicle_params.yaml`.** `max_speed`, `wheelbase`, `steering_center`, `max_steer_angle`, `min_turn_radius`, `max_accel`, `max_brake_accel`. Mark as `TBD/needs_calibration` until measured. Both planner and controller launchers point at this YAML.
3. **Sim skeleton.** Install `ros-foxy-gazebo-ros-pkgs`. BEE1 URDF (2740×1060×1785, dingil 1860). VLP-16, ZED2, Xsens plugins. `simple_test.world` (50 m two-lane straight). Verify `/velodyne_points`, `/zed2/left/image_raw`, `/imu/data` at ≥10 Hz. Prepare rosbag template.
4. **Perception MVP starter.** `lane_node.py`, `traffic_light_node.py`, `lidar_obstacle_node.py`, `perception_diagnostics_node.py` publishing contract-shaped messages. Static TF: `base_link → camera_frame`, `base_link → lidar_frame`. Publishers must populate fields exactly according to `wiki/contracts/message_contracts.md`; not every wrapper/diagnostic message has `age_ms` + `valid_until_ms` (e.g. `TrafficSigns` / `ObstacleTracks` are header-only wrappers; `PerceptionDiagnostics` carries `last_msg_age_ms` and no `valid_until_ms`).
5. **Localization nodes.** `local_ekf_node.py` (IMU + encoder → `/localization/odometry` 50 Hz, `odom→base_link`). `global_localization_node.py` (GPS + NDT + local odometry → `/localization/pose` 30–50 Hz, `map→odom`). `map_origin_publisher.py` (latching). Tunnel fallback weights. Run L-01, L-06, L-07, L-10, L-11.
6. **FSM skeleton.** `fsm_node.py` with 8 modes and `transition_to()`. `/fsm/current_mode` (10 Hz), `/fsm/mission_state` (5 Hz). `stop_reason` discrimination. Watchdog + guard conditions. Safety supervisor signal observed only. Run F-01/02, F-04/05/06, F-13.
7. **GeoJSON + waypoints.** `geojson_parser.py` parses `name` field, sorts by node id. `coord_converter.py` does Equirectangular projection vs `map_origin`. Front-bumper offset: `x_base = x_wp − L_fb × cos(yaw)`. Generate `tur1.geojson`, `tur2.geojson`, `tur3.geojson`. Do not process waypoints until `map_origin.locked = true`.
8. **Planner core.** Subscribe `/fsm/current_mode`, `/localization/pose`, `/localization/status`. `trajectory_sampler.py` from waypoints + centerline. `speed_profile.py` (FSM mode, curvature, TTC, waypoint type). Publish `/planning/trajectory` (20 Hz, `map`), `/planning/target_speed` (20 Hz), `/planning/active_route_context` (10–20 Hz, `base_link`, with `in_stop_zone`), `/planning/status` (10 Hz). Skip trajectory while `mission_active=false`.
9. **Controller core.** Subscribe `/planning/trajectory`, `/planning/target_speed`, `/planning/status`. Stanley + Pure Pursuit + PID. Ackermann kinematics. `can_interface.py` writes 0x560 frames `RC_THRT_DATA` and `AUTONOMOUS_SteeringMot_Control`. `final_speed = min(target_speed.speed, trajectory_point.speed)`. Publish `/controller/feedback` 20 Hz. Run C-02, C-07.
10. **Integration MVP (Tour 1).** `sim_full.launch.py` boots everything. Localization + FSM + planner + controller loop. Tour 1: start → waypoints → park approach. Record all topics. Run C-01/12, F-01/14, L-01/12.
11. **Full perception integration.** `lane_model` consumed by planner. `traffic_light_state` gated to STOP_APPROACH (confirmed + relevant_to_route). `traffic_signs` event memory feeds FSM/planner. `obstacle_tracks` planner-side `in_path` / TTC / collision_risk. `stop_target` to planner. `route_context_valid=false` behavior tested. Run T-01..T-13.
12. **Tours 2 & 3.** Tour 2 (active traffic light + dynamic obstacle + park). Tour 3 (pickup/dropoff + traffic + obstacle + park). Tunnel scenario (GPS loss, IMU/LiDAR dominant, GPS recovery). Slalom (cone positions, temporary corridor). Park (Dubins path, 3-min limit, missed-park behavior). Target ≥90% pass rate over 10 trials.
13. **Simulation video & report packaging.** Single launch command. Save rosbag and terminal logs. Screenshots + topic plots + test tables for the KTR / sim report. Video ≥720p, uninterrupted, intelligible. Done before 2026-06-23.
14. **Real-vehicle integration (camp).** SSH into `192.168.30.100` (user `smart`). Build Docker image and SFTP. Joystick-verify CAN. Confirm sensor topics (`/velodyne_points`, `/zed2`, `/imu/data`). Re-measure static TF on the real BEE1. Update `vehicle_params.yaml`. Tune Stanley + PID. LIO-SAM map collection. Pass technical-control items.

## Verification policy while Ubuntu is unavailable

Active development is happening on a MacBook Air M4. ROS2 Foxy / Ubuntu 20.04 desktop will NOT be available during most implementation steps. The Gate B partial scope above is unchanged — the cleared / blocked message lists still hold.

What this section adds is the **acceptance status** that every milestone has while Ubuntu is unreachable.

- Implementation may continue in small scopes on Mac. Each completed step is **provisionally accepted** — never finally accepted — until Ubuntu verification passes.
- Every implementation deliverable produced on Mac MUST carry all three labels:
  - `static-reviewed on Mac`
  - `ROS2 build pending on Ubuntu 20.04`
  - `ROS2 runtime pending on Ubuntu 20.04`
- Mac-allowed checks: file-layout listing, forbidden-file/forbidden-symbol grep, `package.xml` / `CMakeLists.txt` inspection, `.msg` field-set diff against `wiki/contracts/message_contracts.md`, Python/launch-file syntax review by eye. No `colcon`, `ros2`, `gazebo`, or simulator runs on Mac. Do not produce or fake their output.
- A green Mac review **never** satisfies the Ubuntu gate. Steps marked provisionally accepted on Mac stay provisional in `wiki/log.md` and roll up unverified into downstream milestones — downstream code that consumes them inherits the same provisional status.

### Deferred Ubuntu verification checkpoints

When the Ubuntu 20.04 desktop is reachable, every Mac-provisional step must be cleared by the corresponding checkpoint below before it is finally accepted. Run them in order; do not promote a later step until earlier checkpoints pass.

| # | Mac-provisional artifact | Required Ubuntu 20.04 verification |
|---|---|---|
| V-B1 | Gate B message packages (`common_msgs`, `perception_msgs`, `planning_msgs/ActiveRouteContext`) | `colcon build --packages-select common_msgs perception_msgs planning_msgs` returns 0; `ros2 interface show` succeeds for every cleared `.msg` listed in `wiki/ros2/ros2_foxy_notes.md`. |
| V-B2 | Dummy perception publishers (Step 4 nodes producing contract-shaped messages) | `ros2 run` each node; `ros2 topic list` shows the contract topics; `ros2 topic echo` confirms one message per topic with the expected `frame_id` and field set. |
| V-B3 | Launch files (perception bringup, integration launchers as they appear) | `ros2 launch` smoke test of each launch file: nodes come up, topics appear, no `ERROR` lines in the launch log. |
| V-B4 | Gazebo / sim skeleton (Step 3) | `gazebo` (Gazebo 11) launches the BEE1 world; `ros2 topic hz` shows `/velodyne_points`, `/zed2/left/image_raw`, `/imu/data` at ≥10 Hz; static TF tree (`base_link → camera_frame`, `base_link → lidar_frame`) verified with `tf2_echo`. |

A row only becomes "verified on Ubuntu 20.04" once the listed commands have actually been run on the Ubuntu desktop and their output is recorded in `wiki/log.md`. Until then it stays provisional regardless of how clean the Mac static review looked.

This is a workflow decision driven by hardware availability — it does not relax the ROS2 Foxy / Ubuntu 20.04 compatibility rules in `CLAUDE.md` § "Target Runtime".

## "Cleared to start coding" gate

This gate is split into two stages because the message contract is only partially confirmed.

**Partial message-spine coding (allowed today)** — may begin only after:

- ✅ `common_msgs`, `perception_msgs`, and `planning_msgs` (containing **only** `ActiveRouteContext.msg`) build cleanly with `colcon build --packages-select common_msgs perception_msgs planning_msgs`.
- ✅ `vehicle_params.yaml` exists.
- ✅ Simulation skeleton stands up.
- ✅ Perception MVP can publish dummy contract-shaped messages against the cleared types and is being tested with rosbag or sim topics.

**Full system-spine coding (still BLOCKED)** — remains blocked until:

- ❌ All `draft pending owner confirmation` schemas in `wiki/contracts/message_contracts.md` are owner-confirmed (planner, FSM, controller, localization).
- ❌ `fsm_msgs` and `localization_msgs` are reclassified to `canonical raw` / `team-approved extension` and generated.
- ❌ The remaining `planning_msgs` schemas (`Trajectory`, `TrajectoryPoint`, `TargetSpeed`, `PlanningStatus`, `ControllerFeedback`, `FSMRequest`) are confirmed and generated.

Steps 5 (Localization), 6 (FSM), 8 (Planner core), 9 (Controller core), and downstream integration steps depend on the blocked schemas and cannot start until the full gate opens.

## Risk table (verbatim from §9)

| Risk | Effect | Mitigation |
|---|---|---|
| Perception lags | weak sim video | Perception MVP starts at Step 4 |
| Gazebo not realistic enough for YOLO | weak light/sign tests | Rosbag + dataset + CARLA if needed |
| Enums diverge again | ROS2 integration error | Only `common_msgs/AutonomyMode` |
| TF directions mixed up | wrong coords, safety risk | Single TF tree + `tf2_echo` tests |
| `ego_speed_mps` not flowing | wrong TTC | `controller/feedback → active_route_context` flow |
| Wrong vehicle params | bad control | `vehicle_params.yaml` + real-vehicle calibration |
| Inconsistent timeouts | unnecessary or late braking | Single timeout table, same values everywhere |
| NDT/GPS loss | localization drift | IMU/encoder fallback, status degrade mechanism |
