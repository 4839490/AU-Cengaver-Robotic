#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
parking_planner.py

Algoritma 13: Dubins Path Tabanlı Park Hedefleme
Algoritma 14: Park Son Hizalama
"""

import math
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


R_MIN = 4.1
PARK_SPEED = 0.83
PARK_JERK = 1.0

HEADING_COV_THRESHOLD = 0.05

FRONT_CLEARANCE = 0.20
SIDE_CLEARANCE = 0.10
HEADING_TOL = math.radians(5.0)
MAX_ITERATIONS = 3

DUBINS_TYPES = ['RSR', 'RSL', 'LSR', 'LSL', 'RLR', 'LRL']
POINT_INTERVAL = 0.1


@dataclass
class TrajectoryPoint:
    x: float
    y: float
    yaw: float
    speed: float
    curvature: float
    distance_from_start: float


@dataclass
class ParkSlot:
    slot_x: float
    slot_y: float
    slot_heading: float
    slot_available: bool


@dataclass
class DubinsPath:
    path_type: str
    length: float
    points: List[Tuple[float, float, float]]


@dataclass
class ParkingResult:
    success: bool
    trajectory: List[TrajectoryPoint]
    iterations_used: int
    final_cross_track: float
    final_heading_error: float
    warning_flags: List[str] = field(default_factory=list)


class ParkingPlanner:
    def __init__(self):
        self._iteration_count = 0

    def plan_dubins(
        self,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        slot: ParkSlot,
        heading_covariance: float,
    ) -> Optional[List[TrajectoryPoint]]:

        if heading_covariance >= HEADING_COV_THRESHOLD:
            return None

        if not slot.slot_available:
            return None

        if not self._finite_all(
            ego_x, ego_y, ego_yaw,
            slot.slot_x, slot.slot_y, slot.slot_heading,
            heading_covariance
        ):
            return None

        best_path = self._compute_best_dubins(
            ego_x,
            ego_y,
            ego_yaw,
            slot.slot_x,
            slot.slot_y,
            slot.slot_heading,
        )

        if best_path is None:
            return None

        return self._path_to_trajectory(best_path)

    def align(
        self,
        cross_track_error: float,
        heading_error: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        slot: ParkSlot,
        front_dist: float = 0.5,
        right_dist: float = 0.5,
        left_dist: float = 0.5,
    ) -> ParkingResult:

        warnings: List[str] = []

        if not slot.slot_available:
            return ParkingResult(
                success=False,
                trajectory=[],
                iterations_used=self._iteration_count,
                final_cross_track=cross_track_error,
                final_heading_error=heading_error,
                warning_flags=['PARK_SLOT_NOT_AVAILABLE'],
            )

        conditions_met = self._check_park_conditions(
            cross_track_error,
            heading_error,
            front_dist,
            right_dist,
            left_dist,
        )

        if conditions_met:
            return ParkingResult(
                success=True,
                trajectory=[],
                iterations_used=self._iteration_count,
                final_cross_track=cross_track_error,
                final_heading_error=heading_error,
                warning_flags=[],
            )

        if self._iteration_count >= MAX_ITERATIONS:
            warnings.append('MAX_ITERATIONS_REACHED')
            return ParkingResult(
                success=False,
                trajectory=[],
                iterations_used=self._iteration_count,
                final_cross_track=cross_track_error,
                final_heading_error=heading_error,
                warning_flags=warnings,
            )

        self._iteration_count += 1

        correction = self._compute_correction(
            cross_track_error,
            heading_error,
            ego_x,
            ego_y,
            ego_yaw,
        )

        return ParkingResult(
            success=False,
            trajectory=correction,
            iterations_used=self._iteration_count,
            final_cross_track=cross_track_error,
            final_heading_error=heading_error,
            warning_flags=warnings,
        )

    def reset_iterations(self) -> None:
        self._iteration_count = 0

    def _compute_best_dubins(
        self,
        sx: float,
        sy: float,
        syaw: float,
        gx: float,
        gy: float,
        gyaw: float,
    ) -> Optional[DubinsPath]:

        best_path = None
        best_length = float('inf')

        for path_type in DUBINS_TYPES:
            path = self._compute_dubins_type(
                sx, sy, syaw,
                gx, gy, gyaw,
                path_type,
            )

            if path is not None and path.length < best_length:
                best_length = path.length
                best_path = path

        return best_path

    def _compute_dubins_type(
        self,
        sx: float,
        sy: float,
        syaw: float,
        gx: float,
        gy: float,
        gyaw: float,
        path_type: str,
    ) -> Optional[DubinsPath]:

        r = R_MIN

        dx = gx - sx
        dy = gy - sy
        d = math.hypot(dx, dy)

        if d < 1e-6:
            return None

        if path_type in ('RSR', 'LSL'):
            sign = -1.0 if path_type == 'RSR' else 1.0

            cx_s = sx + sign * r * math.cos(syaw - math.pi / 2.0)
            cy_s = sy + sign * r * math.sin(syaw - math.pi / 2.0)
            cx_g = gx + sign * r * math.cos(gyaw - math.pi / 2.0)
            cy_g = gy + sign * r * math.sin(gyaw - math.pi / 2.0)

            dist_cc = math.hypot(cx_g - cx_s, cy_g - cy_s)

            if dist_cc < 1e-6:
                return None

            center_angle = math.atan2(cy_g - cy_s, cx_g - cx_s)

            arc1 = abs(self._normalize_angle(center_angle - syaw)) * r
            straight = dist_cc
            arc2 = abs(self._normalize_angle(gyaw - center_angle)) * r

            length = arc1 + straight + arc2

        elif path_type in ('RSL', 'LSR'):
            sign1 = -1.0 if path_type[0] == 'R' else 1.0
            sign2 = 1.0 if path_type[2] == 'L' else -1.0

            cx_s = sx + sign1 * r * math.cos(syaw - math.pi / 2.0)
            cy_s = sy + sign1 * r * math.sin(syaw - math.pi / 2.0)
            cx_g = gx + sign2 * r * math.cos(gyaw - math.pi / 2.0)
            cy_g = gy + sign2 * r * math.sin(gyaw - math.pi / 2.0)

            dist_cc = math.hypot(cx_g - cx_s, cy_g - cy_s)

            if dist_cc < 2.0 * r:
                return None

            center_angle = math.atan2(cy_g - cy_s, cx_g - cx_s)

            straight = math.sqrt(max(0.0, dist_cc ** 2 - (2.0 * r) ** 2))
            arc1 = abs(self._normalize_angle(center_angle - syaw)) * r
            arc2 = abs(self._normalize_angle(gyaw - center_angle)) * r

            length = arc1 + straight + arc2

        else:
            if d > 4.0 * r:
                return None

            cos_val = (d ** 2 / (8.0 * r ** 2)) - 0.5
            cos_val = max(-1.0, min(1.0, cos_val))

            arc_mid = r * math.acos(cos_val)
            length = arc_mid * 2.0

        points = self._generate_path_points(
            sx, sy, syaw,
            gx, gy, gyaw,
            length,
        )

        return DubinsPath(
            path_type=path_type,
            length=length,
            points=points,
        )

    def _generate_path_points(
        self,
        sx: float,
        sy: float,
        syaw: float,
        gx: float,
        gy: float,
        gyaw: float,
        total_length: float,
    ) -> List[Tuple[float, float, float]]:

        n = max(10, int(total_length / POINT_INTERVAL))
        points: List[Tuple[float, float, float]] = []

        yaw_delta = self._normalize_angle(gyaw - syaw)

        for i in range(n + 1):
            t = i / float(n)

            x = sx + t * (gx - sx)
            y = sy + t * (gy - sy)
            yaw = self._normalize_angle(syaw + t * yaw_delta)

            points.append((x, y, yaw))

        return points

    def _path_to_trajectory(
        self,
        path: DubinsPath,
    ) -> List[TrajectoryPoint]:

        trajectory: List[TrajectoryPoint] = []
        cum_distance = 0.0

        for i, (x, y, yaw) in enumerate(path.points):
            if i > 0:
                px, py, _ = path.points[i - 1]
                cum_distance += math.hypot(x - px, y - py)

            trajectory.append(
                TrajectoryPoint(
                    x=x,
                    y=y,
                    yaw=yaw,
                    speed=PARK_SPEED,
                    curvature=1.0 / R_MIN,
                    distance_from_start=cum_distance,
                )
            )

        return trajectory

    def _check_park_conditions(
        self,
        cross_track: float,
        heading_err: float,
        front_dist: float,
        right_dist: float,
        left_dist: float,
    ) -> bool:

        return (
            abs(cross_track) < 0.3
            and abs(heading_err) < HEADING_TOL
            and front_dist > FRONT_CLEARANCE
            and right_dist > SIDE_CLEARANCE
            and left_dist > SIDE_CLEARANCE
        )

    def _compute_correction(
        self,
        cross_track: float,
        heading_err: float,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
    ) -> List[TrajectoryPoint]:

        trajectory: List[TrajectoryPoint] = []

        correction_dist = min(0.5, abs(cross_track) * 2.0 + 0.2)

        if abs(heading_err) > HEADING_TOL:
            correction_dist = min(0.5, correction_dist + 0.1)

        n_points = max(5, int(correction_dist / POINT_INTERVAL))

        direction = 1.0
        if abs(cross_track) < 0.05 and abs(heading_err) > HEADING_TOL:
            direction = -1.0

        for i in range(n_points + 1):
            t = i / float(n_points)
            dist = direction * t * correction_dist

            x = ego_x + dist * math.cos(ego_yaw)
            y = ego_y + dist * math.sin(ego_yaw)

            trajectory.append(
                TrajectoryPoint(
                    x=x,
                    y=y,
                    yaw=self._normalize_angle(ego_yaw),
                    speed=PARK_SPEED,
                    curvature=0.0,
                    distance_from_start=abs(dist),
                )
            )

        return trajectory

    @staticmethod
    def _finite_all(*values: float) -> bool:
        return all(math.isfinite(float(v)) for v in values)

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        while angle > math.pi:
            angle -= 2.0 * math.pi

        while angle < -math.pi:
            angle += 2.0 * math.pi

        return angle
