# ROS2 Foxy Notes

Sources: `raw/team_notes/meeting_decisions.md`; roadmap §5; `raw/official_teknofest/...Mimari_Tanımlama...pdf` §4; `raw/official_teknofest/...Kullanıcı_Dokümanı...pdf` §1.3 / §1.5.

## Target

- OS: **Ubuntu 20.04 LTS (focal fossa)**.
- ROS2 distribution: **Foxy Fitzroy** (only 20.04-supported ROS2 LTS that lines up with the BEE1 image).
- Python: 3.8 (Foxy default).
- Build tool: `colcon`.
- Simulator: **Gazebo 11** (`ros-foxy-gazebo-ros-pkgs`).
- macOS may be used for editing; build / run on Foxy only.

## Reconciling official docs

The vehicle ships with a Linux image that has both ROS Noetic and ROS Foxy installed and switchable via `~/.bashrc` (commenting `source /opt/ros/{noetic|foxy}/setup.bash`). Official Genel Bilgilendirme says "ROS Versiyonu: ROS1 veya ROS2" and the Kullanıcı Dokümanı 1.5 explicitly shows the Foxy launch (`ros2 launch smart_can_stuff can_launch.xml`). Our team contract picks ROS2 Foxy. When working on the BEE1 PC, ensure the Foxy environment is sourced and the `Projects/ros2_ws` line in `.bashrc` is uncommented.

## Workspace layout

```
cengaver_ws/
  src/
    common_msgs/             # AutonomyMode (TEK MOD ENUM)
    fsm_msgs/
    localization_msgs/
    perception_msgs/
    planning_msgs/
    localization/
    fsm/
    planner/
    controller/
    perception/
    simulation/
    bringup/
```

Each ROS package: `package.xml` + `CMakeLists.txt` (or `setup.py` for pure Python) + `msg/` (for message packages) + `launch/` + `config/` + `nodes/`.

## Build commands

```bash
# Sourcing (assumes ROS2 Foxy installed):
source /opt/ros/foxy/setup.bash

# From workspace root:
colcon build --symlink-install
source install/setup.bash

# Partial Milestone 1 (Gate B) — only the cleared canonical raw messages:
colcon build --packages-select common_msgs perception_msgs planning_msgs

# Verify each cleared .msg compiles:
ros2 interface show common_msgs/msg/AutonomyMode
ros2 interface show perception_msgs/msg/LaneModel
ros2 interface show perception_msgs/msg/TrafficLightState
ros2 interface show perception_msgs/msg/TrafficSign
ros2 interface show perception_msgs/msg/TrafficSigns
ros2 interface show perception_msgs/msg/ObstacleTrack
ros2 interface show perception_msgs/msg/ObstacleTracks
ros2 interface show perception_msgs/msg/StopTarget
ros2 interface show perception_msgs/msg/Junction
ros2 interface show perception_msgs/msg/PerceptionDiagnostics
ros2 interface show planning_msgs/msg/ActiveRouteContext
```

> **⚠ Gate B partial scope — read before generating any package.**
>
> - `planning_msgs` MUST contain **only** `ActiveRouteContext.msg` until owner confirmations land. Do **NOT** add `Trajectory.msg`, `TrajectoryPoint.msg`, `TargetSpeed.msg`, `PlanningStatus.msg`, `ControllerFeedback.msg`, or `FSMRequest.msg` yet.
> - Do **NOT** create `fsm_msgs` yet (entire package blocked).
> - Do **NOT** create `localization_msgs` yet (entire package blocked).
> - Do **NOT** generate any of the messages tagged `draft pending owner confirmation` in `wiki/contracts/message_contracts.md` § "Pending decisions". They will reopen for generation once their owners (planner — Uluşık, FSM — Üstün, controller — Durmaz, localization — Uluşık) sign off and the page reclassifies them as `canonical raw` or `team-approved extension`.

## Mac development mode

Active development is on a MacBook Air M4 where ROS2 Foxy is **not** installed and is not the supported runtime. The Ubuntu commands in the previous section remain the **only authoritative verification commands** — they are not optional and they cannot be replaced with anything that runs on Mac.

While only Mac is available:

- **Do not run `colcon build` on Mac. Do not fabricate or paraphrase its output.** If ROS2 Foxy is somehow installed on a Mac, treat its results as advisory only — Apple Silicon / macOS is not the target runtime, so a Mac build does not clear the Ubuntu gate.
- **Do not run `ros2 interface show`, `ros2 topic`, `ros2 launch`, or `gazebo` on Mac.** These commands are reserved for the Ubuntu 20.04 desktop.
- **Mac checks are limited to:**
  - File-layout listing (`find cengaver_ws -type f`).
  - Forbidden-file / forbidden-directory grep (`fsm_msgs/`, `localization_msgs/`, `PlannerMode.msg`, `FSMMode.msg`, draft `planning_msgs` files).
  - Forbidden-symbol grep (`PlannerMode`, `FSMMode`, `uint8 mode` in `AutonomyMode.msg`, `warning_flags` field in `StopTarget.msg`, `JUNCTION` / `TUNNEL` / `ROUNDABOUT` in `AutonomyMode.msg`).
  - Package metadata inspection: `package.xml` declares the right `buildtool_depend` / `build_depend` / `exec_depend` and `<member_of_group>rosidl_interface_packages</member_of_group>`; `CMakeLists.txt` lists the right `msg_files` and `DEPENDENCIES`.
  - Static review of `.msg` field sets against `wiki/contracts/message_contracts.md`.
  - Python / launch-file syntax review by eye.
- **Mac static review never replaces** `colcon build`, `ros2 interface show`, `ros2 topic echo/list`, `ros2 launch` smoke tests, or Gazebo 11 sensor-rate checks. The Ubuntu 20.04 desktop is required for all of those, and a Mac-clean step is only **provisionally accepted** — see `wiki/implementation/milestones.md` § "Verification policy while Ubuntu is unavailable" and its "Deferred Ubuntu verification checkpoints" table (V-B1..V-B4).
- **Labeling:** any deliverable produced on Mac must state, verbatim, all three of: `static-reviewed on Mac`, `ROS2 build pending on Ubuntu 20.04`, `ROS2 runtime pending on Ubuntu 20.04`.

The Ubuntu 20.04 + ROS2 Foxy compatibility requirement from `CLAUDE.md` § "Target Runtime" is unchanged. This section only describes which subset of verification work can happen on Mac while the desktop is unreachable.

## Foxy-specific gotchas

- `ament_cmake` for C++ packages; `ament_python` for pure-Python nodes.
- Message-only packages: `ament_cmake` + `rosidl_default_generators` build dep; **don't** mix message generation with executables in the same package.
- Launch files: prefer `launch/*.launch.py` (Foxy XML launch is supported but Python is the idiom).
- QoS: latching → `QoSProfile(reliability=RELIABLE, durability=TRANSIENT_LOCAL, depth=1)` (used for `/localization/map_origin`).
- Frame transforms: `tf2_ros.Buffer` + `TransformListener` + `static_transform_publisher` (use `ros2 run tf2_ros static_transform_publisher x y z qx qy qz qw parent child`).

## Docker on the BEE1 PC

Per the Kullanıcı Dokümanı §4, on-vehicle deployment uses Docker. Pipeline:

```bash
# On dev machine:
docker save -o cengaver-image.tar cengaver-image

# Transfer with FileZilla / sftp to smart@192.168.30.100 (Robotaxi_1)
sftp smart@192.168.30.100   # password: robotaxi

# On vehicle:
docker load -i /home/smart/cengaver-image.tar
sudo docker container run -it --network bridge \
  --name cengaver_ros2 cengaver-image
```

For ROS2 cross-container discovery, prefer `--network host` or set matching `ROS_DOMAIN_ID`.

## Vehicle network

| Robotaxi  | IP             | User   | Password   |
|-----------|---------------|--------|------------|
| Robotaxi_1| 192.168.30.100| smart  | robotaxi   |
| Robotaxi_2| 192.168.10.100| smart  | robotaxi   |

WiFi SSID: `robotaxi_1` / `robotaxi_2`; password: `robotaxi`.
