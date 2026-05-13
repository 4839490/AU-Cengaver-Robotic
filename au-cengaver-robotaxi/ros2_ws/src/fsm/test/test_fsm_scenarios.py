"""
AU Cengaver Robotics — FSM Senaryo Testleri
TEKNOFEST 2026

Gazebo öncesi fake mesajlarla uçtan uca senaryo testi.
FSMNode callback'lerini direkt çağırarak test eder.

Çalıştırmak için:
  python3 -m pytest src/fsm/test/test_fsm_scenarios.py -v
"""

import pytest
from unittest.mock import MagicMock
import sys

# ─────────────────────────────────────────────────────
# ROS2 mock
# ─────────────────────────────────────────────────────
for mod in [
    'rclpy', 'rclpy.node', 'rclpy.qos', 'rclpy.logging', 'rclpy.clock',
    'fsm_msgs', 'fsm_msgs.msg',
    'planning_msgs', 'planning_msgs.msg',
    'perception_msgs', 'perception_msgs.msg',
    'localization_msgs', 'localization_msgs.msg',
    'common_msgs', 'common_msgs.msg',
]:
    sys.modules[mod] = MagicMock()


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
    UNKNOWN  = 0; RED = 1; YELLOW = 2; GREEN = 3; STALE = 4; CONFLICT = 5

class MockLocalizationStatus:
    OK = 0; DEGRADED = 1; LOST = 2

class MockPlanningStatus:
    OK = 0; REPLANNING = 1; EMERGENCY = 2

class MockGoalReached:
    WAYPOINT = 0; PICKUP = 1; DROPOFF = 2; PARK_ENTRY = 3

class MockFSMRequest:
    MODE_CHANGE = 0; REPLANNING_NEEDED = 1; GOAL_CONFIRMED = 2
    OBSTACLE_BLOCKED = 3; LOCALIZATION_DEGRADED = 4; PARK_READY = 5

class MockStopTarget:
    TARGET_TRAFFIC_LIGHT = 0; TARGET_STOP_SIGN = 1
    TARGET_PICKUP = 2; TARGET_DROPOFF = 3

class MockCurrentMode:
    STOP_NONE = 0; STOP_RED_LIGHT = 1; STOP_STOP_SIGN = 2
    STOP_OBSTACLE_TTC = 3; STOP_LOCALIZATION_LOST = 4
    STOP_STALE_SENSOR = 5; STOP_MISSION_ABORT = 6; STOP_PEDESTRIAN = 7

class MockTime:
    def __init__(self, ns=0):
        self.nanoseconds = ns
    def __sub__(self, other):
        r = MockTime(); r.nanoseconds = self.nanoseconds - other.nanoseconds; return r
    def to_msg(self): return MagicMock()

class MockClock:
    def __init__(self): self._ns = 0
    def now(self): return MockTime(self._ns)
    def advance(self, ms): self._ns += ms * 1_000_000

sys.modules['common_msgs.msg'].AutonomyMode       = MockAutonomyMode
sys.modules['perception_msgs.msg'].TrafficLightState = MockTrafficLightState
sys.modules['perception_msgs.msg'].StopTarget     = MockStopTarget
sys.modules['localization_msgs.msg'].LocalizationStatus = MockLocalizationStatus
sys.modules['planning_msgs.msg'].PlanningStatus   = MockPlanningStatus
sys.modules['planning_msgs.msg'].GoalReached      = MockGoalReached
sys.modules['planning_msgs.msg'].FSMRequest       = MockFSMRequest
sys.modules['fsm_msgs.msg'].CurrentMode           = MockCurrentMode

class MockNode:
    def __init__(self, name):
        self._clock = MockClock()
    def get_logger(self): return MagicMock()
    def get_clock(self): return self._clock
    def create_publisher(self, *a, **kw): return MagicMock()
    def create_subscription(self, *a, **kw): return MagicMock()
    def create_timer(self, *a, **kw): return MagicMock()
    def destroy_node(self): pass

sys.modules['rclpy.node'].Node = MockNode
sys.path.insert(0, 'src/fsm')
from fsm.fsm_node import FSMNode


# ─────────────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ─────────────────────────────────────────────────────

def make_fsm():
    return FSMNode()

def trafik(state, relevant=True, confirmed=True, in_stop_zone=False):
    m = MagicMock()
    m.state = state; m.relevant_to_route = relevant
    m.confirmed = confirmed; m.in_stop_zone = in_stop_zone
    return m

def lokalizasyon(status):
    m = MagicMock(); m.status = status; return m

def planner_durum(status):
    m = MagicMock(); m.status = status; return m

def goal_reached(wp_type, wp_id=1, success=True):
    m = MagicMock()
    m.waypoint_type = wp_type; m.waypoint_id = wp_id; m.success = success
    return m

def fsm_request(req_type, wp_id=1, requested_mode=None):
    m = MagicMock()
    m.request_type = req_type; m.waypoint_id = wp_id
    m.requested_mode = requested_mode or MockAutonomyMode.LANE_FOLLOW
    return m

def stop_target(target_type, distance=3.0):
    m = MagicMock()
    m.target_type = target_type; m.distance_from_front_bumper = distance
    return m

def engel_msg(tracks):
    m = MagicMock(); m.tracks = tracks; return m

def engel_track(track_id=1, is_static=False, age_ms=0, ttc=99.0):
    t = MagicMock()
    t.track_id = track_id; t.is_static = is_static
    t.age_ms = age_ms; t.ttc = ttc
    return t


# ═════════════════════════════════════════════════════
# SENARYO 1 — Kırmızı ışık
# ═════════════════════════════════════════════════════

class TestKirmiziIsik:

    def test_kirmizi_stop_approach(self):
        node = make_fsm()
        node.cb_trafik_isigi(trafik(MockTrafficLightState.RED))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "RED_LIGHT"

    def test_yesil_lane_follow(self):
        node = make_fsm()
        node.cb_trafik_isigi(trafik(MockTrafficLightState.RED))
        node.cb_trafik_isigi(trafik(MockTrafficLightState.GREEN))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_rota_disi_etki_etmez(self):
        node = make_fsm()
        node.cb_trafik_isigi(trafik(MockTrafficLightState.RED, relevant=False))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_stale_yesil_sonrasi_stop(self):
        node = make_fsm()
        node.cb_trafik_isigi(trafik(MockTrafficLightState.GREEN))
        node.cb_trafik_isigi(trafik(MockTrafficLightState.STALE))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "STALE_AFTER_GREEN"


# ═════════════════════════════════════════════════════
# SENARYO 2 — Lokalizasyon
# ═════════════════════════════════════════════════════

class TestLokalizasyon:

    def test_lost_stop(self):
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon(MockLocalizationStatus.LOST))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "LOCALIZATION_LOST"

    def test_degraded_mod_degismez(self):
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon(MockLocalizationStatus.DEGRADED))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_watchdog_lokalizasyon_besleniyor(self):
        """cb_lokalizasyon watchdog'u beslemeli"""
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon(MockLocalizationStatus.OK))
        assert node.watchdog.lokalizasyon._last_stamp is not None


# ═════════════════════════════════════════════════════
# SENARYO 3 — Planner emergency + F-01/02
# ═════════════════════════════════════════════════════

class TestPlannerEmergency:

    def test_emergency_stop_approach_ve_event(self):
        """F-04: PLANNER_EMERGENCY → STOP_APPROACH + event"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum(MockPlanningStatus.EMERGENCY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "PLANNER_EMERGENCY"
        node.event_hdlr.emergency_stop.assert_called_once_with("PLANNER_EMERGENCY")

    def test_planner_ok_mod_degismez(self):
        node = make_fsm()
        node.cb_planner_durum(planner_durum(MockPlanningStatus.OK))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_watchdog_planner_besleniyor(self):
        """cb_planner_durum watchdog'u beslemeli"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum(MockPlanningStatus.OK))
        assert node.watchdog.planner._last_stamp is not None


# ═════════════════════════════════════════════════════
# SENARYO 4 — Watchdog F-13
# ═════════════════════════════════════════════════════

class TestWatchdogF13:

    def test_planner_timeout_stop_approach(self):
        """F-13: planner 1001ms sessiz → STOP_APPROACH"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum(MockPlanningStatus.OK))
        node.get_clock().advance(1001)
        node.yayinla_mod()  # watchdog bu timer'da çalışır
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "WATCHDOG_PLANNER_STALE"

    def test_planner_600ms_koru(self):
        """F-13: 600ms sonra mod korunur"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum(MockPlanningStatus.OK))
        node.get_clock().advance(600)
        node.yayinla_mod()
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW


# ═════════════════════════════════════════════════════
# SENARYO 5 — Pickup akışı
# ═════════════════════════════════════════════════════

class TestPickup:

    def test_pickup_yaklasim(self):
        node = make_fsm()
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_PICKUP))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PICKUP_APPROACH

    def test_pickup_tamamlandi_lane_follow(self):
        node = make_fsm()
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_PICKUP))
        node.cb_waypoint_tamam(goal_reached(MockGoalReached.PICKUP, wp_id=1))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert node.pickup_approach_aktif is False
        node.event_hdlr.pickup_complete.assert_called_once_with(1)

    def test_pickup_tekrar_tetiklenmez(self):
        node = make_fsm()
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_PICKUP))
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_PICKUP, 1.0))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PICKUP_APPROACH


# ═════════════════════════════════════════════════════
# SENARYO 6 — Dropoff akışı
# ═════════════════════════════════════════════════════

class TestDropoff:

    def test_dropoff_yaklasim(self):
        node = make_fsm()
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_DROPOFF))
        assert node.mode_mgr.current_mode == MockAutonomyMode.DROPOFF_APPROACH

    def test_dropoff_tamamlandi_lane_follow(self):
        node = make_fsm()
        node.cb_dur_noktasi(stop_target(MockStopTarget.TARGET_DROPOFF))
        node.cb_waypoint_tamam(goal_reached(MockGoalReached.DROPOFF, wp_id=2))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        node.event_hdlr.dropoff_complete.assert_called_once_with(2)


# ═════════════════════════════════════════════════════
# SENARYO 7 — Engel / TTC
# ═════════════════════════════════════════════════════

class TestEngel:

    def test_ttc_kritik_stop(self):
        """F-05: TTC < 2s → STOP_APPROACH(OBSTACLE_TTC)"""
        node = make_fsm()
        track = engel_track(track_id=5, ttc=1.5)
        node.cb_engel(engel_msg([track]))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "OBSTACLE_TTC"

    def test_ttc_guvenli_mod_degismez(self):
        node = make_fsm()
        track = engel_track(track_id=5, ttc=5.0)
        node.cb_engel(engel_msg([track]))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_statik_engel_replanning(self):
        node = make_fsm()
        track = engel_track(track_id=3, is_static=True, age_ms=11000)
        node.cb_engel(engel_msg([track]))
        node.event_hdlr.replanning_request.assert_called_once()

    def test_watchdog_engel_besleniyor(self):
        """cb_engel watchdog'u beslemeli"""
        node = make_fsm()
        track = engel_track()
        node.cb_engel(engel_msg([track]))
        assert node.watchdog.engeller._last_stamp is not None


# ═════════════════════════════════════════════════════
# SENARYO 8 — Park akışı
# ═════════════════════════════════════════════════════

class TestPark:

    def test_park_entry_park_approach(self):
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached(MockGoalReached.PARK_ENTRY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_APPROACH

    def test_park_ready_park_maneuver(self):
        node = make_fsm()
        node.mode_mgr._uygula(MockAutonomyMode.PARK_APPROACH, "TEST")
        node.cb_planner_istegi(fsm_request(MockFSMRequest.PARK_READY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_MANEUVER

    def test_park_complete_mission_complete(self):
        node = make_fsm()
        node.mode_mgr._uygula(MockAutonomyMode.PARK_MANEUVER, "TEST")
        msg = MagicMock(); msg.success = True
        node.cb_park_tamam(msg)
        assert node.mode_mgr.current_mode == MockAutonomyMode.MISSION_COMPLETE

    def test_park_basarisiz_retry(self):
        node = make_fsm()
        node.mode_mgr._uygula(MockAutonomyMode.PARK_MANEUVER, "TEST")
        msg = MagicMock(); msg.success = False
        node.cb_park_tamam(msg)
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_APPROACH
        assert node.mode_mgr.last_reason == "PARK_FAILED_RETRY"


# ═════════════════════════════════════════════════════
# SENARYO 9 — Waypoint + F-01/02 mission_active
# ═════════════════════════════════════════════════════

class TestWaypoint:

    def test_waypoint_lane_follow(self):
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached(MockGoalReached.WAYPOINT, wp_id=3))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_basarisiz_waypoint_mod_degismez(self):
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached(MockGoalReached.PICKUP, success=False))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_mission_active_false_baslangic(self):
        """F-01: Başlangıçta mission_active=false"""
        node = make_fsm()
        assert node.mission_mgr.mission_active is False

    def test_mission_active_true_gorevi_baslat(self):
        """F-02: gorevi_baslat() sonrası mission_active=true"""
        node = make_fsm()
        node.mission_mgr.gorevi_baslat(3)
        assert node.mission_mgr.mission_active is True


# ═════════════════════════════════════════════════════
# SENARYO 10 — Guard condition senaryoları
# ═════════════════════════════════════════════════════

class TestGuardSenaryolari:

    def test_mission_complete_sonrasi_mod_degismez(self):
        """MISSION_COMPLETE terminal — hiçbir callback modu değiştiremez"""
        node = make_fsm()
        node.mode_mgr._uygula(MockAutonomyMode.MISSION_COMPLETE, "PARK_COMPLETE")
        # Kırmızı ışık gelse bile
        node.cb_trafik_isigi(trafik(MockTrafficLightState.RED))
        assert node.mode_mgr.current_mode == MockAutonomyMode.MISSION_COMPLETE

    def test_stop_approach_her_moddan_tetiklenir(self):
        """STOP_APPROACH her moddan tetiklenir — guard bypass"""
        node = make_fsm()
        node.mode_mgr._uygula(MockAutonomyMode.PICKUP_APPROACH, "TEST")
        node.cb_lokalizasyon(lokalizasyon(MockLocalizationStatus.LOST))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
