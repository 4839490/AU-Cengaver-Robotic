"""
AU Cengaver Robotics — Mode Manager
TEKNOFEST 2026

Mod değiştirme mantığı burada.
fsm_node.py bu sınıfı kullanır.
"""

from common_msgs.msg import AutonomyMode
import rclpy.logging

logger = rclpy.logging.get_logger('mode_manager')


class ModeManager:

    def __init__(self, clock):
        """
        clock: node'un get_clock() çıktısı — age_ms hesabı için gerekli
        """
        self.clock             = clock
        self.current_mode      = AutonomyMode.LANE_FOLLOW
        self.previous_mode     = AutonomyMode.LANE_FOLLOW
        self.last_reason       = "SYSTEM_START"
        # age_ms hesabı için — başlangıçta şimdiki zaman
        self.last_mode_change_time = clock.now()

    def mod_degistir(self, yeni_mod, sebep):
        """
        Modu değiştir.
        Zaten aynı moddaysa hiçbir şey yapma.
        """
        if self.current_mode == yeni_mod:
            return False  # değişmedi

        self.previous_mode         = self.current_mode
        self.current_mode          = yeni_mod
        self.last_reason           = sebep
        self.last_mode_change_time = self.clock.now()

        logger.info(f"MOD: {self.previous_mode} → {self.current_mode} | {sebep}")
        return True  # değişti

    def get_current_mode(self):
        return self.current_mode

    def get_previous_mode(self):
        return self.previous_mode

    def get_reason(self):
        return self.last_reason
