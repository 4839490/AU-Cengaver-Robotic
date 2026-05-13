# CAN-Bus Interface

Source: `raw/official_teknofest/2026_..._Kullanıcı_Dokümanı_b.pdf` §2 (`ROS – CAN`), §6 (Pid ve Temel Kontroller). Vehicle uses Beemobs `smart_can_*` package to bridge CANBus ↔ ROS.

> Controller-side detail. Perception does not interact with these topics. Listed here so the planner→controller flow is documented end-to-end.

## Bridge launch

- ROS Noetic: `roslaunch smart_can_stuff start_can_bus.launch`
- ROS2 Foxy: `ros2 launch smart_can_stuff can_launch.xml`

After launch, the topics below appear.

## ROS → CAN (commands)

### `/beemobs/rc_unittoOmux`

Vehicle-level control bits.

| Field | Meaning |
|---|---|
| `RC_Ignition` | 0 OFF / 1 ON (start vehicle in autonomous mode) |
| `RC_SelectionGear` | 0 NEUTRAL / 1 DRIVE / 2 REVERSE |
| `RC_HighBeam` / `RC_LowBeam` / `RC_DRL` | headlight / DRL switches |
| `RC_SignalStatus` | 0 off / 1 right / 2 left / 3 hazard |
| `AUTONOMOUS_DOOR_OPEN` / `AUTONOMOUS_DOOR_CLOSE` | door commands |
| `RC_ReverseLight`, `RC_InteriorLight`, `RC_WindowResintance`, `RC_BrakeLight` | accessories |
| `AUTONOMOUS_EMERGENCY` | 0 deactive / 1 active (cuts motor energy; vehicle can run but cannot move) |

> `AUTONOMOUS_EMERGENCY` here is the CAN write side of the safety channel. The hardware E-stop button(s) and this software bit are OR'd. Once active, only motor + neutral happen — accessories still work. The FSM may **observe and log** but should not be the only thing that triggers it (see [System Overview](../architecture/system_overview.md) hard rules).

### `/beemobs/RC_THRT_DATA`

| Field | Meaning |
|---|---|
| `RC_THRT_PEDAL_PRESS` | 0 pressed / 1 not pressed (set 0 before applying throttle) |
| `RC_THRT_PEDAL_POSITION` | throttle [50–250]; effective range 100–250 due to speed cap |

### `/beemobs/AUTONOMOUS_BrakePedalControl`

| Field | Meaning |
|---|---|
| `AUTONOMOUS_BrakePedalMotor_EN` | enable brake motor (must be 1 to actuate) |
| `AUTONOMOUS_BrakePedalMotor_ACC` | move acceleration (5000–65500) |
| `AUTONOMOUS_BrakePedalMotor_PER` | pedal position (0–100 %) |
| `AUTONOMOUS_BrakeMotor_Voltage` | motor voltage on/off |

### `/beemobs/AUTONOMOUS_SteeringMot_Control`

| Field | Meaning |
|---|---|
| `AUTONOMOUS_SteeringMot_EN` | enable steering motor (must be 1) |
| `AUTONOMOUS_SteeringMot_PWM` | 0–127 → left, 128–255 → right; speed proportional to delta from 127 |

> Mechanical limit switches stop the steering motor at hard limits to prevent damage.

### `/beemobs/AUTONOMOUS_HB_MotorControl`

Hand-brake motor: `AUTONOMOUS_HB_MotEN`, `AUTONOMOUS_HB_MotState` (0 raise / 1 lower), `AUTONOMOUS_HB_Motor_PWM` (200 is a good test value).

## CAN → ROS (feedback)

### `/beemobs/FB_MotorDriver`

`GEAR_STATUS_FROM_MOTOR` (0 N / 1 D / 2 R), `VehicleRPM`.

### `/beemobs/FB_VehicleSpeed`

`FB_VehicleSpeed_KMh` (display speed), `FB_ReelVehicleSpeed_KMh` (real km/h), `FB_ReelVehicleSpeed_Ms` (real m/s).

> **`FB_ReelVehicleSpeed_Ms` is the source for `controller/feedback.actual_speed`**, which the planner uses to populate `active_route_context.ego_speed_mps`, which perception then uses for TTC. (See [Active Route Context](../architecture/active_route_context.md).)

### `/beemobs/FB_OMUX_to_AUTONOMOUS`

Vehicle status bits: `FB_EMERGENCY`, signal lamps, door lock state, battery voltage, charge inlet, headlight states, `FB_IGNITION`, `FB_HazardousLight`, `FB_VehicleStatus` (0 ready / 1 fault), door open/close states, `FB_BatterySOC` (%), `FB_ErrorPowerTrain`, `FB_ErrorBattery`, `FB_BrakePedal_Voltage_EN`.

### `/beemobs/snd_RCUnit_SteeringData`

`RC_Steering_LeftLimit`, `RC_Steering_RightLimit`, `RC_SteeringPWM`, `RC_SteeringDirection` (0 N / 1 right / 2 left).

### `/beemobs/snd_RCUnit_BrakeData`

`RC_BrakePedal_Speed`, `RC_BrakePedal_Acc`, `RC_BrakePedal_Pos`.

### `/beemobs/snd_RCUnit_HandBrakeData`

`RC_HB_PwmValue`, `RC_HandBrake_PRESS`, `RC_HandBrake_FREE`, `RC_HandBrakeData` (0 idle / 1 lowering / 2 raising).

### `/beemobs/AutonomousHeardBit`

`AutonomousManuelSelect` — autonomous-vs-manual selector.

### `/beemobs/FeedbackSteeringAngle`

`FeedBackSteeringAngle`, `FeedBackBrakepedalAngle` — physical wheel angle and brake-pedal angle for closed-loop control.

## Built-in PID controllers (`smart_can_stuff/pid_*`)

`pid.launch` (Noetic) / `pid_launch.py` (Foxy) starts wheel-angle and speed PIDs:

- Topic `/beemobs/steering_target_value` activates wheel-angle PID (drops out if no message in 3 loop ticks).
- Topic `/beemobs/speed_target_value` activates speed PID.
- Tunables in `Projects/ros_ws/src/smart_can_driver/smart_can_stuff/config/steering_pid.yaml` (and `thrt_pid.yaml`); ROS2 path `Projects/ros2_ws/src/smart_can_stuff/launch/pid_params.yaml`.

> Our project's `controller_node` should typically prefer the team's own Stanley + custom PID stack over the vendor PIDs, but the vendor PIDs are useful for early bring-up and ground truth.

## Joystick remote

`smart_can_stuff/beemobs.py` (Noetic) or `ros2 run smart_can_stuff beemobs.py` (Foxy) takes a Logitech-style gamepad. Buttons: ignition on/off, gear up/down, hand-brake up/down, steering left/right, throttle/brake stick.
