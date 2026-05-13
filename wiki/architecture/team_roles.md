# Team Roles

Source: `raw/team_notes/team_roles.md`; roadmap §10.

| Person | Primary | Secondary |
|---|---|---|
| Yusuf Aydın | Perception lead — YOLOv8n, UFLD v2, ZED2, LiDAR pipeline, perception contract | TensorRT optimization |
| Melih Mert Korkmaz | Perception support — image processing, dataset, TensorRT FP16 | Fusion node |
| Ahmet Salih Uluşık | Localization + Planner — global/local EKF, GeoJSON, planner core | Obstacle avoidance, coord conversion |
| Murat Üsame Üstün | FSM — mode transitions, guard conditions, mission management | Decision logic |
| Muhammed Durmaz | Controller — Stanley/PID/Ackermann, CAN-Bus 0x560 | `vehicle_params.yaml`, park control |
| Muhammed Talha | Gazebo simulation, URDF model | System validation |
| Orhan | ROS2 integration, sensor tests, video / report packaging | Simulation scenario management |

## Module ↔ owner quick map

- `common_msgs` / `fsm_msgs` / `localization_msgs` / `perception_msgs` / `planning_msgs` — whole team builds together (Step 1, 1–2 hours).
- `vehicle_params.yaml` — Durmaz.
- `simulation/` — Talha + Orhan.
- `perception/` — Aydın + Korkmaz.
- `localization/`, `planner/` — Uluşık.
- `fsm/` — Üstün.
- `controller/`, `can_interface/` — Durmaz.

Update this page if responsibilities shift.
