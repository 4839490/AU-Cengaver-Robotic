# Timing and Fallback Reference

Source: `Perception_Planner_FSM_v1.4` §14.

| Topic | Target Hz | Min Hz | `valid_until_ms` | Fallback when stale | Critical flag |
|---|---|---|---|---|---|
| `/perception/lane_model` | 20–30 | 15 | 500 | drop speed immediately → 0.5–1 s NDT → STOP_APPROACH | `NO_INPUT` |
| `/perception/traffic_light_state` | 10–30 | 10 | 300 | STALE → conservative on last_state | `NO_INPUT` |
| `/perception/traffic_signs` | 10–30 | 10 | 1000 | count `STALE_MESSAGE` | `NO_INPUT` |
| `/perception/obstacle_tracks` | 20 | 15 | 200 | behave as if obstacle present | `NO_INPUT` |
| `/perception/stop_target` | 10–20 | 10 | 300 | hold last point → cancel | `LOW_OUTPUT_HZ` |
| `/perception/junction` | 10 | 8 | 500 | optional — fallback to `route_direction` | `LOW_OUTPUT_HZ` |
| `/perception/diagnostics` | 1–2 | 0.5 | 2000 | stale warning | `STALE_MESSAGE` |
| `/planning/active_route_context` | 10 | 8 | 500 | `relevant_to_route=false` (conservative) | `STALE_MESSAGE` |

## Universal fallback

- `lane_model` interrupted → drop speed immediately → 0.5–1 s NDT → STOP_APPROACH.
- `traffic_light_state` interrupted → STALE based on last state, conservative.
- `obstacle_tracks` interrupted → assume obstacle present (planner brakes).
- `active_route_context` interrupted → `relevant_to_route=false` (conservative, not "ignore perception").
- Diagnostics `NO_INPUT` or `TF_MISSING` → planner triggers immediate STOP_APPROACH.

## Diagnostics → planner action table

| Condition | Planner / FSM action |
|---|---|
| `NO_INPUT > 500ms` | STOP_APPROACH immediately |
| `TF_MISSING` | STOP_APPROACH |
| `HIGH_LATENCY > 200ms` | treat that topic as stale |
| `LOW_OUTPUT_HZ < 10Hz` | 3 cycles → STOP_APPROACH |
| `gpu_utilization > 0.90` | warn FSM about latency risk |

## Standard `warning_flags`

```
NO_INPUT | LOW_OUTPUT_HZ | HIGH_LATENCY | LOW_CONFIDENCE |
STALE_MESSAGE | TF_MISSING | SYNC_MISMATCH | MODEL_ERROR |
CONFLICT_STATE | CLUSTER_SPLIT | LANE_BOUNDARY_MISSING |
BBOX_MISSING | ROUTE_CONTEXT_MISSING
```
