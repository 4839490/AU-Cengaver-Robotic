#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
waypoint_manager.py

Algoritma 2: Waypoint Yönetimi
Algoritma 3: Öklid Mesafesi + Heading Toleransı
"""

import math
from typing import List, Optional, Tuple
from dataclasses import dataclass

from .geojson_loader import Waypoint


# planning_msgs/GoalReached.msg ile uyumlu:
# PICKUP=0, DROPOFF=1, WAYPOINT=2, PARK_ENTRY=3
TYPE_PICKUP = 0
TYPE_DROPOFF = 1
TYPE_WAYPOINT = 2
TYPE_PARK_ENTRY = 3


THRESHOLDS = {
    TYPE_PICKUP: {'dist': 0.5, 'heading': math.radians(10.0)},
    TYPE_DROPOFF: {'dist': 0.5, 'heading': math.radians(10.0)},
    TYPE_WAYPOINT: {'dist': 0.5, 'heading': math.radians(20.0)},
    TYPE_PARK_ENTRY: {'dist': 1.0, 'heading': math.radians(15.0)},
}

DEGRADED_MULTIPLIER = 2.0


@dataclass(frozen=True)
class WaypointResult:
    reached: bool
    distance: float
    heading_error: float
    waypoint_id: int
    waypoint_type: int
    mission_complete: bool = False
    distance_error: float = 0.0


class WaypointManager:
    """
    Waypoint listesini yönetir ve aktif waypoint'e ulaşılıp ulaşılmadığını kontrol eder.
    """

    def __init__(self, waypoints: List[Waypoint]):
        self._waypoints = list(waypoints) if waypoints else []
        self._active_index = 0
        self._mission_complete = False
        self._completed_ids: List[int] = []

    def update(
        self,
        x: float,
        y: float,
        yaw: float,
        localization_degraded: bool = False,
        position_covariance: float = 0.0,
    ) -> WaypointResult:

        if self._mission_complete or not self._waypoints:
            return WaypointResult(
                reached=False,
                distance=float('inf'),
                heading_error=float('inf'),
                waypoint_id=0,
                waypoint_type=TYPE_WAYPOINT,
                mission_complete=self._mission_complete,
                distance_error=float('inf'),
            )

        wp = self.active_waypoint

        if wp is None:
            self._mission_complete = True

            return WaypointResult(
                reached=False,
                distance=float('inf'),
                heading_error=float('inf'),
                waypoint_id=0,
                waypoint_type=TYPE_WAYPOINT,
                mission_complete=True,
                distance_error=float('inf'),
            )

        dist, h_err = self._check_goal(
            x=float(x),
            y=float(y),
            yaw=float(yaw),
            wp=wp,
        )

        d_thresh, heading_thresh = self._get_thresholds(
            wp_type=int(wp.type),
            degraded=bool(localization_degraded),
            position_covariance=float(position_covariance),
        )

        reached = dist < d_thresh and abs(h_err) < heading_thresh

        return WaypointResult(
            reached=reached,
            distance=dist,
            heading_error=h_err,
            waypoint_id=int(wp.id),
            waypoint_type=int(wp.type),
            mission_complete=False,
            distance_error=dist,
        )

    def advance(self) -> bool:
        """
        Aktif waypoint'i tamamlar ve sıradakine geçer.

        Returns:
            True: sıradaki waypoint var
            False: görev tamamlandı
        """
        if self._mission_complete:
            return False

        wp = self.active_waypoint

        if wp is not None:
            self._completed_ids.append(int(wp.id))

        self._active_index += 1

        if self._active_index >= len(self._waypoints):
            self._mission_complete = True
            return False

        return True

    def reset(self) -> None:
        self._active_index = 0
        self._mission_complete = False
        self._completed_ids = []

    def reload(self, waypoints: List[Waypoint]) -> None:
        self._waypoints = list(waypoints) if waypoints else []
        self.reset()

    @property
    def active_waypoint(self) -> Optional[Waypoint]:
        if 0 <= self._active_index < len(self._waypoints):
            return self._waypoints[self._active_index]
        return None

    @property
    def next_waypoint(self) -> Optional[Waypoint]:
        idx = self._active_index + 1

        if 0 <= idx < len(self._waypoints):
            return self._waypoints[idx]

        return None

    @property
    def waypoints(self) -> List[Waypoint]:
        return list(self._waypoints)

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

    def _check_goal(
        self,
        x: float,
        y: float,
        yaw: float,
        wp: Waypoint,
    ) -> Tuple[float, float]:

        dist = math.hypot(
            float(x) - float(wp.x),
            float(y) - float(wp.y),
        )

        h_err = self._normalize_angle(float(yaw) - float(wp.yaw))

        return dist, h_err

    def _get_thresholds(
        self,
        wp_type: int,
        degraded: bool,
        position_covariance: float,
    ) -> Tuple[float, float]:

        thresh = THRESHOLDS.get(int(wp_type), THRESHOLDS[TYPE_WAYPOINT])

        d_thresh = float(thresh['dist'])
        heading_thresh = float(thresh['heading'])

        if degraded:
            d_thresh *= DEGRADED_MULTIPLIER
            heading_thresh *= DEGRADED_MULTIPLIER

        if math.isfinite(position_covariance) and position_covariance > 1.0:
            scale = min(2.0, 1.0 + float(position_covariance))
            d_thresh *= scale
            heading_thresh *= scale

        return d_thresh, heading_thresh

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        return math.atan2(math.sin(angle), math.cos(angle))
