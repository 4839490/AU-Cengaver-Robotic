"""
AU Cengaver Robotics — FSM Senaryo Testleri
TEKNOFEST 2026

Gazebo öncesi fake mesajlarla uçtan uca senaryo testi.
FSMNode'u spin etmeden, callback'leri direkt çağırarak test eder.

Çalıştırmak için:
  python3 -m pytest src/fsm/test/test_fsm_scenarios.py -v
"""

import pytest
from unittest.mock import MagicMock, patch, call


# ─────────────────────────────────────────────────────
# ROS2 mock — import öncesi
# ─────────────────────────────────────────────────────

import sys

# Tüm ROS2 bağımlılıklarını mock'la
for mod in [
    'rclpy', 'rclpy.node', 'rclpy.qos', 'rclpy.logging', 'rclpy.clock',
    'fsm_msgs', 'fsm_msgs.msg',
    'planning_msgs', 'planning_msgs.msg',
    'perception_msgs', 'perception_msgs.msg',
    'localization_msgs', 'localization_msgs.msg',
    'common_msgs', 'common_msgs.msg',
]:
    sys.modules[mod] = MagicMock()


# Mock sabitler
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

class MockLocalizationStatus:
    OK       = 0
    DEGRADED = 1
    LOST     = 2

class MockPlanningStatus:
    OK        = 0
    REPLANNING = 1
    EMERGENCY = 2

class MockGoalReached:
    WAYPOINT  = 0
    PICKUP    = 1
    DROPOFF   = 2
    PARK_ENTRY = 3

class MockFSMRequest:
    MODE_CHANGE          = 0
    REPLANNING_NEEDED    = 1
    GOAL_CONFIRMED       = 2
    OBSTACLE_BLOCKED     = 3
    LOCALIZATION_DEGRADED = 4
    PARK_READY           = 5

class MockStopTarget:
    TARGET_TRAFFIC_LIGHT = 0
    TARGET_STOP_SIGN     = 1
    TARGET_PICKUP        = 2
    TARGET_DROPOFF       = 3

class MockCurrentMode:
    STOP_NONE             = 0
    STOP_RED_LIGHT        = 1
    STOP_STOP_SIGN        = 2
    STOP_OBSTACLE_TTC     = 3
    STOP_LOCALIZATION_LOST = 4
    STOP_STALE_SENSOR     = 5
    STOP_MISSION_ABORT    = 6
    STOP_PEDESTRIAN       = 7

# Mock'ları yerleştir
sys.modules['common_msgs.msg'].AutonomyMode = MockAutonomyMode
sys.modules['perception_msgs.msg'].TrafficLightState = MockTrafficLightState
sys.modules['perception_msgs.msg'].StopTarget = MockStopTarget
sys.modules['localization_msgs.msg'].LocalizationStatus = MockLocalizationStatus
sys.modules['planning_msgs.msg'].PlanningStatus = MockPlanningStatus
sys.modules['planning_msgs.msg'].GoalReached = MockGoalReached
sys.modules['planning_msgs.msg'].FSMRequest = MockFSMRequest
sys.modules['fsm_msgs.msg'].CurrentMode = MockCurrentMode

# FSMNode için Node base class mock'u
class MockNode:
    def __init__(self, name):
        self._clock = MagicMock()
        self._clock.now.return_value = MagicMock(nanoseconds=0)
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
    """Her test için temiz bir FSMNode örneği döndür"""
    node = FSMNode()
    return node

def trafik_msg(state, relevant=True, confirmed=True, in_stop_zone=False):
    msg = MagicMock()
    msg.state             = state
    msg.relevant_to_route = relevant
    msg.confirmed         = confirmed
    msg.in_stop_zone      = in_stop_zone
    return msg

def lokalizasyon_msg(status):
    msg = MagicMock()
    msg.status = status
    return msg

def planner_durum_msg(status):
    msg = MagicMock()
    msg.status = status
    return msg

def goal_reached_msg(wp_type, wp_id=1, success=True):
    msg = MagicMock()
    msg.waypoint_type = wp_type
    msg.waypoint_id   = wp_id
    msg.success       = success
    return msg

def fsm_request_msg(req_type, wp_id=1, requested_mode=None):
    msg = MagicMock()
    msg.request_type   = req_type
    msg.waypoint_id    = wp_id
    msg.requested_mode = requested_mode or MockAutonomyMode.LANE_FOLLOW
    return msg

def stop_target_msg(target_type, distance=3.0):
    msg = MagicMock()
    msg.target_type                 = target_type
    msg.distance_from_front_bumper  = distance
    return msg

def engel_msg(tracks):
    msg = MagicMock()
    msg.tracks = tracks
    return msg

def engel_track(track_id=1, is_static=False, age_ms=0, in_path=False, ttc=99.0):
    t = MagicMock()
    t.track_id  = track_id
    t.is_static = is_static
    t.age_ms    = age_ms
    t.in_path   = in_path
    t.ttc       = ttc
    return t


# ═════════════════════════════════════════════════════
# SENARYO 1 — Kırmızı ışık
# ═════════════════════════════════════════════════════

class TestSenaryoKirmiziIsik:

    def test_kirmizi_isik_stop_approach(self):
        """Kırmızı ışık → STOP_APPROACH"""
        node = make_fsm()
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.RED))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "RED_LIGHT"

    def test_yesil_isik_lane_follow(self):
        """Kırmızı → Yeşil → LANE_FOLLOW"""
        node = make_fsm()
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.RED))
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.GREEN))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert node.mode_mgr.last_reason == "GREEN_LIGHT"

    def test_rota_disi_isik_etki_etmez(self):
        """relevant_to_route=False → mod değişmemeli"""
        node = make_fsm()
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.RED, relevant=False))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_stale_yesil_sonrasi_stop(self):
        """Yeşilken STALE gelirse STOP_APPROACH"""
        node = make_fsm()
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.GREEN))
        node.cb_trafik_isigi(trafik_msg(MockTrafficLightState.STALE))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "STALE_AFTER_GREEN"


# ═════════════════════════════════════════════════════
# SENARYO 2 — Lokalizasyon kaybı
# ═════════════════════════════════════════════════════

class TestSenaryoLokalizasyon:

    def test_lokalizasyon_lost_stop(self):
        """LOST → STOP_APPROACH"""
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon_msg(MockLocalizationStatus.LOST))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "LOCALIZATION_LOST"

    def test_lokalizasyon_degraded_mod_degismez(self):
        """DEGRADED → mod değişmemeli, sadece log"""
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon_msg(MockLocalizationStatus.DEGRADED))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_lokalizasyon_ok_mod_degismez(self):
        """OK → mod değişmemeli"""
        node = make_fsm()
        node.cb_lokalizasyon(lokalizasyon_msg(MockLocalizationStatus.OK))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW


# ═════════════════════════════════════════════════════
# SENARYO 3 — Planner emergency
# ═════════════════════════════════════════════════════

class TestSenaryoPlannerEmergency:

    def test_emergency_stop_approach(self):
        """PLANNER EMERGENCY → STOP_APPROACH + event gönderilmeli"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum_msg(MockPlanningStatus.EMERGENCY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "PLANNER_EMERGENCY"
        node.event_hdlr.emergency_stop.assert_called_once_with("PLANNER_EMERGENCY")

    def test_planner_ok_mod_degismez(self):
        """Planner OK → mod değişmemeli"""
        node = make_fsm()
        node.cb_planner_durum(planner_durum_msg(MockPlanningStatus.OK))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW


# ═════════════════════════════════════════════════════
# SENARYO 4 — Pickup akışı
# ═════════════════════════════════════════════════════

class TestSenaryoPickup:

    def test_pickup_yaklasim_modu(self):
        """StopTarget PICKUP → PICKUP_APPROACH"""
        node = make_fsm()
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_PICKUP, 3.0))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PICKUP_APPROACH
        assert node.pickup_approach_aktif is True

    def test_pickup_tamamlandi_lane_follow(self):
        """GoalReached PICKUP → LANE_FOLLOW + event"""
        node = make_fsm()
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_PICKUP))
        node.cb_waypoint_tamam(goal_reached_msg(MockGoalReached.PICKUP, wp_id=1))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert node.pickup_approach_aktif is False
        node.event_hdlr.pickup_complete.assert_called_once_with(1)

    def test_pickup_tekrar_tetiklenmez(self):
        """Aktif pickup sırasında tekrar StopTarget gelmesi modu tekrar değiştirmemeli"""
        node = make_fsm()
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_PICKUP))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PICKUP_APPROACH
        # İkinci kez gelirse
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_PICKUP, 1.0))
        # Hâlâ PICKUP_APPROACH — tekrar mod_degistir çağrılmadı
        assert node.mode_mgr.current_mode == MockAutonomyMode.PICKUP_APPROACH


# ═════════════════════════════════════════════════════
# SENARYO 5 — Dropoff akışı
# ═════════════════════════════════════════════════════

class TestSenaryoDropoff:

    def test_dropoff_yaklasim_modu(self):
        """StopTarget DROPOFF → DROPOFF_APPROACH"""
        node = make_fsm()
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_DROPOFF))
        assert node.mode_mgr.current_mode == MockAutonomyMode.DROPOFF_APPROACH
        assert node.dropoff_approach_aktif is True

    def test_dropoff_tamamlandi_lane_follow(self):
        """GoalReached DROPOFF → LANE_FOLLOW + event"""
        node = make_fsm()
        node.cb_dur_noktasi(stop_target_msg(MockStopTarget.TARGET_DROPOFF))
        node.cb_waypoint_tamam(goal_reached_msg(MockGoalReached.DROPOFF, wp_id=2))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
        assert node.dropoff_approach_aktif is False
        node.event_hdlr.dropoff_complete.assert_called_once_with(2)


# ═════════════════════════════════════════════════════
# SENARYO 6 — Engel / TTC
# ═════════════════════════════════════════════════════

class TestSenaryoEngel:

    def test_ttc_kritik_stop(self):
        """TTC < 2s + in_path → STOP_APPROACH"""
        node = make_fsm()
        track = engel_track(track_id=5, in_path=True, ttc=1.5)
        node.cb_engel(engel_msg([track]))
        assert node.mode_mgr.current_mode == MockAutonomyMode.STOP_APPROACH
        assert node.mode_mgr.last_reason == "OBSTACLE_TTC"

    def test_ttc_guvenli_mod_degismez(self):
        """TTC > 2s → mod değişmemeli"""
        node = make_fsm()
        track = engel_track(track_id=5, in_path=True, ttc=5.0)
        node.cb_engel(engel_msg([track]))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_statik_engel_replanning(self):
        """10s hareketsiz statik engel → replanning_request"""
        node = make_fsm()
        track = engel_track(track_id=3, is_static=True, age_ms=11000, in_path=False)
        node.cb_engel(engel_msg([track]))
        node.event_hdlr.replanning_request.assert_called_once()

    def test_ttc_in_path_degil_mod_degismez(self):
        """TTC < 2s ama in_path=False → mod değişmemeli"""
        node = make_fsm()
        track = engel_track(track_id=5, in_path=False, ttc=1.0)
        node.cb_engel(engel_msg([track]))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW


# ═════════════════════════════════════════════════════
# SENARYO 7 — Park akışı
# ═════════════════════════════════════════════════════

class TestSenaryoPark:

    def test_park_entry_park_approach(self):
        """PARK_ENTRY → PARK_APPROACH"""
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached_msg(MockGoalReached.PARK_ENTRY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_APPROACH

    def test_park_ready_park_maneuver(self):
        """FSMRequest PARK_READY → PARK_MANEUVER"""
        node = make_fsm()
        node.cb_planner_istegi(fsm_request_msg(MockFSMRequest.PARK_READY))
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_MANEUVER

    def test_park_complete_mission_complete(self):
        """ParkComplete success → MISSION_COMPLETE"""
        node = make_fsm()
        msg = MagicMock()
        msg.success = True
        node.cb_park_tamam(msg)
        assert node.mode_mgr.current_mode == MockAutonomyMode.MISSION_COMPLETE

    def test_park_basarisiz_retry(self):
        """ParkComplete fail → PARK_APPROACH (retry)"""
        node = make_fsm()
        msg = MagicMock()
        msg.success = False
        node.cb_park_tamam(msg)
        assert node.mode_mgr.current_mode == MockAutonomyMode.PARK_APPROACH
        assert node.mode_mgr.last_reason == "PARK_FAILED_RETRY"


# ═════════════════════════════════════════════════════
# SENARYO 8 — Waypoint tamamlanma
# ═════════════════════════════════════════════════════

class TestSenaryoWaypoint:

    def test_waypoint_reached_lane_follow(self):
        """Normal WAYPOINT → LANE_FOLLOW"""
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached_msg(MockGoalReached.WAYPOINT, wp_id=3))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW

    def test_basarisiz_waypoint_mod_degismez(self):
        """success=False → mod değişmemeli"""
        node = make_fsm()
        node.cb_waypoint_tamam(goal_reached_msg(MockGoalReached.PICKUP, success=False))
        assert node.mode_mgr.current_mode == MockAutonomyMode.LANE_FOLLOW
