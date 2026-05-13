# Wiki Index — AU Cengaver Robotics / TEKNOFEST 2026 Robotaksi

This wiki is the project's living knowledge base. Start here. Read raw PDFs only when this wiki is missing something or contradicts itself (see `CLAUDE.md` for the workflow).

Source priority on conflict: `raw/official_teknofest/` > `raw/final_contracts/` > `raw/team_notes/`.

## ⚠ Current test environment (Mac-only static work)

Active development is on a MacBook Air M4. **ROS2 Foxy / Ubuntu 20.04 desktop is not available during most implementation steps.** Until that desktop is reachable:

- The only authoritative build/runtime environment is **Ubuntu 20.04 + ROS2 Foxy**. macOS is editing-only.
- Mac work is limited to **static review**: file-layout checks, forbidden-file/symbol grep, package-metadata inspection, and reading `.msg` / `package.xml` / `CMakeLists.txt` by eye. No `colcon`, no `ros2`, no Gazebo runs on Mac.
- Every implementation deliverable produced on Mac MUST be labeled with all three of:
  - **static-reviewed on Mac**
  - **ROS2 build pending on Ubuntu 20.04**
  - **ROS2 runtime pending on Ubuntu 20.04**
- Mac static checks **do not replace** `colcon build`, `ros2 interface show`, `ros2 topic echo/list`, `ros2 launch` smoke tests, or Gazebo 11 runs. A green static review is provisional acceptance only — it never satisfies the Ubuntu verification gate. See `wiki/implementation/milestones.md` § "Verification policy while Ubuntu is unavailable" and `wiki/ros2/ros2_foxy_notes.md` § "Mac development mode".

This is a workflow accommodation, not a relaxation of the ROS2 Foxy / Ubuntu 20.04 compatibility requirement defined in `CLAUDE.md` § "Target Runtime".

## ⚠ Current implementation gate (Gate B — partial)

`wiki/contracts/message_contracts.md` separates messages into **canonical raw** (implementable now) and **draft pending owner confirmation** (NOT implementable). The current cleared scope for code generation is:

- `common_msgs` — `AutonomyMode.msg` (constants only).
- `perception_msgs` — all canonical raw messages (`LaneModel`, `TrafficLightState`, `TrafficSign`, `TrafficSigns`, `ObstacleTrack`, `ObstacleTracks`, `StopTarget`, `Junction`, `PerceptionDiagnostics`).
- `planning_msgs` — **only** `ActiveRouteContext.msg`.

**Full five-package message generation is BLOCKED.** Do **NOT** create `fsm_msgs`, `localization_msgs`, or the draft `planning_msgs` schemas (`Trajectory`, `TrajectoryPoint`, `TargetSpeed`, `PlanningStatus`, `ControllerFeedback`, `FSMRequest`) until their owners sign off on the entries in `wiki/contracts/message_contracts.md` § "Pending decisions" and the page reclassifies them as `canonical raw` or `team-approved extension`.

Build command for the cleared scope: `colcon build --packages-select common_msgs perception_msgs planning_msgs` (see `wiki/ros2/ros2_foxy_notes.md`). Step 1 in `wiki/implementation/milestones.md` lists the same scope and the per-message verification commands.

## Architecture
- [System Overview](architecture/system_overview.md) — layered architecture (sensors → perception → localization → FSM → planner → controller), package layout, hard rules.
- [TF Standard](architecture/tf_standard.md) — `map → odom → base_link → camera_frame / lidar_frame`, ownership, sensor extrinsics.
- [Active Route Context](architecture/active_route_context.md) — planner → perception contract, TTC ego_speed source, stale rules.
- [Team Roles](architecture/team_roles.md) — who owns what module.

## Contracts
- [Perception ↔ Planner / FSM Contract (v1.4)](contracts/perception_planner_fsm_contract.md) — top-level summary of the algılama-planner sözleşmesi.
- [Message Contracts](contracts/message_contracts.md) — `.msg` field definitions for `common_msgs`, `perception_msgs`, `planning_msgs`, `fsm_msgs`, `localization_msgs`.
- [Timing and Fallback Table](contracts/timing_and_fallback.md) — Hz, valid_until_ms, fallback per topic, warning flag set.
- [Test Contract](contracts/test_contract.md) — T-01..T-13, F-, L-, C-, Tur tests and rosbag rules.

## Perception
- [Perception Overview](perception/perception_overview.md) — node graph, output topics, MVP order, "perception does not decide".
- [Traffic Light Node](perception/traffic_light_node.md) — YOLO bbox + HSV ROI + 3-frame temporal confirm; STALE/CONFLICT semantics.
- [Traffic Sign Node](perception/traffic_sign_node.md) — YOLOv8n; event_status state machine; event_memory_ttl_ms.
- [Lane Node](perception/lane_node.md) — Track A synthetic MVP; publishes `LaneModel` centerline/boundaries/`lane_lost` from fake `bgr8` lane frames; UFLD v2/TensorRT and real curvature are Phase 2.
- [LiDAR Obstacle Node](perception/lidar_obstacle_node.md) — VLP-16, RANSAC ground + Euclidean cluster + Centroid Kalman, closing-speed TTC.
- [Stop Target Node](perception/stop_target_node.md) — aggregator producing stop evidence (light / sign / pickup / dropoff) with `priority`.
- [Junction Node (Phase-2 optional)](perception/junction_node.md) — visual junction hint; MVP relies on `active_route_context.route_direction`.
- [Perception Diagnostics Node](perception/perception_diagnostics_node.md) — input_hz / output_hz / latency / gpu_utilization / warning_flags.

## ROS2
- [ROS2 Foxy Notes](ros2/ros2_foxy_notes.md) — Foxy on Ubuntu 20.04, package skeleton, build commands, Docker on BEE1.

## Vehicle
- [BEE1 Platform](vehicle/bee1_platform.md) — Beemobs Bee1 dimensions, sensors (VLP-16, ZED2, MTI-680, RTX 3060), sensor extrinsics from BEE1 axle reference.
- [CAN-Bus Interface](vehicle/canbus_interface.md) — `/beemobs/*` topics for ignition, gear, throttle, brake, steering, hand brake, AUTONOMOUS_EMERGENCY.

## Implementation
- [Milestones](implementation/milestones.md) — 14-step development plan (`raw/final_contracts/AU_Cengaver_GANG_Yol_Haritasi`), deadlines, MVP gate.
- [Perception Sprint Plan](implementation/perception_sprint_plan.md) — Sprint 0 complete; Sprint 1 COMPLETE; Sprint 2 Track A + Track B COMPLETE (238 tests, verified 2026-05-12); **Sprint 3 IN PROGRESS** (kickoff 2026-05-12); deadline 2026-06-23.
- [Sprint 3 Perception Integration Kickoff](implementation/sprint3_perception_integration_kickoff.md) — Sprint 3 track breakdown: Track G (Gazebo/sim skeleton, S3-G1..G3), Track S (stop_target_node MVP, S3-S1..S3), Track R (ActiveRouteContext + TTC wiring, S3-R1..R4); blocked items; acceptance gates.
- [Sprint 2 Perception Kickoff](implementation/sprint2_perception_kickoff.md) — Sprint 2 goal, Track A (S2-A1..S2-A5) and Track B (S2-B1..S2-B5) deliverables, architecture boundaries, fake-publisher test approach, required `LaneModel` and `ObstacleTrack` fields, acceptance gates.
- [Sprint 1 Traffic Light Smoke Checklist](implementation/sprint1_traffic_light_smoke_checklist.md) — repeat-verification commands for the traffic_light_node MVP on Ubuntu 20.04 + ROS2 Foxy.
- [Sprint 2 Lane Track A Smoke Checklist](implementation/sprint2_lane_track_a_smoke_checklist.md) — repeat-verification commands for the lane_node synthetic MVP (Track A closure, S2-A5).
- [Sprint 2 LiDAR Track B Smoke Checklist](implementation/sprint2_lidar_track_b_smoke_checklist.md) — repeat-verification commands for the lidar_obstacle_node synthetic MVP (Track B closure, S2-B5); covers simple_obstacle, moving_obstacle, stale gating, empty, and forbidden-topic checks.

## Operational
- [Log](log.md) — chronological ingest / decision / lint entries.
