# traffic_sign_node

Sources: `Perception_Planner_FSM_v1.4` §9; roadmap §6.5.

## Topic

```
/perception/traffic_signs    perception_msgs/TrafficSigns
Hz: 10–30 | valid_until_ms: 1000 | frame_id: base_link
Producer : traffic_sign_node (YOLOv8n + TensorRT FP16)
Consumer : fsm_node, planner_node
```

## Algorithm

1. YOLOv8n detects sign boxes with class probability.
2. 3-frame temporal confirmation → `confirmed=true`.
3. Per-sign `event_status` state machine: `NEW=0 → TRACKED=1 → ALREADY_HANDLED=2 → STALE=3`.
4. `event_memory_ttl_ms` (default 5000 ms) prevents the same sign id from re-firing as `NEW` after it was handled.
5. `relevant_to_route` is derived planner-side from `active_route_context`.

## Type enum (canonical from `.msg`)

```
UNKNOWN_SIGN=0  STOP=1  SPEED_LIMIT=2  NO_ENTRY=3
MANDATORY_LEFT=4  MANDATORY_RIGHT=5  MANDATORY_STRAIGHT=6
MANDATORY_LEFT_STRAIGHT=7  MANDATORY_RIGHT_STRAIGHT=8
ROUNDABOUT=9  PARKING=10  NO_PARKING=11
TUNNEL=12  PEDESTRIAN_CROSSING=13
```

> Contract section 9 prose lists a partial set; the `.msg` is canonical.

## Planner / FSM behavior (consumers — for reference, not perception logic)

This node only publishes evidence. The behaviors below are how planner / FSM / localization consume that evidence. None of them is a perception "mode" or "switch".

| Sign + status | Planner / FSM / localization response |
|---|---|
| `STOP + NEW + relevant=true + confirmed=true` | Planner enters `STOP_APPROACH` (autonomy mode) until FSM emits `SIGN_HANDLED`. |
| `NO_ENTRY` | Planner drops that intersection arm from waypoint candidates. |
| `MANDATORY_* + NEW + relevant=true` | Planner forces that direction at the upcoming junction (still uses normal autonomy modes; junction handling is route-level, not a mode). |
| `ROUNDABOUT` | Planner uses the roundabout entry/exit policy described in `wiki/perception/junction_node.md`. **No new autonomy mode** — the AutonomyMode value remains `LANE_FOLLOW`; route geometry is sourced from `active_route_context.route_direction` and the planner's roundabout policy. |
| `TUNNEL` | Localization switches its weighting to IMU-dominant; planner sets `TargetSpeed.reason = TUNNEL` with a 10 km/h cap. **Not** an autonomy mode. The vehicle stays in `LANE_FOLLOW`. |
| `NO_PARKING` | Planner marks that parking slot as `available=false` in its parking candidate list. |
| `event_status = ALREADY_HANDLED` | Consumers do not produce a new decision for this `sign_id`. |
| `event_status = STALE` or `valid_until_ms` exceeded | Consumers ignore. |

> Perception never "switches mode", "enters tunnel mode", or "starts roundabout handling". It publishes type + status + confidence + relevance and lets planner / FSM / localization act.

## Warning flags

`LOW_CONFIDENCE | STALE_MESSAGE | BBOX_MISSING`

## Cross-links

- Schema: [Message Contracts § TrafficSign](../contracts/message_contracts.md)
- TUNNEL/JUNCTION are NOT modes: [System Overview](../architecture/system_overview.md)
