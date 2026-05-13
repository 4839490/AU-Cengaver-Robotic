# TF Standard

Sources: `Perception_Planner_FSM_v1.4` §3 (FIX-2.6); `AU_Cengaver_GANG_Yol_Haritasi` §1.1, §6.1; `raw/team_notes/meeting_decisions.md`.

## Frame tree (mandatory direction)

```
map ──▶ odom ──▶ base_link ──▶ camera_frame
                            └─▶ lidar_frame
```

Do **not** reverse any edge — not in code, comments, launch files, tests, or wiki.

## Ownership

| Edge | Producer | Mechanism | Failure → |
|---|---|---|---|
| `base_link → camera_frame` | `perception_bringup` / `static_tf` | `tf2_ros static_transform_publisher` (kalibrasyon) | `STALE_MESSAGE` / `TF_MISSING` → STOP |
| `base_link → lidar_frame`  | `perception_bringup` / `static_tf` | `tf2_ros static_transform_publisher` | `TF_MISSING` → STOP |
| `odom → base_link`         | `local_ekf_node` (Localization) | dynamic, IMU + wheel encoder EKF, ~50 Hz | odometri kesilince STOP |
| `map → odom`               | `global_localization_node` (Localization) | dynamic, NDT-LIO-SAM | EKF/IMU dominant fallback |

Controller **consumes** TF; it does not produce any. Perception consumes `odom → base_link` only when fusing time-aligned data — perception output stays in `base_link`.

## Static TF launch (sensor extrinsics from BEE1 docs)

BEE1 sensor positions (ön aks merkezine göre, mm) — see [BEE1 Platform](../vehicle/bee1_platform.md):

| Sensor | X (mm) | Y (mm) | Z (mm) |
|---|---|---|---|
| LIDAR (VLP-16) | -177 | 0 | +620 |
| Right camera (ZED2) | -205 | +60 | +685 |
| Left camera (ZED2) | -205 | -60 | +685 |
| GPS/IMU (Xsens MTI-680) | +1440 | 0 | +1390 |

> ⚠️ The contract example (`base_link camera_frame: 0.5 0.0 0.8`) is illustrative — measure on the real BEE1 and put exact extrinsics in `bringup/launch/static_tf.launch.py` and `vehicle_params.yaml`. `base_link` origin is on the front axle midpoint per BEE1 documentation; pick a fixed convention and stick with it.

## Coordinates rule

- All perception topic outputs: **`base_link`** (`frame_id: base_link`).
- All distances on perception topics: **`distance_from_front_bumper`** (skaler, m).
- Planned trajectory (`/planning/trajectory`): **`map`** frame.
- `active_route_context.target_x/y, target_heading, planned_trajectory[]`: **`base_link`** frame (so perception can compute TTC / in_stop_zone in its own frame).

## What goes wrong if TF breaks

- `tf_static` not published → `TF_MISSING` warning flag → planner triggers `STOP_APPROACH`.
- `odom → base_link` interrupted (EKF/IMU/encoder loss) → `localization/status` degrades → STOP.
- `map → odom` lost (NDT/GNSS lost) → conservative IMU-dominant fallback for tunnel / GPS gap; localization status degrades.
