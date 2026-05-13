# traffic_light_node

Sources: `Perception_Planner_FSM_v1.4` §8; roadmap §6.5; team notes; Sprint 1 implementation (2026-05-12).

## Topic

```
/perception/traffic_light_state    perception_msgs/TrafficLightState
Hz: 10–30 | valid_until_ms: 300 | frame_id: base_link
Producer : traffic_light_node
Consumer : fsm_node, planner_node
```

## MVP status (Sprint 1 — COMPLETE; S3-R4 route context wiring — ✅ PASSED 2026-05-13)

Sprint 1 delivers a fully functional pipeline using a bbox stub and pure-Python classifier. S3-R4 wires route context. Production YOLO/TensorRT inference is a Phase 2 item.

| Component | Status | Phase 2 (future) |
|---|---|---|
| Bbox detection | YOLO stub — configurable fixed rectangle | Real YOLOv8n FP16 via TensorRT |
| Colour classifier | Pure-Python channel-dominance ROI (`colour_classifier.py`) | Same or HSV-space upgrade |
| Temporal filter | 3-frame `TemporalFilter` (`temporal_filter.py`) | Same |
| Route context | **S3-R4**: subscribed to `/planning/active_route_context`; `route_context_apply_utils.py` | — |

## Algorithm (MVP — current implementation)

1. **Image subscriber** — subscribes to `/zed2/left/image_raw` (`sensor_msgs/Image`).
2. **YOLO bbox stub** — when `use_yolo_stub=true` and `stub_bbox_enabled=true`, returns the configured fixed rectangle `(stub_bbox_x, stub_bbox_y, stub_bbox_w, stub_bbox_h)`. If `use_yolo_stub=false` or `stub_bbox_enabled=false`, no bbox → UNKNOWN + BBOX_MISSING. The `model_path` parameter wires the future real-model path; if the path is empty or absent, the node logs INFO and continues with the stub only.
3. **Pure-Python ROI classifier** (`colour_classifier.py`) — samples average channel values inside the bbox ROI. Classification priority: YELLOW (r>0.3 AND g>0.3 AND b<0.25), RED (r_ratio>0.5 AND r>1.5×g AND r>1.5×b), GREEN (g_ratio>0.5 AND g>1.5×r AND g>1.5×b). Confidence capped at 0.85. Supports `bgr8` and `rgb8` encodings; `step` respected for padded rows. `confidence < 0.7` → UNKNOWN + LOW_CONFIDENCE.
4. **3-frame temporal filter** (`temporal_filter.py`) — accumulates per-frame classifications. `confirmed=True` after `confirm_frames` consecutive non-UNKNOWN observations of the same state. Frame deduplication via `header.stamp` so the publish timer (10 Hz) never double-counts the same image. `state_memory_ms` (default 500 ms) caps the gap between qualifying frames before filter resets.
5. **Pre-confirmation evidence** — before `confirm_frames` frames, the observed state (e.g. RED) is published with `confirmed=False`. Planner/FSM must not act on `confirmed=False` (contract behavior table). This gives the planner visibility into sensor output without triggering driving actions.
6. **Publish loop** — three image-availability cases per tick:
   - Case 1 (no image ever received): `state=UNKNOWN`, flags=[LOW_CONFIDENCE, NO_INPUT], `confirmed=False`, filter reset.
   - Case 2 (image stale > `image_stale_ms`): `state=STALE`, flags=[LOW_CONFIDENCE, STALE_MESSAGE], `confirmed=False`, filter reset.
   - Case 3 (fresh image): run classifier → temporal filter → publish result.

## State semantics

- `state ∈ { UNKNOWN=0, RED=1, YELLOW=2, GREEN=3, STALE=4, CONFLICT=5 }`.
- `confidence < 0.7` → publish UNKNOWN, do NOT claim a colored state.
- `confirm_frames` (default 3) consecutive frames agreement → `confirmed=true`.
- `STALE` = image was received previously but the most recent exceeds `image_stale_ms`. Filter resets; `confirmed=False` guaranteed.
- `UNKNOWN` = no image ever received, or classifier confidence too low, or bbox missing.

## `image_stale_ms` and validity window

`image_stale_ms` (default 300 ms) is the wall-clock age threshold after which the node transitions to `state=STALE`. It is **clamped** to `valid_until_ms=300` at startup via `resolve_stale_ms()` in `stale_utils.py` — this ensures stale evidence never outlives its validity window. If the configured value exceeds 300 ms or is ≤ 0, a WARN is logged and the effective threshold is 300 ms.

## Route-context fields (S3-R4 — implemented and verified)

`traffic_light_node` subscribes to `/planning/active_route_context` (`planning_msgs/ActiveRouteContext`) and derives route fields per tick via `route_context_apply_utils.apply_route_context_to_light()`.

### Context usability rule

A context message is usable when **all** hold:

- latest context exists (callback has fired at least once)
- `route_context_valid == True`
- `valid_until_ms > 0`
- `age_ms <= valid_until_ms`
- wall-clock elapsed since callback `<= valid_until_ms`

The `valid_until_ms` window follows the `ActiveRouteContext` contract default: **500 ms**.

### Output when context usable

```python
msg.relevant_to_route = True
msg.in_stop_zone      = active_route_context.in_stop_zone
msg.distance_to_stop  = active_route_context.distance_to_stop_zone
# ROUTE_CONTEXT_MISSING removed from warning_flags if previously present
```

### Output when context missing / stale / invalid / zero-validity

```python
msg.relevant_to_route = False
msg.in_stop_zone      = False
msg.distance_to_stop  = 0.0
# ROUTE_CONTEXT_MISSING added to warning_flags once
```

### Warning flag rules

- `ROUTE_CONTEXT_MISSING` is **additive** — added to the existing image-pipeline flag list; never replaces `NO_INPUT`, `STALE_MESSAGE`, `LOW_CONFIDENCE`, `BBOX_MISSING`, etc.
- Duplicate `ROUTE_CONTEXT_MISSING` entries are prevented (`add_warning_flag_once`).
- When context becomes usable again, `ROUTE_CONTEXT_MISSING` is removed and other flags are preserved.

Planner/FSM must treat `relevant_to_route=False` as "unknown relevance" and apply conservative gating.

## GREEN gate (FIX-2.2)

GREEN must NOT mean "go" by itself. Planner accepts only `state=GREEN + relevant_to_route=true + confirmed=true`. Anything else is "log only" or "wait". During Sprint 1, `relevant_to_route=False` always, so no GREEN-based action is triggered — this is intentional and safe.

## STALE behavior (FIX-2.3)

| Condition | Action |
|---|---|
| `STALE + last_state ∈ {RED,YELLOW} + in_stop_zone=true` | conservative — wait safely |
| `STALE + last_state=GREEN + in_stop_zone=true` | drop to UNKNOWN/conservative — never aggressive continue on stale GREEN |
| `STALE + in_stop_zone=false` | controlled approach, wait for new message |

## Planner / FSM behavior table (paraphrased)

| Condition | Behavior |
|---|---|
| `RED + relevant=true + confirmed=true` | STOP_APPROACH (jerk-limited brake) |
| `YELLOW + relevant=true + confirmed=true` | half speed, approach stop point |
| `GREEN + relevant=true + confirmed=true` | LANE_FOLLOW with smooth acceleration |
| `GREEN + relevant=false` | log only, do not act |
| `GREEN + confirmed=false` | hold, wait |
| `UNKNOWN + relevant=true + in_stop_zone=true` | wait or behave like RED — conservative |
| `UNKNOWN + relevant=true + in_stop_zone=false` | drop speed, controlled approach, stop immediately |
| `CONFLICT` | accept as RED |
| `confirmed=false` | do not act |
| Light + sign collision | LIGHT priority — sign decision cancelled |

## Parameters (Sprint 1 defaults)

| Parameter | Default | Description |
|---|---|---|
| `image_topic` | `/zed2/left/image_raw` | Camera image topic |
| `publish_hz` | 10.0 | Publish rate (Hz) |
| `image_stale_ms` | 300 | Stale threshold; clamped to `valid_until_ms=300` |
| `model_path` | `''` | Path for future real YOLO model; empty = stub only |
| `use_yolo_stub` | `true` | Enable bbox stub |
| `stub_bbox_enabled` | `true` | Return fixed rect from stub |
| `stub_bbox_x/y/w/h` | 250/120/140/240 | Stub bbox rectangle (px, top-left) |
| `confirm_frames` | 3 | Consecutive frames required for `confirmed=True` |
| `state_memory_ms` | 500 | Max gap between qualifying frames before filter resets |

## Warning flags

| Flag | When published |
|---|---|
| `NO_INPUT` | No image ever received |
| `STALE_MESSAGE` | Image was flowing but most recent exceeds `image_stale_ms` |
| `LOW_CONFIDENCE` | Classifier confidence < 0.7, or UNKNOWN state, or stale/missing |
| `BBOX_MISSING` | Fresh image but no bbox (stub disabled or no detection) |
| `MODEL_ERROR` | Unsupported image encoding |
| `SYNC_MISMATCH` | Image data length inconsistent with declared dimensions / step |
| `ROUTE_CONTEXT_MISSING` | `/planning/active_route_context` absent, stale, invalid, or zero-validity (S3-R4) |

## Sample message (from contract §8)

```yaml
header.frame_id: "base_link"
state: 3            # GREEN
confidence: 0.85
relevant_to_route: false   # Sprint 3 placeholder
confirmed: true
in_stop_zone: false        # Sprint 3 placeholder
distance_to_stop: 0.0      # Sprint 3 placeholder
valid_until_ms: 300
age_ms: 45
source_sensor: camera
warning_flags: []
```

## Testing

Unit tests (no ROS2 dep, run with plain `pytest`):
- `test/test_colour_classifier.py` — 16 tests covering RED/GREEN/YELLOW/UNKNOWN/SYNC_MISMATCH/encoding
- `test/test_traffic_light_temporal.py` — 16 tests covering all 5 required temporal filter cases
- `test/test_stale_threshold.py` — 10 tests for `resolve_stale_ms()` boundary conditions
- `test/test_route_context_apply_utils.py` — 8 tests for S3-R4 route context application (missing/invalid/stale/zero-validity/usable/recovery/flag-preservation/no-duplicate)

Sprint 1 (42 tests) + S3-R4 (8 tests) = **50 traffic-light-node tests**.
All **345/345** perception colcon tests PASS on Ubuntu 20.04 + ROS2 Foxy (2026-05-13).

Integration smoke checklist: `wiki/implementation/sprint1_traffic_light_smoke_checklist.md`

## Cross-links

- Schema: [Message Contracts § TrafficLightState](../contracts/message_contracts.md)
- Route context coupling (Sprint 3): [Active Route Context](../architecture/active_route_context.md)
- Timing / fallback: [Timing and Fallback Table](../contracts/timing_and_fallback.md)
- Tests: T-02 .. T-07 in [Test Contract](../contracts/test_contract.md)
- Sprint plan: [Perception Sprint Plan](../implementation/perception_sprint_plan.md)
- Smoke checklist: [Sprint 1 Smoke Checklist](../implementation/sprint1_traffic_light_smoke_checklist.md)
