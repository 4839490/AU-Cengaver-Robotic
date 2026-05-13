#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
route_context_publisher.py

Görev:
  /planning/active_route_context yayınlar — 10-20Hz — base_link frame

Sözleşme: Planner ↔ Controller Contract v1.3 FIX-4
  - frame_id: base_link — TÜM KOORDINATLAR BASE_LINK
  - map→base_link dönüşümü planner içinde yapılır
  - ego_speed_mps: controller/feedback.actual_speed'den beslenir
  - route_context_valid: lokalizasyon + waypoint + planner ACTIVE → true

Perception ↔ Planner Contract v1.4 FIX-2:
  - age_ms > 200ms → relevant_to_route=false
  - route_context_valid=false → perception agresif karar üretmez

4 contractta BİREBİR AYNI şema — değiştirilmemeli!
"""

import math
from typing import List, Optional, Tuple

from .coordinate_transform import CoordinateTransform
from .waypoint_manager import WaypointManager
from .trajectory_builder import TrajectoryPoint


class RouteContextPublisher:
    """
    /planning/active_route_context mesajı için veri üretir.

    Kullanım:
        rcp = RouteContextPublisher(coord_transform)
        ctx = rcp.build(
            ego_x=1.0, ego_y=2.0, ego_yaw=0.5,
            ego_speed=3.0,
            waypoint_manager=wm,
            trajectory=traj,
            planner_mode=0,
            in_stop_zone=False,
            localization_confidence=0.9,
            route_context_valid=True
        )
    """

    def __init__(self, coord_transform: CoordinateTransform):
        self._ct = coord_transform

    # ───────────────────────────────────────────────────────────────────────
    # PUBLIC API
    # ───────────────────────────────────────────────────────────────────────

    def build(
        self,
        ego_x:                   float,
        ego_y:                   float,
        ego_yaw:                 float,
        ego_speed:               float,
        waypoint_manager:        WaypointManager,
        trajectory:              Optional[List[TrajectoryPoint]],
        planner_mode:            int,
        in_stop_zone:            bool,
        localization_confidence: float,
        route_context_valid:     bool,
        lookahead_distance:      float = 1.5,
        distance_to_stop_zone:   float = float('inf'),
        route_direction:         str   = 'STRAIGHT',
    ) -> dict:
        """
        ActiveRouteContext verisi üret.

        Returns:
            dict — planning_msgs/ActiveRouteContext alanları
        """
        # Aktif waypoint
        active_wp = waypoint_manager.active_waypoint
        next_wp   = waypoint_manager.next_waypoint

        active_waypoint_id = active_wp.id if active_wp else 0

        # Hedef noktayı map → base_link'e çevir
        target_x_bl = 0.0
        target_y_bl = 0.0
        target_heading = ego_yaw

        if active_wp is not None:
            target_x_bl, target_y_bl = self._ct.map_to_base_link(
                active_wp.x, active_wp.y,
                ego_x, ego_y, ego_yaw
            )
            target_heading = self._normalize_angle(
                active_wp.yaw - ego_yaw
            )

        # Trajectory → base_link frame noktaları
        planned_trajectory_bl = self._trajectory_to_base_link(
            trajectory, ego_x, ego_y, ego_yaw
        )

        # route_direction — next waypoint'e göre
        if route_direction == 'STRAIGHT' and next_wp is not None \
                and active_wp is not None:
            route_direction = self._compute_route_direction(
                active_wp.yaw, next_wp.yaw
            )

        return {
            # Header
            'frame_id':              'base_link',
            'active_waypoint_id':    active_waypoint_id,

            # Hedef — base_link frame
            'target_x':              target_x_bl,
            'target_y':              target_y_bl,
            'target_heading':        target_heading,

            # Mod ve durum
            'planner_mode':          planner_mode,
            'route_direction':       route_direction,

            # Trajectory — base_link frame
            'planned_trajectory':    planned_trajectory_bl,

            # Lookahead
            'lookahead_distance':    lookahead_distance,

            # Stop zone
            'in_stop_zone':          in_stop_zone,
            'distance_to_stop_zone': distance_to_stop_zone,

            # Lokalizasyon
            'localization_confidence': localization_confidence,

            # ego_speed — controller/feedback'ten gelir
            # TTC hesabında perception bu alanı kullanır
            'ego_speed_mps':         ego_speed,

            # Geçerlilik
            'route_context_valid':   route_context_valid,

            # Zaman
            'age_ms':                0,
            'valid_until_ms':        500,
        }

    # ───────────────────────────────────────────────────────────────────────
    # PRIVATE
    # ───────────────────────────────────────────────────────────────────────

    def _trajectory_to_base_link(
        self,
        trajectory: Optional[List[TrajectoryPoint]],
        ego_x:      float,
        ego_y:      float,
        ego_yaw:    float,
    ) -> List[dict]:
        """
        Trajectory noktalarını map frame'den base_link frame'e çevir.
        geometry_msgs/Point[] formatında döndür.
        """
        if not trajectory:
            return []

        points = []
        for pt in trajectory[:20]:   # max 20 nokta
            x_bl, y_bl = self._ct.map_to_base_link(
                pt.x, pt.y, ego_x, ego_y, ego_yaw
            )
            points.append({
                'x': x_bl,
                'y': y_bl,
                'z': 0.0
            })

        return points

    def _compute_route_direction(
        self,
        current_yaw: float,
        next_yaw:    float,
    ) -> str:
        """
        Rota yönünü belirle.
        STRAIGHT | LEFT | RIGHT | ROUNDABOUT | UNKNOWN
        """
        diff = self._normalize_angle(next_yaw - current_yaw)

        if abs(diff) < math.radians(20):
            return 'STRAIGHT'
        elif diff > 0:
            return 'LEFT'
        else:
            return 'RIGHT'

    @staticmethod
    def _normalize_angle(angle: float) -> float:
        """Açıyı [-π, π] aralığına normalize et."""
        while angle >  math.pi: angle -= 2.0 * math.pi
        while angle < -math.pi: angle += 2.0 * math.pi
        return angle