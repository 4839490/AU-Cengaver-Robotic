"""
AU Cengaver Robotics — Transition Rules
TEKNOFEST 2026

Hangi koşulda hangi moda geçileceği burada tanımlı.
fsm_node.py bu kuralları kullanır.
"""

from common_msgs.msg import AutonomyMode
from perception_msgs.msg import TrafficLightState


# ─────────────────────────────────────────────────────
# SABITLER — TrafficSign.event_status değerleri
# Sözleşme: Perception_Planner_FSM_v1.4
# ─────────────────────────────────────────────────────
STATUS_NEW             = 0
STATUS_TRACKED         = 1
STATUS_ALREADY_HANDLED = 2
STATUS_STALE           = 3

# TrafficSign.type — STOP tabelası
TYPE_STOP = 1
# TYPE_TUNNEL burada kullanılmıyor; tünel modu TargetSpeed.reason'da (planner işi)


class TransitionRules:
    """
    Karar kuralları.
    Her fonksiyon bir sinyal alır, (mod, sebep) tuple'ı veya None döner.
    None döndürürse mod değişmez.
    """

    @staticmethod
    def trafik_isigi_kural(msg, last_light_state):
        """
        Trafik ışığı mesajına göre hangi moda geçilecek?
        Sözleşme: Perception_Planner_FSM_v1.4, Bölüm 8 — Davranış Tablosu
        """
        # 1. Bize ait mi?
        if not msg.relevant_to_route:
            return None

        # 2. Teyit edildi mi? (GREEN dahil — sözleşme FIX-2.2)
        if not msg.confirmed:
            return None

        if msg.state == TrafficLightState.RED:
            return (AutonomyMode.STOP_APPROACH, "RED_LIGHT")

        elif msg.state == TrafficLightState.GREEN:
            return (AutonomyMode.LANE_FOLLOW, "GREEN_LIGHT")

        elif msg.state == TrafficLightState.UNKNOWN:
            if msg.in_stop_zone:
                return (AutonomyMode.STOP_APPROACH, "UNKNOWN_IN_STOP_ZONE")
            return None  # stop_zone dışında — hız düşür, planner işi

        elif msg.state == TrafficLightState.STALE:
            # FIX-2.3: son bilinen yeşilden STALE → konservatif moda düş
            # (eski davranış: yeşilden geliyorsa agresif devam — bu kaldırıldı)
            if last_light_state == TrafficLightState.GREEN:
                return (AutonomyMode.STOP_APPROACH, "STALE_AFTER_GREEN")
            return (AutonomyMode.STOP_APPROACH, "STALE_CONSERVATIVE")

        elif msg.state == TrafficLightState.CONFLICT:
            # CONFLICT → RED kabul et
            return (AutonomyMode.STOP_APPROACH, "LIGHT_CONFLICT")

        return None

    @staticmethod
    def serit_kural(msg):
        """
        Şerit mesajına göre hangi moda geçilecek?
        Sözleşme: Perception_Planner_FSM_v1.4, Bölüm 7
        lane_lost=true → STOP_APPROACH
        Düşük confidence log'ları fsm_node.py'da yapılır.
        """
        if msg.lane_lost:
            return (AutonomyMode.STOP_APPROACH, "LANE_LOST")
        return None

    @staticmethod
    def tabela_kural(sign):
        """
        Tek bir tabela için hangi moda geçilecek?
        Sözleşme: Perception_Planner_FSM_v1.4, Bölüm 9
        """
        if not sign.relevant_to_route:
            return None
        if sign.event_status == STATUS_ALREADY_HANDLED:
            return None
        if sign.event_status == STATUS_STALE:
            return None
        if not sign.confirmed:
            return None

        if sign.type == TYPE_STOP:
            return (AutonomyMode.STOP_APPROACH, "STOP_SIGN")

        return None
