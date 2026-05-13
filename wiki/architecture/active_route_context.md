# Active Route Context (Planner → Perception)

Sources: `Perception_Planner_FSM_v1.4` §1, §4 (FIX-2, FIX-3, FIX-2.5, FIX-2.6); roadmap §5.1.

## Purpose

Perception cannot reason about "is this stop sign on my route?" or "what's my closing speed for TTC?" without ego speed and route bookkeeping. The planner publishes `/planning/active_route_context` so perception can:

- Mirror `in_stop_zone` and `relevant_to_route` from the planner's source-of-truth values into perception's outgoing messages.
- Compute the scalar closing-speed TTC for `obstacle_tracks` using `ego_speed_mps` (still using `distance_from_front_bumper` as the path-distance proxy per contract §6 MVP rule). Perception does **not** compute `in_path` and does **not** re-project onto the planned trajectory; that is planner-side. See [Perception ↔ Planner / FSM Contract](../contracts/perception_planner_fsm_contract.md) and [Message Contracts § TTC ownership](../contracts/message_contracts.md).
- Get junction context (`route_direction`) when `/perception/junction` is not implemented.
- Stay conservative when context is stale or missing.

`planned_trajectory` is included in this message so perception can optionally use it for richer telemetry / debug, but path-gating decisions stay planner-side.

## Topic

```
Topic     : /planning/active_route_context
Frame     : base_link  (target_x/y, planned_trajectory[] — base_link)
Frequency : 10 Hz   (min 8 Hz)
valid_until_ms : 500 ms
```

## Required fields (FIX-3)

| Field | Type | Notes |
|---|---|---|
| `header` | `std_msgs/Header` | `frame_id = base_link` |
| `active_waypoint_id` | `uint32` | GeoJSON node ID |
| `target_x`, `target_y` | `float32` | base_link (m) |
| `target_heading` | `float32` | rad |
| `planner_mode` | `uint8` | **`common_msgs/AutonomyMode` constant — NOT a string** |
| `route_direction` | `string` | `STRAIGHT \| LEFT \| RIGHT \| ROUNDABOUT \| UNKNOWN` |
| `planned_trajectory[]` | `geometry_msgs/Point[]` | base_link, used by planner-side `in_path` calc |
| `lookahead_distance` | `float32` | m |
| `in_stop_zone` | `bool` | vehicle currently inside an active stop zone? |
| `distance_to_stop_zone` | `float32` | m |
| `localization_confidence` | `float32` | EKF confidence |
| `ego_speed_mps` | `float32` | sourced from `/controller/feedback.actual_speed`. **TTC source on perception side.** |
| `route_context_valid` | `bool` | `Localization OK + waypoint active + planner ACTIVE` → `true`; else perception must NOT claim relevance, must add `ROUTE_CONTEXT_MISSING` warning flag |
| `age_ms` | `uint32` | message age. `>200ms` → `relevant_to_route=false` |
| `valid_until_ms` | `uint32` | 500ms; if exceeded, perception treats `route_context_valid=false` |

## Timestamp rule (FIX-2)

- `age_ms > 200` → perception sets `relevant_to_route=false` and adds `STALE_MESSAGE` warning flag.
- `route_context_valid=false` → perception still publishes evidence but sets `relevant_to_route=false`. **It is not "ignore perception"; it is "stay conservative".** Planner must approach controlled even if ışık state=RED with `route_context_valid=false` (ışık tamamen etkisiz KALMAZ — hız düşür).

## Flow for `ego_speed_mps`

```
/controller/feedback.actual_speed → planner_node → /planning/active_route_context.ego_speed_mps → perception TTC
```

Perception MUST NOT subscribe to `/controller/feedback` directly.

## Fake publisher for Sprint 3 Track R

`fake_route_context_pub` (S3-R1) is a test helper that publishes `ActiveRouteContext` at 10 Hz without a real planner. Used to exercise S3-R2/R3/R4 wiring (TTC, stale behavior, traffic light route context). Default values come from `route_context_utils.DEFAULTS` — single source of truth shared with the ROS-free helper and its unit tests.

```bash
# Default run (ego_speed_mps=0.0, route_context_valid=true, age_ms=0)
ros2 run perception fake_route_context_pub

# Ego moving at 2.7 m/s, stale context, in stop zone
ros2 run perception fake_route_context_pub \
  --ros-args -p ego_speed_mps:=2.7 -p age_ms:=600 -p in_stop_zone:=true

# Invalid context (forces ROUTE_CONTEXT_MISSING behavior in consumers)
ros2 run perception fake_route_context_pub \
  --ros-args -p route_context_valid:=false
```

Node does NOT subscribe to anything and does NOT publish to forbidden topics.

## Failure modes / warning flags

| Condition | Perception action |
|---|---|
| topic missing > 500 ms | conservative: `relevant_to_route=false`, `ROUTE_CONTEXT_MISSING` |
| `age_ms > 200` | `relevant_to_route=false`, `STALE_MESSAGE` |
| `route_context_valid=false` | as above; do NOT discard detections |
| `localization_confidence` low | reduce TTC confidence claims |
