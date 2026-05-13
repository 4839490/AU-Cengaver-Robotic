# lane_node

Sources: `Perception_Planner_FSM_v1.4` §7; roadmap §6.5.

## Topic

```
/perception/lane_model    perception_msgs/LaneModel
Hz: 20–30 | valid_until_ms: 500 | frame_id: base_link
Producer : lane_node (Track A synthetic MVP; UFLD v2 + TensorRT FP16 planned for Phase 2)
Consumer : planner_node, fsm_node
```

## Algorithm

- **MVP**: any centerline detector that produces a contract-shaped message. Even a Hough/polynomial approach is acceptable for the first MVP, as long as `centerline[]`, `lane_lost`, `lane_confidence`, `curvature` are populated correctly.
- **Phase-2**: UFLD v2 export to TensorRT FP16 for higher Hz and stability.
- Centerline points must be in `base_link`, ≥5 m forward, spacing ≤ 0.1 m.
- Curvature: `curvature = 0.0` throughout the Track A synthetic MVP. Real curvature estimation (calibrated projection or UFLD v2 / IPM output) is future work (Phase 2). The planner must not assume a non-zero curvature metric is available until Phase 2 is implemented.

## Critical fields

- `lane_confidence ∈ [0, 1]` — planner thresholds: ≥0.7 normal, 0.4–0.7 reduced speed + smoothing, <0.4 immediate speed drop.
- `lane_lost = true` → planner drops speed immediately and falls back to last valid model for 0.5–1.0 s, then NDT/STOP_APPROACH.
- `lane_width_estimate` is published for planner geometry checks.

## Planner / FSM behavior

| Condition | Action |
|---|---|
| `lane_confidence ≥ 0.7` | normal lane following |
| `0.4 ≤ lane_confidence < 0.7` | reduce speed, increase smoothing |
| `lane_confidence < 0.4` or `lane_lost = true` | immediate speed drop → 0.5–1 s last-model fallback → STOP_APPROACH |
| `valid_until_ms` exceeded | treat as `lane_lost = true` |

## Warning flag rules (hardened in S2-A4)

| State | `warning_flags` |
|---|---|
| Both lanes detected, `confidence ≥ 0.7` | `[]` |
| One lane only (`confidence = 0.5 < 0.7`) | `[LOW_CONFIDENCE, LANE_BOUNDARY_MISSING]` |
| No lanes / unsupported encoding | `[LOW_CONFIDENCE, LANE_BOUNDARY_MISSING]` |
| No image ever received | `[LOW_CONFIDENCE, NO_INPUT]` |
| Image stale | `[LOW_CONFIDENCE, STALE_MESSAGE]` |

Canonical flag strings: `LOW_CONFIDENCE | STALE_MESSAGE | LANE_BOUNDARY_MISSING | NO_INPUT`.

## Point contract (both-lane detection)

- `centerline`, `left_boundary`, `right_boundary`: each ≥ 50 points.
- x ∈ [1.0, 10.0] m, monotonically increasing, spacing ≤ 0.1 m, coverage ≥ 5.0 m.
- `centerline.y` = midpoint of `left_boundary.y` and `right_boundary.y`.
- `lane_width_estimate = abs(left_lat − right_lat)` (synthetic MVP; not calibrated real lane width).
- `curvature = 0.0` for straight MVP. Real curvature estimation: future work (post-UFLD-v2).

## Synthetic MVP status (Track A complete — 2026-05-12)

Sprint 2 Track A (S2-A1..S2-A5) is **complete for the synthetic MVP**. The following have been verified on Ubuntu 20.04 + ROS2 Foxy (102 tests, 0 failures):

**Complete:**
- `fake_lane_image_pub.py` — `bgr8` synthetic lane frames (`straight` / `blank` scenarios) at ≥ 10 Hz.
- `lane_node.py` — column-scoring detector, `LaneModel` publication with all contract fields.
- `lane_contract.py` — point contract helpers, warning-flag rules, constants.
- All five warning-flag states (both lanes / one lane / no lanes / no input / stale) unit-tested and runtime-verified.

**Not complete (Phase 2 / future work):**
- Real UFLD v2 or YOLOP model.
- Calibrated camera projection / IPM (real lane width, real coordinates).
- Real curvature estimation (`curvature = 0.0` throughout).
- Real road / video validation.
- `/planning/active_route_context` subscriber (`ego_speed_mps` placeholder until Sprint 3).

For the repeatable smoke checklist see `wiki/implementation/sprint2_lane_track_a_smoke_checklist.md`.

## Cross-links

- Schema: [Message Contracts § LaneModel](../contracts/message_contracts.md)
- Test T-01 in [Test Contract](../contracts/test_contract.md).
- Smoke checklist: [Sprint 2 Lane Track A Smoke Checklist](../implementation/sprint2_lane_track_a_smoke_checklist.md).
