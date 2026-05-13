#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
trajectory_builder.py

Algoritma 6: Şerit Geometrisi Tabanlı Adaptif Lookahead + Lokal Yörünge
  Aktif şerit bilgisinden kısa vadeli referans yolu üretir

Algoritma Tablosu v2.0 §4 Algoritma 6:
  - lane_model.curvature'a göre lookahead mesafesini belirle
    Düz (|curvature| < 0.05):   lookahead = 2.5m
    Orta viraj (0.05–0.2):      lookahead = 1.5m
    Keskin viraj (>0.2):        lookahead = 0.8m
    DEGRADED:                   max lookahead = 1.5m
  - centerline noktalarını lookahead mesafesine kadar al
  - Spline ile ara değerleme → TrajectoryPoint dizisi üret
  - Her noktaya hız ata (FSM moduna göre)

Parametreler:
  lookahead_min = 0.8m
  lookahead_max = 2.5m
  DEGRADED modda lookahead_max = 1.5m
  Nokta aralığı ≤ 0.1m
  Min nokta sayısı = 10

Sözleşme: Planner ↔ Controller Contract v1.3
  - frame_id: map
  - Min 10 nokta, ≤0.1m aralık, ≥3m ufuk
  - status=LOST → trajectory üretme durdur
  - status=DEGRADED → lookahead kıs
"""

import math
from typing import List, Optional, Tuple
from dataclasses import dataclass


# ─── Sabitler ──────────────────────────────────────────────────────────────
LOOKAHEAD_MIN         = 0.8    # metre
LOOKAHEAD_MAX         = 2.5    # metre
LOOKAHEAD_MAX_DEGRADED = 1.5   # metre — DEGRADED modda
POINT_INTERVAL        = 0.1    # metre — nokta aralığı
MIN_POINTS            = 10     # minimum trajectory nokta sayısı
MIN_HORIZON           = 3.0    # metre — minimum ufuk mesafesi

# Eğrilik eşikleri
CURVATURE_STRAIGHT    = 0.05   # düz yol
CURVATURE_MEDIUM      = 0.20   # orta viraj

# Lokalizasyon status sabitleri
LOC_STATUS_OK         = 0
LOC_STATUS_DEGRADED   = 4
LOC_STATUS_LOST       = 6


@dataclass
class TrajectoryPoint:
    """Tek bir trajectory noktası — map frame."""
    x:                   float    # metre — map frame
    y:                   float    # metre — map frame
    yaw:                 float    # radyan
    speed:               float    # m/s — noktasal referans hız
    curvature:           float    # 1/m
    distance_from_start: float    # metre


class TrajectoryBuilder:
    """
    Algoritma 6 — Şerit Geometrisi Tabanlı Adaptif Lookahead + Lokal Yörünge.

    Kullanım:
        builder = TrajectoryBuilder()
        points = builder.build(
            centerline=[(x0,y0), (x1,y1), ...],
            curvature=0.1,
            ego_x=0.0, ego_y=0.0, ego_yaw=0.0,
            ego_speed=2.0,
            target_speed=6.67,
            loc_status=0
        )
    """

    def __init__(self):
        self._last_trajectory: List[TrajectoryPoint] = []

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def build(
        self,
        centerline: List[Tuple[float, float]],
        curvature:   float,
        ego_x:       float,
        ego_y:       float,
        ego_yaw:     float,
        ego_speed:   float,
        target_speed: float,
        loc_status:  int = LOC_STATUS_OK,
    ) -> Optional[List[TrajectoryPoint]]:
        """
        Şerit centerline'ından trajectory üret.

        Args:
            centerline:   [(x, y), ...] — base_link veya map frame noktaları
            curvature:    Anlık yol eğriliği (1/m)
            ego_x/y/yaw:  Araç pozu (map frame)
            ego_speed:    Araç hızı (m/s)
            target_speed: Hedef hız (m/s) — speed_profile'dan gelir
            loc_status:   Lokalizasyon durumu

        Returns:
            List[TrajectoryPoint] veya None (LOST durumunda)
        """
        # status=LOST → trajectory üretme durdur (Algo 6)
        if loc_status == LOC_STATUS_LOST:
            return None

        if not centerline or len(centerline) < 2:
            # Centerline yoksa son trajectory'yi koru
            return self._last_trajectory if self._last_trajectory else None

        # 1. Lookahead mesafesini belirle
        lookahead = self._compute_lookahead(
            curvature, ego_speed, loc_status
        )

        # 2. Centerline noktalarını lookahead mesafesine kadar al
        selected = self._select_points(centerline, lookahead)

        if len(selected) < 2:
            return self._last_trajectory if self._last_trajectory else None

        # 3. Spline ile ara değerleme → eşit aralıklı noktalar
        interpolated = self._interpolate(selected)

        if len(interpolated) < MIN_POINTS:
            # Yeterli nokta yoksa son trajectory'yi koru
            return self._last_trajectory if self._last_trajectory else None

        # 4. Her noktaya yaw, eğrilik ve hız ata
        trajectory = self._assign_attributes(
            interpolated, target_speed, curvature
        )

        self._last_trajectory = trajectory
        return trajectory

    def build_from_waypoints(
        self,
        wp_x: float,
        wp_y: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        target_speed: float,
        loc_status: int = LOC_STATUS_OK,
    ) -> Optional[List[TrajectoryPoint]]:
        """
        Waypoint'e doğru basit düz trajectory üret.
        Şerit modeli yokken fallback olarak kullanılır.
        """
        if loc_status == LOC_STATUS_LOST:
            return None

        # ego'dan waypoint'e doğru noktalar üret
        dx    = wp_x - ego_x
        dy    = wp_y - ego_y
        dist  = math.sqrt(dx ** 2 + dy ** 2)
        angle = math.atan2(dy, dx)

        if dist < 0.1:
            return None

        # Eşit aralıklı noktalar
        n_points = max(MIN_POINTS, int(dist / POINT_INTERVAL))
        points   = []

        for i in range(n_points):
            t = i / (n_points - 1)
            x = ego_x + t * dx
            y = ego_y + t * dy
            d = t * dist
            points.append(TrajectoryPoint(
                x=x, y=y,
                yaw=angle,
                speed=target_speed,
                curvature=0.0,
                distance_from_start=d
            ))

        self._last_trajectory = points
        return points

    @property
    def last_trajectory(self) -> List[TrajectoryPoint]:
        """Son üretilen trajectory."""
        return self._last_trajectory

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 6 Adımları
    # ───────────────────────────────────────────────────────────────────────

    def _compute_lookahead(
        self,
        curvature:  float,
        ego_speed:  float,
        loc_status: int
    ) -> float:
        """
        Algoritma 6 — Eğriliğe göre adaptif lookahead.

        Düz (|curvature| < 0.05):  lookahead = 2.5m
        Orta viraj (0.05–0.2):     lookahead = 1.5m
        Keskin viraj (>0.2):       lookahead = 0.8m
        DEGRADED: max = 1.5m
        """
        abs_curv = abs(curvature)

        if abs_curv < CURVATURE_STRAIGHT:
            lookahead = LOOKAHEAD_MAX
        elif abs_curv < CURVATURE_MEDIUM:
            # Lineer interpolasyon: 0.05→2.5m, 0.2→0.8m
            t = (abs_curv - CURVATURE_STRAIGHT) / \
                (CURVATURE_MEDIUM - CURVATURE_STRAIGHT)
            lookahead = LOOKAHEAD_MAX - t * (LOOKAHEAD_MAX - LOOKAHEAD_MIN)
        else:
            lookahead = LOOKAHEAD_MIN

        # Hıza göre minimum lookahead artır
        speed_factor = max(0.0, ego_speed * 0.3)
        lookahead    = max(lookahead, LOOKAHEAD_MIN + speed_factor)

        # DEGRADED modda max kıs
        if loc_status == LOC_STATUS_DEGRADED:
            lookahead = min(lookahead, LOOKAHEAD_MAX_DEGRADED)

        return max(LOOKAHEAD_MIN, lookahead)

    def _select_points(
        self,
        centerline: List[Tuple[float, float]],
        lookahead:  float
    ) -> List[Tuple[float, float]]:
        """
        Centerline noktalarını lookahead mesafesine kadar seç.
        İlk nokta origin (0,0) — base_link frame varsayımı.
        """
        selected = []
        cumulative = 0.0

        for i, pt in enumerate(centerline):
            if i == 0:
                selected.append(pt)
                continue

            prev = centerline[i - 1]
            dist = math.sqrt(
                (pt[0] - prev[0]) ** 2 + (pt[1] - prev[1]) ** 2
            )
            cumulative += dist
            selected.append(pt)

            if cumulative >= max(lookahead, MIN_HORIZON):
                break

        return selected

    def _interpolate(
        self,
        points: List[Tuple[float, float]]
    ) -> List[Tuple[float, float]]:
        """
        Noktalar arası lineer interpolasyon ile eşit aralıklı nokta üret.
        Nokta aralığı = POINT_INTERVAL (0.1m).
        """
        if len(points) < 2:
            return points

        # Toplam uzunluk hesapla
        total_length = 0.0
        for i in range(1, len(points)):
            dx = points[i][0] - points[i-1][0]
            dy = points[i][1] - points[i-1][1]
            total_length += math.sqrt(dx**2 + dy**2)

        if total_length < POINT_INTERVAL:
            return points

        # Eşit aralıklı noktalar üret
        n_points    = max(MIN_POINTS, int(total_length / POINT_INTERVAL))
        result      = []
        seg_index   = 0
        seg_elapsed = 0.0

        for i in range(n_points):
            target_dist = i * (total_length / (n_points - 1))

            # Hangi segment üzerindeyiz bul
            while seg_index < len(points) - 2:
                dx = points[seg_index+1][0] - points[seg_index][0]
                dy = points[seg_index+1][1] - points[seg_index][1]
                seg_len = math.sqrt(dx**2 + dy**2)

                if seg_elapsed + seg_len >= target_dist:
                    break

                seg_elapsed += seg_len
                seg_index   += 1

            # Segment üzerinde interpolasyon
            dx = points[seg_index+1][0] - points[seg_index][0]
            dy = points[seg_index+1][1] - points[seg_index][1]
            seg_len = math.sqrt(dx**2 + dy**2)

            if seg_len < 1e-6:
                result.append(points[seg_index])
                continue

            t = (target_dist - seg_elapsed) / seg_len
            t = max(0.0, min(1.0, t))

            x = points[seg_index][0] + t * dx
            y = points[seg_index][1] + t * dy
            result.append((x, y))

        return result

    def _assign_attributes(
        self,
        points:       List[Tuple[float, float]],
        target_speed: float,
        curvature:    float
    ) -> List[TrajectoryPoint]:
        """Her noktaya yaw, eğrilik ve hız ata."""
        trajectory   = []
        cum_distance = 0.0

        for i, pt in enumerate(points):
            # Yaw — bir sonraki noktaya bakarak hesapla
            if i < len(points) - 1:
                dx  = points[i+1][0] - pt[0]
                dy  = points[i+1][1] - pt[1]
                yaw = math.atan2(dy, dx)
            else:
                # Son nokta — bir öncekiyle aynı yaw
                yaw = trajectory[-1].yaw if trajectory else 0.0

            # Mesafe
            if i > 0:
                dx = pt[0] - points[i-1][0]
                dy = pt[1] - points[i-1][1]
                cum_distance += math.sqrt(dx**2 + dy**2)

            trajectory.append(TrajectoryPoint(
                x=pt[0],
                y=pt[1],
                yaw=yaw,
                speed=target_speed,
                curvature=curvature,
                distance_from_start=cum_distance
            ))

        return trajectory

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle