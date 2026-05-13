"""
AU Cengaver Robotics — FSM Unit Testleri
TEKNOFEST 2026

Gazebo gerektirmez, bağımsız çalışır.
Çalıştırmak için:
  cd ros2_ws
  colcon test --packages-select fsm
  veya:
  python3 -m pytest src/fsm/test/test_fsm_unit.py -v
"""

import pytest
from unittest.mock import MagicMock
import sys


# ─────────────────────────────────────────────────────
# MOCK
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

class MockTime:
    def __init__(self, ns=0):
        self.nanoseconds = ns
    def __sub__(self, other):
        r = MockTime()
        r.nanoseconds = self.nanoseconds - other.nanoseconds
        return r

class MockClock:
    def __init__(self, ns=0):
        self._ns = ns
    def now(self):
        return MockTime(self._ns)
    def advance(self, ms):
        self._ns += ms * 1_000_000

sys.modules['rclpy']                = MagicMock()
sys.modules['rclpy.logging']        = MagicMock()
sys.modules['common_msgs']          = MagicMock()
sys.modules['common_msgs.msg']      = MagicMock()
sys.modules['perception_msgs']      = MagicMock()
sys.modules['perception_msgs.msg']  = MagicMock()

import common_msgs.msg as cm
cm.AutonomyMode = MockAutonomyMode
import perception_msgs.msg as pm
pm.TrafficLightState = MockTrafficLightState

sys.path.insert(0, 'src/fsm')
from fsm.mode_manager import ModeManager
from fsm.mission_state_manager import MissionStateManager
from fsm.transition_rules import TransitionRules
from fsm.watchdog import FSMWatchdog


# ═════════════════════════════════════════════════════
# ModeManager — temel testler
# ═════════════════════════════════════════════════════

class TestModeManager:

    def setup_method(self):
        self.clock = MockClock()
        self.mgr   = ModeManager(self.clock)

    def test_baslangic_lane_follow(self):
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_transition_to_basarili(self):
        result = self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        assert result is True
        assert self.mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert self.mgr.previous_mode == MockAutonomyMode.LANE_FOLLOW
        assert self.mgr.last_reason == "RED_LIGHT"

    def test_ayni_mod_degismez(self):
        self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        result = self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "STOP_SIGN")
        assert result is False
        assert self.mgr.last_reason == "RED_LIGHT"

    def test_ardisik_gecisler(self):
        self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        self.mgr.transition_to(MockAutonomyMode.LANE_FOLLOW, "GREEN_LIGHT")
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert self.mgr.previous_mode == MockAutonomyMode.STOP_APPROACH

    def test_mod_degistir_geriye_uyumlu(self):
        result = self.mgr.mod_degistir(MockAutonomyMode.STOP_APPROACH, "TEST")
        assert result is True


# ═════════════════════════════════════════════════════
# Guard condition testleri
# ═════════════════════════════════════════════════════

class TestGuardConditions:

    def setup_method(self):
        self.clock = MockClock()
        self.mgr   = ModeManager(self.clock)

    def test_stop_approach_her_moddan_tetiklenir(self):
        self.mgr._uygula(MockAutonomyMode.PICKUP_APPROACH, "TEST")
        result = self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "EMERGENCY")
        assert result is True

    def test_mission_complete_terminal(self):
        self.mgr._uygula(MockAutonomyMode.MISSION_COMPLETE, "PARK_COMPLETE")
        result = self.mgr.transition_to(MockAutonomyMode.LANE_FOLLOW, "DENEME")
        assert result is False
        assert self.mgr.current_mode == MockAutonomyMode.MISSION_COMPLETE

    def test_stop_approach_park_maneuver_reddedilir(self):
        self.mgr.transition_to(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        result = self.mgr.transition_to(MockAutonomyMode.PARK_MANEUVER, "DENEME")
        assert result is False

    def test_lane_follow_park_approach_izinli(self):
        result = self.mgr.transition_to(MockAutonomyMode.PARK_APPROACH, "PARK_ENTRY")
        assert result is True

    def test_park_approach_park_maneuver_izinli(self):
        self.mgr._uygula(MockAutonomyMode.PARK_APPROACH, "PARK_ENTRY")
        result = self.mgr.transition_to(MockAutonomyMode.PARK_MANEUVER, "PARK_READY")
        assert result is True

    def test_park_maneuver_mission_complete_izinli(self):
        self.mgr._uygula(MockAutonomyMode.PARK_MANEUVER, "PARK_READY")
        result = self.mgr.transition_to(MockAutonomyMode.MISSION_COMPLETE, "PARK_COMPLETE")
        assert result is True

    def test_obstacle_avoid_lane_follow_izinli(self):
        self.mgr._uygula(MockAutonomyMode.OBSTACLE_AVOID, "BLOCKED")
        result = self.mgr.transition_to(MockAutonomyMode.LANE_FOLLOW, "CLEARED")
        assert result is True


# ═════════════════════════════════════════════════════
# Watchdog testleri — F-13
# ═════════════════════════════════════════════════════

class TestFSMWatchdog:

    def setup_method(self):
        self.clock    = MockClock()
        self.mgr      = ModeManager(self.clock)
        self.watchdog = FSMWatchdog(
            clock=self.clock,
            mod_degistir_fn=self.mgr.transition_to
        )

    def test_beslenince_stale_degil(self):
        self.watchdog.planner.besle(self.clock)
        assert self.watchdog.planner.stale_mi(self.clock) is False

    def test_hic_beslenmemis_stale_degil(self):
        assert self.watchdog.planner.stale_mi(self.clock) is False

    def test_planner_1001ms_stale_stop(self):
        """F-13: 1001ms sessiz → STOP_APPROACH"""
        self.watchdog.planner.besle(self.clock)
        self.clock.advance(1001)
        self.watchdog.kontrol(MockAutonomyMode.LANE_FOLLOW)
        assert self.mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert self.mgr.last_reason == "WATCHDOG_PLANNER_STALE"

    def test_planner_600ms_hala_tamam(self):
        """F-13: 600ms sonra koru — STOP_APPROACH değil"""
        self.watchdog.planner.besle(self.clock)
        self.clock.advance(600)
        self.watchdog.kontrol(MockAutonomyMode.LANE_FOLLOW)
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_lokalizasyon_stale_stop(self):
        self.watchdog.lokalizasyon.besle(self.clock)
        self.clock.advance(601)
        self.watchdog.kontrol(MockAutonomyMode.LANE_FOLLOW)
        assert self.mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert self.mgr.last_reason == "WATCHDOG_LOCALIZATION_STALE"

    def test_zaten_stop_approach_watchdog_calismaz(self):
        self.mgr._uygula(MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")
        self.watchdog.planner.besle(self.clock)
        self.clock.advance(2000)
        self.watchdog.kontrol(MockAutonomyMode.STOP_APPROACH)
        assert self.mgr.last_reason == "RED_LIGHT"  # değişmemeli

    def test_mission_complete_watchdog_calismaz(self):
        self.mgr._uygula(MockAutonomyMode.MISSION_COMPLETE, "PARK_COMPLETE")
        self.watchdog.planner.besle(self.clock)
        self.clock.advance(2000)
        self.watchdog.kontrol(MockAutonomyMode.MISSION_COMPLETE)
        assert self.mgr.current_mode == MockAutonomyMode.MISSION_COMPLETE

    def test_tum_perception_stale_stop(self):
        self.watchdog.trafik_isigi.besle(self.clock)
        self.watchdog.serit.besle(self.clock)
        self.watchdog.engeller.besle(self.clock)
        self.clock.advance(601)
        self.watchdog.kontrol(MockAutonomyMode.LANE_FOLLOW)
        assert self.mgr.current_mode == MockAutonomyMode.STOP_APPROACH

    def test_kismi_perception_stale_mod_degismez(self):
        self.watchdog.trafik_isigi.besle(self.clock)
        self.watchdog.serit.besle(self.clock)
        self.clock.advance(601)
        # iki tane stale oldu ama üçü değil
        self.watchdog.kontrol(MockAutonomyMode.LANE_FOLLOW)
        assert self.mgr.current_mode == MockAutonomyMode.LANE_FOLLOW


# ═════════════════════════════════════════════════════
# MissionStateManager testleri
# ═════════════════════════════════════════════════════

class TestMissionStateManager:

    def setup_method(self):
        self.mgr = MissionStateManager()

    def test_baslangic(self):
        assert self.mgr.mission_active is False
        assert self.mgr.total_waypoints == 0

    def test_gorevi_baslat(self):
        self.mgr.gorevi_baslat(5)
        assert self.mgr.mission_active is True
        assert self.mgr.total_waypoints == 5
        assert self.mgr.completed_waypoints == 0

    def test_gorevi_bitir(self):
        self.mgr.gorevi_baslat(3)
        self.mgr.gorevi_bitir()
        assert self.mgr.mission_active is False

    def test_waypoint_sayac(self):
        self.mgr.gorevi_baslat(3)
        self.mgr.waypoint_tamamla(1, 0)
        assert self.mgr.completed_waypoints == 1

    def test_pickup_tamamla(self):
        self.mgr.gorevi_baslat(3)
        self.mgr.pickup_tamamla(1)
        assert self.mgr.pickup_complete is True

    def test_dropoff_tamamla(self):
        self.mgr.gorevi_baslat(3)
        self.mgr.dropoff_tamamla(2)
        assert self.mgr.dropoff_complete is True

    def test_sonraki_waypoint_reset(self):
        self.mgr.gorevi_baslat(3)
        self.mgr.pickup_tamamla(1)
        self.mgr.sonraki_waypoint_ayarla(2, 0)
        assert self.mgr.pickup_complete is False
        assert self.mgr.dropoff_complete is False

    def test_gorev_bitti_mi(self):
        self.mgr.gorevi_baslat(2)
        self.mgr.waypoint_tamamla(1, 0)
        assert self.mgr.gorev_bitti_mi() is False
        self.mgr.waypoint_tamamla(2, 0)
        assert self.mgr.gorev_bitti_mi() is True

    def test_sifir_waypoint(self):
        assert self.mgr.gorev_bitti_mi() is False


# ═════════════════════════════════════════════════════
# TransitionRules testleri
# ═════════════════════════════════════════════════════

class TestTransitionRules:

    def _t(self, state, relevant=True, confirmed=True, in_stop_zone=False):
        msg = MagicMock()
        msg.state             = state
        msg.relevant_to_route = relevant
        msg.confirmed         = confirmed
        msg.in_stop_zone      = in_stop_zone
        return msg

    def _sign(self, tip, relevant=True, confirmed=True, status=0):
        s = MagicMock()
        s.type              = tip
        s.relevant_to_route = relevant
        s.confirmed         = confirmed
        s.event_status      = status
        return s

    def _lane(self, lost=False):
        m = MagicMock()
        m.lane_lost       = lost
        m.lane_confidence = 0.9
        return m

    def test_kirmizi(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.RED), MockTrafficLightState.UNKNOWN
        ) == (MockAutonomyMode.STOP_APPROACH, "RED_LIGHT")

    def test_yesil(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.GREEN), MockTrafficLightState.RED
        ) == (MockAutonomyMode.LANE_FOLLOW, "GREEN_LIGHT")

    def test_rota_disi(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.RED, relevant=False),
            MockTrafficLightState.UNKNOWN
        ) is None

    def test_teyitsiz(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.RED, confirmed=False),
            MockTrafficLightState.UNKNOWN
        ) is None

    def test_stale_yesil_sonrasi(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.STALE), MockTrafficLightState.GREEN
        ) == (MockAutonomyMode.STOP_APPROACH, "STALE_AFTER_GREEN")

    def test_stale_konservatif(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.STALE), MockTrafficLightState.RED
        ) == (MockAutonomyMode.STOP_APPROACH, "STALE_CONSERVATIVE")

    def test_conflict(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.CONFLICT), MockTrafficLightState.UNKNOWN
        ) == (MockAutonomyMode.STOP_APPROACH, "LIGHT_CONFLICT")

    def test_unknown_stop_zone(self):
        assert TransitionRules.trafik_isigi_kural(
            self._t(MockTrafficLightState.UNKNOWN, in_stop_zone=True),
            MockTrafficLightState.UNKNOWN
        ) == (MockAutonomyMode.STOP_APPROACH, "UNKNOWN_IN_STOP_ZONE")

    def test_serit_kayip(self):
        assert TransitionRules.serit_kural(self._lane(lost=True)) == \
               (MockAutonomyMode.STOP_APPROACH, "LANE_LOST")

    def test_serit_normal(self):
        assert TransitionRules.serit_kural(self._lane(lost=False)) is None

    def test_stop_tabelasi(self):
        assert TransitionRules.tabela_kural(self._sign(tip=1)) == \
               (MockAutonomyMode.STOP_APPROACH, "STOP_SIGN")

    def test_tabela_rota_disi(self):
        assert TransitionRules.tabela_kural(self._sign(tip=1, relevant=False)) is None

    def test_tabela_islendi(self):
        assert TransitionRules.tabela_kural(self._sign(tip=1, status=2)) is None

    def test_tabela_stale(self):
        assert TransitionRules.tabela_kural(self._sign(tip=1, status=3)) is None

    def test_tabela_teyitsiz(self):
        assert TransitionRules.tabela_kural(self._sign(tip=1, confirmed=False)) is None
