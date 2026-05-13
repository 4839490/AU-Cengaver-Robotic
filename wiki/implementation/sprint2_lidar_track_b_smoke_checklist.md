# Sprint 2 Track B — LiDAR Obstacle Node Smoke Checklist

Sources: `wiki/implementation/perception_sprint_plan.md`, `wiki/perception/lidar_obstacle_node.md`, `wiki/implementation/sprint2_perception_kickoff.md`.

> **Purpose:** Repeatable verification commands for the Track B LiDAR obstacle MVP on Ubuntu 20.04 + ROS2 Foxy. Run these to confirm the node still builds, tests pass, and runtime behaviour is correct after any future change to the `perception` package.

> **Scope boundary:** These checks cover the **synthetic MVP only** — `fake_pointcloud_pub` + `lidar_obstacle_node` with synthetic PointCloud2 frames. They do NOT validate real VLP-16 hardware, real RANSAC ground removal, or production obstacle detection models. TTC is 0.0 throughout (Sprint 3 dependency).

---

## Prerequisites

```bash
# Ubuntu 20.04 + ROS2 Foxy only (not macOS)
source /opt/ros/foxy/setup.bash
cd ~/Desktop/robotaksi/cengaver_ws
```

Kill any leftover processes from a previous session:

```bash
# pkill is blocked in this environment — use explicit PIDs from 'ps aux | grep ...'
# or restart the terminal. Alternatively:
kill $(pgrep -f lidar_obstacle_node) 2>/dev/null || true
kill $(pgrep -f fake_pointcloud_pub) 2>/dev/null || true
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

Exit code must be 0. After a successful build, source the install:

```bash
source install/setup.bash
```

---

## Step 2 — Run All Tests

```bash
colcon test --packages-select perception
colcon test-result --verbose
```

**Expected — S2-B5 baseline (238 tests):**
```
Summary: 238 tests, 0 errors, 0 failures, 0 skipped
```

Breakdown:
| File | Tests | Scope |
|---|---|---|
| `test_colour_classifier.py` | 16 | S1 traffic light HSV classifier — must not regress |
| `test_traffic_light_temporal.py` | 16 | S1 temporal filter — must not regress |
| `test_stale_threshold.py` | 10 | S1 stale-threshold helper — must not regress |
| `test_lane_image.py` | 13 | S2-A2 lane frame generation |
| `test_lane_detector.py` | 12 | S2-A3 column-scoring detector |
| `test_lane_contract.py` | 35 | S2-A4 contract helpers and flag rules |
| `test_pointcloud_utils.py` | 23 | S2-B2 synthetic PointCloud2 builder |
| `test_lidar_cluster_utils.py` | 44 | S2-B3 decode / filter / cluster / distance |
| `test_centroid_tracker.py` | 28 | S2-B4 centroid tracker — ID persistence / velocity / lifetime |
| `test_lidar_obstacle_pipeline.py` | **41** | **S2-B5 contract field tests — new** |

Any failure means a regression. Investigate before marking Track B as re-verified.

---

## Step 3 — Runtime Smoke A: `simple_obstacle`

Tests that `lidar_obstacle_node` publishes a correct `ObstacleTrack` for a stationary obstacle.

**Use a clean domain ID (change if 53 is already in use). Run this export in every terminal before any ros2 command.**

**Terminal A — start the obstacle node:**
```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception lidar_obstacle_node
```

Expected startup log line:
```
lidar_obstacle_node up (S2-B4) — subscribing /velodyne_points, publishing /perception/obstacle_tracks at 20.0 Hz. ...
```

**Terminal B — start fake publisher (simple_obstacle scenario):**
```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_pointcloud_pub --ros-args -p scenario:=simple_obstacle
```

**Terminal C — echo obstacle tracks:**
```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
python3 -c "
import rclpy
from rclpy.node import Node
from perception_msgs.msg import ObstacleTracks

class Echo(Node):
    def __init__(self):
        super().__init__('echo_node')
        self.count = 0
        self.create_subscription(ObstacleTracks, '/perception/obstacle_tracks', self.cb, 10)

    def cb(self, msg):
        self.count += 1
        if self.count > 15:
            return
        if msg.tracks:
            t = msg.tracks[0]
            print(f'[{self.count:02d}] tracks={len(msg.tracks)} id={t.track_id} '
                  f'pos_x={t.position_x:.3f} distance={t.distance:.3f} '
                  f'vx={t.velocity_x:.4f} vy={t.velocity_y:.4f} '
                  f'is_static={t.is_static} age_ms={t.age_ms} '
                  f'valid_until_ms={t.valid_until_ms} warning_flags={t.warning_flags} '
                  f'geometry_source={t.geometry_source!r} '
                  f'source_sensor={t.source_sensor!r} '
                  f'semantic_source={t.semantic_source!r}')
        else:
            print(f'[{self.count:02d}] tracks=0')

rclpy.init()
node = Echo()
rclpy.spin(node)
"
```

**Expected values (simple_obstacle):**
| Field | Expected | Notes |
|---|---|---|
| `tracks_count` | 1 | exactly one cluster |
| `track_id` | 1, stable | never changes for a single persistent obstacle |
| `pos_x` | ≈ 5.00 | centroid x of obstacle cluster |
| `distance` | ≈ 4.59 | pos_x − 0.410 m front-bumper offset |
| `velocity_x` | ≈ 0.000 | stationary |
| `velocity_y` | ≈ 0.000 | stationary |
| `is_static` | True | \|v\| < 0.1 m/s |
| `age_ms` | < 200 | ~22 ms fresh tick, ~72 ms cached tick |
| `valid_until_ms` | 200 | contract-canonical |
| `warning_flags` | [] | no fault flags for valid cluster |
| `geometry_source` | `'lidar'` | contract-canonical |
| `source_sensor` | `'lidar_cluster'` | contract-canonical |
| `semantic_source` | `'none'` | no camera fusion |

---

## Step 4 — Runtime Smoke B: `moving_obstacle`

Tests that velocity_x ≈ 1.0 m/s and is_static=False.

Stop the `fake_pointcloud_pub` from Step 3 (kill it), then start with the moving_obstacle scenario:

**Terminal B:**
```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_pointcloud_pub --ros-args -p scenario:=moving_obstacle
```

Keep the `lidar_obstacle_node` and the echo subscriber running.

**Expected values (moving_obstacle):**
| Field | Expected | Notes |
|---|---|---|
| `track_id` | 1, stable | same track across frames |
| `pos_x` | increasing (8.x → 8.x + 0.1) | obstacle advances 0.1 m per 0.1 s |
| `velocity_x` | ≈ 1.000 m/s | range 0.999–1.001 acceptable |
| `velocity_y` | ≈ 0.000 | no lateral motion |
| `is_static` | False | speed > 0.1 m/s threshold |
| `age_ms` | < 200 | alternates ~22 ms / ~72 ms (20 Hz node / 10 Hz publisher) |

---

## Step 5 — Runtime Smoke C: Stale Gating

Tests that `tracks=[]` is published when the PointCloud2 publisher stops.

With `lidar_obstacle_node` running and `simple_obstacle` or `moving_obstacle` publisher active:

1. Confirm tracks=1 appearing in the echo.
2. Stop (kill) the `fake_pointcloud_pub` process.
3. Wait ~800 ms (> 200 ms stale threshold).
4. Observe the echo — it must show `tracks=0` on every subsequent tick.

**Expected after publisher stop:**
```
[XX] tracks=0
[XX] tracks=0
[XX] tracks=0
```

---

## Step 6 — Runtime Smoke D: Empty Scenario

Tests that no spurious tracks are published for a zero-point cloud.

**Terminal B — start fake publisher (empty):**
```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
source ~/Desktop/robotaksi/cengaver_ws/install/setup.bash
ros2 run perception fake_pointcloud_pub --ros-args -p scenario:=empty
```

**Expected:**
```
[XX] tracks=0
[XX] tracks=0
```

---

## Step 7 — Forbidden Topic Check

Confirms that `lidar_obstacle_node` does NOT publish to any control, command, or planning topics.

With `lidar_obstacle_node` running (any scenario):

```bash
export ROS_DOMAIN_ID=53
source /opt/ros/foxy/setup.bash
ros2 topic list
```

**Allowed topics only:**
```
/parameter_events
/perception/obstacle_tracks
/rosout
/velodyne_points
```

**Forbidden (must NOT appear):**
- `/cmd_vel`
- `/control/*`
- `/beemobs/*`
- `/planning/*`

If any forbidden topic appears, the architecture boundary has been violated — investigate immediately.

---

## TTC Placeholder Note

Throughout all scenarios, `ttc = 0.0` on every track. This is correct — Sprint 3 will wire `/planning/active_route_context.ego_speed_mps` to compute real TTC. The 0.0 value is an explicit placeholder, not a bug.

---

## Scope Boundaries (what this checklist does NOT test)

| Out of scope | Why |
|---|---|
| Real VLP-16 hardware | Requires physical sensor + cables + host machine |
| Gazebo Velodyne plugin | Sprint 3+ integration target |
| RANSAC / PCL ground removal | MVP uses pure-Python BFS ground filter |
| PointPillars | Phase-2 / research item |
| TTC computation | Sprint 3 dependency (`ego_speed_mps` from planner) |
| `/planning/active_route_context` subscription | Sprint 3 wiring |
| `in_path` computation | Planner-side, never in perception |
| Real obstacle classification | Camera fusion (fusion_node) — Phase 2 |
