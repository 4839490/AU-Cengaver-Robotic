# Sprint 2 Track A — Lane Node Smoke Checklist

Sources: `wiki/implementation/perception_sprint_plan.md`, `wiki/perception/lane_node.md`, `wiki/implementation/sprint2_perception_kickoff.md`.

> **Purpose:** Repeatable verification commands for the Track A synthetic lane MVP on Ubuntu 20.04 + ROS2 Foxy. Run these to confirm the node still builds, tests pass, and runtime behaviour is correct after any future change to the `perception` package.

> **Scope boundary:** These checks cover the **synthetic MVP only** — `fake_lane_image_pub` + `lane_node` with `bgr8` synthetic frames. They do NOT validate real road imagery, calibrated projection, or production inference models.

---

## Prerequisites

```bash
# On Ubuntu 20.04 + ROS2 Foxy only (not macOS)
source /opt/ros/foxy/setup.bash
cd ~/Desktop/robotaksi/cengaver_ws
```

Make sure no leftover `lane_node` or `fake_lane_image_pub` processes are running from a previous session:

```bash
pkill -f lane_node || true
pkill -f fake_lane_image_pub || true
```

---

## Step 1 — Build

```bash
colcon build --packages-select perception
```

**Expected:**
```
Starting >>> perception
Finished <<< perception [~1s]
Summary: 1 package finished [~1.3s]
```

Exit code must be 0. Any build error means the package is broken — fix before proceeding.

After a successful build, source the install:

```bash
source install/setup.bash
```

---

## Step 2 — Run All Tests

```bash
colcon test --packages-select perception
colcon test-result --verbose
```

**Expected:**
```
Summary: 102 tests, 0 errors, 0 failures, 0 skipped
```

Breakdown:
- `test_colour_classifier.py`: 16 tests (S1 traffic light classifier — must not regress)
- `test_traffic_light_temporal.py`: 12 tests (S1 temporal filter — must not regress)
- `test_lane_image.py`: 12 tests (S2-A2 lane frame generation)
- `test_lane_detector.py`: 27 tests (S2-A3 column-scoring detector)
- `test_lane_contract.py`: 35 tests (S2-A4 contract helpers and flag rules)

Any failure means a regression. Investigate before marking Track A as re-verified.

---

## Step 3 — Straight Scenario Runtime Smoke

Test that `lane_node` publishes a correct `LaneModel` when given a synthetic straight-lane frame.

**Terminal A — start fake publisher (straight):**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_lane_image_pub --ros-args -p scenario:=straight
```

**Terminal B — start lane_node:**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception lane_node
```

**Terminal C — inspect output:**

> ⚠ **Foxy CLI limitation:** `ros2 topic echo --once` is NOT supported in some ROS2 Foxy distributions. Use one of these alternatives:

Option A — `ros2 topic echo` + Ctrl-C after observing one message:
```bash
ros2 topic echo /perception/lane_model
# Observe one message, then press Ctrl-C
```

Option B — Python rclpy probe (use if `echo` output is garbled or `--once` fails):
```python
# probe_lane.py  (run as: python3 probe_lane.py)
import rclpy
from rclpy.node import Node
from perception_msgs.msg import LaneModel

class Probe(Node):
    def __init__(self):
        super().__init__('probe')
        self.sub = self.create_subscription(LaneModel, '/perception/lane_model', self.cb, 10)
    def cb(self, msg):
        print(f"lane_lost: {msg.lane_lost}")
        print(f"lane_confidence: {msg.lane_confidence}")
        print(f"warning_flags: {msg.warning_flags}")
        print(f"centerline_count: {len(msg.centerline)}")
        print(f"left_boundary_count: {len(msg.left_boundary)}")
        print(f"right_boundary_count: {len(msg.right_boundary)}")
        print(f"lane_width_estimate: {msg.lane_width_estimate}")
        print(f"curvature: {msg.curvature}")
        print(f"valid_until_ms: {msg.valid_until_ms}")
        print(f"source_sensor: {msg.source_sensor}")
        print(f"frame_id: {msg.header.frame_id}")
        raise SystemExit

rclpy.init()
rclpy.spin(Probe())
```

**Expected output (straight scenario):**
```
lane_lost: False
lane_confidence: 1.0
warning_flags: []
centerline_count: 91
left_boundary_count: 91
right_boundary_count: 91
lane_width_estimate: ~1.85  (abs(left_lat - right_lat), synthetic)
curvature: 0.0
valid_until_ms: 500
source_sensor: camera
frame_id: base_link
```

Key invariants:
- `lane_lost = false`
- `lane_confidence >= 0.7` (= 1.0 for both-lane detection)
- `warning_flags = []` (empty — both lanes detected at full confidence)
- Each array: exactly 91 points (x ∈ [1.0, 10.0] m at 0.1 m spacing)
- `lane_width_estimate > 0`
- `curvature = 0.0` (straight MVP; real curvature estimation is future work)
- `frame_id = "base_link"`

**Kill processes before next check:**
```bash
pkill -f fake_lane_image_pub || true
pkill -f lane_node || true
```

---

## Step 4 — Blank Scenario Runtime Smoke

Test that `lane_node` publishes `lane_lost=true` and the correct warning flags when given a blank (no-lane) frame.

**Terminal A — start fake publisher (blank):**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_lane_image_pub --ros-args -p scenario:=blank
```

**Terminal B — start lane_node:**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception lane_node
```

**Terminal C — inspect output (same method as Step 3):**

**Expected output (blank scenario):**
```
lane_lost: True
lane_confidence: 0.0
warning_flags: ['LOW_CONFIDENCE', 'LANE_BOUNDARY_MISSING']
centerline_count: 0
left_boundary_count: 0
right_boundary_count: 0
```

Key invariants:
- `lane_lost = true`
- `lane_confidence = 0.0`
- `warning_flags` contains exactly `LOW_CONFIDENCE` and `LANE_BOUNDARY_MISSING`
- All three point arrays are empty

**Kill processes:**
```bash
pkill -f fake_lane_image_pub || true
pkill -f lane_node || true
```

---

## Step 5 — No-Input Smoke (optional)

Test that `lane_node` publishes `NO_INPUT` when no image has ever been received.

**Start lane_node only (no fake publisher):**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception lane_node
```

**Inspect output (same method as Step 3):**

**Expected output (no image ever received):**
```
lane_lost: True
lane_confidence: 0.0
warning_flags: ['LOW_CONFIDENCE', 'NO_INPUT']
centerline_count: 0
left_boundary_count: 0
right_boundary_count: 0
age_ms: 999999  (sentinel — no image)
```

Key invariants:
- `warning_flags` contains `NO_INPUT` (not `STALE_MESSAGE`)
- `age_ms = 999999` (the "no image ever" sentinel)

**Kill lane_node:**
```bash
pkill -f lane_node || true
```

---

## Step 6 — Rate Check

Test that `/perception/lane_model` is published at ≥ 15 Hz.

**Terminal A — start straight scenario:**
```bash
source /opt/ros/foxy/setup.bash && source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_lane_image_pub --ros-args -p scenario:=straight &
ros2 run perception lane_node &
```

**Terminal B — measure rate:**

> ⚠ **Foxy CLI limitation:** `ros2 topic hz` may not produce output for some message types in ROS2 Foxy due to the default QoS incompatibility between RELIABLE publisher and BEST_EFFORT subscriber used by the CLI. If `ros2 topic hz` shows no output, use the Python rate probe:

Option A — `ros2 topic hz`:
```bash
ros2 topic hz /perception/lane_model
```

Option B — Python rclpy rate probe:
```python
# rate_probe.py  (run as: python3 rate_probe.py)
import rclpy, time
from rclpy.node import Node
from perception_msgs.msg import LaneModel

class RateProbe(Node):
    def __init__(self):
        super().__init__('rate_probe')
        self.count = 0
        self.start = time.time()
        self.sub = self.create_subscription(LaneModel, '/perception/lane_model', self.cb, 10)
    def cb(self, msg):
        self.count += 1
        elapsed = time.time() - self.start
        if elapsed >= 5.0:
            print(f"Messages received: {self.count} in {elapsed:.1f}s → {self.count/elapsed:.1f} Hz")
            raise SystemExit

rclpy.init()
rclpy.spin(RateProbe())
```

**Expected:** ≥ 15 Hz (nominal ~20 Hz)

**Kill processes:**
```bash
pkill -f fake_lane_image_pub || true
pkill -f lane_node || true
```

---

## Step 7 — Forbidden Topic Check

Verify that no driving-decision topics are published.

With `lane_node` and/or `fake_lane_image_pub` running:

```bash
ros2 topic list | grep -E '^(/cmd_vel|/control|/beemobs)' || echo "PASS: no forbidden topics"
```

**Expected:** `PASS: no forbidden topics`

This check must pass in every smoke run. Any match means a critical architecture violation.

---

## Checklist Summary

| Check | Command | Expected |
|---|---|---|
| Build | `colcon build --packages-select perception` | Exit 0, 1 package finished |
| Tests | `colcon test --packages-select perception && colcon test-result --verbose` | 102 tests, 0 failures, 0 errors |
| Straight smoke | `lane_node` + `fake_lane_image_pub scenario:=straight` | `lane_lost=false`, `confidence=1.0`, `warning_flags=[]`, 91 pts each array, `lane_width_estimate>0`, `curvature=0.0`, `frame_id=base_link` |
| Blank smoke | `lane_node` + `fake_lane_image_pub scenario:=blank` | `lane_lost=true`, `confidence=0.0`, empty arrays, `[LOW_CONFIDENCE, LANE_BOUNDARY_MISSING]` |
| No-input smoke | `lane_node` only (no publisher) | `lane_lost=true`, `confidence=0.0`, `[LOW_CONFIDENCE, NO_INPUT]`, `age_ms=999999` |
| Rate | Python rclpy probe or `ros2 topic hz` | ≥ 15 Hz |
| Forbidden topics | `ros2 topic list \| grep -E '^(/cmd_vel\|/control\|/beemobs)'` | No matches |

---

## Foxy CLI Limitations (summary)

- `ros2 topic echo --once` — **NOT supported** in some ROS2 Foxy distributions. Use `ros2 topic echo` + Ctrl-C, or a Python rclpy probe subscriber.
- `ros2 topic hz` — may silently produce no output for certain message types due to QoS mismatch (RELIABLE publisher vs. BEST_EFFORT CLI subscriber). Use the Python rate probe if this occurs.
- Between consecutive straight/blank runs: **kill all lingering `fake_lane_image_pub` and `lane_node` processes** to prevent cross-contamination. Residual publishers from a prior run will continue injecting frames into the new `lane_node` process, giving misleading results.
- `ros2 daemon stop && ros2 daemon start` — clears stale FastRTPS discovery cache if `ros2 topic list` or `ros2 topic echo` shows unexpected results.

---

## Track A Synthetic MVP Limitations

These limitations apply to all checks above. They are by design and do NOT represent failures:

- `curvature = 0.0` — the column-scoring detector does not compute real curvature. Real estimation requires UFLD v2 + TensorRT (Phase 2).
- `lane_width_estimate` is a synthetic pixel-to-metric approximation (`col_to_lateral_m`), not a calibrated IPM result.
- `frame_id = "base_link"` with synthetic coordinate mapping — not tied to real camera extrinsics.
- Only `bgr8` synthetic frames are tested here. Real road imagery is NOT validated in Track A.
- `/planning/active_route_context` is NOT subscribed. `ego_speed_mps` remains 0.0 until Sprint 3.

See `wiki/perception/lane_node.md` §"Synthetic MVP status" and `wiki/implementation/perception_sprint_plan.md` §"Track A completion summary" for the full list of what is and is not in scope.

---

## Track A Verification Status

- **S2-A1 through S2-A4:** PASSED on Ubuntu 20.04 + ROS2 Foxy (Linux 5.15.0-139-generic, 2026-05-12). See `wiki/log.md` entries `[2026-05-12] implementation | S2-A4 — LaneModel contract hardening and tests`.
- **S2-A5 (this checklist):** COMPLETE. No code changes. Checklist and wiki documentation finalized.
- **Track B next:** `lidar_obstacle_node` MVP (S2-B1..S2-B5). See `wiki/implementation/sprint2_perception_kickoff.md` §"Track B".
