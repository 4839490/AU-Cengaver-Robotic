# stop_target_node

Sources: `Perception_Planner_FSM_v1.4` §11; roadmap §6.5.
Sprint 3 implementation: `wiki/implementation/sprint3_perception_integration_kickoff.md` §Track S.

## Topic

```
/perception/stop_target    perception_msgs/StopTarget
Hz: 10–20 | valid_until_ms: 300 | frame_id: base_link
Producer : stop_target_node
Consumers: planner_node, fsm_node
```

## Purpose

Aggregates stop evidence from multiple sources (traffic light, STOP sign, GeoJSON pickup/dropoff) into a single prioritized "where should the vehicle stop next" message. **Does not decide** to stop — emits evidence and a `priority`. Planner / FSM combine this with route context, mode, and TTC to actually act.

## Sprint 3 implementation status

| Gate | Status |
|---|---|
| **S3-S1** | ✅ **PASSED** (2026-05-13) — subscriber skeleton; subscribes to `/perception/traffic_light_state` and `/perception/traffic_signs`; publisher available on `/perception/stop_target` but NOT called in S3-S1; 33 ROS-free unit tests; 271 total colcon tests; forbidden topics: NONE; smokes A/B/C passed on Ubuntu 20.04 + ROS2 Foxy. |
| **S3-S2** | ✅ **PASSED** (2026-05-13, Codex-fixed 2026-05-13) — priority logic wired; `fake_traffic_light_state_pub` → RED+confirmed+relevant_to_route=True → StopTarget `target_type=0 priority=3 confidence=0.850 valid_until_ms=300 source=perception_only frame_id=base_link waypoint_id=-1`; smokes A–E PASS; forbidden topics: NONE; 285 tests, 0 failures. Codex fix: `build_stop_target_fields()` returns `None` (not clamped dict) when `evidence.age_ms + node_delta_ms > STOP_TARGET_VALID_UNTIL_MS`; node skips publish on `None`. Verified Ubuntu 20.04 + ROS2 Foxy 2026-05-13. |
| **S3-S3** | ✅ **PASSED** (2026-05-13) — verification + docs only; no code changes. Build: `colcon build --packages-select perception bringup` OK. Tests: 285/285 PASS (0 failures). Smokes A–D PASS (ROS_DOMAIN_ID isolation, Ubuntu 20.04 + ROS2 Foxy): (A) RED+confirmed+relevant_to_route=True → StopTarget type=0, priority=3, conf=0.850, valid_until_ms=300, source=perception_only, frame_id=base_link, waypoint_id=-1; (B) no-publisher → no StopTarget; (C) UNKNOWN+unconfirmed → no StopTarget; (D) topic list: /perception/stop_target + /perception/traffic_light_state + /perception/traffic_signs only — no /cmd_vel, /control/*, /beemobs/*. Static: no `warning_flags` on StopTarget anywhere; no empty/zero StopTarget published on no-evidence path. `git diff --check` clean. Track S complete. |

## Architecture mandate

`stop_target_node` is an **aggregator, not a decision maker.** It must never:
- Publish `/cmd_vel`, `/control/*`, `/beemobs/*`, or mode changes.
- Set `planner_mode` or modify autonomy mode.
- Compute `in_path` (planner-side).
- Decide whether the vehicle should stop.

**No-publish rule:** If no fresh upstream stop evidence exists, the node publishes **nothing**. Consumers rely on `valid_until_ms=300` expiry of the last published `StopTarget`. Publishing a message with `target_type=0` (default) on no-evidence would look identical to a real `TRAFFIC_LIGHT_STOP`.

## Inputs

| Topic | Message type | Role |
|---|---|---|
| `/perception/traffic_light_state` | `perception_msgs/TrafficLightState` | Primary: RED+confirmed → `TRAFFIC_LIGHT_STOP` |
| `/perception/traffic_signs` | `perception_msgs/TrafficSigns` | Signs: STOP+NEW/TRACKED → `STOP_SIGN` |
| `/planning/active_route_context` | `planning_msgs/ActiveRouteContext` | Optional: stop-zone gating, route relevance (wired in Track R). |

## Policy module — `stop_target_policy.py`

ROS-free module for freshness and evidence evaluation (testable without ROS):

| Function | Returns | Notes |
|---|---|---|
| `is_fresh(received_wall_s, now_wall_s, stale_ms)` | `bool` | Wall-clock freshness check |
| `evaluate_light_stop_evidence(...)` | `StopEvidence \| None` | None for all non-RED / stale / unconfirmed cases; `StopEvidence` for fresh confirmed RED |
| `has_stop_sign_evidence(signs, ...)` | `bool` | True if STOP sign is fresh **and** confirmed **and** valid age (per-sign `age_ms ≤ valid_until_ms`); missing fields → False |
| `build_stop_target_fields(evidence, now_age_ms)` | `dict \| None` | **Returns None** when `evidence.age_ms + now_age_ms > STOP_TARGET_VALID_UNTIL_MS`; node must skip publish on None. Returns field dict otherwise. |

`StopEvidence` policy object fields: `source_topic`, `target_type`, `priority`, `confidence`, `age_ms`, `distance_m`. **No `warning_flags` field** — `StopTarget.msg` contract §15 omits it.

**Combined-age validity rule (Codex fix):** `build_stop_target_fields()` returns `None` when the combined age (`evidence.age_ms` from the upstream message + `node_delta_ms` elapsed in the node since the last callback) exceeds `STOP_TARGET_VALID_UNTIL_MS=300`. Clamping stale evidence to 300ms and still publishing would produce a StopTarget that appears fresh but is backed by expired data. The node skips publish on `None`; the last real StopTarget expires naturally via `valid_until_ms=300` at the consumer.

**Sign evidence rule (after Codex fix):** A STOP sign is actionable only when the TrafficSigns wrapper is within `stale_ms`, AND `sign.type=STOP`, AND `sign.event_status ∈ {NEW, TRACKED}`, AND `sign.confirmed=True`, AND `sign.age_ms ≠ None`, AND `sign.valid_until_ms > 0`, AND `sign.age_ms ≤ sign.valid_until_ms`. `relevant_to_route` is NOT required in S3-S1 — route gating is deferred to S3-S2 / Track R.

## StopTarget field highlights

- `target_type`: `TRAFFIC_LIGHT_STOP=0 | STOP_SIGN=1 | PICKUP=2 | DROPOFF=3`.
- `priority`: `LOW=0 | NORMAL=1 | HIGH=2 | CRITICAL=3`.
- `source`: `"map_plus_perception"` when GeoJSON waypoint is involved, `"perception_only"` for purely sensed targets.
- `source_topic`: which perception topic produced the evidence (e.g. `/perception/traffic_light_state`).
- `waypoint_id`: GeoJSON node id for PICKUP / DROPOFF.
- `heading_at_stop`: ±10° tolerance.
- `required_stop_duration_ms`: 0 → wait for FSM signal; >0 → planner waits that long.
- `stop_reason_id`: debug id for matching with FSM `stop_reason`.
- **No `warning_flags` field** — contract §15 raw `.msg` omits it.
- **Geometry placeholder (S3-S2)**: `distance_from_front_bumper` mirrors `TrafficLightState.distance_to_stop` (currently 0.0 in `traffic_light_node` until route context is wired in S3-R4). `target_x = target_y = 0.0`. Planner must treat these as evidence placeholders until stop-line geometry from route context is available.

## Priority rules (S3-S2+)

| Condition | target_type | priority |
|---|---|---|
| `RED + confirmed=true + relevant_to_route=true` | `TRAFFIC_LIGHT_STOP` | `CRITICAL=3` |
| `RED + confirmed=true + relevant_to_route=false` | `TRAFFIC_LIGHT_STOP` | `HIGH=2` |
| `YELLOW + confirmed=true` | `TRAFFIC_LIGHT_STOP` | `NORMAL=1` |
| `STOP_SIGN + event_status=NEW/TRACKED` | `STOP_SIGN` | `HIGH=2` |
| Two targets simultaneously | highest priority wins |  |
| No fresh upstream evidence | **Do not publish.** | |

S3-S1: priority defaults to `HIGH` (relevant_to_route not yet wired from route context). S3-S2 upgrades to `CRITICAL` when `relevant_to_route=True`.

## Planner / FSM behavior (consumer)

| Condition | Action |
|---|---|
| `TRAFFIC_LIGHT_STOP + CRITICAL` | jerk-limited brake (STOP_APPROACH) |
| `STOP_SIGN + HIGH` | full stop, wait for FSM `COMPLETE` event |
| `PICKUP/DROPOFF + NORMAL` | 5 m before target → 3 km/h, right offset, verify `waypoint_id` |
| Two targets simultaneously | highest `priority` wins |
| `valid_until_ms` exceeded | cancel that stop point |

## Sample message (from contract)

```yaml
target_type: 0                  # TRAFFIC_LIGHT_STOP
distance_from_front_bumper: 8.6
target_x: 8.4
target_y: 0.1
priority: 3                     # CRITICAL
source_topic: "/perception/traffic_light_state"
```

## Cross-links

- Schema: [Message Contracts § StopTarget](../contracts/message_contracts.md)
- Light upstream: [traffic_light_node](traffic_light_node.md)
- Sign upstream: [traffic_sign_node](traffic_sign_node.md)
- Sprint 3 Track S: [sprint3_perception_integration_kickoff](../implementation/sprint3_perception_integration_kickoff.md)
