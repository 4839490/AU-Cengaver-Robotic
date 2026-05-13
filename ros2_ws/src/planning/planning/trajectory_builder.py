#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
trajectory_builder.py

Algoritma 6: Şerit Geometrisi Tabanlı Adaptif Lookahead + Lokal Yörünge
"""

import math
from typing import List, Optional, Tuple
from dataclasses import dataclass


LOOKAHEAD_MIN = 0.8
LOOKAHEAD_MAX = 2.5
LOOKAHEAD_MAX_DEGRADED = 1.5

POINT_INTERVAL = 0.1
MIN_POINTS = 10
MIN_HORIZON = 3.0

CURVATURE_STRAIGHT = 0.05
CURVATURE_MEDIUM = 0.20

LOC_STATUS_OK = 0
LOC_STATUS_DEGRADED = 4
LOC_STATUS_LOST = 6


@dataclass
class TrajectoryPoint:
    """Tek bir trajectory noktası — map frame."""
    x: float
    y: float
    yaw: float
    speed: float
    curvature: float
    distance_from_start: float


class TrajectoryBuilder:
    """
    Şerit centerline veya waypoint üzerinden map frame trajectory üretir.

    Not:
      /planning/trajectory contract'a göre map frame'de yayınlanmalıdır.
      Eğer centerline perception'dan geliyorsa genelde base_link frame'dedir.
      Bu yüzden build() içinde centerline_frame='base_link' verilirse map'e çevrilir.
    """

    def __init__(self):
        self._last_trajectory: List[TrajectoryPoint] = []

    def build(
        self,
        centerline: List[Tuple[float, float]],
        curvature: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        ego_speed: float,
        target_speed: float,
        loc_status: int = LOC_STATUS_OK,
        centerline_frame: str = 'base_link',
    ) -> Optional[List[TrajectoryPoint]]:

        if loc_status == LOC_STATUS_LOST:
            self._last_trajectory = []
            return None

        if not centerline or len(centerline) < 2:
            return self._last_trajectory if self._last_trajectory else None

        centerline = self._sanitize_points(centerline)

        if len(centerline) < 2:
            return self._last_trajectory if self._last_trajectory else None

        if centerline_frame == 'base_link':
            centerline_map = [
                self._base_link_to_map(
                    x_bl=x,
                    y_bl=y,
                    ego_x=ego_x,
                    ego_y=ego_y,
                    ego_yaw=ego_yaw,
                )
                for x, y in centerline
            ]

        elif centerline_frame == 'map':
            centerline_map = centerline

        else:
            return self._last_trajectory if self._last_trajectory else None

        lookahead = self._compute_lookahead(
            curvature=curvature,
            ego_speed=ego_speed,
            loc_status=loc_status,
        )

        selected = self._select_points(
            centerline=centerline_map,
            lookahead=max(lookahead, MIN_HORIZON),
        )

        if len(selected) < 2:
            return self._last_trajectory if self._last_trajectory else None

        interpolated = self._interpolate(selected)

        if len(interpolated) < MIN_POINTS:
            return self._last_trajectory if self._last_trajectory else None

        trajectory = self._assign_attributes(
            points=interpolated,
            target_speed=target_speed,
            curvature=curvature,
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

        if loc_status == LOC_STATUS_LOST:
            self._last_trajectory = []
            return None

        dx = float(wp_x) - float(ego_x)
        dy = float(wp_y) - float(ego_y)
        dist = math.hypot(dx, dy)

        if dist < 0.1:
            return None

        angle = math.atan2(dy, dx)
        n_points = max(MIN_POINTS, int(dist / POINT_INTERVAL) + 1)

        points: List[TrajectoryPoint] = []

        for i in range(n_points):
            t = i / float(n_points - 1)

            x = float(ego_x) + t * dx
            y = float(ego_y) + t * dy
            d = t * dist

            points.append(
                TrajectoryPoint(
                    x=x,
                    y=y,
                    yaw=angle,
                    speed=max(0.0, float(target_speed)),
                    curvature=0.0,
                    distance_from_start=d,
                )
            )

        self._last_trajectory = points
        return points

    @property
    def last_trajectory(self) -> List[TrajectoryPoint]:
        return self._last_trajectory

    def _compute_lookahead(
        self,
        curvature: float,
        ego_speed: float,
        loc_status: int,
    ) -> float:

        curvature = self._safe_float(curvature, 0.0)
        ego_speed = max(0.0, self._safe_float(ego_speed, 0.0))

        abs_curv = abs(curvature)

        if abs_curv < CURVATURE_STRAIGHT:
            lookahead = LOOKAHEAD_MAX

        elif abs_curv < CURVATURE_MEDIUM:
            t = (
                (abs_curv - CURVATURE_STRAIGHT)
                / (CURVATURE_MEDIUM - CURVATURE_STRAIGHT)
            )

            lookahead = LOOKAHEAD_MAX - t * (LOOKAHEAD_MAX - LOOKAHEAD_MIN)

        else:
            lookahead = LOOKAHEAD_MIN

        speed_factor = ego_speed * 0.3
        lookahead = max(lookahead, LOOKAHEAD_MIN + speed_factor)

        if loc_status == LOC_STATUS_DEGRADED:
            lookahead = min(lookahead, LOOKAHEAD_MAX_DEGRADED)

        return max(LOOKAHEAD_MIN, lookahead)

    def _select_points(
        self,
        centerline: List[Tuple[float, float]],
        lookahead: float,
    ) -> List[Tuple[float, float]]:

        if not centerline:
            return []

        selected = [centerline[0]]
        cumulative = 0.0

        for i in range(1, len(centerline)):
            prev = centerline[i - 1]
            pt = centerline[i]

            dist = math.hypot(
                pt[0] - prev[0],
                pt[1] - prev[1],
            )

            cumulative += dist
            selected.append(pt)

            if cumulative >= lookahead:
                break

        return selected

    def _interpolate(
        self,
        points: List[Tuple[float, float]],
    ) -> List[Tuple[float, float]]:

        if len(points) < 2:
            return points

        cumulative = [0.0]

        for i in range(1, len(points)):
            cumulative.append(
                cumulative[-1]
                + math.hypot(
                    points[i][0] - points[i - 1][0],
                    points[i][1] - points[i - 1][1],
                )
            )

        total_length = cumulative[-1]

        if total_length < POINT_INTERVAL:
            return points

        n_points = max(MIN_POINTS, int(total_length / POINT_INTERVAL) + 1)
        result: List[Tuple[float, float]] = []

        seg_index = 0

        for i in range(n_points):
            target_dist = (
                i * total_length / float(n_points - 1)
            )

            while (
                seg_index < len(points) - 2
                and cumulative[seg_index + 1] < target_dist
            ):
                seg_index += 1

            p0 = points[seg_index]
            p1 = points[seg_index + 1]

            seg_start = cumulative[seg_index]
            seg_end = cumulative[seg_index + 1]
            seg_len = seg_end - seg_start

            if seg_len < 1e-6:
                result.append(p0)
                continue

            t = (target_dist - seg_start) / seg_len
            t = max(0.0, min(1.0, t))

            x = p0[0] + t * (p1[0] - p0[0])
            y = p0[1] + t * (p1[1] - p0[1])

            result.append((x, y))

        return result

    def _assign_attributes(
        self,
        points: List[Tuple[float, float]],
        target_speed: float,
        curvature: float,
    ) -> List[TrajectoryPoint]:

        trajectory: List[TrajectoryPoint] = []
        cum_distance = 0.0

        target_speed = max(0.0, self._safe_float(target_speed, 0.0))
        curvature = self._safe_float(curvature, 0.0)

        for i, pt in enumerate(points):
            if i < len(points) - 1:
                dx = points[i + 1][0] - pt[0]
                dy = points[i + 1][1] - pt[1]
                yaw = math.atan2(dy, dx)

            elif trajectory:
                yaw = trajectory[-1].yaw

            else:
                yaw = 0.0

            if i > 0:
                cum_distance += math.hypot(
                    pt[0] - points[i - 1][0],
                    pt[1] - points[i - 1][1],
                )

            trajectory.append(
                TrajectoryPoint(
                    x=float(pt[0]),
                    y=float(pt[1]),
                    yaw=self._normalize_angle(yaw),
                    speed=target_speed,
                    curvature=curvature,
                    distance_from_start=cum_distance,
                )
            )

        return trajectory

    @staticmethod
    def _base_link_to_map(
        x_bl: float,
        y_bl: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
    ) -> Tuple[float, float]:

        ego_yaw = TrajectoryBuilder._normalize_angle(float(ego_yaw))

        x_map = (
            float(ego_x)
            + float(x_bl) * math.cos(ego_yaw)
            - float(y_bl) * math.sin(ego_yaw)
        )

        y_map = (
            float(ego_y)
            + float(x_bl) * math.sin(ego_yaw)
            + float(y_bl) * math.cos(ego_yaw)
        )

        return x_map, y_map

    @staticmethod
    def _sanitize_points(
        points: List[Tuple[float, float]],
    ) -> List[Tuple[float, float]]:

        result = []

        for p in points:
            try:
                x = float(p[0])
                y = float(p[1])
            except Exception:
                continue

            if not math.isfinite(x) or not math.isfinite(y):
                continue

            if result:
                prev = result[-1]
                if math.hypot(x - prev[0], y - prev[1]) < 1e-4:
                    continue

            result.append((x, y))

        return result

    @staticmethod
    def _safe_float(value, fallback: float = 0.0) -> float:
        try:
            value = float(value)
        except Exception:
            return fallback

        if not math.isfinite(value):
            return fallback

        return value

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle
