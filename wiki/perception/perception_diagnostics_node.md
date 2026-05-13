# perception_diagnostics_node

Source: `Perception_Planner_FSM_v1.4` §13.

## Topic

```
/perception/diagnostics    perception_msgs/PerceptionDiagnostics
Hz: 1–2 | valid_until_ms: 2000 | frame_id: —
Producer : every perception node publishes its own diagnostics under this topic
Consumers: debugger, supervisor, fsm_node
```

## Purpose

Single channel to monitor perception health. Each perception node fills `node_name` and reports its own metrics. The FSM and safety supervisor use this to decide when to demand a `STOP_APPROACH`.

## Field summary

| Field | Notes |
|---|---|
| `node_name` | `traffic_light_node \| lane_node \| lidar_obstacle_node \| sign_node \| stop_target_node \| junction_node \| fusion_node` |
| `input_hz` | sensor input frequency observed by the node |
| `output_hz` | message output frequency |
| `latency_ms` | end-to-end node latency |
| `last_msg_age_ms` | freshness of last successful publication |
| `mean_confidence` | rolling mean over recent outputs |
| `num_outputs` | message count |
| `gpu_utilization` | RTX 3060 utilization (0..1) |
| `warning_flags` | union of standard flag set |

## FSM action mapping

| Condition | Planner / FSM action |
|---|---|
| `NO_INPUT > 500ms` | immediate STOP_APPROACH |
| `TF_MISSING` | STOP_APPROACH |
| `HIGH_LATENCY > 200ms` | treat that topic as stale |
| `LOW_OUTPUT_HZ < 10Hz` (3 cycles) | STOP_APPROACH |
| `gpu_utilization > 0.90` | warn FSM about latency risk |

## Cross-links

- [Timing & Fallback](../contracts/timing_and_fallback.md) for valid_until / Hz reference.
- [Message Contracts § PerceptionDiagnostics](../contracts/message_contracts.md).
