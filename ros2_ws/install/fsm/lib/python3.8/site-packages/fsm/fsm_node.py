#!/usr/bin/env python3
"""
AU Cengaver Robotics — FSM Node
TEKNOFEST 2026

Sorumlu: Murat Üsame Üstün

Bu dosya sistemin karar merkezidir.
Algılama ve planner'dan gelen sinyallere bakarak
aracın hangi modda olduğuna karar verir ve tüm sisteme yayınlar.

Yol haritası Adım 6:
  1. 8 mod ve transition_to() mekanizması          ✅ mode_manager.py
  2. /fsm/current_mode (10 Hz) + /fsm/mission_state (5 Hz) ✅
  3. stop_reason ayrımı                             ✅
  4. Guard condition + watchdog                     ✅ watchdog.py
  5. mission_active=false → planner trajectory üretmez ✅
  6. Safety supervisor sinyalini izle/logla         ✅
  7. F-01/02, F-04/05/06, F-13 testleri            → test/

Yardımcı modüller:
  mode_manager.py          — transition_to() + guard conditions
  watchdog.py              — stale topic tespiti
  transition_rules.py      — karar kuralları
  event_handler.py         — event gönderme
  mission_state_manager.py — görev takibi
"""

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy, HistoryPolicy

from fsm_msgs.msg import CurrentMode, MissionState, FSMEvent
from planning_msgs.msg import PlanningStatus, GoalReached, ParkComplete, FSMRequest
from perception_msgs.msg import TrafficLightState, LaneModel, TrafficSigns, ObstacleTracks, StopTarget
from localization_msgs.msg import LocalizationStatus
from common_msgs.msg import AutonomyMode

from fsm.mode_manager import ModeManager
from fsm.watchdog import FSMWatchdog
from fsm.transition_rules import TransitionRules
from fsm.event_handler import EventHandler
from fsm.mission_state_manager import MissionStateManager


# ─────────────────────────────────────────────────────
# QoS — sözleşmede tanımlı, değiştirme
# ─────────────────────────────────────────────────────
QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)

# ─────────────────────────────────────────────────────
# stop_reason haritası — CurrentMode.msg sabitleriyle eşleşmeli
# Sözleşme: FSM_Planner_Contract_v1.1, Bölüm 5
# ─────────────────────────────────────────────────────
_STOP_REASON = {
    "RED_LIGHT":                  CurrentMode.STOP_RED_LIGHT,
    "UNKNOWN_IN_STOP_ZONE":       CurrentMode.STOP_RED_LIGHT,     # konservatif
    "STALE_AFTER_GREEN":          CurrentMode.STOP_RED_LIGHT,     # konservatif
    "STALE_CONSERVATIVE":         CurrentMode.STOP_RED_LIGHT,
    "LIGHT_CONFLICT":             CurrentMode.STOP_RED_LIGHT,
    "STOP_SIGN":                  CurrentMode.STOP_STOP_SIGN,
    "OBSTACLE_TTC":               CurrentMode.STOP_OBSTACLE_TTC,
    "LANE_LOST":                  CurrentMode.STOP_STALE_SENSOR,
    "LOCALIZATION_LOST":          CurrentMode.STOP_LOCALIZATION_LOST,
    "MISSION_ABORT":              CurrentMode.STOP_MISSION_ABORT,
    "PLANNER_EMERGENCY":          CurrentMode.STOP_MISSION_ABORT,
    "WATCHDOG_PLANNER_STALE":     CurrentMode.STOP_STALE_SENSOR,
    "WATCHDOG_LOCALIZATION_STALE": CurrentMode.STOP_LOCALIZATION_LOST,
    "WATCHDOG_PERCEPTION_STALE":  CurrentMode.STOP_STALE_SENSOR,
}


class FSMNode(Node):

    def __init__(self):
        super().__init__('fsm_node')

        # ─────────────────────────────────────────────
        # YARDIMCI MODÜLLER
        # ─────────────────────────────────────────────
        self.mode_mgr    = ModeManager(self.get_clock())
        self.mission_mgr = MissionStateManager()

        # Watchdog — stale topic tespiti (F-13)
        self.watchdog = FSMWatchdog(
            clock=self.get_clock(),
            mod_degistir_fn=self.mode_mgr.transition_to
        )

        # Trafik ışığı son bilinen durum — STALE kararı için
        # FIX: önce state sakla, sonra kural çalıştır
        self.last_light_state = TrafficLightState.UNKNOWN

        # PICKUP/DROPOFF yaklaşım durumu
        self.pickup_approach_aktif  = False
        self.dropoff_approach_aktif = False

        self.get_logger().info("FSM başladı — mod: LANE_FOLLOW, görev bekleniyor")

        # ─────────────────────────────────────────────
        # PUBLISHER'LAR
        # ─────────────────────────────────────────────
        self.pub_mode    = self.create_publisher(CurrentMode,  '/fsm/current_mode',  QOS)
        self.pub_mission = self.create_publisher(MissionState, '/fsm/mission_state', QOS)
        self.pub_event   = self.create_publisher(FSMEvent,     '/fsm/event',         QOS)

        self.event_hdlr = EventHandler(self.pub_event, self.get_clock())

        # ─────────────────────────────────────────────
        # SUBSCRIBER'LAR
        # ─────────────────────────────────────────────

        # Perception'dan
        self.create_subscription(TrafficLightState, '/perception/traffic_light_state', self.cb_trafik_isigi, QOS)
        self.create_subscription(LaneModel,         '/perception/lane_model',          self.cb_serit,        QOS)
        self.create_subscription(TrafficSigns,      '/perception/traffic_signs',       self.cb_tabela,       QOS)
        self.create_subscription(ObstacleTracks,    '/perception/obstacle_tracks',     self.cb_engel,        QOS)
        self.create_subscription(StopTarget,        '/perception/stop_target',         self.cb_dur_noktasi,  QOS)

        # Planner'dan
        self.create_subscription(GoalReached,    '/planning/goal_reached',  self.cb_waypoint_tamam, QOS)
        self.create_subscription(FSMRequest,     '/planning/fsm_request',   self.cb_planner_istegi, QOS)
        self.create_subscription(ParkComplete,   '/planning/park_complete', self.cb_park_tamam,     QOS)
        self.create_subscription(PlanningStatus, '/planning/status',        self.cb_planner_durum,  QOS)

        # Lokalizasyondan
        self.create_subscription(LocalizationStatus, '/localization/status', self.cb_lokalizasyon, QOS)

        # ─────────────────────────────────────────────
        # TIMER'LAR
        # ─────────────────────────────────────────────
        self.create_timer(0.1, self.yayinla_mod)      # 10 Hz — aynı zamanda watchdog
        self.create_timer(0.2, self.yayinla_gorev)    # 5 Hz


    # ═════════════════════════════════════════════════
    # CALLBACK'LER — perception'dan
    # ═════════════════════════════════════════════════

    def cb_trafik_isigi(self, msg):
        # Watchdog'u besle
        self.watchdog.trafik_isigi.besle(self.get_clock())

        # FIX: önce state güncelle, sonra kural çalıştır
        self.last_light_state = msg.state
        sonuc = TransitionRules.trafik_isigi_kural(msg, self.last_light_state)
        if sonuc:
            mod, sebep = sonuc
            self.mode_mgr.transition_to(mod, sebep)

        if msg.state == TrafficLightState.YELLOW and msg.relevant_to_route and msg.confirmed:
            self.get_logger().info("Sarı ışık — planner yavaşlıyor")

    def cb_serit(self, msg):
        # Watchdog'u besle
        self.watchdog.serit.besle(self.get_clock())

        sonuc = TransitionRules.serit_kural(msg)
        if sonuc:
            mod, sebep = sonuc
            self.mode_mgr.transition_to(mod, sebep)
            self.get_logger().warn("Şerit kayboldu!")
        elif msg.lane_confidence < 0.4:
            self.get_logger().warn(f"Şerit güveni çok düşük: {msg.lane_confidence:.2f}")
        elif msg.lane_confidence < 0.7:
            self.get_logger().info(f"Şerit güveni düşük: {msg.lane_confidence:.2f}")

    def cb_tabela(self, msg):
        for sign in msg.signs:
            sonuc = TransitionRules.tabela_kural(sign)
            if sonuc:
                mod, sebep = sonuc
                self.mode_mgr.transition_to(mod, sebep)

    def cb_engel(self, msg):
        """
        Sözleşme: Perception_Planner_FSM_v1.4, Bölüm 6
        FIX: ObstacleTrack.msg'de in_path alanı YOK — yol haritası Bağlayıcı Mimari Kararlar.
             TTC eşiği planner planned_trajectory ile hesaplar.
             FSM sadece ttc < 2s eşiğine bakar, in_path koşulu olmadan.
        10s hareketsiz statik engel → replanning_request
        """
        # Watchdog'u besle
        self.watchdog.engeller.besle(self.get_clock())

        for track in msg.tracks:
            # TTC kritik eşik — in_path alanı mesajda YOK
            if hasattr(track, 'ttc') and 0 < track.ttc < 2.0:
                self.get_logger().warn(
                    f"Engel {track.track_id} TTC={track.ttc:.1f}s — STOP_APPROACH"
                )
                self.mode_mgr.transition_to(AutonomyMode.STOP_APPROACH, "OBSTACLE_TTC")
                return

            # 10s hareketsiz statik engel → replanning
            if track.is_static and track.age_ms > 10000:
                self.get_logger().warn(
                    f"Engel {track.track_id} 10s hareketsiz — replanning"
                )
                self.event_hdlr.replanning_request(
                    self.mission_mgr.current_waypoint_id,
                    f"static_obstacle_{track.track_id}"
                )
                return

    def cb_dur_noktasi(self, msg):
        """
        StopTarget — pickup/dropoff hedefine yaklaşıldığında moda geç.
        Sözleşme: FSM mod geçiş tablosu — PICKUP_APPROACH / DROPOFF_APPROACH
        """
        if msg.target_type == StopTarget.TARGET_PICKUP:
            if not self.pickup_approach_aktif:
                self.pickup_approach_aktif = True
                self.mode_mgr.transition_to(AutonomyMode.PICKUP_APPROACH, "PICKUP_APPROACH_START")
                self.get_logger().info(
                    f"Pickup yakın — {msg.distance_from_front_bumper:.1f}m"
                )

        elif msg.target_type == StopTarget.TARGET_DROPOFF:
            if not self.dropoff_approach_aktif:
                self.dropoff_approach_aktif = True
                self.mode_mgr.transition_to(AutonomyMode.DROPOFF_APPROACH, "DROPOFF_APPROACH_START")
                self.get_logger().info(
                    f"Dropoff yakın — {msg.distance_from_front_bumper:.1f}m"
                )


    # ═════════════════════════════════════════════════
    # CALLBACK'LER — planner'dan
    # ═════════════════════════════════════════════════

    def cb_waypoint_tamam(self, msg):
        if not msg.success:
            return

        if msg.waypoint_type == GoalReached.PICKUP:
            self.event_hdlr.pickup_complete(msg.waypoint_id)
            self.mission_mgr.pickup_tamamla(msg.waypoint_id)
            self.pickup_approach_aktif = False
            self.mode_mgr.transition_to(AutonomyMode.LANE_FOLLOW, "PICKUP_DONE")
            self.get_logger().info(f"Pickup tamamlandı — wp {msg.waypoint_id}")

        elif msg.waypoint_type == GoalReached.DROPOFF:
            self.event_hdlr.dropoff_complete(msg.waypoint_id)
            self.mission_mgr.dropoff_tamamla(msg.waypoint_id)
            self.dropoff_approach_aktif = False
            self.mode_mgr.transition_to(AutonomyMode.LANE_FOLLOW, "DROPOFF_DONE")
            self.get_logger().info(f"Dropoff tamamlandı — wp {msg.waypoint_id}")

        elif msg.waypoint_type == GoalReached.WAYPOINT:
            self.mission_mgr.waypoint_tamamla(msg.waypoint_id, 2)
            self.mode_mgr.transition_to(AutonomyMode.LANE_FOLLOW, "WAYPOINT_REACHED")

        elif msg.waypoint_type == GoalReached.PARK_ENTRY:
            self.mode_mgr.transition_to(AutonomyMode.PARK_APPROACH, "PARK_ENTRY_REACHED")
            self.get_logger().info("Park girişine ulaşıldı — PARK_READY bekleniyor")

    def cb_planner_istegi(self, msg):
        if msg.request_type == FSMRequest.MODE_CHANGE:
            self.mode_mgr.transition_to(msg.requested_mode, "PLANNER_MODE_CHANGE")

        elif msg.request_type == FSMRequest.REPLANNING_NEEDED:
            self.event_hdlr.replanning_request(msg.waypoint_id)

        elif msg.request_type == FSMRequest.GOAL_CONFIRMED:
            self.get_logger().info(f"Waypoint {msg.waypoint_id} onaylandı")

        elif msg.request_type == FSMRequest.OBSTACLE_BLOCKED:
            self.mode_mgr.transition_to(AutonomyMode.OBSTACLE_AVOID, "OBSTACLE_BLOCKED")

        elif msg.request_type == FSMRequest.LOCALIZATION_DEGRADED:
            self.get_logger().warn("Lokalizasyon bozuk — planner hız düşürüyor")

        elif msg.request_type == FSMRequest.PARK_READY:
            self.mode_mgr.transition_to(AutonomyMode.PARK_MANEUVER, "PARK_READY")
            self.get_logger().info("Park manevrası başlıyor")

        else:
            self.get_logger().warn(
                f"Bilinmeyen FSMRequest tipi: {msg.request_type} — işlenmedi"
            )

    def cb_park_tamam(self, msg):
        if msg.success:
            self.mode_mgr.transition_to(AutonomyMode.MISSION_COMPLETE, "PARK_COMPLETE")
            self.mission_mgr.gorevi_bitir()
            self.get_logger().info("Görev tamamlandı!")
        else:
            self.get_logger().warn("Park başarısız — tekrar deneniyor")
            self.mode_mgr.transition_to(AutonomyMode.PARK_APPROACH, "PARK_FAILED_RETRY")

    def cb_planner_durum(self, msg):
        # Watchdog'u besle
        self.watchdog.planner.besle(self.get_clock())

        if msg.status == PlanningStatus.EMERGENCY:
            self.get_logger().error("Planner EMERGENCY!")
            # Önce modu değiştir — controller STOP_APPROACH'ı görür
            self.mode_mgr.transition_to(AutonomyMode.STOP_APPROACH, "PLANNER_EMERGENCY")
            # Sonra event gönder
            self.event_hdlr.emergency_stop("PLANNER_EMERGENCY")


    # ═════════════════════════════════════════════════
    # CALLBACK — lokalizasyondan
    # ═════════════════════════════════════════════════

    def cb_lokalizasyon(self, msg):
        # Watchdog'u besle
        self.watchdog.lokalizasyon.besle(self.get_clock())

        if msg.status == LocalizationStatus.LOST:
            self.mode_mgr.transition_to(AutonomyMode.STOP_APPROACH, "LOCALIZATION_LOST")
            self.get_logger().error("Lokalizasyon LOST!")
        elif msg.status == LocalizationStatus.DEGRADED:
            self.get_logger().warn("Lokalizasyon DEGRADED — izleniyor")


    # ═════════════════════════════════════════════════
    # PERİYODİK YAYINLAR
    # ═════════════════════════════════════════════════

    def yayinla_mod(self):
        """
        Her 100ms'de — 10 Hz
        Aynı zamanda watchdog kontrolü yapılır.
        Yol haritası Adım 6, Madde 4: Guard condition + watchdog
        """
        # Watchdog kontrolü — F-13
        self.watchdog.kontrol(self.mode_mgr.current_mode)

        now = self.get_clock().now()
        msg = CurrentMode()
        msg.header.stamp   = now.to_msg()
        msg.mode           = self.mode_mgr.current_mode
        msg.previous_mode  = self.mode_mgr.previous_mode
        msg.reason         = self.mode_mgr.last_reason
        msg.waypoint_id    = self.mission_mgr.current_waypoint_id
        msg.valid_until_ms = 500

        # stop_reason: sadece STOP_APPROACH modunda anlamlı
        if self.mode_mgr.current_mode == AutonomyMode.STOP_APPROACH:
            msg.stop_reason = _STOP_REASON.get(
                self.mode_mgr.last_reason,
                CurrentMode.STOP_NONE
            )
        else:
            msg.stop_reason = CurrentMode.STOP_NONE

        # age_ms: mod son değiştiğinden bu yana geçen süre
        elapsed_ns = (now - self.mode_mgr.last_mode_change_time).nanoseconds
        msg.age_ms = int(elapsed_ns / 1_000_000)

        self.pub_mode.publish(msg)

    def yayinla_gorev(self):
        """
        Her 200ms'de — 5 Hz
        Yol haritası Adım 6, Madde 5:
          mission_active=false iken planner trajectory üretmez.
          Bu mesajı gören planner bu kuralı uygular.
        """
        m = self.mission_mgr
        msg = MissionState()
        msg.header.stamp          = self.get_clock().now().to_msg()
        msg.mission_active        = m.mission_active
        msg.total_waypoints       = m.total_waypoints
        msg.completed_waypoints   = m.completed_waypoints
        msg.current_waypoint_id   = m.current_waypoint_id
        msg.current_waypoint_type = m.current_waypoint_type
        msg.next_waypoint_id      = m.next_waypoint_id
        msg.next_waypoint_type    = m.next_waypoint_type
        msg.pickup_complete       = m.pickup_complete
        msg.dropoff_complete      = m.dropoff_complete
        msg.valid_until_ms        = 1000
        self.pub_mission.publish(msg)


# ─────────────────────────────────────────────────────
# GİRİŞ NOKTASI
# ─────────────────────────────────────────────────────

def main(args=None):
    rclpy.init(args=args)
    node = FSMNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
