"""
BEE1 Kontrol ROS2 Node
======================
Planner ↔ Controller Sözleşmesi v1.2
Vehicle Interface ↔ Controller CAN Sözleşmesi v1.0

SUBSCRİBE:
  /planning/trajectory    20Hz  planning_msgs/Trajectory
  /planning/target_speed  20Hz  planning_msgs/TargetSpeed
  /planning/status        10Hz  planning_msgs/PlanningStatus
  /emergency              olay  std_msgs/Bool

PUBLISH:
  /controller/feedback    20Hz  planning_msgs/ControllerFeedback
  /control_debug          20Hz  std_msgs/String (debug)
"""

import math
import time
import json
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool

from planning_msgs.msg import Trajectory
from planning_msgs.msg import TargetSpeed
from planning_msgs.msg import PlanningStatus
from planning_msgs.msg import ControllerFeedback

from ackermann_model  import AckermannKinematic, AckermannParams
from speed_controller import HybridPIDController, PIDConfig, PIDGains   # DÜZELTİLDİ: hybrid_pid → speed_controller
from can_interface    import BEE1CANInterface, SteeringCalibration
from emergency_stop   import EmergencyStopManager, EmergencySource, EmergencyType


# ─── AutonomyMode (common_msgs/AutonomyMode.msg) ─────────────────────────────
# LANE_FOLLOW=0 STOP_APPROACH=1 PICKUP_APPROACH=2 DROPOFF_APPROACH=3
# OBSTACLE_AVOID=4 PARK_APPROACH=5 PARK_MANEUVER=6 MISSION_COMPLETE=7
# ⚠️ EMERGENCY_STOP bu enum'da YOK — TargetSpeed.reason sabitidir!
class AutonomyMode:
    LANE_FOLLOW      = 0
    STOP_APPROACH    = 1
    PICKUP_APPROACH  = 2
    DROPOFF_APPROACH = 3
    OBSTACLE_AVOID   = 4
    PARK_APPROACH    = 5
    PARK_MANEUVER    = 6
    MISSION_COMPLETE = 7


# ─── TargetSpeed reason (planning_msgs/TargetSpeed.msg) ──────────────────────
# REASON_LANE_FOLLOW=0 REASON_APPROACH_STOP=1 REASON_PICKUP_DROPOFF=2
# REASON_OBSTACLE_SLOW=3 REASON_JUNCTION=4 REASON_TUNNEL=5
# REASON_PARK_APPROACH=6 REASON_PARK_MANEUVER=7 REASON_EMERGENCY_STOP=8
# REASON_LOCALIZATION_DEGRADED=9 REASON_LANE_LOST=10
class TargetSpeedReason:
    LANE_FOLLOW           = 0
    APPROACH_STOP         = 1
    PICKUP_DROPOFF        = 2
    OBSTACLE_SLOW         = 3
    JUNCTION              = 4
    TUNNEL                = 5
    PARK_APPROACH         = 6
    PARK_MANEUVER         = 7
    EMERGENCY_STOP        = 8
    LOCALIZATION_DEGRADED = 9    # DÜZELTİLDİ: MSG'de var, eklendi
    LANE_LOST             = 10   # DÜZELTİLDİ: MSG'de var, eklendi


# ─── PlanningStatus sabitleri (planning_msgs/PlanningStatus.msg) ──────────────
# STATUS_ACTIVE=0 STATUS_WAITING_FSM=1 STATUS_OBSTACLE_BLOCKED=2
# STATUS_LANE_LOST=3 STATUS_LOCALIZATION_DEGRADED=4
# STATUS_EMERGENCY=5 STATUS_MISSION_COMPLETE=6
class PlanningStatusCode:
    ACTIVE                = 0
    WAITING_FSM           = 1
    OBSTACLE_BLOCKED      = 2
    LANE_LOST             = 3
    LOCALIZATION_DEGRADED = 4
    EMERGENCY             = 5
    MISSION_COMPLETE      = 6


TIMEOUT_NORMAL_MS = 500
TIMEOUT_BRAKE_MS  = 1000


class BEE1ControlNode(Node):

    def __init__(self):
        super().__init__('bee1_control_node')

        self.declare_parameter('wheelbase',            2.40)
        self.declare_parameter('track_width',          1.03)
        self.declare_parameter('max_steer_angle_deg',  32.5)
        self.declare_parameter('min_turn_radius',      4.1)
        self.declare_parameter('toe_in_offset',        0)
        self.declare_parameter('control_rate_hz',      20.0)
        self.declare_parameter('cte_kp',     0.8)
        self.declare_parameter('cte_ki',     0.01)
        self.declare_parameter('cte_kd',     0.15)
        self.declare_parameter('heading_kp', 1.2)
        self.declare_parameter('heading_ki', 0.005)
        self.declare_parameter('heading_kd', 0.25)

        ackermann_params = AckermannParams(
            wheelbase       = self.get_parameter('wheelbase').value,
            track_width     = self.get_parameter('track_width').value,
            max_steer_angle = math.radians(self.get_parameter('max_steer_angle_deg').value),
            min_turn_radius = self.get_parameter('min_turn_radius').value,
        )
        self.ackermann = AckermannKinematic(ackermann_params)

        pid_config = PIDConfig(
            cte_gains     = PIDGains(
                kp = self.get_parameter('cte_kp').value,
                ki = self.get_parameter('cte_ki').value,
                kd = self.get_parameter('cte_kd').value,
            ),
            heading_gains = PIDGains(
                kp = self.get_parameter('heading_kp').value,
                ki = self.get_parameter('heading_ki').value,
                kd = self.get_parameter('heading_kd').value,
            )
        )
        self.pid = HybridPIDController(pid_config)

        steer_cal = SteeringCalibration(
            max_steer_angle_rad = ackermann_params.max_steer_angle,
            toe_in_offset       = self.get_parameter('toe_in_offset').value,
        )
        self.can_if = BEE1CANInterface(cal=steer_cal)
        self.can_if.connect()
        self.can_if.kontak_ac()

        self.emergency_mgr = EmergencyStopManager(
            on_software_estop = self.can_if.emergency_stop,
            on_hardware_estop = lambda: self.get_logger().error(
                'Donanımsal ESTOP — safety supervisor aracı durduruyor!')
        )

        # Durum değişkenleri
        self._cte               = 0.0
        self._heading_error     = 0.0
        self._traj_speed_mps    = 0.0
        self._traj_last_time    = 0.0
        self._traj_valid        = False
        self._traj_points       = []
        self._target_speed_mps  = 0.0
        self._target_jerk       = 2.0
        self._target_reason     = 0
        self._target_last_time  = 0.0
        self._planner_mode      = AutonomyMode.STOP_APPROACH
        self._loc_degraded      = False
        self._obstacle_blocked  = False
        self._lane_lost         = False
        self._actual_speed      = 0.0
        self._actual_steer_deg  = 0.0

        # Subscriptions
        self.create_subscription(Trajectory,     '/planning/trajectory',   self._trajectory_cb,   10)
        self.create_subscription(TargetSpeed,    '/planning/target_speed', self._target_speed_cb, 10)
        self.create_subscription(PlanningStatus, '/planning/status',       self._status_cb,       10)
        self.create_subscription(Bool,           '/emergency',             self._emergency_cb,    10)
        self.create_subscription(String,         '/odometry',              self._odometry_cb,     10)

        # Publishers
        self._feedback_pub = self.create_publisher(ControllerFeedback, '/controller/feedback', 10)
        self._debug_pub    = self.create_publisher(String,             '/control_debug',        10)

        rate = self.get_parameter('control_rate_hz').value
        self.create_timer(1.0 / rate, self._control_loop)

        self.get_logger().info('BEE1 Kontrol Node başladı — Sözleşme v1.2 / CAN v1.0')

    # ── Callbacks ─────────────────────────────────────────────────────────────

    def _trajectory_cb(self, msg: Trajectory):
        """
        Trajectory.msg:
          TrajectoryPoint[] points → x(f64), y(f64), yaw(f64), speed(f32),
                                     curvature(f32), distance_from_start(f32)
          uint8  planner_mode
          uint32 valid_until_ms
          uint32 age_ms
          string[] warning_flags
        """
        if not msg.points:
            self.get_logger().warn('Trajectory boş — nokta yok!')
            return
        self._traj_speed_mps = float(msg.points[0].speed)
        self._traj_points    = msg.points
        self._planner_mode   = int(msg.planner_mode)
        self._traj_valid     = True
        self._traj_last_time = time.monotonic()

    def _target_speed_cb(self, msg: TargetSpeed):
        """
        TargetSpeed.msg:
          float32 speed, float32 jerk_limit, uint8 reason (0-10),
          uint32 valid_until_ms, uint32 age_ms, string[] warning_flags
        """
        prev_reason = self._target_reason
        self._target_speed_mps = float(msg.speed)
        self._target_jerk      = float(msg.jerk_limit)
        self._target_reason    = int(msg.reason)
        self._target_last_time = time.monotonic()

        if self._target_reason == TargetSpeedReason.EMERGENCY_STOP:
            self.get_logger().error('EMERGENCY_STOP komutu! (reason=8)')
            self.emergency_mgr.trigger_software(EmergencySource.PLANNER, 'reason=8')

        if self._target_reason != prev_reason:
            self.pid.reset()
            self.get_logger().info(f'Reason: {prev_reason}→{self._target_reason} — PID sıfırlandı')

    def _status_cb(self, msg: PlanningStatus):
        """
        PlanningStatus.msg:
          uint8  status (0-6)
          bool   trajectory_valid, goal_reached, parking_entry_reached,
                 obstacle_blocking, lane_lost, localization_degraded
          uint32 active_waypoint_id  ← uint32 (uint8 DEĞİL!)
          float32 distance_to_goal
          uint8  planner_mode
          uint32 age_ms, valid_until_ms
          string[] warning_flags
        """
        self._traj_valid       = bool(msg.trajectory_valid)
        self._loc_degraded     = bool(msg.localization_degraded)
        self._obstacle_blocked = bool(msg.obstacle_blocking)
        self._lane_lost        = bool(msg.lane_lost)
        status                 = int(msg.status)

        if status == PlanningStatusCode.EMERGENCY and not self.emergency_mgr.is_active:
            self.get_logger().error('Planner EMERGENCY! (status=5)')
            self.emergency_mgr.trigger_software(EmergencySource.PLANNING_STATUS, 'status=5')

        if status == PlanningStatusCode.MISSION_COMPLETE:
            self.get_logger().info('MISSION_COMPLETE — el freni çekiliyor.')
            self.can_if.park_complete()

    def _emergency_cb(self, msg: Bool):
        if msg.data:
            self.get_logger().error('Donanımsal EMERGENCY sinyali!')
            self.emergency_mgr.trigger_hardware_observed('/emergency=True')
        else:
            self.emergency_mgr.reset_hardware()

    def _odometry_cb(self, msg: String):
        """Geçici JSON. Gerçekte localization_msgs/LocalizationOdometry olacak."""
        try:
            data = json.loads(msg.data)
            self._actual_speed     = float(data.get('speed',        0.0))
            self._actual_steer_deg = float(data.get('steering_deg', 0.0))
        except (json.JSONDecodeError, KeyError, TypeError):
            pass

    # ── Ana Kontrol Döngüsü ───────────────────────────────────────────────────

    def _control_loop(self):
        now = time.monotonic()
        traj_age   = (now - self._traj_last_time)   * 1000
        target_age = (now - self._target_last_time) * 1000

        # Trajectory timeout
        if self._traj_last_time > 0:
            if traj_age > TIMEOUT_BRAKE_MS:
                self.get_logger().warn(f'Trajectory timeout {traj_age:.0f}ms — TAM FREN')
                self.emergency_mgr.trigger_software(
                    EmergencySource.TRAJECTORY,
                    f'Trajectory {traj_age:.0f}ms gelmedi',
                    EmergencyType.TRAJECTORY_TIMEOUT)
                self._publish_feedback(brake=True, full_brake=True)
                return
            elif traj_age > TIMEOUT_NORMAL_MS:
                self.get_logger().warn(f'Trajectory geç {traj_age:.0f}ms — hız %50')
                self._traj_speed_mps *= 0.5

        # TargetSpeed timeout
        if self._target_last_time > 0:
            if target_age > TIMEOUT_BRAKE_MS:
                self.get_logger().warn(f'TargetSpeed timeout {target_age:.0f}ms — TAM FREN')
                self.emergency_mgr.trigger_software(
                    EmergencySource.TARGET_SPEED,
                    f'TargetSpeed {target_age:.0f}ms gelmedi',
                    EmergencyType.TARGET_SPEED_TIMEOUT)
                self._publish_feedback(brake=True, full_brake=True)
                return
            elif target_age > TIMEOUT_NORMAL_MS:
                self.get_logger().warn(f'TargetSpeed geç {target_age:.0f}ms — son hız korunuyor')

        if self.emergency_mgr.is_active:
            self._publish_feedback(brake=True, full_brake=True)
            return

        mode = self._planner_mode

        # Hız öncelik kuralı FIX-5: final = min(target, trajectory_point)
        raw_speed = min(self._target_speed_mps, self._traj_speed_mps)

        if self._loc_degraded:
            raw_speed *= 0.5
            self.get_logger().warn('Lokalizasyon zayıf — hız %50.')

        # Mod bazlı hız sınırları
        if mode in (AutonomyMode.STOP_APPROACH, AutonomyMode.MISSION_COMPLETE):
            self.can_if.emergency_stop()
            self._publish_feedback(brake=True, full_brake=False)
            return
        elif mode == AutonomyMode.PARK_MANEUVER:
            final_speed = min(raw_speed, 0.83)
        elif mode in (AutonomyMode.PICKUP_APPROACH, AutonomyMode.DROPOFF_APPROACH):
            final_speed = min(raw_speed, 0.83)
        elif mode == AutonomyMode.PARK_APPROACH:
            final_speed = min(raw_speed, 1.39)
        elif mode == AutonomyMode.OBSTACLE_AVOID:
            final_speed = min(raw_speed, 0.5) if self._obstacle_blocked else raw_speed
        elif mode == AutonomyMode.LANE_FOLLOW:
            final_speed = raw_speed
        else:
            self.get_logger().warn(f'Bilinmeyen planner_mode: {mode} — dur')
            self.can_if.emergency_stop()
            return

        delta         = self.pid.compute(self._cte, self._heading_error)
        ackermann_out = self.ackermann.compute(delta)

        self.can_if.send_command(steer_rad=delta, speed_mps=final_speed)

        self._publish_feedback(brake=(final_speed < 0.01), full_brake=False)
        self._publish_debug(delta, ackermann_out, final_speed)

    # ── Publishers ────────────────────────────────────────────────────────────

    def _publish_feedback(self, brake: bool, full_brake: bool):
        """
        ControllerFeedback.msg alanları:
          std_msgs/Header header
          float32 actual_speed, actual_steering_deg
          float32 cross_track_error, heading_error
          bool    brake_active, full_brake_active
          uint32  age_ms       ← DÜZELTİLDİ: MSG'de var
          uint32  valid_until_ms
        """
        msg = ControllerFeedback()
        msg.header.stamp        = self.get_clock().now().to_msg()
        msg.actual_speed        = float(self._actual_speed)
        msg.actual_steering_deg = float(self._actual_steer_deg)
        msg.cross_track_error   = float(self._cte)
        msg.heading_error       = float(self._heading_error)
        msg.brake_active        = brake
        msg.full_brake_active   = full_brake
        msg.age_ms              = 0
        msg.valid_until_ms      = 200
        self._feedback_pub.publish(msg)

    def _publish_debug(self, delta, ackermann_out, final_speed):
        debug = {
            'planner_mode':    self._planner_mode,
            'cte_m':           round(self._cte, 4),
            'heading_err_deg': round(math.degrees(self._heading_error), 2),
            'delta_deg':       round(math.degrees(delta), 2),
            'inner_deg':       round(math.degrees(ackermann_out.delta_inner), 2),
            'outer_deg':       round(math.degrees(ackermann_out.delta_outer), 2),
            'traj_speed':      round(self._traj_speed_mps, 2),
            'target_speed':    round(self._target_speed_mps, 2),
            'final_speed':     round(final_speed, 2),
            'loc_degraded':    self._loc_degraded,
            'emergency':       self.emergency_mgr.get_status(),
            'pid':             self.pid.debug_info,
        }
        self._debug_pub.publish(String(data=json.dumps(debug)))

    def destroy_node(self):
        self.get_logger().info('Node kapatılıyor...')
        self.can_if.disconnect()
        super().destroy_node()


def main(args=None):
    rclpy.init(args=args)
    node = BEE1ControlNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
