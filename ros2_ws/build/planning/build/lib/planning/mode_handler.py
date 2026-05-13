#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
mode_handler.py

FSM moduna göre planner davranışını yönetir.
"""

import time
from dataclasses import dataclass
from typing import Optional


# ─── AutonomyMode Sabitleri ────────────────────────────────────────────────
MODE_LANE_FOLLOW = 0
MODE_STOP_APPROACH = 1
MODE_PICKUP_APPROACH = 2
MODE_DROPOFF_APPROACH = 3
MODE_OBSTACLE_AVOID = 4
MODE_PARK_APPROACH = 5
MODE_PARK_MANEUVER = 6
MODE_MISSION_COMPLETE = 7

# ─── StopReason Sabitleri ──────────────────────────────────────────────────
STOP_NONE = 0
STOP_RED_LIGHT = 1
STOP_STOP_SIGN = 2
STOP_OBSTACLE_TTC = 3
STOP_LOCALIZATION_LOST = 4
STOP_STALE_SENSOR = 5
STOP_MISSION_ABORT = 6
STOP_PEDESTRIAN = 7

# ─── FSMEvent Sabitleri ────────────────────────────────────────────────────
EVENT_PICKUP_COMPLETE = 0
EVENT_DROPOFF_COMPLETE = 1
EVENT_OBSTACLE_CLEARED = 2
EVENT_REPLANNING = 3
EVENT_MISSION_ABORT = 4
EVENT_RESUME = 5
EVENT_PARK_SLOT_CHANGE = 6
EVENT_EMERGENCY_STOP = 7

# ─── FSMRequest Sabitleri ──────────────────────────────────────────────────
REQUEST_MODE_CHANGE = 0
REQUEST_REPLANNING_NEEDED = 1
REQUEST_GOAL_CONFIRMED = 2
REQUEST_OBSTACLE_BLOCKED = 3
REQUEST_LOCALIZATION_DEGRADED = 4
REQUEST_PARK_READY = 5


@dataclass(frozen=True)
class ModeAction:
    """Mod bazlı planner eylemi."""
    produce_trajectory: bool
    target_speed: float
    jerk_limit: float
    use_dubins: bool
    use_sampling: bool
    lateral_offset: float
    description: str


MODE_ACTIONS = {
    MODE_LANE_FOLLOW: ModeAction(
        produce_trajectory=True,
        target_speed=6.67,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='LANE_FOLLOW — normal şerit takibi'
    ),

    MODE_STOP_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.0,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='STOP_APPROACH — jerk sınırlı fren'
    ),

    MODE_PICKUP_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.5,
        description='PICKUP_APPROACH — 3 km/h sağa offset yaklaşım'
    ),

    MODE_DROPOFF_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.5,
        description='DROPOFF_APPROACH — 3 km/h sağa offset yaklaşım'
    ),

    MODE_OBSTACLE_AVOID: ModeAction(
        produce_trajectory=True,
        target_speed=2.78,
        jerk_limit=1.5,
        use_dubins=False,
        use_sampling=True,
        lateral_offset=0.0,
        description='OBSTACLE_AVOID — trajectory sampling + kaçınma'
    ),

    MODE_PARK_APPROACH: ModeAction(
        produce_trajectory=True,
        target_speed=1.39,
        jerk_limit=1.5,
        use_dubins=True,
        use_sampling=False,
        lateral_offset=0.0,
        description='PARK_APPROACH — Dubins path ile slot yaklaşımı'
    ),

    MODE_PARK_MANEUVER: ModeAction(
        produce_trajectory=True,
        target_speed=0.83,
        jerk_limit=1.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='PARK_MANEUVER — düşük hız hassas hizalama'
    ),

    MODE_MISSION_COMPLETE: ModeAction(
        produce_trajectory=False,
        target_speed=0.0,
        jerk_limit=2.0,
        use_dubins=False,
        use_sampling=False,
        lateral_offset=0.0,
        description='MISSION_COMPLETE — trajectory üretme, speed=0'
    ),
}


SAFE_STOP_ACTION = ModeAction(
    produce_trajectory=True,
    target_speed=0.0,
    jerk_limit=2.0,
    use_dubins=False,
    use_sampling=False,
    lateral_offset=0.0,
    description='SAFE_STOP — güvenli duruş'
)


WAIT_ACTION = ModeAction(
    produce_trajectory=False,
    target_speed=0.0,
    jerk_limit=2.0,
    use_dubins=False,
    use_sampling=False,
    lateral_offset=0.0,
    description='WAIT — mission_active=false, trajectory üretme'
)


class ModeHandler:
    """
    FSM mod yöneticisi.

    FSM /fsm/current_mode yayınlar.
    Planner bu moda göre trajectory ve hız davranışını seçer.
    """

    def __init__(self):
        self._current_mode = MODE_LANE_FOLLOW
        self._previous_mode = MODE_LANE_FOLLOW
        self._stop_reason = STOP_NONE
        self._mission_active = False
        self._waypoint_id = 0
        self._mode_changed = False

        self._last_fsm_update_ns: Optional[int] = None
        self._fsm_timeout_ms = 1000.0

    def update_mode(
        self,
        mode: int,
        stop_reason: int = STOP_NONE,
        mission_active: bool = False,
        waypoint_id: int = 0,
    ) -> None:
        """FSM'den gelen mod güncellemesini işler."""
        self._last_fsm_update_ns = time.monotonic_ns()

        mode = int(mode)
        stop_reason = int(stop_reason)
        waypoint_id = int(waypoint_id)

        self._mode_changed = mode != self._current_mode
        self._previous_mode = self._current_mode
        self._current_mode = mode
        self._stop_reason = stop_reason
        self._mission_active = bool(mission_active)
        self._waypoint_id = waypoint_id

    def get_action(self) -> ModeAction:
        """
        Mevcut FSM moduna göre planner eylemini döndürür.

        Güvenlik:
          - mission_active=false ise trajectory üretmez.
          - FSM timeout olursa güvenli duruş döndürür.
          - bilinmeyen mode gelirse LANE_FOLLOW değil, güvenli duruş döndürür.
        """
        if not self._mission_active:
            return WAIT_ACTION

        if self._is_fsm_timed_out():
            return SAFE_STOP_ACTION

        return MODE_ACTIONS.get(self._current_mode, SAFE_STOP_ACTION)

    def should_produce_trajectory(self) -> bool:
        return self.get_action().produce_trajectory

    def is_stopping(self) -> bool:
        if self._is_fsm_timed_out():
            return True

        return self._current_mode in (
            MODE_STOP_APPROACH,
            MODE_MISSION_COMPLETE,
        )

    def is_parking(self) -> bool:
        return self._current_mode in (
            MODE_PARK_APPROACH,
            MODE_PARK_MANEUVER,
        )

    def is_pickup_dropoff(self) -> bool:
        return self._current_mode in (
            MODE_PICKUP_APPROACH,
            MODE_DROPOFF_APPROACH,
        )

    def get_stop_reason_description(self) -> str:
        descriptions = {
            STOP_NONE: 'Yok',
            STOP_RED_LIGHT: 'Kırmızı ışık',
            STOP_STOP_SIGN: 'STOP tabelası',
            STOP_OBSTACLE_TTC: 'Engel TTC',
            STOP_LOCALIZATION_LOST: 'Lokalizasyon kaybı',
            STOP_STALE_SENSOR: 'Sensör timeout',
            STOP_MISSION_ABORT: 'Görev iptali',
            STOP_PEDESTRIAN: 'Yaya',
        }

        if self._is_fsm_timed_out():
            return 'FSM timeout'

        return descriptions.get(self._stop_reason, 'Bilinmiyor')

    def build_fsm_request(
        self,
        request_type: int,
        requested_mode: int = 0,
        waypoint_id: int = 0,
        reason: str = '',
        valid_until_ms: int = 500,
    ) -> dict:
        """
        planning_msgs/FSMRequest.msg alanlarına uygun veri üretir.

        FSMRequest.msg:
          uint8 request_type
          uint8 requested_mode
          uint32 waypoint_id
          string reason
          uint32 age_ms
          uint32 valid_until_ms
        """
        return {
            'request_type': int(request_type),
            'requested_mode': int(requested_mode),
            'waypoint_id': int(waypoint_id),
            'reason': str(reason),
            'age_ms': 0,
            'valid_until_ms': int(valid_until_ms),
        }

    @property
    def current_mode(self) -> int:
        return self._current_mode

    @property
    def previous_mode(self) -> int:
        return self._previous_mode

    @property
    def stop_reason(self) -> int:
        if self._is_fsm_timed_out():
            return STOP_STALE_SENSOR
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

    @property
    def fsm_timed_out(self) -> bool:
        return self._is_fsm_timed_out()

    def _is_fsm_timed_out(self) -> bool:
        """FSM mesajı 1000 ms'den eskiyse timeout kabul eder."""
        if self._last_fsm_update_ns is None:
            return False

        elapsed_ms = (time.monotonic_ns() - self._last_fsm_update_ns) / 1e6
        return elapsed_ms > self._fsm_timeout_ms
