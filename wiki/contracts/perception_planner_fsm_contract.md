# Perception ↔ Planner / FSM Contract (v1.4)

Source: `raw/final_contracts/Perception_Planner_FSM_v1.4_FINAL_DUZELTILMIS.pdf`. Owners: Algılama — Yusuf Aydın / Melih Korkmaz; Planner — Ahmet Salih Uluşık.

This page is the **structural summary** of the contract. Per-topic detail lives in [Message Contracts](message_contracts.md), [Timing & Fallback](timing_and_fallback.md), and individual perception node pages.

## Core principle

> Perception karar vermez, durum bildirir. Tüm mesajlar temporal filtre + güven skoru + rota bağlamı içeren teyitli olay bilgisidir.
> *Perception does not decide — it reports state. Every message is confirmed event evidence with temporal filter + confidence + route context.*

## Common rules (apply to every perception topic)

- Mandatory header fields: `header.stamp`, `header.frame_id`, `confidence`, `valid_until_ms`.
- `frame_id = base_link` for all coordinates.
- Distance fields use `distance_from_front_bumper` — front-bumper-referenced scalar (not per-coordinate).
- TTC formula (FIX-2.1): `ttc = distance_along_path / max(closing_speed, ε)` with ε = 0.001. **Static obstacles get a finite scalar TTC** (perception treats `is_static=true` as `closing_speed = ego_speed`); `closing_speed ≤ 0` → `ttc = inf`. Perception does **not** know `in_path`; the planner is responsible for path-gating the resulting action. See [Message Contracts § TTC ownership and computation](message_contracts.md).
- GREEN light decision is conditional like RED: requires `relevant_to_route=true` AND `confirmed=true` (FIX-2.2).
- STALE light: must track `last_state`. STALE+`in_stop_zone=true`+`last_state=GREEN` → drop to conservative (no aggressive continue) (FIX-2.3).
- `/perception/junction` is OPTIONAL in MVP — junction context is taken from `active_route_context.route_direction` (FIX-2.5).
- Active route context staleness: `age_ms > 200` → `relevant_to_route=false`; `route_context_valid=false` → do not assert relevance (FIX-2 timestamp rule).
- Planner mode is `uint8` from `common_msgs/AutonomyMode` — never a string (FIX-3).

## Topic registry (MVP-required marked ✓)

| Topic | Hz | Producer | frame_id | MVP |
|---|---|---|---|---|
| `/perception/lane_model` | 20–30 | `lane_node` | `base_link` | ✓ |
| `/perception/traffic_light_state` | 10–30 | `traffic_light_node` | `base_link` | ✓ |
| `/perception/traffic_signs` | 10–30 | `traffic_sign_node` | `base_link` | ✓ |
| `/perception/obstacle_tracks` | 20 | `lidar_obstacle_node + fusion_node` | `base_link` | ✓ |
| `/perception/stop_target` | 10–20 | `stop_target_node` | `base_link` | ✓ |
| `/perception/junction` | 10 | `junction_node` | `base_link` | optional (Phase-2) |
| `/perception/diagnostics` | 1–2 | all perception nodes | — | ✓ |
| `/planning/active_route_context` | 10 | `planner_node` | `base_link` | ✓ |

## Responsibility split (who computes what)

| Concept | Perception | Planner |
|---|---|---|
| Obstacle position / size / velocity | ✓ (`position_x/y`, `width/length/height`, `velocity_x/y`) | — |
| Per-track scalar TTC evidence (closing-speed based) | ✓ — formula in [Message Contracts § ObstacleTrack](message_contracts.md). Uses `distance_from_front_bumper` as a scalar proxy for `distance_along_path` per contract §6 (MVP) | — |
| Path-relative TTC / final action gating | ✗ | ✓ — re-projects onto `planned_trajectory` if needed; gates action by `in_path` |
| `in_path` | ✗ — **not a perception field** | ✓ — computed from `/planning/active_route_context.planned_trajectory` and `/planning/trajectory` |
| `bypass_possible` | ✗ | ✓ — uses lane + obstacle dimensions |
| `relevant_to_route` (light/sign) | populates the boolean field, but the truth is derived planner-side | ✓ — `active_route_context` is the source of truth |
| `in_stop_zone` | mirrors the value from `active_route_context` for STALE behavior | ✓ — owns the value |
| STALE `last_state` tracking | ✓ publishes last valid state | ✓ planner also remembers |

## Velocity-dependent braking (planner side)

Perception only delivers `distance` and TTC. Planner decides:
```
emergency_distance = max(0.3, v_mps * 0.3 + 0.2)
if planner_in_path and (distance < emergency_distance or ttc < 2.0):
    request full brake from controller
```

## Standard `warning_flags` set

`NO_INPUT | LOW_OUTPUT_HZ | HIGH_LATENCY | LOW_CONFIDENCE | STALE_MESSAGE | TF_MISSING | SYNC_MISMATCH | MODEL_ERROR | CONFLICT_STATE | CLUSTER_SPLIT | LANE_BOUNDARY_MISSING | BBOX_MISSING | ROUTE_CONTEXT_MISSING`

## Activation gate (contract checklist §17 — paraphrased)

The contract is "active" only after all of these hold:
- All `perception_msgs` `.msg` files build cleanly.
- `tf_static` for `base_link → camera_frame` and `base_link → lidar_frame` is launched.
- `traffic_light_state` produces `confirmed` (3-frame), `relevant_to_route` from route context, and `in_stop_zone`.
- `traffic_signs` runs `event_status` + `event_memory_ttl_ms`.
- `lane_model` centerline points spaced ≤ 0.1 m, `lane_lost` populated.
- `obstacle_tracks` uses closing-speed TTC; static obstacles in path produce **finite** TTC. **No `in_path` field.**
- `stop_target` populates `priority`, `stop_reason_id`, `source_topic`.
- `/perception/junction` is optional in MVP.
- Diagnostics produces `gpu_utilization` and full `warning_flags`.
- Localization owns the TF tree (Controller does not).
- Planner publishes `active_route_context` 10 Hz, base_link, with `in_stop_zone`.
- Planner enforces `relevant_to_route=true + confirmed=true` for GREEN gate.
- Planner tracks STALE last_state; STALE + `in_stop_zone=true` + `last_state=GREEN` → conservative.
- Planner computes `in_path` via `planned_trajectory`.
- All test scenarios T-01..T-13 are recorded with rosbag.

## Cross-links

- Field-level definitions: [Message Contracts](message_contracts.md)
- Hz / valid_until / fallback per topic: [Timing & Fallback](timing_and_fallback.md)
- Per-node responsibilities: see [Perception Overview](../perception/perception_overview.md)
- Planner→Perception side: [Active Route Context](../architecture/active_route_context.md)
- Test grid: [Test Contract](test_contract.md)
