# junction_node — OPTIONAL (Phase-2)

Source: `Perception_Planner_FSM_v1.4` §12 (FIX-2.5).

## Topic

```
/perception/junction    perception_msgs/Junction
Hz: 10 | valid_until_ms: 500 | frame_id: base_link
Producer : junction_node (camera-based, Phase-2)
Consumers: planner_node, fsm_node
```

## MVP rule

**This topic is optional in the MVP.** When the topic is not published, the planner derives junction context from `/planning/active_route_context.route_direction` (`STRAIGHT | LEFT | RIGHT | ROUNDABOUT | UNKNOWN`).

Implement this node only after the rest of perception is stable.

## Purpose (when implemented)

Produces a *visual* junction hint:
- `detected: bool` — visual junction is in front.
- `junction_type`: `NORMAL=0 | ROUNDABOUT=1`.
- `arm_count`: number of intersection arms.
- `distance_to_entry`: front-bumper-referenced scalar (m).
- `confidence`.

## Planner / FSM behavior (consumers — not perception logic)

Perception only reports `detected`, `junction_type`, `arm_count`, `distance_to_entry`, and `confidence`. The behaviors below are planner-side responses; this node never picks an autonomy mode and never "starts handling". `JUNCTION` is **not** an autonomy mode (contract §1, roadmap §11) — it is route context plus a `TargetSpeed.reason` value.

| Evidence | Planner response |
|---|---|
| `detected=true + distance_to_entry < 10 m` | Planner sets `TargetSpeed.reason = JUNCTION` with ~10 km/h cap; selects junction policy using `active_route_context.route_direction`. AutonomyMode stays `LANE_FOLLOW`. |
| `junction_type = ROUNDABOUT` | Planner applies its roundabout policy (counter-clockwise entry, min-bearing exit). Still no new autonomy mode. |
| `detected=false` | Planner runs normal `LANE_FOLLOW`. |
| Topic not published (MVP) | Planner falls back to `active_route_context.route_direction`. |
| `valid_until_ms` exceeded | Consumers behave as if `detected=false`. |

## Warning flags

`LOW_CONFIDENCE | STALE_MESSAGE`

## Cross-links

- Active route context fallback: [Active Route Context](../architecture/active_route_context.md)
- JUNCTION is not a mode — see [System Overview](../architecture/system_overview.md) hard rules.
