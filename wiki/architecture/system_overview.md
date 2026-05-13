# System Overview

Sources: `raw/final_contracts/AU_Cengaver_GANG_Yol_Haritasi_DUZELTILMIS.pdf` §1, §3, §5; `raw/team_notes/meeting_decisions.md`; `raw/official_teknofest/...Mimari_Tanımlama...pdf`.

## Layered architecture

| Layer | Responsibility |
|---|---|
| Sensors | Camera (ZED2), LiDAR (VLP-16), IMU + GNSS (Xsens MTI-680-DK), wheel encoders |
| Perception | Describes the scene — produces evidence (detections, tracks, confidence, validity) |
| Localization | Where the vehicle is — `odom`, `map → odom`, `pose`, `status`, `map_origin` |
| FSM | Decides what to do next — 8-mode state machine with `transition_to()` and guard conditions |
| Planner | Decides how to get there — trajectory, target speed, active route context |
| Controller | Executes on hardware — Stanley / Pure Pursuit, PID throttle, Ackermann kinematics, CAN 0x560 frames |
| Safety Supervisor | Hardware safety channel (`AUTONOMOUS_EMERGENCY`) — independent of FSM |

See [Team Roles](team_roles.md) for module ownership.

## Hard architecture rules (do not silently change)

- **Perception does not make driving decisions.** It only publishes contract-shaped evidence.
- **Controller does not subscribe to perception topics for control.** Controller consumes only `/planning/*` and `/controller/feedback` paths. Perception → FSM/Planner → Controller is the only allowed flow.
- **Stanley / Pure Pursuit live in the controller**, not the planner. Planner produces a trajectory; controller follows it.
- **One mode enum**: `common_msgs/AutonomyMode.msg`. `PlannerMode.msg` and `FSMMode.msg` MUST NOT exist.
- **`JUNCTION` and `TUNNEL` are not modes** — represent them via `TargetSpeed.reason` or `active_route_context.route_direction` / route context.
- **`ObstacleTrack.msg` has no `in_path` field.** Planner computes `in_path` from `planned_trajectory`.
- **Planner must NOT read `/localization/raw_gps`.** Use `/localization/pose` only. `raw_gps` is debug/rosbag.
- **`EMERGENCY_STOP` ≠ `AUTONOMOUS_EMERGENCY`.** The first is a software full-brake request (planner publishes); the second is a hardware safety channel handled by the safety supervisor — FSM may only observe and log it.

## Frame conventions

- All perception outputs use `frame_id = base_link`.
- `planned_trajectory[]` and `Trajectory.msg` use `frame_id = map`.
- `active_route_context.target_x/y` is `base_link`.
- See [TF Standard](tf_standard.md).

## Workspace skeleton

```
cengaver_ws/
  src/
    common_msgs/             # AutonomyMode (TEK MOD ENUM)
    fsm_msgs/                # CurrentMode, MissionState, FSMEvent
    localization_msgs/       # Pose, Odometry, Status, MapOrigin, RawGPS
    perception_msgs/         # LaneModel, TrafficLightState, TrafficSign(s), ObstacleTrack(s), StopTarget, Junction, PerceptionDiagnostics
    planning_msgs/           # Trajectory, TargetSpeed, PlanningStatus, ActiveRouteContext, FSMRequest, ControllerFeedback
    localization/            # local_ekf_node, global_localization_node, map_origin_publisher, lidar_undistortion
    fsm/                     # fsm_node + states/*.py
    planner/                 # planner_node, geojson_parser, coord_converter, trajectory_sampler, dubins_path, ...
    controller/              # controller_node, stanley_controller, pure_pursuit_controller, pid_controller, can_interface
    perception/              # lane_node, traffic_light_node, traffic_sign_node, lidar_obstacle_node, fusion_node, stop_target_node, perception_diagnostics_node
    simulation/              # Gazebo URDF, world, launch (BEE1 model 2740×1060×1785 mm, dingil 1860 mm)
    bringup/                 # top-level launch + static TFs
```

## Target runtime

- Ubuntu 20.04 LTS, ROS2 Foxy, Gazebo 11. macOS may be used for editing only; build/test happens on Foxy.
- Target real platform: BEE1 (Beemobs) — see [BEE1 Platform](../vehicle/bee1_platform.md).
- Vehicle PC: Advantech MIC-770V3H + MIC-75G20, RTX 3060 12 GB, 32 GB RAM, 1 TB SSD. Reach via SSH `smart@192.168.30.100` (Robotaxi_1) or `192.168.10.100` (Robotaxi_2). See [CAN-Bus Interface](../vehicle/canbus_interface.md).

## Critical reminders (verbatim from roadmap §11)

- `PlannerMode.msg` ve `FSMMode.msg` YOKTUR. Tek enum: `common_msgs/AutonomyMode`.
- `JUNCTION` / `TUNNEL` mode değildir.
- Planner Stanley kontrolcüsü YAZMAZ — Stanley controller'dadır.
- Tüm koordinatlar: trajectory = `map` frame; `active_route_context` = `base_link` frame.
- `ObstacleTrack.msg` içinde `in_path` alanı YOKTUR — planner planned_trajectory ile hesaplar.
- Planner `/localization/raw_gps` OKUMAZ — yalnızca `/localization/pose`.
- `EMERGENCY_STOP` (yazılım) vs `AUTONOMOUS_EMERGENCY` (donanım kanalı, safety supervisor).
- `ego_speed_mps` zorunlu — `controller/feedback → planner → active_route_context` akışıyla.
- `route_context_valid=false` algıyı yok saymak değildir — konservatif davranıştır.
- Static TF: `base_link → camera_frame`, `base_link → lidar_frame`.
- Tüm testler rosbag ile saklanır.
- Simülasyon video teslim tarihi: 2026-06-23. Gerçek araç kampı: Temmuz–Ağustos 2026 (Bilişim Vadisi).
