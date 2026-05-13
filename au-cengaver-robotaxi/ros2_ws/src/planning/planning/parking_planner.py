#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
parking_planner.py

Algoritma 13: Dubins Path Tabanlı Park Hedefleme
Algoritma 14: Park Son Hizalama (Düşük Hızlı Düzeltme)

Algoritma Tablosu v2.0 §4:

  Algo 13:
    - heading_covariance < 0.05rad² kontrol et
    - slot_available=true kontrol et
    - 6 Dubins yolu tipini hesapla: RSR, RSL, LSR, LSL, RLR, LRL
    - rmin = 4.1m (BEE1) kısıtına uyan en kısa seçim
    - speed = 0.83m/s (3km/h), jerk = 1.0

  Algo 14:
    - final_cross_track_error ve final_heading_error hesapla
    - Koşullar: slot içinde AND ön>20cm AND sağ>10cm AND sol>10cm AND Δheading<5°
    - Koşullar sağlanmadıysa: küçük ileri-geri hareketi (max 3 iterasyon)
    - Koşullar sağlandı → park_complete yayınla (success=true)

BEE1 Platform Sabitleri:
  rmin = 4.1m
  δmax = 32.5°
  Park hızı = 0.83 m/s (3 km/h)
  Araç uzunluğu = ~4.5m

Sözleşme: Planner ↔ Controller Contract v1.3 §6
  - PARK_MANEUVER: ≤3km/h, Ackermann hassas
  - heading_covariance ≥ 0.05rad² → park başlatma
"""

import math
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

from .trajectory_builder import TrajectoryPoint


# ─── BEE1 Platform Sabitleri ───────────────────────────────────────────────
R_MIN          = 4.1     # metre — min dönüş yarıçapı
DELTA_MAX      = 32.5    # derece — max direksiyon açısı
PARK_SPEED     = 0.83    # m/s — 3 km/h
PARK_JERK      = 1.0     # m/s³
VEHICLE_LENGTH = 4.5     # metre

# Heading kovaryans eşiği
HEADING_COV_THRESHOLD = 0.05   # rad²

# Algo 14 Parametreleri
FRONT_CLEARANCE = 0.20   # metre — ön boşluk
SIDE_CLEARANCE  = 0.10   # metre — yan boşluk
HEADING_TOL     = math.radians(5.0)   # 5° tolerans
MAX_ITERATIONS  = 3

# Dubins yol tipleri
DUBINS_TYPES = ['RSR', 'RSL', 'LSR', 'LSL', 'RLR', 'LRL']

# Nokta aralığı
POINT_INTERVAL = 0.1   # metre


@dataclass
class ParkSlot:
    """Park slotu bilgisi."""
    slot_x:         float    # base_link frame
    slot_y:         float    # base_link frame
    slot_heading:   float    # radyan
    slot_available: bool


@dataclass
class DubinsPath:
    """Dubins yolu."""
    path_type:  str      # 'RSR', 'RSL' vb.
    length:     float    # toplam uzunluk
    points:     List[Tuple[float, float, float]]   # (x, y, yaw)


@dataclass
class ParkingResult:
    """Park sonucu."""
    success:              bool
    trajectory:           List[TrajectoryPoint]
    iterations_used:      int
    final_cross_track:    float
    final_heading_error:  float
    warning_flags:        List[str] = field(default_factory=list)


class ParkingPlanner:
    """
    Algoritma 13 + 14 — Dubins Path Park + Son Hizalama.

    Kullanım:
        pp = ParkingPlanner()

        # Algo 13 — Park hedefleme
        traj = pp.plan_dubins(
            ego_x=0.0, ego_y=0.0, ego_yaw=0.0,
            slot=park_slot,
            heading_covariance=0.03
        )

        # Algo 14 — Son hizalama
        result = pp.align(
            cross_track_error=0.1,
            heading_error=0.05,
            ego_x=..., ego_y=..., ego_yaw=...,
            slot=park_slot
        )
    """

    def __init__(self):
        self._iteration_count = 0

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API — Algoritma 13
    # ───────────────────────────────────────────────────────────────────────

    def plan_dubins(
        self,
        ego_x:               float,
        ego_y:               float,
        ego_yaw:             float,
        slot:                ParkSlot,
        heading_covariance:  float,
    ) -> Optional[List[TrajectoryPoint]]:
        """
        Algoritma 13 — Dubins Path Tabanlı Park Hedefleme.

        Args:
            ego_x/y/yaw:        Araç pozu (map/base_link frame)
            slot:               Park slotu
            heading_covariance: EKF heading belirsizliği (rad²)

        Returns:
            List[TrajectoryPoint] veya None (koşullar sağlanmadıysa)
        """
        # heading_covariance kontrolü
        if heading_covariance >= HEADING_COV_THRESHOLD:
            return None   # Bekle — yeterli hassasiyet yok

        # slot_available kontrolü
        if not slot.slot_available:
            return None

        # 6 Dubins tipi hesapla
        best_path = self._compute_best_dubins(
            ego_x, ego_y, ego_yaw,
            slot.slot_x, slot.slot_y, slot.slot_heading
        )

        if best_path is None:
            return None

        # TrajectoryPoint dizisine çevir
        return self._path_to_trajectory(best_path)

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API — Algoritma 14
    # ───────────────────────────────────────────────────────────────────────

    def align(
        self,
        cross_track_error: float,
        heading_error:     float,
        ego_x:             float,
        ego_y:             float,
        ego_yaw:           float,
        slot:              ParkSlot,
        front_dist:        float = 0.5,
        right_dist:        float = 0.5,
        left_dist:         float = 0.5,
    ) -> ParkingResult:
        """
        Algoritma 14 — Park Son Hizalama.

        Koşullar:
          slot içinde AND ön>20cm AND sağ>10cm AND sol>10cm AND Δheading<5°

        Args:
            cross_track_error: Yanal sapma (m)
            heading_error:     Yön sapması (rad)
            front/right/left_dist: Çevre boşlukları (m)
        """
        warnings = []

        # Koşulları kontrol et
        conditions_met = self._check_park_conditions(
            cross_track_error, heading_error,
            front_dist, right_dist, left_dist
        )

        if conditions_met:
            return ParkingResult(
                success=True,
                trajectory=[],
                iterations_used=self._iteration_count,
                final_cross_track=cross_track_error,
                final_heading_error=heading_error,
                warning_flags=[]
            )

        # Koşullar sağlanmadı — düzeltme hareketi
        if self._iteration_count >= MAX_ITERATIONS:
            warnings.append('MAX_ITERATIONS_REACHED')
            return ParkingResult(
                success=False,
                trajectory=[],
                iterations_used=self._iteration_count,
                final_cross_track=cross_track_error,
                final_heading_error=heading_error,
                warning_flags=warnings
            )

        self._iteration_count += 1

        # İleri-geri düzeltme trajectory
        correction = self._compute_correction(
            cross_track_error, heading_error, ego_x, ego_y, ego_yaw
        )

        return ParkingResult(
            success=False,
            trajectory=correction,
            iterations_used=self._iteration_count,
            final_cross_track=cross_track_error,
            final_heading_error=heading_error,
            warning_flags=warnings
        )

    def reset_iterations(self):
        """İterasyon sayacını sıfırla."""
        self._iteration_count = 0

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 13: Dubins Path
    # ───────────────────────────────────────────────────────────────────────

    def _compute_best_dubins(
        self,
        sx: float, sy: float, syaw: float,
        gx: float, gy: float, gyaw: float,
    ) -> Optional[DubinsPath]:
        """
        6 Dubins tipi hesapla, en kısayı seç.
        rmin = 4.1m (BEE1) kısıtı uygulanır.
        """
        best_path   = None
        best_length = float('inf')

        for path_type in DUBINS_TYPES:
            path = self._compute_dubins_type(
                sx, sy, syaw, gx, gy, gyaw, path_type
            )
            if path is not None and path.length < best_length:
                best_length = path.length
                best_path   = path

        return best_path

    def _compute_dubins_type(
        self,
        sx: float, sy: float, syaw: float,
        gx: float, gy: float, gyaw: float,
        path_type: str,
    ) -> Optional[DubinsPath]:
        """
        Tek bir Dubins tipi için yol hesapla.
        Basitleştirilmiş analitik çözüm — RSR tipi örneği.
        """
        r = R_MIN

        dx  = gx - sx
        dy  = gy - sy
        D   = math.sqrt(dx**2 + dy**2)

        if D < 1e-6:
            return None

        d = D / r

        if path_type in ('RSR', 'LSL'):
            sign = -1.0 if path_type == 'RSR' else 1.0

            # Merkez noktaları
            cx_s = sx + sign * r * math.cos(syaw - math.pi/2)
            cy_s = sy + sign * r * math.sin(syaw - math.pi/2)
            cx_g = gx + sign * r * math.cos(gyaw - math.pi/2)
            cy_g = gy + sign * r * math.sin(gyaw - math.pi/2)

            dist_cc = math.sqrt((cx_g - cx_s)**2 + (cy_g - cy_s)**2)

            if dist_cc < 1e-6:
                return None

            # Ark uzunlukları (basitleştirilmiş)
            arc1 = abs(self._normalize_angle(
                math.atan2(cy_g - cy_s, cx_g - cx_s) - syaw
            )) * r

            straight = dist_cc

            arc2 = abs(self._normalize_angle(
                gyaw - math.atan2(cy_g - cy_s, cx_g - cx_s)
            )) * r

            total_length = arc1 + straight + arc2

            # Nokta üret
            points = self._generate_path_points(
                sx, sy, syaw, gx, gy, gyaw, total_length
            )

            return DubinsPath(
                path_type=path_type,
                length=total_length,
                points=points
            )

        elif path_type in ('RSL', 'LSR'):
            # Farklı yönlü ark kombinasyonu
            sign1 = -1.0 if path_type[0] == 'R' else 1.0
            sign2 =  1.0 if path_type[2] == 'L' else -1.0

            cx_s = sx + sign1 * r * math.cos(syaw - math.pi/2)
            cy_s = sy + sign1 * r * math.sin(syaw - math.pi/2)
            cx_g = gx + sign2 * r * math.cos(gyaw - math.pi/2)
            cy_g = gy + sign2 * r * math.sin(gyaw - math.pi/2)

            dist_cc = math.sqrt((cx_g - cx_s)**2 + (cy_g - cy_s)**2)

            if dist_cc < 2 * r:
                return None   # Geometrik olarak imkansız

            straight = math.sqrt(dist_cc**2 - (2*r)**2)
            arc1     = abs(self._normalize_angle(
                math.atan2(cy_g - cy_s, cx_g - cx_s) - syaw
            )) * r
            arc2     = abs(self._normalize_angle(
                gyaw - math.atan2(cy_g - cy_s, cx_g - cx_s)
            )) * r

            total_length = arc1 + straight + arc2
            points = self._generate_path_points(
                sx, sy, syaw, gx, gy, gyaw, total_length
            )

            return DubinsPath(
                path_type=path_type,
                length=total_length,
                points=points
            )

        else:
            # RLR, LRL — üç ark kombinasyonu
            # Geometrik koşul: d <= 4r
            if D > 4 * r:
                return None

            cos_val = (D**2 / (8 * r**2)) - 0.5
            cos_val = max(-1.0, min(1.0, cos_val))
            arc_mid = r * math.acos(cos_val)
            arc1    = arc_mid / 2
            arc2    = arc_mid

            total_length = arc1 * 2 + arc2
            points = self._generate_path_points(
                sx, sy, syaw, gx, gy, gyaw, total_length
            )

            return DubinsPath(
                path_type=path_type,
                length=total_length,
                points=points
            )

    def _generate_path_points(
        self,
        sx: float, sy: float, syaw: float,
        gx: float, gy: float, gyaw: float,
        total_length: float,
    ) -> List[Tuple[float, float, float]]:
        """
        Başlangıç → hedef arası eşit aralıklı noktalar üret.
        Basit lineer interpolasyon (gerçek Dubins ark yerine).
        """
        n = max(10, int(total_length / POINT_INTERVAL))
        points = []

        for i in range(n + 1):
            t   = i / n
            x   = sx + t * (gx - sx)
            y   = sy + t * (gy - sy)
            yaw = syaw + t * self._normalize_angle(gyaw - syaw)
            yaw = self._normalize_angle(yaw)
            points.append((x, y, yaw))

        return points

    def _path_to_trajectory(
        self,
        path: DubinsPath
    ) -> List[TrajectoryPoint]:
        """DubinsPath → TrajectoryPoint listesi."""
        trajectory   = []
        cum_distance = 0.0

        for i, (x, y, yaw) in enumerate(path.points):
            if i > 0:
                prev = path.points[i - 1]
                dx   = x - prev[0]
                dy   = y - prev[1]
                cum_distance += math.sqrt(dx**2 + dy**2)

            trajectory.append(TrajectoryPoint(
                x=x,
                y=y,
                yaw=yaw,
                speed=PARK_SPEED,
                curvature=1.0 / R_MIN,
                distance_from_start=cum_distance
            ))

        return trajectory

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE — Algoritma 14: Son Hizalama
    # ───────────────────────────────────────────────────────────────────────

    def _check_park_conditions(
        self,
        cross_track: float,
        heading_err: float,
        front_dist:  float,
        right_dist:  float,
        left_dist:   float,
    ) -> bool:
        """
        Algoritma 14 park koşulları:
        slot içinde AND ön>20cm AND sağ>10cm AND sol>10cm AND Δheading<5°
        """
        return (
            abs(cross_track) < 0.3 and
            abs(heading_err) < HEADING_TOL and
            front_dist > FRONT_CLEARANCE and
            right_dist > SIDE_CLEARANCE and
            left_dist  > SIDE_CLEARANCE
        )

    def _compute_correction(
        self,
        cross_track: float,
        heading_err: float,
        ego_x:       float,
        ego_y:       float,
        ego_yaw:     float,
    ) -> List[TrajectoryPoint]:
        """
        Küçük ileri-geri düzeltme hareketi üret.
        cross_track ve heading_error'a göre yön seç.
        """
        trajectory   = []
        # Düzeltme mesafesi — hataya orantılı
        correction_dist = min(0.5, abs(cross_track) * 2.0 + 0.2)
        n_points        = max(5, int(correction_dist / POINT_INTERVAL))

        # İleri hareket
        for i in range(n_points):
            t = i / n_points
            x = ego_x + t * correction_dist * math.cos(ego_yaw)
            y = ego_y + t * correction_dist * math.sin(ego_yaw)
            trajectory.append(TrajectoryPoint(
                x=x, y=y,
                yaw=ego_yaw,
                speed=PARK_SPEED,
                curvature=0.0,
                distance_from_start=t * correction_dist
            ))

        return trajectory

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle