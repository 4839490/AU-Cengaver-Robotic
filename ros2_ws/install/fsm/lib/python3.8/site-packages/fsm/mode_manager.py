"""
AU Cengaver Robotics — Mode Manager
TEKNOFEST 2026

Mod değiştirme ve guard condition mantığı burada.
fsm_node.py bu sınıfı kullanır.

Yol haritası Adım 6, Madde 1:
  fsm_node.py: 8 mod ve transition_to() mekanizması.
"""

from common_msgs.msg import AutonomyMode
import rclpy.logging

logger = rclpy.logging.get_logger('mode_manager')

# ─────────────────────────────────────────────────────
# Guard condition tablosu
# (kaynak_mod, hedef_mod) → True ise geçişe izin var
# Sözleşme: FSM_Planner_Contract_v1.1, Bölüm 4
# ─────────────────────────────────────────────────────
_GECIS_TABLOSU = {
    # LANE_FOLLOW'dan her moda geçilebilir
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.STOP_APPROACH):    True,
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.PICKUP_APPROACH):  True,
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.DROPOFF_APPROACH): True,
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.OBSTACLE_AVOID):   True,
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.PARK_APPROACH):    True,
    (AutonomyMode.LANE_FOLLOW, AutonomyMode.MISSION_COMPLETE): True,

    # STOP_APPROACH → LANE_FOLLOW'a döner
    (AutonomyMode.STOP_APPROACH, AutonomyMode.LANE_FOLLOW): True,

    # PICKUP/DROPOFF → LANE_FOLLOW veya acil STOP
    (AutonomyMode.PICKUP_APPROACH,  AutonomyMode.LANE_FOLLOW):   True,
    (AutonomyMode.PICKUP_APPROACH,  AutonomyMode.STOP_APPROACH): True,
    (AutonomyMode.DROPOFF_APPROACH, AutonomyMode.LANE_FOLLOW):   True,
    (AutonomyMode.DROPOFF_APPROACH, AutonomyMode.STOP_APPROACH): True,

    # OBSTACLE_AVOID → LANE_FOLLOW veya STOP
    (AutonomyMode.OBSTACLE_AVOID, AutonomyMode.LANE_FOLLOW):   True,
    (AutonomyMode.OBSTACLE_AVOID, AutonomyMode.STOP_APPROACH): True,

    # PARK_APPROACH → PARK_MANEUVER veya STOP
    (AutonomyMode.PARK_APPROACH, AutonomyMode.PARK_MANEUVER): True,
    (AutonomyMode.PARK_APPROACH, AutonomyMode.STOP_APPROACH): True,

    # PARK_MANEUVER → MISSION_COMPLETE, retry veya STOP
    (AutonomyMode.PARK_MANEUVER, AutonomyMode.MISSION_COMPLETE): True,
    (AutonomyMode.PARK_MANEUVER, AutonomyMode.PARK_APPROACH):    True,
    (AutonomyMode.PARK_MANEUVER, AutonomyMode.STOP_APPROACH):    True,

    # MISSION_COMPLETE → terminal durum
}


class ModeManager:

    def __init__(self, clock):
        """
        clock: node'un get_clock() çıktısı — age_ms hesabı için gerekli
        """
        self.clock                 = clock
        self.current_mode          = AutonomyMode.LANE_FOLLOW
        self.previous_mode         = AutonomyMode.LANE_FOLLOW
        self.last_reason           = "SYSTEM_START"
        self.last_mode_change_time = clock.now()

    def transition_to(self, yeni_mod, sebep) -> bool:
        """
        Merkezi mod geçiş fonksiyonu — guard condition kontrolü içerir.

        - Aynı modsa: False döner, log atmaz
        - STOP_APPROACH: her moddan tetiklenebilir (watchdog, emergency)
        - MISSION_COMPLETE: terminal durum, çıkış yok
        - Tabloda yoksa: uyarı log, False döner
        - Başarılıysa: True döner

        Yol haritası Adım 6, Madde 1
        """
        if self.current_mode == yeni_mod:
            return False

        # STOP_APPROACH her moddan tetiklenebilir
        if yeni_mod == AutonomyMode.STOP_APPROACH:
            return self._uygula(yeni_mod, sebep)

        # MISSION_COMPLETE terminal durum — çıkış yok
        if self.current_mode == AutonomyMode.MISSION_COMPLETE:
            logger.warn(
                f"GUARD: MISSION_COMPLETE terminal — "
                f"{yeni_mod} geçişi reddedildi | {sebep}"
            )
            return False

        # Guard condition kontrolü
        if not _GECIS_TABLOSU.get((self.current_mode, yeni_mod), False):
            logger.warn(
                f"GUARD: {self.current_mode} → {yeni_mod} izinsiz geçiş "
                f"— reddedildi | {sebep}"
            )
            return False

        return self._uygula(yeni_mod, sebep)

    def _uygula(self, yeni_mod, sebep) -> bool:
        """Guard kontrolü olmadan geçişi uygular."""
        self.previous_mode         = self.current_mode
        self.current_mode          = yeni_mod
        self.last_reason           = sebep
        self.last_mode_change_time = self.clock.now()
        logger.info(f"MOD: {self.previous_mode} → {self.current_mode} | {sebep}")
        return True

    # Geriye dönük uyumluluk
    def mod_degistir(self, yeni_mod, sebep) -> bool:
        return self.transition_to(yeni_mod, sebep)

    def get_current_mode(self):
        return self.current_mode

    def get_previous_mode(self):
        return self.previous_mode

    def get_reason(self):
        return self.last_reason
