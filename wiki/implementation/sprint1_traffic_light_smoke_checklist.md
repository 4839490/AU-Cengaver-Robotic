# Sprint 1 Traffic Light Node — Smoke Checklist

This checklist is for **repeat verification** of the Sprint 1 `traffic_light_node` MVP on Ubuntu 20.04 + ROS2 Foxy. It is not a source-of-truth; see `wiki/perception/traffic_light_node.md` for semantics and `wiki/contracts/message_contracts.md` §8 for the full field contract.

**Environment:** Ubuntu 20.04 LTS + ROS2 Foxy. All commands run from the repo root (`~/Desktop/robotaksi`) unless noted.

---

## 0. Build and unit tests

```bash
source /opt/ros/foxy/setup.bash
cd ~/Desktop/robotaksi/cengaver_ws
colcon build --packages-select perception bringup
source install/setup.bash
colcon test --packages-select perception
colcon test-result --verbose
```

**Expected:**
```
Summary: 2 packages finished [~2s]     # colcon build
Summary: 42 tests, 0 errors, 0 failures, 0 skipped   # colcon test-result
```

Breakdown: 16 colour-classifier tests + 16 temporal-filter tests + 10 stale-threshold tests = 42.

---

## 1. No-image-ever path (UNKNOWN + NO_INPUT)

Terminal 1:
```bash
ros2 run perception traffic_light_node
```

Terminal 2:
```bash
ros2 topic echo /perception/traffic_light_state
```

**Expected:**
```yaml
state: 0              # UNKNOWN
confidence: 0.0
confirmed: false
age_ms: 999999        # sentinel: never received
valid_until_ms: 300
warning_flags: [LOW_CONFIDENCE, NO_INPUT]
```

---

## 2. RED image → RED + confirmed=true after 3 frames

Terminal 1 (start both in same shell or use separate terminals with sourced setup):
```bash
ros2 run perception fake_image_pub --ros-args -p color:=red &
ros2 run perception traffic_light_node &
sleep 5
ros2 topic echo /perception/traffic_light_state
```

**Expected:**
```yaml
state: 1              # RED
confidence: 0.85
confirmed: true       # temporal filter: 3 frames confirmed
bbox_x: 250.0  bbox_y: 120.0  bbox_w: 140.0  bbox_h: 240.0
warning_flags: []
```

---

## 3. GREEN image → GREEN + confirmed=true

Same as above but `color:=green`.

**Expected:** `state: 3` (GREEN), `confidence: 0.85`, `confirmed: true`.

---

## 4. YELLOW image → YELLOW + confirmed=true

Same with `color:=yellow`.

**Expected:** `state: 2` (YELLOW), `confidence: 0.85`, `confirmed: true`.

---

## 5. Unknown/gray image → UNKNOWN + LOW_CONFIDENCE

Same with `color:=unknown`.

**Expected:**
```yaml
state: 0              # UNKNOWN
confidence: 0.0
confirmed: false
warning_flags: [LOW_CONFIDENCE]
```

---

## 6. use_yolo_stub:=false → UNKNOWN + BBOX_MISSING

```bash
ros2 run perception fake_image_pub --ros-args -p color:=red &
ros2 run perception traffic_light_node --ros-args -p use_yolo_stub:=false &
sleep 4
ros2 topic echo /perception/traffic_light_state
```

**Expected:**
```yaml
state: 0
confirmed: false
warning_flags: [LOW_CONFIDENCE, BBOX_MISSING]
bbox_x: 0.0  bbox_y: 0.0  bbox_w: 0.0  bbox_h: 0.0
```

---

## 7. Stale check (default 300 ms threshold)

```bash
# Start publisher + node, wait for confirmed=true, then kill publisher
ros2 run perception fake_image_pub --ros-args -p color:=red &
FAKE_PID=$!
ros2 run perception traffic_light_node &
sleep 5          # wait for confirmed=true
kill $FAKE_PID
sleep 2          # wait > 300 ms after publisher stops
ros2 topic echo /perception/traffic_light_state
```

**Expected after kill:**
```yaml
state: 4              # STALE
confidence: 0.0
confirmed: false
age_ms: >300          # wall-clock ms since last image
warning_flags: [LOW_CONFIDENCE, STALE_MESSAGE]
```

---

## 8. image_stale_ms:=500 → clamp warning + STALE at 300 ms

```bash
ros2 run perception traffic_light_node --ros-args -p image_stale_ms:=500
```

**Expected log line:**
```
[WARN] image_stale_ms=500 exceeds valid_until_ms=300; clamped to 300 ms ...
```

After publisher is killed and > 300 ms elapses, `state: 4` (STALE) appears — same as above. The node does NOT wait 500 ms; it transitions at 300 ms.

---

## 9. Launch file smoke (traffic_light_mvp.launch.py)

```bash
ros2 launch bringup traffic_light_mvp.launch.py color:=red
```

Terminal 2:
```bash
ros2 topic echo /perception/traffic_light_state
```

**Expected:** same as check 2 (RED + confirmed=true). Additionally:
```bash
ros2 run tf2_ros tf2_echo base_link camera_frame
# → Translation: [-0.205, 0.000, 0.685]
```

---

## 10. Forbidden-topic check

```bash
ros2 topic list | grep -E '^(/cmd_vel|/control|/beemobs)' || echo PASS
```

**Expected:** `PASS` — no driving topics published by any perception node.

---

## Notes

- `ros2 topic hz` does not produce output for large `sensor_msgs/Image` messages in ROS2 Foxy with RELIABLE QoS. Use consecutive timestamp deltas from `ros2 topic echo` to verify rate instead.
- ROS2 Foxy does not support `ros2 topic echo --once`. Use plain `ros2 topic echo` and interrupt manually after observing the expected message.
- Start `ros2 daemon start` before running `ros2 topic echo` if nodes are launched in separate terminals, to avoid DDS discovery delays.
- For multi-terminal tests, all terminals must `source /opt/ros/foxy/setup.bash` and `source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash`.
