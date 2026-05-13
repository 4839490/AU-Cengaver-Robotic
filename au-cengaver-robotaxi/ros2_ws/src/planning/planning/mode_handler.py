#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
mode_handler.py

Görev:
  FSM moduna göre planner davranışını yönetir
  Mod geçişlerini izler, planner eylemlerini belirler

Sözleşme: FSM ↔ Planner Contract v1.1
  - FSM mod geçiş kararını verir → /fsm/current_mode
  - Planner moda göre trajectory ve hız üretir
  - mission_active=false → trajectory ÜRETMEZ
  - MISSION_COMPLETE → speed=0, /planning/status DEVAM EDER

FSM Mod Geçiş Tablosu (Contract v1.1 §4):
  LANE_FOLLOW     → trajectory + adaptif lookahead
  STOP_APPROACH   → speed=0, jerk sınırlı fren, stop_reason ile ayrım
  PICKUP_APPROACH → 3km/h yaklaşım, sağa offset
  DROPOFF_APPROACH→ 3km/h yaklaşım, sağa offset
  OBSTACLE_AVOID  → trajectory sampling + kaçınma
  PARK_APPROACH   → Dubins Path hesapla
  PARK_MANEUVER   → ≤3km/h, hassas hizalama
  MISSION_COMPLETE→ speed=0
"""

from dataclasses import dataclass
from typing import Optional


# ─── AutonomyMode Sabitleri ────────────────────────────────────────────────
MODE_LANE_FOLLOW       = 0
MODE_STOP_APPROACH     = 1
MODE_PICKUP_APPROACH   = 2
MODE_DROPOFF_APPROACH  = 3
MODE_OBSTACLE_AVOID    = 4
MODE_PARK_APPROACH     = 5
MODE_PARK_MANEUVER     = 6
MODE_MISSION_COMPLETE  = 7

# ─── StopReason Sabitleri (common_msgs/StopReason) ─────────────────────────
STOP_NONE              = 0
STOP_RED_LIGHT         = 1
STOP_STOP_SIGN         = 2
STOP_OBSTACLE_TTC      = 3
STOP_LOCALIZATION_LOST = 4
STOP_STALE_SENSOR      = 5
STOP_MISSION_ABORT     = 6
STOP_PEDESTRIAN        = 7

# ─── FSMEvent Sabitleri ────────────────────────────────────────────────────
EVENT_PICKUP_COMPLETE   = 0
EVENT_DROPOFF_COMPLETE  = 1
EVENT_OBSTACLE_CLEARED  = 2
EVENT_REPLANNING        = 3
EVENT_MISSION_ABORT     = 4
EVENT_RESUME            = 5
EVENT_PARK_SLOT_CHANGE  = 6
EVENT_EMERGENCY_STOP    = 7

# ─── FSMRequest Sabitleri ──────────────────────────────────────────────────
REQUEST_MODE_CHANGE     = 0
REQUEST_REPLANNING      = 1
REQUEST_GOAL_CONFIRMED  = 2
REQUEST_OBSTACLE_BLOCKED = 3
REQUEST_LOC_DEGRADED    = 4
REQUEST_PARK_READY      = 5

# ─── Lokalizasyon Status ───────────────────────────────────────────────────
LOC_STATUS_DEGRADED = 4
LOC_STATUS_LOST     = 6


@dataclass
class ModeAction:
    """Mod bazlı planner eylemi."""
    produce_trajectory:  bool     # Trajectory üret mi?
    target_speed:        float    # m/s
    jerk_limit:          float    # m/s³
    use_dubins:          bool     # Dubins Path kullan mı?
    use_sampling:        bool     # Trajectory sampling kullan mı?
    lateral_offset:      float    # metre — sağa offset (pickup/dropoff)
    description:         str


# ─── Mod → Eylem Tablosu ───────────────────────────────────────────────────
MODE_ACTIONS = {
    MODE_LANE_FOLLOW: ModeAction(
        produce_trajectory=True,
        target_speed=6.67,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='Normal şerit takibi — adaptif lookahead'
    ),
    MODE_STOP_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.0,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='Jerk sınırlı fren — dur çizgisine'
    ),
    MODE_PICKUP_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.5,   # sağa offset
        description='3km/h yaklaşım — yolcu tarafına'
    ),
    MODE_DROPOFF_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.5,   # sağa offset
        description='3km/h yaklaşım — yolcu tarafına'
    ),
    MODE_OBSTACLE_AVOID: ModeAction(
        produce_trajectory=True,
        target_speed=2.78,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=True,    # Trajectory sampling
        lateral_offset=0.0,
        description='Trajectory sampling + engel kaçınma'
    ),
    MODE_PARK_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=1.39,
        jerk_limit=1.5,
        use_dubins=True,      # Dubins Path
        use_sampling=False,
        lateral_offset=0.0,
        description='Dubins Path — park slot girişi'
    ),
    MODE_PARK_MANEUVER: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='≤3km/h hassas hizalama'
    ),
    MODE_MISSION_COMPLETE: ModeAction(
        produce_trajectory=False,
        target_speed=0.0,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='Görev tamamlandı — dur'
    ),
}


class ModeHandler:
    """
    FSM Mod Yöneticisi.

    Kullanım:
        mh = ModeHandler()
        mh.update_mode(mode=1, stop_reason=1, mission_active=True)
        action = mh.get_action()
        if action.produce_trajectory:
            # trajectory üret
    """

    def __init__(self):
        self._current_mode    = MODE_LANE_FOLLOW
        self._previous_mode   = MODE_LANE_FOLLOW
        self._stop_reason     = STOP_NONE
        self._mission_active  = False
        self._waypoint_id     = 0
        self._mode_changed    = False

        # FSM timeout — Contract v1.1
        # valid_until_ms aşılırsa son modu 1s koru → STOP_APPROACH
        self._last_fsm_update_ns: Optional[int] = None
        self._fsm_timeout_ms = 500

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def update_mode(
        self,
        mode:           int,
        stop_reason:    int  = STOP_NONE,
        mission_active: bool = False,
        waypoint_id:    int  = 0,
    ):
        """FSM'den gelen mod güncellemesi."""
        import time
        self._last_fsm_update_ns = time.monotonic_ns()

        self._mode_changed   = (mode != self._current_mode)
        self._previous_mode  = self._current_mode
        self._current_mode   = mode
        self._stop_reason    = stop_reason
        self._mission_active = mission_active
        self._waypoint_id    = waypoint_id

    def get_action(self) -> ModeAction:
        """
        Mevcut moda göre planner eylemini döndür.

        FSM Contract v1.1 FIX-3:
          mission_active=false → trajectory ÜRETMEZ
        """
        # mission_active=false → trajectory üretme
        if not self._mission_active:
            return ModeAction(
                produce_trajectory=False,
                target_speed=0.0,
                jerk_limit=2.0,
                use_dubins=False,
                use_sampling=False,
                lateral_offset=0.0,
                description='mission_active=false — bekleme'
            )

        # FSM timeout kontrolü
        if self._is_fsm_timed_out():
            return ModeAction(
                produce_trajectory=True,
                target_speed=0.0,
                jerk_limit=2.0,
                use_dubins=False,
                use_sampling=False,
                lateral_offset=0.0,
                description='FSM timeout — STOP_APPROACH'
            )

        action = MODE_ACTIONS.get(
            self._current_mode,
            MODE_ACTIONS[MODE_LANE_FOLLOW]
        )

        return action

    def should_produce_trajectory(self) -> bool:
        """Trajectory üretilmeli mi?"""
        return self.get_action().produce_trajectory

    def is_stopping(self) -> bool:
        """Araç durma modunda mı?"""
        return self._current_mode in (
            MODE_STOP_APPROACH,
            MODE_MISSION_COMPLETE
        )

    def is_parking(self) -> bool:
        """Park modunda mı?"""
        return self._current_mode in (
            MODE_PARK_APPROACH,
            MODE_PARK_MANEUVER
        )

    def is_pickup_dropoff(self) -> bool:
        """Pickup/dropoff modunda mı?"""
        return self._current_mode in (
            MODE_PICKUP_APPROACH,
            MODE_DROPOFF_APPROACH
        )

    def get_stop_reason_description(self) -> str:
        """Stop reason açıklaması."""
        descriptions = {
            STOP_NONE:              'Yok',
            STOP_RED_LIGHT:         'Kırmızı ışık',
            STOP_STOP_SIGN:         'STOP tabelası',
            STOP_OBSTACLE_TTC:      'Engel TTC',
            STOP_LOCALIZATION_LOST: 'Lokalizasyon kaybı',
            STOP_STALE_SENSOR:      'Sensör timeout',
            STOP_MISSION_ABORT:     'Görev iptali',
            STOP_PEDESTRIAN:        'Yaya',
        }
        return descriptions.get(self._stop_reason, 'Bilinmiyor')

    def build_fsm_request(
        self,
        request_type:   int,
        requested_mode: int = 0,
        waypoint_id:    int = 0,
        reason:         str = '',
    ) -> dict:
        """
        /planning/fsm_request mesajı için veri üret.
        Planner → FSM mod isteği.
        """
        return {
            'request_type':   request_type,
            'requested_mode': requested_mode,
            'waypoint_id':    waypoint_id,
            'reason':         reason,
            'age_ms':         0,
        }

    # ───────────────────────────────────────────────────────────────────────
    # PROPERTIES
    # ───────────────────────────────────────────────────────────────────────

    @property
    def current_mode(self) -> int:
        return self._current_mode

    @property
    def previous_mode(self) -> int:
        return self._previous_mode

    @property
    def stop_reason(self) -> int:
        return self._stop_reason

    @property
    def mission_active(self) -> bool:
        return self._mission_active

    @property
    def mode_changed(self) -> bool:
        return self._mode_changed

    @property
    def waypoint_id(self) -> int:
        return self._waypoint_id

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _is_fsm_timed_out(self) -> bool:
        """
        FSM timeout kontrolü.
        Contract v1.1: valid_until_ms aşılırsa → STOP_APPROACH
        """
        if self._last_fsm_update_ns is None:
            return False   # Henüz hiç güncelleme yok

        import time
        elapsed_ms = (
            time.monotonic_ns() - self._last_fsm_update_ns
        ) / 1e6

        # 1000ms → STOP_APPROACH (STALE_SENSOR)
        return elapsed_ms > 1000.0