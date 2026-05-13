#!/usr/bin/env python3
from typing import Tuple, List
"""
AU Cengaver Robotics — TEKNOFEST 2026
speed_profile.py

Algoritma 9: FSM Moduna + Eğriliğe Bağlı Dinamik Hız Profili
"""

import math
from dataclasses import dataclass


# ─── AutonomyMode Sabitleri ────────────────────────────────────────────────
MODE_LANE_FOLLOW = 0
MODE_STOP_APPROACH = 1
MODE_PICKUP_APPROACH = 2
MODE_DROPOFF_APPROACH = 3
MODE_OBSTACLE_AVOID = 4
MODE_PARK_APPROACH = 5
MODE_PARK_MANEUVER = 6
MODE_MISSION_COMPLETE = 7

# ─── TargetSpeed Reason Sabitleri ──────────────────────────────────────────
REASON_LANE_FOLLOW = 0
REASON_APPROACH_STOP = 1
REASON_PICKUP_DROPOFF = 2
REASON_OBSTACLE_SLOW = 3
REASON_JUNCTION = 4
REASON_TUNNEL = 5
REASON_PARK_APPROACH = 6
REASON_PARK_MANEUVER = 7
REASON_EMERGENCY_STOP = 8
REASON_LOCALIZATION_DEGRADED = 9
REASON_LANE_LOST = 10

# ─── Lokalizasyon Status ───────────────────────────────────────────────────
LOC_STATUS_OK = 0
LOC_STATUS_DEGRADED = 4
LOC_STATUS_LOST = 6

# ─── Hız Tablosu, m/s ──────────────────────────────────────────────────────
SPEED_TABLE = {
    MODE_LANE_FOLLOW: 6.67,
    MODE_STOP_APPROACH: 0.0,
    MODE_PICKUP_APPROACH: 0.83,
    MODE_DROPOFF_APPROACH: 0.83,
    MODE_OBSTACLE_AVOID: 2.78,
    MODE_PARK_APPROACH: 1.39,
    MODE_PARK_MANEUVER: 0.83,
    MODE_MISSION_COMPLETE: 0.0,
}

# ─── Jerk Tablosu, m/s³ ────────────────────────────────────────────────────
JERK_TABLE = {
    MODE_LANE_FOLLOW: 2.0,
    MODE_STOP_APPROACH: 2.0,
    MODE_PICKUP_APPROACH: 1.5,
    MODE_DROPOFF_APPROACH: 1.5,
    MODE_OBSTACLE_AVOID: 1.5,
    MODE_PARK_APPROACH: 1.5,
    MODE_PARK_MANEUVER: 1.0,
    MODE_MISSION_COMPLETE: 2.0,
}


@dataclass(frozen=True)
class SpeedOutput:
    speed: float
    jerk_limit: float
    reason: int


class SpeedProfile:
    """
    FSM modu, yol eğriliği ve lokalizasyon kalitesine göre hedef hız üretir.
    """

    def __init__(self):
        self._k_curvature = 2.0
        self._v_max = 6.67

    def compute(
        self,
        mode: int,
        curvature: float = 0.0,
        localization_confidence: float = 1.0,
        loc_status: int = LOC_STATUS_OK,
        emergency: bool = False,
        junction: bool = False,
        tunnel: bool = False,
        lane_lost: bool = False,
    ) -> SpeedOutput:

        mode = int(mode)
        loc_status = int(loc_status)

        if emergency:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=10.0,
                reason=REASON_EMERGENCY_STOP,
            )

        if loc_status == LOC_STATUS_LOST:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_LOCALIZATION_DEGRADED,
            )

        if lane_lost:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_LANE_LOST,
            )

        if mode == MODE_MISSION_COMPLETE:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_APPROACH_STOP,
            )

        if junction:
            return SpeedOutput(
                speed=2.78,
                jerk_limit=2.0,
                reason=REASON_JUNCTION,
            )

        if tunnel:
            return SpeedOutput(
                speed=2.78,
                jerk_limit=2.0,
                reason=REASON_TUNNEL,
            )

        if mode not in SPEED_TABLE:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_APPROACH_STOP,
            )

        base_speed = SPEED_TABLE[mode]
        jerk_limit = JERK_TABLE.get(mode, 2.0)
        reason = self._mode_to_reason(mode)

        if mode == MODE_LANE_FOLLOW:
            base_speed = self._curvature_speed(curvature)

        base_speed, reason = self._apply_localization_factor(
            speed=base_speed,
            confidence=localization_confidence,
            loc_status=loc_status,
            current_reason=reason,
        )

        base_speed = max(0.0, min(self._v_max, base_speed))

        return SpeedOutput(
            speed=base_speed,
            jerk_limit=jerk_limit,
            reason=reason,
        )

    def compute_stop_approach(
        self,
        distance_to_stop: float,
        current_speed: float,
        d_start: float = 5.0,
    ) -> SpeedOutput:

        distance_to_stop = float(distance_to_stop)
        current_speed = max(0.0, float(current_speed))
        d_start = max(0.1, float(d_start))

        if distance_to_stop <= 0.3:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_APPROACH_STOP,
            )

        if distance_to_stop >= d_start:
            return SpeedOutput(
                speed=current_speed,
                jerk_limit=2.0,
                reason=REASON_LANE_FOLLOW,
            )

        ratio = max(0.0, min(1.0, distance_to_stop / d_start))
        speed = current_speed * math.sqrt(ratio)

        return SpeedOutput(
            speed=max(0.0, speed),
            jerk_limit=2.0,
            reason=REASON_APPROACH_STOP,
        )

    def set_k_curvature(self, k: float) -> None:
        k = float(k)
        if math.isfinite(k) and k >= 0.0:
            self._k_curvature = k

    def set_v_max(self, v_max: float) -> None:
        v_max = float(v_max)
        if math.isfinite(v_max) and v_max > 0.0:
            self._v_max = v_max
            SPEED_TABLE[MODE_LANE_FOLLOW] = v_max

    def _curvature_speed(self, curvature: float) -> float:
        try:
            curvature = abs(float(curvature))
        except Exception:
            curvature = 0.0

        if not math.isfinite(curvature):
            curvature = 0.0

        reduction = self._k_curvature * curvature
        speed = self._v_max * (1.0 - reduction)

        return max(0.5, min(self._v_max, speed))

    def _apply_localization_factor(
        self,
        speed: float,
        confidence: float,
        loc_status: int,
        current_reason: int,
    ) -> Tuple[float, int]:

        speed = max(0.0, float(speed))

        try:
            confidence = float(confidence)
        except Exception:
            confidence = 0.0

        if not math.isfinite(confidence):
            confidence = 0.0

        confidence = max(0.0, min(1.0, confidence))

        reason = current_reason

        if loc_status == LOC_STATUS_DEGRADED:
            speed *= 0.7
            reason = REASON_LOCALIZATION_DEGRADED

        if confidence < 0.5:
            speed *= 0.5
            reason = REASON_LOCALIZATION_DEGRADED

        return speed, reason

    @staticmethod
    def _mode_to_reason(mode: int) -> int:
        mapping = {
            MODE_LANE_FOLLOW: REASON_LANE_FOLLOW,
            MODE_STOP_APPROACH: REASON_APPROACH_STOP,
            MODE_PICKUP_APPROACH: REASON_PICKUP_DROPOFF,
            MODE_DROPOFF_APPROACH: REASON_PICKUP_DROPOFF,
            MODE_OBSTACLE_AVOID: REASON_OBSTACLE_SLOW,
            MODE_PARK_APPROACH: REASON_PARK_APPROACH,
            MODE_PARK_MANEUVER: REASON_PARK_MANEUVER,
            MODE_MISSION_COMPLETE: REASON_APPROACH_STOP,
        }

        return mapping.get(int(mode), REASON_APPROACH_STOP)
