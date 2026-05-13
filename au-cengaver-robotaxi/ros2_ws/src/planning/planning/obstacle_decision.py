#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
obstacle_decision.py

Algoritma 10: Trajectory Sampling + Ağırlıklı Maliyet
Algoritma 11: Mesafe Katmanlı Reaktif Engel Kaçınma
"""

import math
from dataclasses import dataclass
from typing import List, Optional, Tuple, Any


# ─── Trajectory Sampling ───────────────────────────────────────────────────
K_SAMPLES = 20
SIM_TIME = 0.5
SIM_DT = 0.05

W_PATH = 1.0
W_OBS = 5.0
W_HEAD = 0.5
COLLISION_COST = 1000.0

# ─── Reaktif Engel Kararı ──────────────────────────────────────────────────
TTC_WATCH = 3.0
TTC_SLOW = 2.0
TTC_STOP = 1.0

REACTION_TIME = 0.3
BRAKING_MARGIN = 0.2
PEDESTRIAN_MULT = 2.0

# ─── Araç Sabitleri ────────────────────────────────────────────────────────
WHEELBASE = 2.40        # Contract v1.3 vehicle_params referans
MAX_STEER_DEG = 32.5
V_MAX = 6.67

# ─── Localization Status ───────────────────────────────────────────────────
LOC_OK = 0
LOC_DEGRADED = 4
LOC_LOST = 6


@dataclass
class ObstacleTrack:
    """Perception'dan gelen engel bilgisi."""
    track_id: int
    class_label: str
    position_x: float        # base_link
    position_y: float        # base_link
    distance: float          # front_bumper mesafe
    ttc: float               # saniye
    is_static: bool
    velocity: float = 0.0


@dataclass
class ObstacleDecisionResult:
    """Engel karar çıktısı."""
    action: str              # CONTINUE | SLOW | STOP_APPROACH | EMERGENCY
    speed_factor: float      # 0.0–1.0
    in_path: bool
    critical_track: Optional[ObstacleTrack]
    warning_flags: List[str]


class ObstacleDecision:
    """
    Engel karar modülü.

    Not:
      decide() fonksiyonuna verilen trajectory noktaları base_link frame'de olmalıdır.
      /planning/trajectory map frame ise, planner önce base_link'e çevirmelidir.
    """

    def __init__(self):
        self._loc_status = LOC_OK

    def decide(
        self,
        tracks: List[ObstacleTrack],
        trajectory: List[Any],
        ego_speed: float,
        loc_status: int = LOC_OK,
    ) -> ObstacleDecisionResult:
        """Mesafe + TTC tabanlı engel kararı üretir."""
        self._loc_status = int(loc_status)

        if loc_status == LOC_LOST:
            return ObstacleDecisionResult(
                action='EMERGENCY',
                speed_factor=0.0,
                in_path=True,
                critical_track=None,
                warning_flags=['LOCALIZATION_LOST_OBSTACLE_DECISION_BLOCKED'],
            )

        if not tracks:
            return ObstacleDecisionResult(
                action='CONTINUE',
                speed_factor=1.0,
                in_path=False,
                critical_track=None,
                warning_flags=[],
            )

        ego_speed = max(0.0, float(ego_speed))

        warnings: List[str] = []
        worst_action = 'CONTINUE'
        worst_factor = 1.0
        critical_track: Optional[ObstacleTrack] = None
        any_in_path = False

        for track in tracks:
            if not self._is_valid_track(track):
                warnings.append(f'INVALID_TRACK:{getattr(track, "track_id", -1)}')
                continue

            in_path = self._check_in_path(track, trajectory)

            if not in_path:
                continue

            any_in_path = True

            is_pedestrian = track.class_label.lower() in (
                'pedestrian',
                'person',
                'yaya',
            )

            mult = PEDESTRIAN_MULT if is_pedestrian else 1.0

            ttc_watch = TTC_WATCH * mult
            ttc_slow = TTC_SLOW * mult
            ttc_stop = TTC_STOP * mult

            ttc = self._safe_ttc(track)
            emergency_dist = self._emergency_distance(ego_speed)

            if track.distance < emergency_dist or ttc <= ttc_stop:
                action = 'EMERGENCY'
                factor = 0.0
                warnings.append(
                    f'EMERGENCY:track_{track.track_id}:'
                    f'ttc={ttc:.2f}:dist={track.distance:.2f}'
                )

            elif ttc <= ttc_slow:
                action = 'STOP_APPROACH'
                factor = 0.0
                warnings.append(
                    f'STOP_APPROACH:track_{track.track_id}:ttc={ttc:.2f}'
                )

            elif ttc <= ttc_watch:
                action = 'SLOW'
                factor = max(0.3, min(1.0, ttc / ttc_watch))
                warnings.append(
                    f'SLOW:track_{track.track_id}:ttc={ttc:.2f}'
                )

            else:
                action = 'CONTINUE'
                factor = 1.0

            if self._is_worse(action, factor, worst_action, worst_factor):
                worst_action = action
                worst_factor = factor
                critical_track = track

        return ObstacleDecisionResult(
            action=worst_action,
            speed_factor=worst_factor,
            in_path=any_in_path,
            critical_track=critical_track,
            warning_flags=warnings,
        )

    def sample_trajectories(
        self,
        tracks: List[ObstacleTrack],
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        ego_speed: float,
        target_speed: float,
        loc_status: int = LOC_OK,
    ) -> Optional[List[Tuple[float, float, float]]]:
        """
        Basit trajectory sampling.

        Çıktı: [(x, y, yaw), ...]
        Bu fonksiyondaki x/y, verilen ego_x/ego_y frame'ine bağlıdır.
        Genelde local/base_link kullanım için ego_x=0, ego_y=0, ego_yaw=0 verilebilir.
        """
        if loc_status == LOC_LOST:
            return None

        k = K_SAMPLES // 2 if loc_status == LOC_DEGRADED else K_SAMPLES
        sim_time = SIM_TIME / 2.0 if loc_status == LOC_DEGRADED else SIM_TIME

        speed = max(0.0, min(float(target_speed), float(ego_speed), V_MAX))

        best_trajectory = None
        best_cost = float('inf')

        steer_samples = self._linspace(
            -math.radians(MAX_STEER_DEG),
            math.radians(MAX_STEER_DEG),
            k,
        )

        for steer in steer_samples:
            traj = self._simulate(
                x=float(ego_x),
                y=float(ego_y),
                yaw=float(ego_yaw),
                speed=speed,
                steer=steer,
                sim_time=sim_time,
            )

            cost = self._compute_cost(
                trajectory=traj,
                steer=steer,
                target_yaw=float(ego_yaw),
                tracks=tracks,
            )

            if cost < best_cost:
                best_cost = cost
                best_trajectory = traj

        return best_trajectory

    def _check_in_path(
        self,
        track: ObstacleTrack,
        trajectory: List[Any],
    ) -> bool:
        """
        Engel planlanan yol üzerinde mi?

        trajectory base_link frame'de olmalıdır.
        Eğer boşsa basit ön bölge kontrolü yapılır.
        """
        if not trajectory:
            return (
                track.position_x > 0.0
                and track.distance < 10.0
                and abs(track.position_y) < 1.5
            )

        lateral_threshold = 1.5

        for pt in trajectory:
            px, py = self._extract_xy(pt)

            dx = track.position_x - px
            dy = track.position_y - py

            if math.hypot(dx, dy) < lateral_threshold:
                return True

        return False

    @staticmethod
    def _extract_xy(point: Any) -> Tuple[float, float]:
        """Tuple/list veya msg point tipinden x/y çeker."""
        if hasattr(point, 'x') and hasattr(point, 'y'):
            return float(point.x), float(point.y)

        if isinstance(point, (tuple, list)) and len(point) >= 2:
            return float(point[0]), float(point[1])

        raise TypeError('Trajectory point x/y alanı içermiyor.')

    @staticmethod
    def _is_valid_track(track: ObstacleTrack) -> bool:
        values = [
            track.position_x,
            track.position_y,
            track.distance,
        ]

        return all(math.isfinite(float(v)) for v in values)

    @staticmethod
    def _safe_ttc(track: ObstacleTrack) -> float:
        """Geçersiz TTC gelirse distance üzerinden güvenli yorum yapar."""
        ttc = float(track.ttc)

        if math.isfinite(ttc) and ttc >= 0.0:
            return ttc

        if track.distance <= 0.0:
            return 0.0

        return float('inf')

    @staticmethod
    def _emergency_distance(speed: float) -> float:
        return max(0.3, float(speed) * REACTION_TIME + BRAKING_MARGIN)

    def _simulate(
        self,
        x: float,
        y: float,
        yaw: float,
        speed: float,
        steer: float,
        sim_time: float,
    ) -> List[Tuple[float, float, float]]:
        """Bisiklet modeli ile kısa ufuk simülasyon."""
        trajectory = [(x, y, self._normalize_angle(yaw))]
        steps = max(1, int(sim_time / SIM_DT))

        for _ in range(steps):
            yaw = self._normalize_angle(yaw)

            x += speed * math.cos(yaw) * SIM_DT
            y += speed * math.sin(yaw) * SIM_DT
            yaw += (speed / WHEELBASE) * math.tan(steer) * SIM_DT
            yaw = self._normalize_angle(yaw)

            trajectory.append((x, y, yaw))

        return trajectory

    def _compute_cost(
        self,
        trajectory: List[Tuple[float, float, float]],
        steer: float,
        target_yaw: float,
        tracks: List[ObstacleTrack],
    ) -> float:
        """Maliyet fonksiyonu."""
        if not trajectory:
            return float('inf')

        path_cost = abs(float(steer))

        final_yaw = trajectory[-1][2]
        heading_cost = abs(self._normalize_angle(final_yaw - target_yaw))

        obstacle_cost = 0.0

        for px, py, _ in trajectory:
            for track in tracks:
                if not self._is_valid_track(track):
                    continue

                dist = math.hypot(
                    px - track.position_x,
                    py - track.position_y,
                )

                if dist < 0.5:
                    obstacle_cost += COLLISION_COST
                elif dist < 2.0:
                    obstacle_cost += 1.0 / (dist + 0.1)

        return (
            W_PATH * path_cost
            + W_OBS * obstacle_cost
            + W_HEAD * heading_cost
        )

    @staticmethod
    def _action_severity(action: str) -> int:
        severity = {
            'CONTINUE': 0,
            'SLOW': 1,
            'STOP_APPROACH': 2,
            'EMERGENCY': 3,
        }
        return severity.get(action, 0)

    def _is_worse(
        self,
        action: str,
        factor: float,
        worst_action: str,
        worst_factor: float,
    ) -> bool:
        action_severity = self._action_severity(action)
        worst_severity = self._action_severity(worst_action)

        if action_severity > worst_severity:
            return True

        if action_severity == worst_severity and factor < worst_factor:
            return True

        return False

    @staticmethod
    def _linspace(start: float, stop: float, n: int) -> List[float]:
        if n <= 1:
            return [float(start)]

        step = (stop - start) / float(n - 1)
        return [float(start) + i * step for i in range(n)]

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle
