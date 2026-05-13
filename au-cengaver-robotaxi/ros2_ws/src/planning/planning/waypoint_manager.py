#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
waypoint_manager.py

Algoritma 2: Waypoint Yönetimi (Sıralı Liste + İndeks)
Algoritma 3: Öklid Mesafesi + Heading Toleransı (Hedef Doğrulama)

Algoritma Tablosu v2.0 §4:
  Algo 2:
    - Anlık pose ile aktif waypoint arasındaki Öklid mesafesini hesapla
    - Mesafe < eşik AND Δheading < tolerans → hedef doğrulama
    - Doğrulama başarılı → active_waypoint_id++ ve goal_reached yayınla
    - Tüm waypointler tamamlandı → MISSION_COMPLETE

  Algo 3:
    - dist = sqrt((x−x_t)²+(y−y_t)²)
    - Δheading = │yaw−yaw_t│ (mod 2π)
    - dist < d_thresh AND Δheading < θ_thresh → ulaşıldı

Parametreler (Algo 2):
  WAYPOINT:     mesafe < 0.5m, Δheading < ±20°
  PICKUP/DROPOFF: mesafe < 0.5m, Δheading < ±10°
  PARK:         mesafe < 1.0m, Δheading < ±15°
  DEGRADED modda tüm eşikler ×2
"""

import math
from typing import List, Optional, Tuple
from dataclasses import dataclass

from .geojson_loader import Waypoint, WAYPOINT_TYPE_MAP


# ─── Waypoint Tipleri ──────────────────────────────────────────────────────
TYPE_WAYPOINT   = 0
TYPE_PICKUP     = 1
TYPE_DROPOFF    = 2
TYPE_PARK_ENTRY = 3

# ─── Eşik Değerleri (Algo 2) ───────────────────────────────────────────────
THRESHOLDS = {
    TYPE_WAYPOINT:   {'dist': 0.5, 'heading': math.radians(20.0)},
    TYPE_PICKUP:     {'dist': 0.5, 'heading': math.radians(10.0)},
    TYPE_DROPOFF:    {'dist': 0.5, 'heading': math.radians(10.0)},
    TYPE_PARK_ENTRY: {'dist': 1.0, 'heading': math.radians(15.0)},
}

# DEGRADED modda eşik çarpanı
DEGRADED_MULTIPLIER = 2.0


@dataclass
class WaypointResult:
    """Waypoint kontrolü sonucu."""
    reached:        bool
    distance:       float
    heading_error:  float
    waypoint_id:    int
    waypoint_type:  int
    mission_complete: bool = False


class WaypointManager:
    """
    Algoritma 2 + 3 — Waypoint Yönetimi ve Hedef Doğrulama.

    Kullanım:
        manager = WaypointManager(waypoints)
        result = manager.update(x, y, yaw, localization_degraded=False)
        if result.reached:
            manager.advance()
    """

    def __init__(self, waypoints: List[Waypoint]):
        self._waypoints       = waypoints
        self._active_index    = 0
        self._mission_complete = False
        self._completed_ids: List[int] = []

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def update(
        self,
        x: float,
        y: float,
        yaw: float,
        localization_degraded: bool = False,
        position_covariance:   float = 0.0
    ) -> WaypointResult:
        """
        Anlık pose ile aktif waypoint arasındaki mesafeyi hesapla.
        Algoritma 2 + 3.

        Args:
            x, y, yaw: Anlık araç pozu (map frame)
            localization_degraded: DEGRADED mod → eşikler ×2
            position_covariance: Yüksekse eşikler dinamik genişler

        Returns:
            WaypointResult
        """
        if self._mission_complete or not self._waypoints:
            return WaypointResult(
                reached=False,
                distance=float('inf'),
                heading_error=float('inf'),
                waypoint_id=-1,
                waypoint_type=-1,
                mission_complete=self._mission_complete
            )

        wp = self.active_waypoint
        if wp is None:
            return WaypointResult(
                reached=False,
                distance=float('inf'),
                heading_error=float('inf'),
                waypoint_id=-1,
                waypoint_type=-1,
                mission_complete=True
            )

        # Algoritma 3 — Öklid mesafesi + heading toleransı
        dist, h_err = self._check_goal(x, y, yaw, wp)

        # Eşik değerleri
        d_thresh, θ_thresh = self._get_thresholds(
            wp.type,
            localization_degraded,
            position_covariance
        )

        reached = (dist < d_thresh) and (abs(h_err) < θ_thresh)

        return WaypointResult(
            reached=reached,
            distance=dist,
            heading_error=h_err,
            waypoint_id=wp.id,
            waypoint_type=wp.type,
            mission_complete=False
        )

    def advance(self) -> bool:
        """
        Aktif waypoint'i tamamla, sıradakine geç.

        Returns:
            True: Sıradaki waypoint var
            False: Tüm waypointler tamamlandı (MISSION_COMPLETE)
        """
        if self._mission_complete:
            return False

        wp = self.active_waypoint
        if wp is not None:
            self._completed_ids.append(wp.id)

        self._active_index += 1

        if self._active_index >= len(self._waypoints):
            self._mission_complete = True
            return False

        return True

    def reset(self):
        """Waypoint listesini başa al."""
        self._active_index     = 0
        self._mission_complete = False
        self._completed_ids    = []

    def reload(self, waypoints: List[Waypoint]):
        """Yeni waypoint listesi yükle."""
        self._waypoints = waypoints
        self.reset()

    # ───────────────────────────────────────────────────────────────────────
    # PROPERTIES
    # ───────────────────────────────────────────────────────────────────────

    @property
    def active_waypoint(self) -> Optional[Waypoint]:
        """Aktif waypoint."""
        if self._active_index < len(self._waypoints):
            return self._waypoints[self._active_index]
        return None

    @property
    def next_waypoint(self) -> Optional[Waypoint]:
        """Sonraki waypoint."""
        idx = self._active_index + 1
        if idx < len(self._waypoints):
            return self._waypoints[idx]
        return None

    @property
    def active_index(self) -> int:
        return self._active_index

    @property
    def total_waypoints(self) -> int:
        return len(self._waypoints)

    @property
    def completed_count(self) -> int:
        return len(self._completed_ids)

    @property
    def mission_complete(self) -> bool:
        return self._mission_complete

    @property
    def completed_ids(self) -> List[int]:
        return list(self._completed_ids)

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 3
    # ───────────────────────────────────────────────────────────────────────

    def _check_goal(
        self,
        x: float, y: float, yaw: float,
        wp: Waypoint
    ) -> Tuple[float, float]:
        """
        Algoritma 3 — Öklid mesafesi + heading toleransı.

        dist = sqrt((x−x_t)²+(y−y_t)²)
        Δheading = │yaw−yaw_t│ (mod 2π) → [-π, π]
        """
        # Öklid mesafesi
        dist = math.sqrt((x - wp.x) ** 2 + (y - wp.y) ** 2)

        # Heading hatası — normalize et
        h_err = self._normalize_angle(yaw - wp.yaw)

        return dist, h_err

    def _get_thresholds(
        self,
        wp_type: int,
        degraded: bool,
        position_covariance: float
    ) -> Tuple[float, float]:
        """
        Algoritma 2 — Waypoint tipine göre eşik değerleri.
        DEGRADED modda ×2, yüksek kovaryans'ta dinamik genişleme.
        """
        thresh = THRESHOLDS.get(wp_type, THRESHOLDS[TYPE_WAYPOINT])
        d_thresh = thresh['dist']
        θ_thresh = thresh['heading']

        # DEGRADED mod → ×2
        if degraded:
            d_thresh *= DEGRADED_MULTIPLIER
            θ_thresh *= DEGRADED_MULTIPLIER

        # Yüksek kovaryans → dinamik genişleme
        # Localization Contract §7
        if position_covariance > 1.0:
            scale    = min(2.0, 1.0 + position_covariance)
            d_thresh *= scale
            θ_thresh *= scale

        return d_thresh, θ_thresh

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle