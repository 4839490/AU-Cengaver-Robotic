"""
BEE1 Kontrol ROS2 Node
======================
Planner ↔ Controller Sözleşmesi v1.2
Vehicle Interface ↔ Controller CAN Sözleşmesi v1.0

MESAJ STRATEJİSİ:
  Şu an: JSON String kullanıyoruz (planning_msgs henüz eklenmedi)
  Planner planning_msgs ekleyince: import satırları değişecek,
  callback içleri aynı kalacak.

  Değişecek SADECE şu 3 yer:
    1. import satırları (en üstte)
    2. create_subscription tip argümanları
    3. callback'lerde msg.alan yerine msg["alan"]

SUBSCRİBE (Planner → Controller):
  /planning/trajectory      20Hz  JSON String → Trajectory.msg olacak
  /planning/target_speed    20Hz  JSON String → TargetSpeed.msg olacak
  /planning/status          10Hz  JSON String → PlanningStatus.msg olacak
  /emergency                olay  std_msgs/Bool (değişmeyecek)

PUBLISH (Controller → Planner):
  /controller/feedback      20Hz  JSON String → ControllerFeedback.msg olacak
  /control_debug            20Hz  JSON String (debug, değişmeyecek)

JSON FORMATLARI:
  /planning/trajectory:
    {
      "points": [{"x":0.0,"y":0.0,"yaw":0.0,"speed":0.0,"curvature":0.0}],
      "planner_mode": 0,
      "valid_until_ms": 200
    }

  /planning/target_speed:
    {
      "speed": 2.78,
      "jerk_limit": 2.0,
      "reason": 0,
      "valid_until_ms": 200
    }

  /planning/status:
    {
      "status": 0,
      "trajectory_valid": true,
      "localization_degraded": false,
      "obstacle_blocking": false,
      "lane_lost": false,
      "planner_mode": 0
    }

  /controller/feedback:
    {
      "actual_speed": 0.0,
      "actual_steering_deg": 0.0,
      "cross_track_error": 0.0,
      "heading_error": 0.0,
      "brake_active": false,
      "full_brake_active": false,
      "valid_until_ms": 200
    }
"""

import json
import math
import time
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Bool

# ── planning_msgs GELINCE BU SATIRLAR DEĞİŞECEK ──────────────────────────────
# from planning_msgs.msg import Trajectory
# from planning_msgs.msg import TargetSpeed
# from planning_msgs.msg import PlanningStatus
# from controller_msgs.msg import ControllerFeedback
# ─────────────────────────────────────────────────────────────────────────────

from ackermann_model import AckermannKinematic, AckermannParams
from hybrid_pid      import HybridPIDController, PIDConfig, PIDGains
from can_interface   import BEE1CANInterface, SteeringCalibration
from emergency_stop  import EmergencyStopManager, EmergencySource, EmergencyType


# ─── FSM Mod Sabitleri (Sözleşme v1.2 — uint8) ───────────────────────────────
class PlannerMode:
    LANE_FOLLOW      = 0
    STOP_APPROACH    = 1
    PICKUP_APPROACH  = 2
    DROPOFF_APPROACH = 3
    OBSTACLE_AVOID   = 4
    PARK_APPROACH    = 5
    PARK_MANEUVER    = 6
    MISSION_COMPLETE = 7
    EMERGENCY_STOP   = 8


# ─── Timeout Sabitleri (Sözleşme v1.2) ───────────────────────────────────────
# Timeout değerleri — Yol Haritası v1.1
TIMEOUT_NORMAL_MS  = 500    # 0-500ms    → normal
TIMEOUT_REDUCE_MS  = 1000   # 500-1000ms → hız %50 düşür
TIMEOUT_BRAKE_MS   = 1000   # >1000ms    → tam fren
FEEDBACK_RATE_HZ   = 20

class BEE1ControlNode(Node):
    """
    Ana kontrol node'u.
    Planner'dan trajectory + hız alır, CAN'e komut gönderir.
    """

    def __init__(self):
        super().__init__('bee1_control_node')

        # ── Parametreler ───────────────────────────────────────────────────────
        self.declare_parameter('wheelbase',            2.40)   # Tragger T-Car kataloğu
        self.declare_parameter('track_width',          1.03)   # Ön iz genişliği
        self.declare_parameter('max_steer_angle_deg',  32.5)   # Sözleşmeden — ölçülecek
        self.declare_parameter('min_turn_radius',      4.1)    # Sözleşmeden — ölçülecek
        self.declare_parameter('toe_in_offset',        0)      # Arazide bulunacak
        self.declare_parameter('control_rate_hz',      20.0)

        # PID kazanımları — arazide tune edilecek
        self.declare_parameter('cte_kp',     0.8)
        self.declare_parameter('cte_ki',     0.01)
        self.declare_parameter('cte_kd',     0.15)
        self.declare_parameter('heading_kp', 1.2)
        self.declare_parameter('heading_ki', 0.005)
        self.declare_parameter('heading_kd', 0.25)

        # ── Modüller ───────────────────────────────────────────────────────────
        ackermann_params = AckermannParams(
            wheelbase       = self.get_parameter('wheelbase').value,
            track_width     = self.get_parameter('track_width').value,
            max_steer_angle = math.radians(
                self.get_parameter('max_steer_angle_deg').value),
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

        # ── Emergency Stop Manager ─────────────────────────────────────────────
        self.emergency_mgr = EmergencyStopManager(
            on_software_estop = self.can_if.emergency_stop,
            on_hardware_estop = lambda: self.get_logger().error(
                'Donanımsal ESTOP gözlemlendi — safety supervisor aracı durduruyor!')
        )

        # ── Durum Değişkenleri ─────────────────────────────────────────────────
        # Trajectory
        self._cte:               float = 0.0
        self._heading_error:     float = 0.0
        self._traj_speed_mps:    float = 0.0
        self._traj_last_time:    float = 0.0
        self._traj_valid:        bool  = False
        self._traj_points:       list  = []    # tüm trajectory noktaları

        # Target speed
        self._target_speed_mps:  float = 0.0
        self._target_jerk:       float = 2.0
        self._target_reason:     int   = 0
        self._target_last_time:  float = 0.0

        # Planner status
        self._planner_mode:      int   = PlannerMode.STOP_APPROACH
        self._loc_degraded:      bool  = False
        self._obstacle_blocked:  bool  = False
        self._lane_lost:         bool  = False

        # Emergency — EmergencyStopManager ile yönetiliyor
        # self._emergency bool'u kaldırıldı → self.emergency_mgr.is_active kullan

        # Gerçek araç durumu (odometri — ağustosta encoder'dan gelecek)
        self._actual_speed:      float = 0.0
        self._actual_steer_deg:  float = 0.0

        # ── Subscriptions ──────────────────────────────────────────────────────
        # ŞU AN: JSON String kullanıyoruz
        # planning_msgs GELINCE: String → Trajectory, TargetSpeed, PlanningStatus
        self.create_subscription(
            String, '/planning/trajectory',
            self._trajectory_cb, 10)

        self.create_subscription(
            String, '/planning/target_speed',
            self._target_speed_cb, 10)

        self.create_subscription(
            String, '/planning/status',
            self._status_cb, 10)

        # Bool — değişmeyecek
        self.create_subscription(
            Bool, '/emergency',
            self._emergency_cb, 10)

        # Odometri — gerçek araçta nav_msgs/Odometry olacak
        self.create_subscription(
            String, '/odometry',
            self._odometry_cb, 10)

        # ── Publishers ────────────────────────────────────────────────────────
        # ŞU AN: JSON String
        # controller_msgs GELINCE: String → ControllerFeedback
        self._feedback_pub = self.create_publisher(
            String, '/controller/feedback', 10)

        self._debug_pub = self.create_publisher(
            String, '/control_debug', 10)

        # ── Timer ─────────────────────────────────────────────────────────────
        rate = self.get_parameter('control_rate_hz').value
        self.create_timer(1.0 / rate, self._control_loop)

        self.get_logger().info(
            'BEE1 Kontrol Node başladı — Sözleşme v1.2 / CAN v1.0')

    # ─────────────────────────────────────────────────────────────────────────
    # CALLBACKS
    # ─────────────────────────────────────────────────────────────────────────

    def _trajectory_cb(self, msg: String):
        """
        /planning/trajectory — şu an JSON String
        planning_msgs gelince: msg: Trajectory

        Beklenen JSON:
        {
          "points": [
            {"x":0.0, "y":0.0, "yaw":0.0, "speed":2.0, "curvature":0.0},
            ...
          ],
          "planner_mode": 0,
          "valid_until_ms": 200
        }

        planning_msgs gelince değişecek kısım:
          ÖNCE: data = json.loads(msg.data)
          SONRA: data = msg  (direkt msg alanları)

          ÖNCE: data["points"][0]["speed"]
          SONRA: msg.points[0].speed
        """
        try:
            data = json.loads(msg.data)

            points = data.get('points', [])
            if not points:
                self.get_logger().warn('Trajectory boş — nokta yok!')
                return

            # İlk noktadan CTE ve heading error al
            # (Stanley/PurePursuit entegre edilince burası değişecek)
            first = points[0]
            self._cte            = float(first.get('cte',           0.0))
            self._heading_error  = float(first.get('heading_error', 0.0))
            self._traj_speed_mps = float(first.get('speed',         0.0))
            self._traj_points    = points

            self._planner_mode   = int(data.get('planner_mode',   0))
            self._traj_valid     = True
            self._traj_last_time = time.monotonic()

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            self.get_logger().warn(f'Trajectory parse hatası: {e}')

    def _target_speed_cb(self, msg: String):
        """
        /planning/target_speed — şu an JSON String
        planning_msgs gelince: msg: TargetSpeed

        Beklenen JSON:
        {
          "speed": 2.78,
          "jerk_limit": 2.0,
          "reason": 0,
          "valid_until_ms": 200
        }

        planning_msgs gelince değişecek kısım:
          ÖNCE: data["speed"]
          SONRA: msg.speed
        """
        try:
            data = json.loads(msg.data)

            prev_reason = self._target_reason

            self._target_speed_mps = float(data.get('speed',      0.0))
            self._target_jerk      = float(data.get('jerk_limit', 2.0))
            self._target_reason    = int(data.get('reason',       0))
            self._target_last_time = time.monotonic()

            # EMERGENCY_STOP — reason=8
            if self._target_reason == PlannerMode.EMERGENCY_STOP:
                self.get_logger().error('EMERGENCY_STOP komutu alındı!')
                self.emergency_mgr.trigger_software(
                    EmergencySource.PLANNER,
                    'reason=8 geldi'
                )

            # Mod değişiminde PID sıfırla
            if self._target_reason != prev_reason:
                self.pid.reset()
                self.get_logger().info(
                    f'Mod değişti: {prev_reason} → {self._target_reason} — PID sıfırlandı')

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            self.get_logger().warn(f'TargetSpeed parse hatası: {e}')

    def _status_cb(self, msg: String):
        """
        /planning/status — şu an JSON String
        planning_msgs gelince: msg: PlanningStatus

        Beklenen JSON:
        {
          "status": 0,
          "trajectory_valid": true,
          "localization_degraded": false,
          "obstacle_blocking": false,
          "lane_lost": false,
          "planner_mode": 0
        }

        planning_msgs gelince değişecek kısım:
          ÖNCE: data["localization_degraded"]
          SONRA: msg.localization_degraded
        """
        try:
            data = json.loads(msg.data)

            self._traj_valid       = bool(data.get('trajectory_valid',      True))
            self._loc_degraded     = bool(data.get('localization_degraded', False))
            self._obstacle_blocked = bool(data.get('obstacle_blocking',     False))
            self._lane_lost        = bool(data.get('lane_lost',             False))
            status                 = int(data.get('status', 0))

            # EMERGENCY — status=5
            if status == 5 and not self.emergency_mgr.is_active:
                self.get_logger().error('Planner status=EMERGENCY!')
                self.emergency_mgr.trigger_software(
                    EmergencySource.PLANNING_STATUS,
                    'Planner status=5'
                )

            # MISSION_COMPLETE — status=6
            if status == 6:
                self.get_logger().info('MISSION_COMPLETE — el freni çekiliyor.')
                self.can_if.park_complete()

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            self.get_logger().warn(f'PlanningStatus parse hatası: {e}')

    def _emergency_cb(self, msg: Bool):
        """Donanımsal acil sinyal — Bool, değişmeyecek."""
        if msg.data:
            self.get_logger().error('Donanımsal EMERGENCY sinyali alındı!')
            self.emergency_mgr.trigger_hardware_observed(
                '/emergency=True — safety supervisor tetikledi'
            )
        else:
            # Sinyal kalktı — donanımsal reset
            self.emergency_mgr.reset_hardware()

    def _odometry_cb(self, msg: String):
        """
        Odometri — gerçek araçta nav_msgs/Odometry olacak.
        Şu an JSON: {"speed": 0.0, "steering_deg": 0.0}
        """
        try:
            data = json.loads(msg.data)
            self._actual_speed     = float(data.get('speed',        0.0))
            self._actual_steer_deg = float(data.get('steering_deg', 0.0))
        except (json.JSONDecodeError, KeyError, TypeError):
            pass

    # ─────────────────────────────────────────────────────────────────────────
    # ANA KONTROL DÖNGÜSÜ
    # ─────────────────────────────────────────────────────────────────────────

    def _control_loop(self):
        """20Hz ana kontrol döngüsü."""
        now = time.monotonic()

        # ── Timeout kontrolleri (Sözleşme v1.2) ──────────────────────────────
        traj_age   = (now - self._traj_last_time)   * 1000  # ms
        target_age = (now - self._target_last_time) * 1000  # ms

        # ── Trajectory timeout — üç kademeli (Yol Haritası v1.1) ──────────────
        if self._traj_last_time > 0:
            if traj_age > TIMEOUT_BRAKE_MS:
                # > 1000ms → tam fren
                self.get_logger().warn(
                    f'Trajectory timeout! {traj_age:.0f}ms > {TIMEOUT_BRAKE_MS}ms — TAM FREN')
                self.emergency_mgr.trigger_software(
                    EmergencySource.TRAJECTORY,
                    f'Trajectory {traj_age:.0f}ms gelmedi',
                    EmergencyType.TRAJECTORY_TIMEOUT
                )
                self._publish_feedback(brake=True, full_brake=True)
                return
            elif traj_age > TIMEOUT_NORMAL_MS:
                # 500-1000ms → hız %50 düşür, devam et
                self.get_logger().warn(
                    f'Trajectory geç! {traj_age:.0f}ms > {TIMEOUT_NORMAL_MS}ms — hız %50 düşürüldü')
                self._traj_speed_mps *= 0.5

        # ── Target speed timeout — üç kademeli ───────────────────────────────
        if self._target_last_time > 0:
            if target_age > TIMEOUT_BRAKE_MS:
                # > 1000ms → tam fren
                self.get_logger().warn(
                    f'TargetSpeed timeout! {target_age:.0f}ms > {TIMEOUT_BRAKE_MS}ms — TAM FREN')
                self.emergency_mgr.trigger_software(
                    EmergencySource.TARGET_SPEED,
                    f'TargetSpeed {target_age:.0f}ms gelmedi',
                    EmergencyType.TARGET_SPEED_TIMEOUT
                )
                self._publish_feedback(brake=True, full_brake=True)
                return
            elif target_age > TIMEOUT_NORMAL_MS:
                # 500-1000ms → son hızı koru, devam et
                self.get_logger().warn(
                    f'TargetSpeed geç! {target_age:.0f}ms > {TIMEOUT_NORMAL_MS}ms — son hız korunuyor')

        # ── Acil durum ────────────────────────────────────────────────────────
        if self.emergency_mgr.is_active:
            self._publish_feedback(brake=True, full_brake=True)
            return

        mode = self._planner_mode

        # ── Hız öncelik kuralı (Sözleşme v1.2 FIX-5) ────────────────────────
        # final_speed = min(target_speed, trajectory_point.speed)
        raw_speed = min(self._target_speed_mps, self._traj_speed_mps)

        # Lokalizasyon zayıfsa %50 düşür
        if self._loc_degraded:
            raw_speed *= 0.5
            self.get_logger().warn('Lokalizasyon zayıf — hız %50 düşürüldü.')

        # ── Mod bazlı hız sınırları ───────────────────────────────────────────
        if mode in (PlannerMode.STOP_APPROACH, PlannerMode.MISSION_COMPLETE):
            self.can_if.emergency_stop()
            self._publish_feedback(brake=True, full_brake=False)
            return

        elif mode == PlannerMode.PARK_MANEUVER:
            final_speed = min(raw_speed, 0.83)   # max 3 km/h

        elif mode in (PlannerMode.PICKUP_APPROACH, PlannerMode.DROPOFF_APPROACH):
            final_speed = min(raw_speed, 0.83)   # max 3 km/h

        elif mode == PlannerMode.PARK_APPROACH:
            final_speed = min(raw_speed, 1.39)   # max 5 km/h

        elif mode == PlannerMode.OBSTACLE_AVOID:
            final_speed = min(raw_speed, 0.5) if self._obstacle_blocked else raw_speed

        elif mode == PlannerMode.LANE_FOLLOW:
            final_speed = raw_speed

        else:
            self.get_logger().warn(f'Bilinmeyen planner_mode: {mode} — dur')
            self.can_if.emergency_stop()
            return

        # ── PID + Ackermann ───────────────────────────────────────────────────
        delta         = self.pid.compute(self._cte, self._heading_error)
        ackermann_out = self.ackermann.compute(delta)

        # ── CAN'e gönder ──────────────────────────────────────────────────────
        self.can_if.send_command(
            steer_rad = delta,
            speed_mps = final_speed,
        )

        # ── Feedback yayınla ──────────────────────────────────────────────────
        brake = (final_speed < 0.01)
        self._publish_feedback(brake=brake, full_brake=False)

        # ── Debug yayınla ─────────────────────────────────────────────────────
        self._publish_debug(delta, ackermann_out, final_speed)

    # ─────────────────────────────────────────────────────────────────────────
    # PUBLISHER FONKSİYONLARI
    # ─────────────────────────────────────────────────────────────────────────

    def _publish_feedback(self, brake: bool, full_brake: bool):
        """
        /controller/feedback — şu an JSON String
        controller_msgs gelince: ControllerFeedback msg olacak

        Değişecek kısım:
          ÖNCE:
            msg = String(data=json.dumps({...}))
            self._feedback_pub.publish(msg)

          SONRA:
            msg = ControllerFeedback()
            msg.actual_speed = self._actual_speed
            msg.cross_track_error = self._cte
            ...
            self._feedback_pub.publish(msg)
        """
        feedback = {
            'actual_speed':        round(self._actual_speed,     3),
            'actual_steering_deg': round(self._actual_steer_deg, 2),
            'cross_track_error':   round(self._cte,              4),
            'heading_error':       round(self._heading_error,    4),
            'brake_active':        brake,
            'full_brake_active':   full_brake,
            'valid_until_ms':      200,
        }
        self._feedback_pub.publish(String(data=json.dumps(feedback)))

    def _publish_debug(self, delta, ackermann_out, final_speed):
        """Debug bilgisi — değişmeyecek."""
        debug = {
            'planner_mode':    self._planner_mode,
            'cte_m':           round(self._cte,                          4),
            'heading_err_deg': round(math.degrees(self._heading_error),  2),
            'delta_deg':       round(math.degrees(delta),                2),
            'inner_deg':       round(math.degrees(ackermann_out.delta_inner), 2),
            'outer_deg':       round(math.degrees(ackermann_out.delta_outer), 2),
            'traj_speed':      round(self._traj_speed_mps,               2),
            'target_speed':    round(self._target_speed_mps,             2),
            'final_speed':     round(final_speed,                        2),
            'loc_degraded':    self._loc_degraded,
            'emergency':       self.emergency_mgr.get_status(),
            'pid':             self.pid.debug_info,
        }
        self._debug_pub.publish(String(data=json.dumps(debug)))

    # ── Node Kapatma ─────────────────────────────────────────────────────────

    def destroy_node(self):
        self.get_logger().info('Node kapatılıyor...')
        self.can_if.disconnect()
        super().destroy_node()


# ─── Entry Point ──────────────────────────────────────────────────────────────
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
