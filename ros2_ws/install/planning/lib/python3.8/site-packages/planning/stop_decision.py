#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
stop_decision.py

Algoritma 15: Stop Line Yaklaşımı + Jerk Sınırlı Fren Profili
"""

import math
from dataclasses import dataclass
from typing import Any, List, Optional


# ─── Trafik Işığı State Sabitleri ──────────────────────────────────────────
LIGHT_UNKNOWN = 0
LIGHT_RED = 1
LIGHT_YELLOW = 2
LIGHT_GREEN = 3
LIGHT_STALE = 4
LIGHT_CONFLICT = 5

# ─── TargetSpeed.reason Sabitleri ──────────────────────────────────────────
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

# ─── StopTarget reason yardımcıları ────────────────────────────────────────
STOP_TARGET_RED_LIGHT = 0
STOP_TARGET_STOP_SIGN = 1
STOP_TARGET_PICKUP = 2
STOP_TARGET_DROPOFF = 3
STOP_TARGET_PARK = 4
STOP_TARGET_UNKNOWN = 255

# ─── Parametreler ──────────────────────────────────────────────────────────
D_START = 5.0
D_STOP = 0.5
D_TOLERANCE = 0.3
JERK_LIMIT = 2.0
A_BRAKE_MAX = 6.5
NO_STOP_DISTANCE = -1.0


@dataclass(frozen=True)
class StopDecisionResult:
    should_stop: bool
    target_speed: float
    jerk_limit: float
    reason: int
    distance: float
    warning_flags: List[str]


@dataclass(frozen=True)
class TrafficLightInfo:
    state: int
    confidence: float
    relevant_to_route: bool
    confirmed: bool
    in_stop_zone: bool
    distance_to_stop: float
    last_state: int = LIGHT_UNKNOWN


@dataclass(frozen=True)
class StopTargetInfo:
    distance_from_front_bumper: float
    reason: Any
    confidence: float


class StopDecision:
    """
    Trafik ışığı, STOP tabelası ve stop target bilgilerine göre durma kararı verir.
    """

    def __init__(self):
        self._last_light_state = LIGHT_UNKNOWN

    def decide(
        self,
        light: Optional[TrafficLightInfo],
        stop_target: Optional[StopTargetInfo],
        current_speed: float,
    ) -> StopDecisionResult:
        warnings: List[str] = []
        current_speed = max(0.0, self._safe_float(current_speed, 0.0))

        light_result = self._evaluate_light(
            light=light,
            current_speed=current_speed,
            warnings=warnings,
        )

        if light_result is not None:
            return light_result

        if stop_target is not None:
            return self._evaluate_stop_target(
                stop_target=stop_target,
                current_speed=current_speed,
                warnings=warnings,
            )

        return StopDecisionResult(
            should_stop=False,
            target_speed=current_speed,
            jerk_limit=JERK_LIMIT,
            reason=REASON_LANE_FOLLOW,
            distance=NO_STOP_DISTANCE,
            warning_flags=warnings,
        )

    def apply_to_trajectory(
        self,
        trajectory: List[Any],
        stop_distance: float,
        current_speed: float,
    ) -> List[Any]:
        """
        Trajectory noktalarına fren profili uygular.

        Not:
          Bu fonksiyon, gelen point tipinin aynı class'ı ile yeni obje üretmeye çalışır.
          Constructor uyumsuzsa mevcut objeyi günceller.
        """
        if not trajectory:
            return trajectory

        stop_distance = self._safe_float(stop_distance, NO_STOP_DISTANCE)
        current_speed = max(0.0, self._safe_float(current_speed, 0.0))

        if stop_distance < 0.0:
            return trajectory

        updated = []

        for pt in trajectory:
            d = stop_distance - self._safe_float(
                getattr(pt, 'distance_from_start', 0.0),
                0.0,
            )

            if d <= D_TOLERANCE:
                speed = 0.0
            elif d < D_START:
                ratio = max(0.0, min(1.0, d / D_START))
                speed = current_speed * math.sqrt(ratio)
            else:
                speed = self._safe_float(getattr(pt, 'speed', current_speed), current_speed)

            speed = max(0.0, speed)

            try:
                updated.append(
                    pt.__class__(
                        x=float(pt.x),
                        y=float(pt.y),
                        yaw=float(pt.yaw),
                        speed=float(speed),
                        curvature=float(getattr(pt, 'curvature', 0.0)),
                        distance_from_start=float(
                            getattr(pt, 'distance_from_start', 0.0)
                        ),
                    )
                )
            except Exception:
                try:
                    pt.speed = float(speed)
                except Exception:
                    pass
                updated.append(pt)

        return updated

    def update_light_state(self, state: int) -> None:
        state = int(state)

        if state not in (LIGHT_STALE, LIGHT_UNKNOWN):
            self._last_light_state = state

    def _evaluate_light(
        self,
        light: Optional[TrafficLightInfo],
        current_speed: float,
        warnings: List[str],
    ) -> Optional[StopDecisionResult]:

        if light is None:
            return None

        state = int(light.state)
        confidence = self._safe_float(light.confidence, 0.0)
        distance = self._safe_distance(light.distance_to_stop)

        self.update_light_state(state)

        if confidence < 0.3:
            warnings.append('LOW_LIGHT_CONFIDENCE')
            return None

        if not bool(light.confirmed):
            warnings.append('LIGHT_NOT_CONFIRMED')
            return None

        if not bool(light.relevant_to_route):
            return None

        if state == LIGHT_RED:
            return self._make_stop_result(
                distance=distance,
                current_speed=current_speed,
                reason=REASON_APPROACH_STOP,
                warnings=warnings,
            )

        if state == LIGHT_YELLOW:
            speed = min(
                current_speed * 0.5,
                self._brake_profile(distance, current_speed),
            )

            warnings.append('YELLOW_LIGHT')

            return StopDecisionResult(
                should_stop=False,
                target_speed=max(0.0, speed),
                jerk_limit=JERK_LIMIT,
                reason=REASON_APPROACH_STOP,
                distance=distance,
                warning_flags=warnings,
            )

        if state == LIGHT_GREEN:
            return None

        if state == LIGHT_UNKNOWN and bool(light.in_stop_zone):
            warnings.append('UNKNOWN_LIGHT_IN_STOP_ZONE')

            return self._make_stop_result(
                distance=distance,
                current_speed=current_speed,
                reason=REASON_APPROACH_STOP,
                warnings=warnings,
            )

        if state == LIGHT_STALE:
            if self._last_light_state == LIGHT_GREEN and bool(light.in_stop_zone):
                warnings.append('STALE_GREEN_CONSERVATIVE')

                speed = min(
                    current_speed * 0.5,
                    self._brake_profile(distance, current_speed),
                )

                return StopDecisionResult(
                    should_stop=False,
                    target_speed=max(0.0, speed),
                    jerk_limit=JERK_LIMIT,
                    reason=REASON_APPROACH_STOP,
                    distance=distance,
                    warning_flags=warnings,
                )

            if self._last_light_state in (LIGHT_RED, LIGHT_YELLOW):
                warnings.append('STALE_PREVIOUS_STOP_STATE')

                return self._make_stop_result(
                    distance=distance,
                    current_speed=current_speed,
                    reason=REASON_APPROACH_STOP,
                    warnings=warnings,
                )

        if state == LIGHT_CONFLICT:
            warnings.append('CONFLICT_LIGHT')

            return self._make_stop_result(
                distance=distance,
                current_speed=current_speed,
                reason=REASON_APPROACH_STOP,
                warnings=warnings,
            )

        return None

    def _evaluate_stop_target(
        self,
        stop_target: StopTargetInfo,
        current_speed: float,
        warnings: List[str],
    ) -> StopDecisionResult:

        distance = self._safe_distance(stop_target.distance_from_front_bumper)
        confidence = self._safe_float(stop_target.confidence, 0.0)

        if confidence < 0.3:
            warnings.append('LOW_STOP_TARGET_CONFIDENCE')
            return StopDecisionResult(
                should_stop=False,
                target_speed=current_speed,
                jerk_limit=JERK_LIMIT,
                reason=REASON_LANE_FOLLOW,
                distance=distance,
                warning_flags=warnings,
            )

        reason = self._stop_target_reason_to_target_speed_reason(
            stop_target.reason
        )

        return self._make_stop_result(
            distance=distance,
            current_speed=current_speed,
            reason=reason,
            warnings=warnings,
        )

    def _make_stop_result(
        self,
        distance: float,
        current_speed: float,
        reason: int,
        warnings: List[str],
    ) -> StopDecisionResult:

        speed = self._brake_profile(distance, current_speed)

        return StopDecisionResult(
            should_stop=(distance <= D_STOP),
            target_speed=speed,
            jerk_limit=JERK_LIMIT,
            reason=int(reason),
            distance=distance,
            warning_flags=list(warnings),
        )

    def _brake_profile(
        self,
        distance: float,
        current_speed: float,
    ) -> float:

        distance = self._safe_distance(distance)
        current_speed = max(0.0, self._safe_float(current_speed, 0.0))

        if distance <= D_TOLERANCE:
            return 0.0

        if distance >= D_START:
            return current_speed

        ratio = max(0.0, min(1.0, distance / D_START))
        speed = current_speed * math.sqrt(ratio)

        return max(0.0, speed)

    @staticmethod
    def _stop_target_reason_to_target_speed_reason(reason: Any) -> int:
        if isinstance(reason, str):
            reason_str = reason.upper()

            if reason_str in ('RED_LIGHT', 'STOP_SIGN', 'STOP', 'TRAFFIC_LIGHT'):
                return REASON_APPROACH_STOP

            if reason_str in ('PICKUP', 'DROPOFF'):
                return REASON_PICKUP_DROPOFF

            if reason_str in ('PARK', 'PARK_ENTRY', 'PARK_APPROACH'):
                return REASON_PARK_APPROACH

            return REASON_APPROACH_STOP

        try:
            reason_int = int(reason)
        except Exception:
            return REASON_APPROACH_STOP

        if reason_int in (STOP_TARGET_RED_LIGHT, STOP_TARGET_STOP_SIGN):
            return REASON_APPROACH_STOP

        if reason_int in (STOP_TARGET_PICKUP, STOP_TARGET_DROPOFF):
            return REASON_PICKUP_DROPOFF

        if reason_int == STOP_TARGET_PARK:
            return REASON_PARK_APPROACH

        return REASON_APPROACH_STOP

    @staticmethod
    def _safe_distance(value: Any) -> float:
        distance = StopDecision._safe_float(value, NO_STOP_DISTANCE)

        if not math.isfinite(distance):
            return NO_STOP_DISTANCE

        if distance < 0.0:
            return NO_STOP_DISTANCE

        return distance

    @staticmethod
    def _safe_float(value: Any, fallback: float = 0.0) -> float:
        try:
            value = float(value)
        except Exception:
            return fallback

        if not math.isfinite(value):
            return fallback

        return value
