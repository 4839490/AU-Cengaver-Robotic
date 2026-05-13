#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
speed_profile.py

Algoritma 9: FSM Moduna + Eğriliğe Bağlı Dinamik Hız Profili
  FSM moduna ve yol geometrisine göre hedef hızı belirler

Algoritma Tablosu v2.0 §4 Algoritma 9:
  - planner_mode'a göre baz hız seç
  - LANE_FOLLOW: v = v_max · (1 − k · |curvature|)
  - localization_confidence < 0.5 → hızı %50 düşür
  - status=DEGRADED → hızı %30 düşür
  - jerk_limit belirle (mod bazlı)

Parametreler:
  LANE_FOLLOW:    max 6.67 m/s (24 km/h) — vehicle_params.yaml
  JUNCTION/TUNNEL: 2.78 m/s (10 km/h)
  PICKUP/DROPOFF: 0.83 m/s (3 km/h)
  PARK_APPROACH:  1.39 m/s (5 km/h)
  PARK_MANEUVER:  0.83 m/s (3 km/h)
  jerk_limit:     1.0–10.0 m/s³

Sözleşme: Planner ↔ Controller Contract v1.3 §6 + §8
  - Tek kaynak: vehicle_params.yaml
  - final_speed = min(TargetSpeed.speed, TrajectoryPoint.speed)
  - EMERGENCY_STOP: jerk=10.0
"""

import math
from dataclasses import dataclass
from typing import Optional


# ─── AutonomyMode Sabitleri (common_msgs/AutonomyMode) ─────────────────────
MODE_LANE_FOLLOW      = 0
MODE_STOP_APPROACH    = 1
MODE_PICKUP_APPROACH  = 2
MODE_DROPOFF_APPROACH = 3
MODE_OBSTACLE_AVOID   = 4
MODE_PARK_APPROACH    = 5
MODE_PARK_MANEUVER    = 6
MODE_MISSION_COMPLETE = 7

# ─── TargetSpeed Reason Sabitleri (planning_msgs/TargetSpeed) ──────────────
REASON_LANE_FOLLOW    = 0
REASON_APPROACH_STOP  = 1
REASON_PICKUP_DROPOFF = 2
REASON_OBSTACLE_SLOW  = 3
REASON_JUNCTION       = 4
REASON_TUNNEL         = 5
REASON_PARK_APPROACH  = 6
REASON_PARK_MANEUVER  = 7
REASON_EMERGENCY_STOP = 8

# ─── Lokalizasyon Status ───────────────────────────────────────────────────
LOC_STATUS_DEGRADED = 4
LOC_STATUS_LOST     = 6

# ─── Hız Tablosu (m/s) — vehicle_params.yaml referansı ───────────────────
# Planner ↔ Controller Contract v1.3 §6
SPEED_TABLE = {
    MODE_LANE_FOLLOW:      6.67,   # 24 km/h
    MODE_STOP_APPROACH:    0.0,
    MODE_PICKUP_APPROACH:  0.83,   # 3 km/h
    MODE_DROPOFF_APPROACH: 0.83,   # 3 km/h
    MODE_OBSTACLE_AVOID:   2.78,   # 10 km/h — TTC'ye göre kademeli
    MODE_PARK_APPROACH:    1.39,   # 5 km/h
    MODE_PARK_MANEUVER:    0.83,   # 3 km/h
    MODE_MISSION_COMPLETE: 0.0,
}

# ─── Jerk Tablosu (m/s³) ──────────────────────────────────────────────────
JERK_TABLE = {
    MODE_LANE_FOLLOW:      2.0,
    MODE_STOP_APPROACH:    2.0,
    MODE_PICKUP_APPROACH:  1.5,
    MODE_DROPOFF_APPROACH: 1.5,
    MODE_OBSTACLE_AVOID:   1.5,
    MODE_PARK_APPROACH:    1.5,
    MODE_PARK_MANEUVER:    1.0,
    MODE_MISSION_COMPLETE: 2.0,
}


@dataclass
class SpeedOutput:
    """Hız profili çıktısı."""
    speed:      float   # m/s
    jerk_limit: float   # m/s³
    reason:     int     # TargetSpeed reason sabiti


class SpeedProfile:
    """
    Algoritma 9 — FSM Moduna + Eğriliğe Bağlı Dinamik Hız Profili.

    Kullanım:
        sp = SpeedProfile()
        output = sp.compute(
            mode=MODE_LANE_FOLLOW,
            curvature=0.1,
            localization_confidence=0.9,
            loc_status=LOC_STATUS_OK
        )
    """

    def __init__(self):
        # Eğrilik-hız katsayısı — kalibrasyon testi gerekli
        self._k_curvature = 2.0

        # Araç max hızı — vehicle_params.yaml'dan okunmalı
        self._v_max = 6.67   # m/s (24 km/h)

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def compute(
        self,
        mode:                    int,
        curvature:               float = 0.0,
        localization_confidence: float = 1.0,
        loc_status:              int   = 0,
        emergency:               bool  = False,
        junction:                bool  = False,
        tunnel:                  bool  = False,
    ) -> SpeedOutput:
        """
        Algoritma 9 — Dinamik hız profili hesapla.

        Args:
            mode:                    FSM modu (AutonomyMode)
            curvature:               Yol eğriliği (1/m)
            localization_confidence: EKF güveni (0.0–1.0)
            loc_status:              Lokalizasyon durumu
            emergency:               EMERGENCY_STOP gerekiyor mu
            junction:                Kavşak modu
            tunnel:                  Tünel modu

        Returns:
            SpeedOutput(speed, jerk_limit, reason)
        """
        # EMERGENCY_STOP — her şeyden önce
        if emergency:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=10.0,
                reason=REASON_EMERGENCY_STOP
            )

        # MISSION_COMPLETE — dur
        if mode == MODE_MISSION_COMPLETE:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_APPROACH_STOP
            )

        # JUNCTION / TUNNEL — TargetSpeed.reason olarak kullanılır
        # Planner ↔ Controller Contract v1.3: JUNCTION mode değil!
        if junction:
            return SpeedOutput(
                speed=2.78,   # 10 km/h
                jerk_limit=2.0,
                reason=REASON_JUNCTION
            )

        if tunnel:
            return SpeedOutput(
                speed=2.78,   # 10 km/h
                jerk_limit=2.0,
                reason=REASON_TUNNEL
            )

        # Baz hız — mod tablosundan
        base_speed = SPEED_TABLE.get(mode, 0.0)
        jerk_limit = JERK_TABLE.get(mode, 2.0)
        reason     = self._mode_to_reason(mode)

        # LANE_FOLLOW: eğrilik bazlı hız azaltma
        if mode == MODE_LANE_FOLLOW:
            base_speed = self._curvature_speed(curvature)

        # Lokalizasyon bazlı hız azaltma
        base_speed = self._apply_localization_factor(
            base_speed, localization_confidence, loc_status
        )

        # Negatif hız olmasın
        base_speed = max(0.0, base_speed)

        return SpeedOutput(
            speed=base_speed,
            jerk_limit=jerk_limit,
            reason=reason
        )

    def compute_stop_approach(
        self,
        distance_to_stop: float,
        current_speed:    float,
        d_start:          float = 5.0
    ) -> SpeedOutput:
        """
        Dur çizgisine kademeli fren profili.
        Algoritma 15 için yardımcı.

        v(d) = v_max · sqrt(d / d_start) — kök profili
        """
        if distance_to_stop <= 0.3:
            return SpeedOutput(
                speed=0.0,
                jerk_limit=2.0,
                reason=REASON_APPROACH_STOP
            )

        if distance_to_stop >= d_start:
            # Henüz fren bölgesinde değil
            return SpeedOutput(
                speed=current_speed,
                jerk_limit=2.0,
                reason=REASON_LANE_FOLLOW
            )

        # Kök profili
        ratio = distance_to_stop / d_start
        speed = current_speed * math.sqrt(ratio)
        speed = max(0.0, speed)

        return SpeedOutput(
            speed=speed,
            jerk_limit=2.0,
            reason=REASON_APPROACH_STOP
        )

    def set_k_curvature(self, k: float):
        """Eğrilik-hız katsayısını ayarla (kalibrasyon)."""
        self._k_curvature = k

    def set_v_max(self, v_max: float):
        """Maksimum hızı ayarla — vehicle_params.yaml'dan."""
        self._v_max = v_max

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _curvature_speed(self, curvature: float) -> float:
        """
        Algoritma 9 — Eğrilik bazlı hız.
        v = v_max · (1 − k · |curvature|)
        """
        reduction = self._k_curvature * abs(curvature)
        speed     = self._v_max * (1.0 - reduction)
        return max(0.5, min(self._v_max, speed))

    def _apply_localization_factor(
        self,
        speed:      float,
        confidence: float,
        loc_status: int
    ) -> float:
        """
        Lokalizasyon kalitesine göre hız azalt.

        Algo 9:
          confidence < 0.5 → hız %50
          DEGRADED          → hız %70
        """
        # status=LOST → 0 hız
        if loc_status == LOC_STATUS_LOST:
            return 0.0

        # DEGRADED → %70
        if loc_status == LOC_STATUS_DEGRADED:
            speed *= 0.7

        # Düşük confidence → %50
        if confidence < 0.5:
            speed *= 0.5

        return speed

    def _mode_to_reason(self, mode: int) -> int:
        """FSM modu → TargetSpeed reason."""
        mapping = {
            MODE_LANE_FOLLOW:      REASON_LANE_FOLLOW,
            MODE_STOP_APPROACH:    REASON_APPROACH_STOP,
            MODE_PICKUP_APPROACH:  REASON_PICKUP_DROPOFF,
            MODE_DROPOFF_APPROACH: REASON_PICKUP_DROPOFF,
            MODE_OBSTACLE_AVOID:   REASON_OBSTACLE_SLOW,
            MODE_PARK_APPROACH:    REASON_PARK_APPROACH,
            MODE_PARK_MANEUVER:    REASON_PARK_MANEUVER,
            MODE_MISSION_COMPLETE: REASON_APPROACH_STOP,
        }
        return mapping.get(mode, REASON_LANE_FOLLOW)