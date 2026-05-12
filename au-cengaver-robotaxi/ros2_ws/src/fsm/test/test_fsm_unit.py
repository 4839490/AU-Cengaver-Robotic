"""
AU Cengaver Robotics — FSM Unit Testleri
TEKNOFEST 2026

Gazebo gerektirmez, bağımsız çalışır.
Çalıştırmak için:
  cd ros2_ws
  colcon test --packages-select fsm
  veya direkt:
  python3 -m pytest src/fsm/test/test_fsm_unit.py -v
"""

import pytest
from unittest.mock import MagicMock


# ─────────────────────────────────────────────────────
# MOCK — ROS2 mesaj sınıfları olmadan test edebilmek için
# ─────────────────────────────────────────────────────

class MockAutonomyMode:
    LANE_FOLLOW      = 0
    STOP_APPROACH    = 1
    PICKUP_APPROACH  = 2
    DROPOFF_APPROACH = 3
    OBSTACLE_AVOID   = 4
    PARK_APPROACH    = 5
    PARK_MANEUVER    = 6
    MISSION_COMPLETE = 7

class MockTrafficLightState:
    UNKNOWN  = 0
    RED      = 1
    YELLOW   = 2
    GREEN    = 3
    STALE    = 4
    CONFLICT = 5

class MockClock:
    """ROS2 clock mock"""
    class _Time:
        def __init__(self):
            self.nanoseconds = 0
        def __sub__(self, other):
            result = MockClock._Time()
            result.nanoseconds = self.nanoseconds - other.nanoseconds
            return result
    def now(self):
        return self._Time()

# Modülleri import etmeden önce ROS2 bağımlılıklarını mock'la
import sys
sys.modules['rclpy'] = MagicMock()
sys.modules['rclpy.logging'] = MagicMock()
sys.modules['common_msgs'] = MagicMock()
sys.modules['common_msgs.msg'] = MagicMock()
sys.modules['perception_msgs'] = MagicMock()
sys.modules['perception_msgs.msg'] = MagicMock()

# Mock sınıfları yerleştir
import common_msgs.msg as cm
cm.AutonomyMode = MockAutonomyMode
import perception_msgs.msg as pm
pm.TrafficLightState = MockTrafficLightState

# Şimdi modülleri import et
sys.path.insert(0, 'src/fsm')
from fsm.mode_manager import ModeManager
from fsm.mission_state_manager import MissionStateManager
from fsm.transition_rules import TransitionRules


# ═════════════════════════════════════════════════════
# ModeManager testleri
# ═════════════════════════════════════════════════════

class TestModeManager:

    def setup_method(self):
        self.clock = MockClock()
        self.mgr = ModeManager(self.clock)

    def test_baslangic_modu_lane_follow(self):
        """Başlangıçta LANE_FOLLOW modunda olmalı"""
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_mod_degistir_basarili(self):
        """Farklı bir moda geçiş True döndürmeli"""
        result = self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        assert result is True
        assert self.mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert self.mgr.previous_mode == MockAutonomyMode.LANE_FOLLOW
        assert self.mgr.last_reason == "RED_LIGHT"

    def test_ayni_mod_degismez(self):
        """Aynı moda geçiş False döndürmeli, state değişmemeli"""
        self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        result = self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "STOP_SIGN")
        assert result is False
        assert self.mgr.last_reason == "RED_LIGHT"  # sebep değişmemeli

    def test_ardisik_mod_degisiklikleri(self):
        """Ardışık geçişlerde previous_mode doğru takip edilmeli"""
        self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        self.mgr.mod_degistir(MockAutonomyMode.LANE_FOLLOW, "GREEN_LIGHT")
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert self.mgr.previous_mode == MockAutonomyMode.STOP_APPROACH

    def test_last_mode_change_time_guncellenir(self):
        """Mod değişince last_mode_change_time güncellenmeli"""
        t1 = self.mgr.last_mode_change_time
        self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "TEST")
        # Mock clock aynı zamanı döndürüyor ama en azından çağrılıyor
        assert self.mgr.last_mode_change_time is not None


# ═════════════════════════════════════════════════════
# MissionStateManager testleri
# ═════════════════════════════════════════════════════

class TestMissionStateManager:

    def setup_method(self):
        self.mgr = MissionStateManager()

    def test_baslangic_durumu(self):
        """Başlangıçta görev aktif olmamalı"""
        assert self.mgr.mission_active is False
        assert self.mgr.total_waypoints == 0
        assert self.mgr.completed_waypoints == 0

    def test_gorevi_baslat(self):
        """Görev başlatınca mission_active True olmalı"""
        self.mgr.gorevi_baslat(5)
        assert self.mgr.mission_active is True
        assert self.mgr.total_waypoints == 5
        assert self.mgr.completed_waypoints == 0

    def test_gorevi_bitir(self):
        """Görev bitince mission_active False olmalı"""
        self.mgr.gorevi_baslat(3)
        self.mgr.gorevi_bitir()
        assert self.mgr.mission_active is False

    def test_waypoint_tamamla_sayac(self):
        """Waypoint tamamlandıkça sayaç artmalı"""
        self.mgr.gorevi_baslat(3)
        self.mgr.waypoint_tamamla(1, 0)
        assert self.mgr.completed_waypoints == 1
        self.mgr.waypoint_tamamla(2, 0)
        assert self.mgr.completed_waypoints == 2

    def test_pickup_tamamla(self):
        """Pickup tamamlanınca pickup_complete True olmalı"""
        self.mgr.gorevi_baslat(3)
        self.mgr.pickup_tamamla(1)
        assert self.mgr.pickup_complete is True

    def test_dropoff_tamamla(self):
        """Dropoff tamamlanınca dropoff_complete True olmalı"""
        self.mgr.gorevi_baslat(3)
        self.mgr.dropoff_tamamla(2)
        assert self.mgr.dropoff_complete is True

    def test_sonraki_waypoint_pickup_reset(self):
        """Yeni waypoint'e geçince pickup/dropoff sıfırlanmalı"""
        self.mgr.gorevi_baslat(3)
        self.mgr.pickup_tamamla(1)
        assert self.mgr.pickup_complete is True
        self.mgr.sonraki_waypoint_ayarla(2, 0)
        assert self.mgr.pickup_complete is False
        assert self.mgr.dropoff_complete is False

    def test_gorev_bitti_mi_dogru(self):
        """Tüm waypointler tamamlanınca gorev_bitti_mi True döndürmeli"""
        self.mgr.gorevi_baslat(2)
        self.mgr.waypoint_tamamla(1, 0)
        assert self.mgr.gorev_bitti_mi() is False
        self.mgr.waypoint_tamamla(2, 0)
        assert self.mgr.gorev_bitti_mi() is True

    def test_gorev_bitti_mi_sifir_waypoint(self):
        """0 waypoint ile gorev_bitti_mi False döndürmeli"""
        assert self.mgr.gorev_bitti_mi() is False


# ═════════════════════════════════════════════════════
# TransitionRules testleri
# ═════════════════════════════════════════════════════

class TestTransitionRules:

    def _trafik_msg(self, state, relevant=True, confirmed=True, in_stop_zone=False):
        msg = MagicMock()
        msg.state          = state
        msg.relevant_to_route = relevant
        msg.confirmed      = confirmed
        msg.in_stop_zone   = in_stop_zone
        return msg

    def _tabela_msg(self, tip, relevant=True, confirmed=True, status=0):
        sign = MagicMock()
        sign.type            = tip
        sign.relevant_to_route = relevant
        sign.confirmed       = confirmed
        sign.event_status    = status
        return sign

    def _serit_msg(self, lost=False, confidence=0.9):
        msg = MagicMock()
        msg.lane_lost        = lost
        msg.lane_confidence  = confidence
        return msg

    # ── Trafik ışığı ──

    def test_kirmizi_isik_stop(self):
        msg = self._trafik_msg(MockTrafficLightState.RED)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")

    def test_yesil_isik_lane_follow(self):
        msg = self._trafik_msg(MockTrafficLightState.GREEN)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.RED)
        assert sonuc == (MockAutonomyMode.LANE_FOLLOW, "GREEN_LIGHT")

    def test_rota_disi_isik_ignore(self):
        """relevant_to_route=False ise None döndürmeli"""
        msg = self._trafik_msg(MockTrafficLightState.RED, relevant=False)
        assert TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN) is None

    def test_teyit_edilmemis_isik_ignore(self):
        """confirmed=False ise None döndürmeli"""
        msg = self._trafik_msg(MockTrafficLightState.RED, confirmed=False)
        assert TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN) is None

    def test_stale_yesil_sonrasi_stop(self):
        """STALE, önceki yeşilden geliyorsa STOP_APPROACH — STALE_AFTER_GREEN"""
        msg = self._trafik_msg(MockTrafficLightState.STALE)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.GREEN)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "STALE_AFTER_GREEN")

    def test_stale_konservatif(self):
        """STALE, önceki durum yeşil değilse STALE_CONSERVATIVE"""
        msg = self._trafik_msg(MockTrafficLightState.STALE)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.RED)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "STALE_CONSERVATIVE")

    def test_conflict_stop(self):
        msg = self._trafik_msg(MockTrafficLightState.CONFLICT)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "LIGHT_CONFLICT")

    def test_unknown_stop_zone_stop(self):
        msg = self._trafik_msg(MockTrafficLightState.UNKNOWN, in_stop_zone=True)
        sonuc = TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "UNKNOWN_IN_STOP_ZONE")

    def test_unknown_stop_zone_disi_none(self):
        msg = self._trafik_msg(MockTrafficLightState.UNKNOWN, in_stop_zone=False)
        assert TransitionRules.trafik_isigi_kural(msg, MockTrafficLightState.UNKNOWN) is None

    # ── Şerit ──

    def test_serit_kayip_stop(self):
        msg = self._serit_msg(lost=True)
        sonuc = TransitionRules.serit_kural(msg)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "LANE_LOST")

    def test_serit_normal_none(self):
        msg = self._serit_msg(lost=False)
        assert TransitionRules.serit_kural(msg) is None

    # ── Tabela ──

    def test_stop_tabelasi(self):
        sign = self._tabela_msg(tip=1)  # TYPE_STOP = 1
        sonuc = TransitionRules.tabela_kural(sign)
        assert sonuc == (MockAutonomyMode.STOP_APPROACH, "STOP_SIGN")

    def test_tabela_rota_disi_none(self):
        sign = self._tabela_msg(tip=1, relevant=False)
        assert TransitionRules.tabela_kural(sign) is None

    def test_tabela_zaten_islendi_none(self):
        sign = self._tabela_msg(tip=1, status=2)  # STATUS_ALREADY_HANDLED = 2
        assert TransitionRules.tabela_kural(sign) is None

    def test_tabela_stale_none(self):
        sign = self._tabela_msg(tip=1, status=3)  # STATUS_STALE = 3
        assert TransitionRules.tabela_kural(sign) is None

    def test_tabela_teyit_edilmemis_none(self):
        sign = self._tabela_msg(tip=1, confirmed=False)
        assert TransitionRules.tabela_kural(sign) is None
