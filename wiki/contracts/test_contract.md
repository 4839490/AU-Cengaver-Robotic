# Test Contract

Sources: `Perception_Planner_FSM_v1.4` §16; roadmap §8. Every test must be recorded with rosbag; ≥90% pass rate over 10 trials is the success criterion.

## Perception (T-XX)

| ID | Topic | Scenario | Expected |
|---|---|---|---|
| T-01 | `/perception/lane_model` | `lane_lost=true` | speed drop, NDT fallback |
| T-02 | `/perception/traffic_light_state` | RED valid: `RED+relevant=true+confirmed=true` | STOP_APPROACH |
| T-03 | `/perception/traffic_light_state` | GREEN valid: `GREEN+relevant=true+confirmed=true` | LANE_FOLLOW |
| T-04 | `/perception/traffic_light_state` | `GREEN+relevant=false` | log only, no decision |
| T-05 | `/perception/traffic_light_state` | `GREEN+confirmed=false` | hold, wait |
| T-06 | `/perception/traffic_light_state` | `STALE+in_stop_zone=true+last=GREEN` | drop to conservative |
| T-07 | `/perception/traffic_light_state` | `UNKNOWN+relevant=true+in_stop_zone=true` | wait or behave like RED |
| T-08 | `/perception/obstacle_tracks` | static obstacle TTC: `is_static=true, dist=5.4, ego=2.7 m/s` | `ttc≈2.0s → STOP_APPROACH` (TTC not inf) |
| T-09 | `/perception/obstacle_tracks` | dynamic obstacle: `velocity_x=0.5, ttc=3.5` | watch / prepare |
| T-10 | `/perception/obstacle_tracks` | PEDESTRIAN threshold: `class_label=PEDESTRIAN, ttc=2.5` | TTC threshold ×2 → STOP_APPROACH |
| T-11 | all | `valid_until_ms` exceeded | each topic's own fallback |
| T-12 | TF | `tf_static` stops | localization unable → STOP |
| T-13 | `/planning/active_route_context` | waypoint_id changes | `relevant_to_route` updated |

## FSM (F-XX)

| ID | Scenario | Expected |
|---|---|---|
| F-01/02 | `mission_active` toggle | false → no trajectory; true → trajectory begins |
| F-04/05/06 | `stop_reason` separation | `RED_LIGHT / OBSTACLE / LOK_LOST` distinguished |
| F-13 | timeout test | 600 ms drop → preserve, then STOP_APPROACH |

## Localization (L-XX)

| ID | Scenario | Expected |
|---|---|---|
| L-06/07 | two-stage timeout | 400 ms → speed drop, 1200 ms → STOP_APPROACH |
| L-10 | `ndt_healthy=false` | planner reduces speed |
| L-11 | `map_origin.locked=false` | planner does not process waypoints |

## Controller (C-XX)

| ID | Scenario | Expected |
|---|---|---|
| C-02 | trajectory timeout | > 1000 ms → safe full brake |
| C-07 | speed priority | `min(2.0, 3.0) = 2.0` applied |

## Integration (Tur-XX)

| ID | Scenario | Expected |
|---|---|---|
| Tur-1 | waypoint + park | all topics flow correctly, park succeeds |
| Tur-2 | traffic + dynamic obstacles | no light violation, no obstacle hit |
| Tur-3 | full scenario | pickup/dropoff + park completes |

## Fake-publisher example (T-08 static-obstacle TTC) — ILLUSTRATIVE

This snippet is illustrative, not a turn-key executable. The full T-08 scenario also requires a matching `/planning/active_route_context` publication so that the planner can compute `in_path=true` against `planned_trajectory`. Without the route context, a planner consuming this topic alone will not gate a `STOP_APPROACH` from the perception evidence below.

```bash
# Perception side — ego_speed = 2.7 m/s, distance = 5.4 → ttc ≈ 2.0 s (FINITE, not inf).
# Fields match perception_msgs/msg/ObstacleTrack as defined in
# wiki/contracts/message_contracts.md (no in_path field).
ros2 topic pub --once /perception/obstacle_tracks \
  perception_msgs/msg/ObstacleTracks \
  '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"},
    tracks: [{track_id: 1, class_label: 0, confidence: 0.8,
              position_x: 5.4, position_y: 0.0,
              distance: 5.4,
              velocity_x: 0.0, velocity_y: 0.0,
              ttc: 2.0,
              width: 0.5, length: 0.5, height: 1.0,
              is_static: true,
              source_sensor: "lidar_cluster",
              semantic_source: "none",
              geometry_source: "lidar",
              age_ms: 0, valid_until_ms: 200,
              warning_flags: []}]}'

# Companion route-context publication required for planner-side in_path=true:
ros2 topic pub --once /planning/active_route_context \
  planning_msgs/msg/ActiveRouteContext \
  '{header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"},
    active_waypoint_id: 1,
    target_x: 10.0, target_y: 0.0, target_heading: 0.0,
    planner_mode: 0,                       # AutonomyMode.LANE_FOLLOW
    route_direction: "STRAIGHT",
    planned_trajectory: [
      {x: 1.0, y: 0.0, z: 0.0},
      {x: 3.0, y: 0.0, z: 0.0},
      {x: 5.0, y: 0.0, z: 0.0},
      {x: 7.0, y: 0.0, z: 0.0}],
    lookahead_distance: 8.0,
    in_stop_zone: false, distance_to_stop_zone: 0.0,
    localization_confidence: 0.95,
    ego_speed_mps: 2.7,
    route_context_valid: true,
    age_ms: 0, valid_until_ms: 500}'

# Expected planner behavior with both topics: planner computes in_path=true
# from the trajectory that runs through (5.0, 0.0), then with ttc≈2.0 s the
# obstacle_tracks behavior table maps to STOP_APPROACH. With route context
# absent or stale, perception's ttc=2.0 alone is NOT sufficient.
```
