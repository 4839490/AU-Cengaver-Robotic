#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
route_context_publisher.py

/planning/active_route_context için veri üretir.
Tüm koordinatlar base_link frame'indedir.
"""

import math
from typing import Any, List, Optional

from .coordinate_transform import CoordinateTransform


VALID_ROUTE_DIRECTIONS = {
    'STRAIGHT',
    'LEFT',
    'RIGHT',
    'ROUNDABOUT',
    'UNKNOWN',
}


class RouteContextPublisher:
    """
    ActiveRouteContext mesajı için dict üretir.

    Planner node bu dict'i planning_msgs/ActiveRouteContext mesajına çevirir.
    """

    def __init__(self, coord_transform: CoordinateTransform):
        self._ct = coord_transform

    def build(
        self,
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
        ego_speed: float,
        waypoint_manager: Any,
        trajectory: Optional[List[Any]],
        planner_mode: int,
        in_stop_zone: bool,
        localization_confidence: float,
        route_context_valid: bool,
        lookahead_distance: float = 1.5,
        distance_to_stop_zone: float = -1.0,
        route_direction: str = 'UNKNOWN',
    ) -> dict:
        """
        ActiveRouteContext alanlarına uygun dict üretir.
        """

        warning_flags: List[str] = []

        ego_yaw = self._normalize_angle(float(ego_yaw))

        active_wp = getattr(waypoint_manager, 'active_waypoint', None)
        next_wp = getattr(waypoint_manager, 'next_waypoint', None)

        if active_wp is None:
            warning_flags.append('NO_ACTIVE_WAYPOINT')

        if not route_context_valid:
            warning_flags.append('ROUTE_CONTEXT_INVALID')

        if localization_confidence < 0.5:
            warning_flags.append('LOW_LOCALIZATION_CONFIDENCE')

        active_waypoint_id = int(getattr(active_wp, 'id', 0)) if active_wp else 0

        target_x_bl = 0.0
        target_y_bl = 0.0
        target_heading = 0.0

        if active_wp is not None:
            try:
                target_x_bl, target_y_bl = self._ct.map_to_base_link(
                    target_x_map=float(active_wp.x),
                    target_y_map=float(active_wp.y),
                    ego_x=float(ego_x),
                    ego_y=float(ego_y),
                    ego_yaw=ego_yaw,
                )

                target_heading = self._normalize_angle(
                    float(getattr(active_wp, 'yaw', ego_yaw)) - ego_yaw
                )

            except Exception:
                target_x_bl = 0.0
                target_y_bl = 0.0
                target_heading = 0.0
                route_context_valid = False
                warning_flags.append('TARGET_TRANSFORM_FAILED')

        planned_trajectory_bl = self._trajectory_to_base_link(
            trajectory=trajectory,
            ego_x=float(ego_x),
            ego_y=float(ego_y),
            ego_yaw=ego_yaw,
        )

        route_direction = str(route_direction).upper()

        if route_direction not in VALID_ROUTE_DIRECTIONS:
            route_direction = 'UNKNOWN'
            warning_flags.append('INVALID_ROUTE_DIRECTION')

        if route_direction == 'UNKNOWN' and active_wp is not None and next_wp is not None:
            route_direction = self._compute_route_direction(
                current_yaw=float(getattr(active_wp, 'yaw', 0.0)),
                next_yaw=float(getattr(next_wp, 'yaw', 0.0)),
            )

        distance_to_stop_zone = self._safe_float32_value(
            distance_to_stop_zone,
            fallback=-1.0,
        )

        return {
            'frame_id': 'base_link',

            'active_waypoint_id': active_waypoint_id,

            'target_x': float(target_x_bl),
            'target_y': float(target_y_bl),
            'target_heading': float(target_heading),

            'planner_mode': int(planner_mode),
            'route_direction': route_direction,

            'planned_trajectory': planned_trajectory_bl,

            'lookahead_distance': max(0.0, float(lookahead_distance)),

            'in_stop_zone': bool(in_stop_zone),
            'distance_to_stop_zone': float(distance_to_stop_zone),

            'localization_confidence': max(
                0.0,
                min(1.0, float(localization_confidence)),
            ),

            'ego_speed_mps': max(0.0, float(ego_speed)),

            'route_context_valid': bool(route_context_valid),

            'age_ms': 0,
            'valid_until_ms': 500,
            'warning_flags': warning_flags,
        }

    def _trajectory_to_base_link(
        self,
        trajectory: Optional[List[Any]],
        ego_x: float,
        ego_y: float,
        ego_yaw: float,
    ) -> List[dict]:
        """
        map frame trajectory noktalarını base_link frame'e çevirir.
        """
        if not trajectory:
            return []

        points: List[dict] = []

        for pt in trajectory[:20]:
            try:
                px = float(getattr(pt, 'x'))
                py = float(getattr(pt, 'y'))

                x_bl, y_bl = self._ct.map_to_base_link(
                    target_x_map=px,
                    target_y_map=py,
                    ego_x=ego_x,
                    ego_y=ego_y,
                    ego_yaw=ego_yaw,
                )

                points.append({
                    'x': float(x_bl),
                    'y': float(y_bl),
                    'z': 0.0,
                })

            except Exception:
                continue

        return points

    def _compute_route_direction(
        self,
        current_yaw: float,
        next_yaw: float,
    ) -> str:
        """
        STRAIGHT | LEFT | RIGHT döndürür.
        """
        diff = self._normalize_angle(float(next_yaw) - float(current_yaw))

        if abs(diff) < math.radians(20.0):
            return 'STRAIGHT'

        if diff > 0.0:
            return 'LEFT'

        return 'RIGHT'

    @staticmethod
    def _safe_float32_value(value: float, fallback: float = -1.0) -> float:
        """
        ROS float32 alanlarına inf/nan basmayı engeller.
        """
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
