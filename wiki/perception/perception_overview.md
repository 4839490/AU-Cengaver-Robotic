# Perception Overview

Sources: `Perception_Planner_FSM_v1.4` §1, §2; roadmap §6.5; team notes.

## Mandate

Perception describes the scene. It does not steer, brake, or pick targets. Every output is timestamped, confidence-scored, route-context-aware evidence with bounded validity (`valid_until_ms`). Planner / FSM consume that evidence and decide.

## Node graph

```
                                  /planning/active_route_context (10 Hz, base_link)
                                              │
                                              ▼
   ZED2 ─▶ traffic_light_node ─▶ /perception/traffic_light_state (10–30 Hz)
                ─▶ traffic_sign_node ─▶ /perception/traffic_signs (10–30 Hz)
                ─▶ lane_node ─▶ /perception/lane_model (20–30 Hz)
                ─▶ junction_node (Phase-2) ─▶ /perception/junction (10 Hz)
   VLP-16 ─▶ lidar_obstacle_node ─┐
                                  ├─▶ fusion_node ─▶ /perception/obstacle_tracks (20 Hz)
   camera semantic ───────────────┘
   light + sign + map waypoints ─▶ stop_target_node ─▶ /perception/stop_target (10–20 Hz)
   all of the above ─▶ perception_diagnostics_node ─▶ /perception/diagnostics (1–2 Hz)
```

## MVP order (do not skip steps)

1. Message packages (`common_msgs`, `perception_msgs`, etc.) build cleanly.
2. Empty `perception` package skeleton + launch file.
3. Dummy publishers producing contract-shaped messages (so planner/FSM can integrate).
4. Static TF: `base_link → camera_frame`, `base_link → lidar_frame`.
5. `perception_diagnostics_node` (input_hz / output_hz / latency / mean_confidence).
6. `traffic_light_node` MVP (YOLO bbox + HSV ROI + 3-frame confirm).
7. `lane_node` MVP (centerline / lane_lost / confidence — UFLD comes later).
8. `lidar_obstacle_node` MVP (RANSAC ground + Euclidean cluster + Centroid Kalman, classical first; PointPillars is NOT MVP).
9. `stop_target_node`.
10. Integration tests with rosbag / Gazebo.

Then layer in real algorithms (UFLD v2 + TensorRT, YOLOv8n FP16, fusion, junction node).

## Per-node pages

- [traffic_light_node](traffic_light_node.md)
- [traffic_sign_node](traffic_sign_node.md)
- [lane_node](lane_node.md)
- [lidar_obstacle_node](lidar_obstacle_node.md)
- [stop_target_node](stop_target_node.md)
- [junction_node](junction_node.md) — Phase-2
- [perception_diagnostics_node](perception_diagnostics_node.md)

## Cross-links

- [Perception ↔ Planner / FSM Contract](../contracts/perception_planner_fsm_contract.md)
- [Active Route Context](../architecture/active_route_context.md)
- [Timing & Fallback](../contracts/timing_and_fallback.md)
- [Test Contract](../contracts/test_contract.md)
