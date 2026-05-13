#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
stop_decision.py

Algoritma 15: Stop Line Yaklaşımı + Jerk Sınırlı Fren Profili
  Trafik ışığı veya STOP tabelasında dur çizgisine yumuşak fren ile durur

Algoritma Tablosu v2.0 §4 Algoritma 15:
  - distance_from_front_bumper'dan kademeli yavaşlama profili hesapla
  - v(d) = v_max · sqrt(d / d_start) — kök profili
  - Her trajectory noktasına o noktadaki hedef hızı ata
  - distance < 0.5m → speed=0 noktaları ekle
  - traffic_light GREEN → normal LANE_FOLLOW'a dön

Parametreler:
  d_start = 5.0m (yavaşlama başlangıç mesafesi)
  jerk_limit = 2.0 m/s³
  afren = 6.5 m/s² (BEE1 maks fiziksel fren)
  Dur toleransı = ±0.3m

Sözleşme: Perception ↔ Planner Contract v1.4 §8
  - state=RED + relevant=true + confirmed=true → STOP_APPROACH
  - state=GREEN + relevant=true + confirmed=true → LANE_FOLLOW
  - state=STALE + last_state=GREEN + in_stop_zone → konservatif mod
  - confirmed=false → işleme alma
"""

import math
from dataclasses import dataclass
from typing import List, Optional

from .trajectory_builder import TrajectoryPoint


# ─── Trafik Işığı State Sabitleri ──────────────────────────────────────────
LIGHT_UNKNOWN  = 0
LIGHT_RED      = 1
LIGHT_YELLOW   = 2
LIGHT_GREEN    = 3
LIGHT_STALE    = 4
LIGHT_CONFLICT = 5

# ─── Parametreler ──────────────────────────────────────────────────────────
D_START        = 5.0    # metre — yavaşlama başlangıç mesafesi
D_STOP         = 0.5    # metre — dur eşiği
D_TOLERANCE    = 0.3    # metre — dur toleransı
JERK_LIMIT     = 2.0    # m/s³
A_BRAKE_MAX    = 6.5    # m/s² — BEE1 maks fiziksel fren


@dataclass
class StopDecisionResult:
    """Dur kararı çıktısı."""
    should_stop:    bool
    target_speed:   float    # m/s
    jerk_limit:     float    # m/s³
    reason:         str      # 'RED_LIGHT', 'STOP_SIGN', 'YELLOW', 'CLEAR'
    distance:       float    # dur noktasına mesafe
    warning_flags:  List[str]


@dataclass
class TrafficLightInfo:
    """Trafik ışığı bilgisi."""
    state:              int     # LIGHT_* sabitleri
    confidence:         float   # 0.0–1.0
    relevant_to_route:  bool
    confirmed:          bool    # 3 kare teyit
    in_stop_zone:       bool
    distance_to_stop:   float   # front_bumper'a mesafe
    last_state:         int = LIGHT_UNKNOWN


@dataclass
class StopTargetInfo:
    """Stop target bilgisi."""
    distance_from_front_bumper: float
    reason:                     str     # 'RED_LIGHT', 'STOP_SIGN', 'PICKUP', 'DROPOFF'
    confidence:                 float


class StopDecision:
    """
    Algoritma 15 — Stop Line Yaklaşımı + Jerk Sınırlı Fren Profili.

    Kullanım:
        sd = StopDecision()
        result = sd.decide(
            light=traffic_light_info,
            stop_target=stop_target_info,
            current_speed=4.0
        )
    """

    def __init__(self):
        self._last_light_state = LIGHT_UNKNOWN
        self._stop_confirmed   = False

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def decide(
        self,
        light:         Optional[TrafficLightInfo],
        stop_target:   Optional[StopTargetInfo],
        current_speed: float,
    ) -> StopDecisionResult:
        """
        Dur kararı ver.

        Perception ↔ Planner Contract v1.4 §8 kuralları:
          RED + relevant + confirmed → STOP_APPROACH
          GREEN + relevant + confirmed → LANE_FOLLOW
          STALE + last=GREEN + in_stop_zone → konservatif
          confirmed=false → işleme alma
        """
        warnings = []

        # Trafik ışığı kararı
        light_result = self._evaluate_light(light, current_speed, warnings)
        if light_result is not None:
            return light_result

        # Stop target kararı (STOP tabela, pickup/dropoff)
        if stop_target is not None:
            return self._evaluate_stop_target(
                stop_target, current_speed, warnings
            )

        # Hiçbir dur koşulu yok
        return StopDecisionResult(
            should_stop=False,
            target_speed=current_speed,
            jerk_limit=JERK_LIMIT,
            reason='CLEAR',
            distance=float('inf'),
            warning_flags=warnings
        )

    def apply_to_trajectory(
        self,
        trajectory:    List[TrajectoryPoint],
        stop_distance: float,
        current_speed: float,
    ) -> List[TrajectoryPoint]:
        """
        Trajectory noktalarına fren profili uygula.
        Algoritma 15: v(d) = v_max · sqrt(d / d_start)
        """
        if not trajectory:
            return trajectory

        updated = []
        for pt in trajectory:
            d = stop_distance - pt.distance_from_start

            if d <= D_TOLERANCE:
                speed = 0.0
            elif d < D_START:
                ratio = d / D_START
                speed = current_speed * math.sqrt(ratio)
                speed = max(0.0, speed)
            else:
                speed = pt.speed

            updated.append(TrajectoryPoint(
                x=pt.x,
                y=pt.y,
                yaw=pt.yaw,
                speed=speed,
                curvature=pt.curvature,
                distance_from_start=pt.distance_from_start
            ))

        return updated

    def update_light_state(self, state: int):
        """Son trafik ışığı durumunu güncelle (STALE için)."""
        if state not in (LIGHT_STALE, LIGHT_UNKNOWN):
            self._last_light_state = state

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _evaluate_light(
        self,
        light:         Optional[TrafficLightInfo],
        current_speed: float,
        warnings:      List[str]
    ) -> Optional[StopDecisionResult]:
        """
        Trafik ışığı kararı.
        Perception ↔ Planner Contract v1.4 §8 davranış tablosu.
        """
        if light is None:
            return None

        self.update_light_state(light.state)

        # confirmed=false → işleme alma
        if not light.confirmed:
            warnings.append('LIGHT_NOT_CONFIRMED')
            return None

        # relevant_to_route=false → sadece logla
        if not light.relevant_to_route:
            return None

        state = light.state
        dist  = light.distance_to_stop

        # RED → STOP_APPROACH
        if state == LIGHT_RED:
            speed = self._brake_profile(dist, current_speed)
            return StopDecisionResult(
                should_stop=True,
                target_speed=speed,
                jerk_limit=JERK_LIMIT,
                reason='RED_LIGHT',
                distance=dist,
                warning_flags=warnings
            )

        # YELLOW → hız yarıya indir, yaklaş
        if state == LIGHT_YELLOW:
            speed = min(current_speed * 0.5,
                        self._brake_profile(dist, current_speed))
            warnings.append('YELLOW_LIGHT')
            return StopDecisionResult(
                should_stop=False,
                target_speed=speed,
                jerk_limit=JERK_LIMIT,
                reason='YELLOW',
                distance=dist,
                warning_flags=warnings
            )

        # GREEN + relevant + confirmed → LANE_FOLLOW
        if state == LIGHT_GREEN:
            return None   # Devam et

        # UNKNOWN + in_stop_zone → RED gibi davran
        if state == LIGHT_UNKNOWN and light.in_stop_zone:
            warnings.append('UNKNOWN_LIGHT_IN_STOP_ZONE')
            speed = self._brake_profile(dist, current_speed)
            return StopDecisionResult(
                should_stop=True,
                target_speed=speed,
                jerk_limit=JERK_LIMIT,
                reason='RED_LIGHT',
                distance=dist,
                warning_flags=warnings
            )

        # STALE + last=GREEN + in_stop_zone → konservatif
        if state == LIGHT_STALE:
            if self._last_light_state == LIGHT_GREEN \
               and light.in_stop_zone:
                warnings.append('STALE_LIGHT_CONSERVATIVE')
                speed = min(current_speed * 0.5,
                            self._brake_profile(dist, current_speed))
                return StopDecisionResult(
                    should_stop=False,
                    target_speed=speed,
                    jerk_limit=JERK_LIMIT,
                    reason='YELLOW',
                    distance=dist,
                    warning_flags=warnings
                )
            elif self._last_light_state in (LIGHT_RED, LIGHT_YELLOW):
                # Eski kırmızıyla bekle
                speed = self._brake_profile(dist, current_speed)
                return StopDecisionResult(
                    should_stop=True,
                    target_speed=speed,
                    jerk_limit=JERK_LIMIT,
                    reason='RED_LIGHT',
                    distance=dist,
                    warning_flags=warnings
                )

        # CONFLICT → RED kabul et
        if state == LIGHT_CONFLICT:
            warnings.append('CONFLICT_LIGHT')
            speed = self._brake_profile(dist, current_speed)
            return StopDecisionResult(
                should_stop=True,
                target_speed=speed,
                jerk_limit=JERK_LIMIT,
                reason='RED_LIGHT',
                distance=dist,
                warning_flags=warnings
            )

        return None

    def _evaluate_stop_target(
        self,
        stop_target:   StopTargetInfo,
        current_speed: float,
        warnings:      List[str]
    ) -> StopDecisionResult:
        """STOP tabela, pickup/dropoff dur kararı."""
        dist  = stop_target.distance_from_front_bumper
        speed = self._brake_profile(dist, current_speed)

        return StopDecisionResult(
            should_stop=(dist <= D_STOP),
            target_speed=speed,
            jerk_limit=JERK_LIMIT,
            reason=stop_target.reason,
            distance=dist,
            warning_flags=warnings
        )

    def _brake_profile(
        self,
        distance:      float,
        current_speed: float
    ) -> float:
        """
        Algoritma 15 — Kök fren profili.
        v(d) = v_max · sqrt(d / d_start)
        """
        if distance <= D_TOLERANCE:
            return 0.0

        if distance >= D_START:
            return current_speed

        ratio = distance / D_START
        speed = current_speed * math.sqrt(ratio)
        return max(0.0, speed)