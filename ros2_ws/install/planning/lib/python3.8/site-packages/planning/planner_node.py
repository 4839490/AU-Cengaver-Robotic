#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
planner_node.py

Ana Planner Koordinatörü
"""

import os
import math

import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile,
    ReliabilityPolicy,
    DurabilityPolicy,
    HistoryPolicy,
)

from geometry_msgs.msg import Point

from planning_msgs.msg import (
    Trajectory,
    TrajectoryPoint as TrajPointMsg,
    TargetSpeed,
    PlanningStatus,
    ActiveRouteContext,
    GoalReached,
    ParkComplete,
    ControllerFeedback,
    FSMRequest,
)

from localization_msgs.msg import (
    LocalizationPose,
    LocalizationOdometry,
    LocalizationStatus,
    MapOrigin,
)

from perception_msgs.msg import (
    LaneModel,
    TrafficLightState,
    ObstacleTracks,
    StopTarget,
)

from fsm_msgs.msg import CurrentMode, MissionState, FSMEvent

from .timeout_checker import TimeoutChecker
from .coordinate_transform import CoordinateTransform
from .geojson_loader import GeoJsonLoader
from .waypoint_manager import WaypointManager
from .trajectory_builder import TrajectoryBuilder
from .speed_profile import SpeedProfile
from .obstacle_decision import ObstacleDecision, ObstacleTrack
from .stop_decision import StopDecision, TrafficLightInfo, StopTargetInfo
from .parking_planner import ParkingPlanner, ParkSlot
from .route_context_publisher import RouteContextPublisher
from .mode_handler import (
    ModeHandler,
    MODE_PARK_APPROACH,
    REQUEST_GOAL_CONFIRMED,
)


RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10,
)

TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1,
)


class PlannerNode(Node):
    """Ana Planner Node."""

    def __init__(self):
        super().__init__('planner_node')

        # ─── Parameters ────────────────────────────────────────────────────
        self.declare_parameter('mission_file', '')
        self.declare_parameter('publish_hz', 20.0)
        self.declare_parameter('status_hz', 10.0)
        self.declare_parameter('context_hz', 10.0)
        self.declare_parameter('valid_until_ms', 500)

        self.mission_file = str(self.get_parameter('mission_file').value)
        self.publish_hz = float(self.get_parameter('publish_hz').value)
        self.status_hz = float(self.get_parameter('status_hz').value)
        self.context_hz = float(self.get_parameter('context_hz').value)
        self.valid_until_ms = int(self.get_parameter('valid_until_ms').value)

        if self.publish_hz <= 0.0:
            self.publish_hz = 20.0

        if self.status_hz <= 0.0:
            self.status_hz = 10.0

        if self.context_hz <= 0.0:
            self.context_hz = 10.0

        # ─── Modules ───────────────────────────────────────────────────────
        self.timeout_checker = TimeoutChecker()
        self.coord_transform = CoordinateTransform()
        self.geojson_loader = GeoJsonLoader(self.coord_transform)
        self.waypoint_manager = WaypointManager([])
        self.traj_builder = TrajectoryBuilder()
        self.speed_profile = SpeedProfile()
        self.obstacle_decision = ObstacleDecision()
        self.stop_decision = StopDecision()
        self.parking_planner = ParkingPlanner()
        self.route_ctx_pub = RouteContextPublisher(self.coord_transform)
        self.mode_handler = ModeHandler()

        # ─── Localization state ────────────────────────────────────────────
        self.ego_x = 0.0
        self.ego_y = 0.0
        self.ego_yaw = 0.0
        self.ego_speed = 0.0

        self.loc_confidence = 0.0
        self.loc_status = 0
        self.heading_cov = 1.0
        self.position_cov = 1.0
        self.map_origin_locked = False

        # ─── Perception state ──────────────────────────────────────────────
        self.latest_lane_model = None
        self.latest_traffic_light = None
        self.latest_obstacles = None
        self.latest_stop_target = None

        # ─── Controller feedback ───────────────────────────────────────────
        self.actual_speed = 0.0
        self.cross_track_error = 0.0
        self.heading_error = 0.0
        self.full_brake_active = False

        # ─── Planning state ────────────────────────────────────────────────
        self.current_trajectory = []
        self.last_goal_reached = False
        self.last_obstacle_blocking = False

        # ─── Publishers ────────────────────────────────────────────────────
        self.traj_pub = self.create_publisher(
            Trajectory,
            '/planning/trajectory',
            RELIABLE_QOS,
        )

        self.speed_pub = self.create_publisher(
            TargetSpeed,
            '/planning/target_speed',
            RELIABLE_QOS,
        )

        self.status_pub = self.create_publisher(
            PlanningStatus,
            '/planning/status',
            RELIABLE_QOS,
        )

        self.context_pub = self.create_publisher(
            ActiveRouteContext,
            '/planning/active_route_context',
            RELIABLE_QOS,
        )

        self.goal_pub = self.create_publisher(
            GoalReached,
            '/planning/goal_reached',
            RELIABLE_QOS,
        )

        self.park_pub = self.create_publisher(
            ParkComplete,
            '/planning/park_complete',
            RELIABLE_QOS,
        )

        self.fsm_req_pub = self.create_publisher(
            FSMRequest,
            '/planning/fsm_request',
            RELIABLE_QOS,
        )

        # ─── Subscribers: Localization ─────────────────────────────────────
        self.create_subscription(
            LocalizationPose,
            '/localization/pose',
            self.pose_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            LocalizationOdometry,
            '/localization/odometry',
            self.odom_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            LocalizationStatus,
            '/localization/status',
            self.loc_status_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            MapOrigin,
            '/localization/map_origin',
            self.map_origin_callback,
            TRANSIENT_QOS,
        )

        # ─── Subscribers: Perception ───────────────────────────────────────
        self.create_subscription(
            LaneModel,
            '/perception/lane_model',
            self.lane_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            TrafficLightState,
            '/perception/traffic_light_state',
            self.traffic_light_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            ObstacleTracks,
            '/perception/obstacle_tracks',
            self.obstacle_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            StopTarget,
            '/perception/stop_target',
            self.stop_target_callback,
            RELIABLE_QOS,
        )

        # ─── Subscribers: FSM ──────────────────────────────────────────────
        self.create_subscription(
            CurrentMode,
            '/fsm/current_mode',
            self.fsm_mode_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            MissionState,
            '/fsm/mission_state',
            self.mission_state_callback,
            RELIABLE_QOS,
        )

        self.create_subscription(
            FSMEvent,
            '/fsm/event',
            self.fsm_event_callback,
            RELIABLE_QOS,
        )

        # ─── Subscribers: Controller ───────────────────────────────────────
        self.create_subscription(
            ControllerFeedback,
            '/controller/feedback',
            self.feedback_callback,
            RELIABLE_QOS,
        )

        # ─── Timers ────────────────────────────────────────────────────────
        self.create_timer(
            1.0 / self.publish_hz,
            self.planning_loop,
        )

        self.create_timer(
            1.0 / self.status_hz,
            self.publish_status,
        )

        self.create_timer(
            1.0 / self.context_hz,
            self.publish_route_context,
        )

        self.get_logger().info('planner_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — Localization
    # ───────────────────────────────────────────────────────────────────────

    def pose_callback(self, msg: LocalizationPose):
        self.timeout_checker.update('/localization/pose')

        self.ego_x = float(msg.x)
        self.ego_y = float(msg.y)
        self.ego_yaw = float(msg.yaw)

        self.loc_confidence = float(
            getattr(msg, 'localization_confidence', 0.0)
        )

        self.position_cov = float(
            getattr(msg, 'position_covariance', 1.0)
        )

        self.heading_cov = float(
            getattr(msg, 'heading_covariance', 1.0)
        )

    def odom_callback(self, msg: LocalizationOdometry):
        self.timeout_checker.update('/localization/odometry')

        self.ego_speed = float(
            getattr(msg, 'linear_velocity', 0.0)
        )

    def loc_status_callback(self, msg: LocalizationStatus):
        self.timeout_checker.update('/localization/status')

        self.loc_status = int(
            getattr(msg, 'status', 0)
        )

    def map_origin_callback(self, msg: MapOrigin):
        if msg.locked and not self.map_origin_locked:
            self.coord_transform.set_origin(
                lat_ref=float(msg.lat_ref),
                lon_ref=float(msg.lon_ref),
                yaw_ref=float(msg.yaw_ref),
            )

            self.map_origin_locked = True

            self.get_logger().info(
                f'Map origin kilitlendi: '
                f'lat={msg.lat_ref:.6f}, lon={msg.lon_ref:.6f}'
            )

            self._load_mission()

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — Perception
    # ───────────────────────────────────────────────────────────────────────

    def lane_callback(self, msg: LaneModel):
        self.timeout_checker.update('/perception/lane_model')
        self.latest_lane_model = msg

    def traffic_light_callback(self, msg: TrafficLightState):
        self.timeout_checker.update('/perception/traffic_light_state')
        self.latest_traffic_light = msg

        if hasattr(self.stop_decision, 'update_light_state'):
            self.stop_decision.update_light_state(msg.state)

    def obstacle_callback(self, msg: ObstacleTracks):
        self.timeout_checker.update('/perception/obstacle_tracks')
        self.latest_obstacles = msg

    def stop_target_callback(self, msg: StopTarget):
        self.timeout_checker.update('/perception/stop_target')
        self.latest_stop_target = msg

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — FSM
    # ───────────────────────────────────────────────────────────────────────

    def fsm_mode_callback(self, msg: CurrentMode):
        self.timeout_checker.update('/fsm/current_mode')

        self.mode_handler.update_mode(
            mode=int(msg.mode),
            stop_reason=int(getattr(msg, 'stop_reason', 0)),
            mission_active=self.mode_handler.mission_active,
            waypoint_id=int(getattr(msg, 'waypoint_id', 0)),
        )

    def mission_state_callback(self, msg: MissionState):
        self.timeout_checker.update('/fsm/mission_state')

        self.mode_handler.update_mode(
            mode=self.mode_handler.current_mode,
            stop_reason=self.mode_handler.stop_reason,
            mission_active=bool(msg.mission_active),
            waypoint_id=int(getattr(msg, 'current_waypoint_id', 0)),
        )

    def fsm_event_callback(self, msg: FSMEvent):
        self.timeout_checker.update('/fsm/event')

        event_type = int(getattr(msg, 'event_type', 255))

        if event_type == 2:
            self.get_logger().info('FSM event: OBSTACLE_CLEARED')

        elif event_type == 3:
            self.get_logger().info('FSM event: REPLANNING')
            self.current_trajectory = []

        elif event_type == 4:
            self.get_logger().warn('FSM event: MISSION_ABORT')
            self.current_trajectory = []

        elif event_type == 7:
            self.get_logger().warn('FSM event: EMERGENCY_STOP')
            self._publish_emergency_stop()

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — Controller
    # ───────────────────────────────────────────────────────────────────────

    def feedback_callback(self, msg: ControllerFeedback):
        self.timeout_checker.update('/controller/feedback')

        self.actual_speed = float(getattr(msg, 'actual_speed', 0.0))
        self.cross_track_error = float(getattr(msg, 'cross_track_error', 0.0))
        self.heading_error = float(getattr(msg, 'heading_error', 0.0))
        self.full_brake_active = bool(getattr(msg, 'full_brake_active', False))

        self.ego_speed = self.actual_speed

    # ───────────────────────────────────────────────────────────────────────
    # MAIN LOOP
    # ───────────────────────────────────────────────────────────────────────

    def planning_loop(self):
        now = self.get_clock().now()
        self.last_goal_reached = False
        self.last_obstacle_blocking = False

        timeout_result = self.timeout_checker.check_all()

        if timeout_result.get('emergency', False):
            self._publish_emergency_stop()
            return

        if not self.mode_handler.should_produce_trajectory():
            self.current_trajectory = []
            self._publish_target_speed(
                speed=0.0,
                jerk=2.0,
                reason=7,
                now=now,
            )
            return

        if self.full_brake_active:
            self._publish_target_speed(
                speed=0.0,
                jerk=10.0,
                reason=8,
                now=now,
            )
            return

        wp_result = self.waypoint_manager.update(
            self.ego_x,
            self.ego_y,
            self.ego_yaw,
            localization_degraded=(self.loc_status == 4),
            position_covariance=self.position_cov,
        )

        if wp_result.reached:
            self.last_goal_reached = True
            self._handle_waypoint_reached(wp_result)

        speed_output = self.speed_profile.compute(
            mode=self.mode_handler.current_mode,
            curvature=self._get_curvature(),
            localization_confidence=self.loc_confidence,
            loc_status=self.loc_status,
            emergency=timeout_result.get('emergency', False),
        )

        obs_result = self._check_obstacles()

        if obs_result is not None:
            self.last_obstacle_blocking = bool(obs_result.in_path)

            if obs_result.action == 'EMERGENCY':
                self._publish_emergency_stop()
                return

        stop_result = self._check_stop()

        trajectory = self._build_trajectory(speed_output.speed)

        if trajectory is None:
            self.current_trajectory = []
            self._publish_target_speed(
                speed=0.0,
                jerk=2.0,
                reason=0,
                now=now,
            )
            return

        final_speed = float(speed_output.speed)
        final_reason = int(speed_output.reason)

        if stop_result is not None and stop_result.should_stop:
            final_speed = float(stop_result.target_speed)
            final_reason = int(getattr(stop_result, 'reason', final_reason))

        if obs_result is not None:
            final_speed *= float(obs_result.speed_factor)

            if obs_result.action == 'STOP_APPROACH':
                final_reason = 8 if final_speed <= 0.0 else final_reason
            elif obs_result.action == 'SLOW':
                final_reason = 6

        final_speed = max(0.0, final_speed)

        self._publish_trajectory(trajectory, final_speed, now)
        self._publish_target_speed(
            final_speed,
            float(speed_output.jerk_limit),
            final_reason,
            now,
        )

    # ───────────────────────────────────────────────────────────────────────
    # TRAJECTORY HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _build_trajectory(self, target_speed: float):
        mode = self.mode_handler.current_mode

        if mode == MODE_PARK_APPROACH and self.latest_stop_target is not None:
            slot = ParkSlot(
                slot_x=float(getattr(self.latest_stop_target, 'stop_x', 0.0)),
                slot_y=float(getattr(self.latest_stop_target, 'stop_y', 0.0)),
                slot_heading=float(
                    getattr(self.latest_stop_target, 'stop_heading', 0.0)
                ),
                slot_available=bool(
                    getattr(self.latest_stop_target, 'slot_available', True)
                ),
            )

            traj = self.parking_planner.plan_dubins(
                ego_x=self.ego_x,
                ego_y=self.ego_y,
                ego_yaw=self.ego_yaw,
                slot=slot,
                heading_covariance=self.heading_cov,
            )

            if traj:
                self.current_trajectory = traj
                return traj

        if self.latest_lane_model is not None:
            centerline = self._extract_lane_centerline()

            if centerline:
                traj = self.traj_builder.build(
                    centerline=centerline,
                    centerline_frame='base_link',
                    curvature=float(
                        getattr(self.latest_lane_model, 'curvature', 0.0)
                    ),
                    ego_x=self.ego_x,
                    ego_y=self.ego_y,
                    ego_yaw=self.ego_yaw,
                    ego_speed=self.ego_speed,
                    target_speed=float(target_speed),
                    loc_status=self.loc_status,
                )

                if traj:
                    self.current_trajectory = traj
                    return traj

        wp = self.waypoint_manager.active_waypoint

        if wp is not None:
            traj = self.traj_builder.build_from_waypoints(
                wp_x=float(wp.x),
                wp_y=float(wp.y),
                ego_x=self.ego_x,
                ego_y=self.ego_y,
                ego_yaw=self.ego_yaw,
                target_speed=float(target_speed),
                loc_status=self.loc_status,
            )

            if traj:
                self.current_trajectory = traj
                return traj

        return None

    def _extract_lane_centerline(self):
        if self.latest_lane_model is None:
            return []

        centerline_raw = getattr(self.latest_lane_model, 'centerline', [])

        if not centerline_raw:
            return []

        centerline = []
        first = centerline_raw[0]

        if hasattr(first, 'x') and hasattr(first, 'y'):
            for pt in centerline_raw:
                centerline.append((float(pt.x), float(pt.y)))
            return centerline

        try:
            values = list(centerline_raw)
            for i in range(0, len(values) - 1, 2):
                centerline.append((float(values[i]), float(values[i + 1])))
            return centerline
        except Exception:
            return []

    # ───────────────────────────────────────────────────────────────────────
    # DECISION HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _check_obstacles(self):
        if self.latest_obstacles is None:
            return None

        tracks = []

        for t in self.latest_obstacles.tracks:
            tracks.append(
                ObstacleTrack(
                    track_id=int(getattr(t, 'track_id', 0)),
                    class_label=str(getattr(t, 'class_label', 'unknown')),
                    position_x=float(getattr(t, 'position_x', 0.0)),
                    position_y=float(getattr(t, 'position_y', 0.0)),
                    distance=float(getattr(t, 'distance', 999.0)),
                    ttc=float(getattr(t, 'ttc', float('inf'))),
                    is_static=bool(getattr(t, 'is_static', False)),
                    velocity=float(getattr(t, 'velocity', 0.0)),
                )
            )

        trajectory_bl = []

        for pt in self.current_trajectory:
            try:
                x_bl, y_bl = self.coord_transform.map_to_base_link(
                    target_x_map=float(pt.x),
                    target_y_map=float(pt.y),
                    ego_x=self.ego_x,
                    ego_y=self.ego_y,
                    ego_yaw=self.ego_yaw,
                )

                trajectory_bl.append((x_bl, y_bl, float(pt.yaw)))
            except Exception:
                continue

        return self.obstacle_decision.decide(
            tracks=tracks,
            trajectory=trajectory_bl,
            ego_speed=self.ego_speed,
            loc_status=self.loc_status,
        )

    def _check_stop(self):
        light_info = None
        stop_info = None

        if self.latest_traffic_light is not None:
            tl = self.latest_traffic_light

            light_info = TrafficLightInfo(
                state=int(getattr(tl, 'state', 0)),
                confidence=float(getattr(tl, 'confidence', 0.0)),
                relevant_to_route=bool(
                    getattr(tl, 'relevant_to_route', False)
                ),
                confirmed=bool(getattr(tl, 'confirmed', False)),
                in_stop_zone=bool(getattr(tl, 'in_stop_zone', False)),
                distance_to_stop=float(
                    getattr(tl, 'distance_to_stop', 999.0)
                ),
            )

        if self.latest_stop_target is not None:
            st = self.latest_stop_target

            distance = float(
                getattr(
                    st,
                    'distance_from_front_bumper',
                    math.hypot(
                        float(getattr(st, 'stop_x', 0.0)),
                        float(getattr(st, 'stop_y', 0.0)),
                    ),
                )
            )

            stop_info = StopTargetInfo(
                distance_from_front_bumper=distance,
                reason=int(getattr(st, 'reason', 0)),
                confidence=float(getattr(st, 'confidence', 0.0)),
            )

        return self.stop_decision.decide(
            light=light_info,
            stop_target=stop_info,
            current_speed=self.ego_speed,
        )

    def _get_curvature(self) -> float:
        if self.latest_lane_model is not None:
            return float(getattr(self.latest_lane_model, 'curvature', 0.0))
        return 0.0

    # ───────────────────────────────────────────────────────────────────────
    # WAYPOINT / FSM
    # ───────────────────────────────────────────────────────────────────────

    def _handle_waypoint_reached(self, wp_result):
        now = self.get_clock().now()

        msg = GoalReached()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.waypoint_id = int(wp_result.waypoint_id)
        msg.waypoint_type = int(wp_result.waypoint_type)
        msg.success = True

        if hasattr(msg, 'distance_error'):
            msg.distance_error = float(getattr(wp_result, 'distance_error', 0.0))

        if hasattr(msg, 'heading_error'):
            msg.heading_error = float(getattr(wp_result, 'heading_error', 0.0))

        if hasattr(msg, 'age_ms'):
            msg.age_ms = 0

        if hasattr(msg, 'valid_until_ms'):
            msg.valid_until_ms = self.valid_until_ms

        if hasattr(msg, 'warning_flags'):
            msg.warning_flags = []

        self.goal_pub.publish(msg)

        req_msg = FSMRequest()
        req_msg.header.stamp = now.to_msg()
        req_msg.header.frame_id = 'map'
        req_msg.request_type = REQUEST_GOAL_CONFIRMED
        req_msg.requested_mode = self.mode_handler.current_mode
        req_msg.waypoint_id = int(wp_result.waypoint_id)
        req_msg.reason = 'WAYPOINT_REACHED'

        if hasattr(req_msg, 'age_ms'):
            req_msg.age_ms = 0

        if hasattr(req_msg, 'valid_until_ms'):
            req_msg.valid_until_ms = self.valid_until_ms

        self.fsm_req_pub.publish(req_msg)

        has_next = self.waypoint_manager.advance()

        if not has_next:
            self.get_logger().info('Tüm waypointler tamamlandı!')

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def _publish_trajectory(self, trajectory, speed: float, now):
        msg = Trajectory()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.planner_mode = int(self.mode_handler.current_mode)
        msg.age_ms = 0
        msg.valid_until_ms = self.valid_until_ms

        for pt in trajectory:
            tp = TrajPointMsg()
            tp.x = float(pt.x)
            tp.y = float(pt.y)
            tp.yaw = float(pt.yaw)
            tp.speed = float(speed)
            tp.curvature = float(getattr(pt, 'curvature', 0.0))
            tp.distance_from_start = float(
                getattr(pt, 'distance_from_start', 0.0)
            )

            msg.points.append(tp)

        self.traj_pub.publish(msg)

    def _publish_target_speed(
        self,
        speed: float,
        jerk: float,
        reason: int,
        now,
    ):
        msg = TargetSpeed()
        msg.header.stamp = now.to_msg()

        msg.speed = float(speed)
        msg.jerk_limit = float(jerk)
        msg.reason = int(reason)

        msg.age_ms = 0
        msg.valid_until_ms = self.valid_until_ms

        self.speed_pub.publish(msg)

    def _publish_emergency_stop(self):
        now = self.get_clock().now()

        msg = TargetSpeed()
        msg.header.stamp = now.to_msg()
        msg.speed = 0.0
        msg.jerk_limit = 10.0
        msg.reason = 8
        msg.age_ms = 0
        msg.valid_until_ms = self.valid_until_ms

        self.speed_pub.publish(msg)
        self.get_logger().warn('EMERGENCY_STOP yayınlandı!')

    def publish_status(self):
        now = self.get_clock().now()
        wp = self.waypoint_manager.active_waypoint

        msg = PlanningStatus()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'

        msg.status = 0
        msg.trajectory_valid = len(self.current_trajectory) > 0
        msg.goal_reached = bool(self.last_goal_reached)
        msg.obstacle_blocking = bool(self.last_obstacle_blocking)

        lane_lost = False
        if self.latest_lane_model is not None:
            lane_lost = bool(getattr(self.latest_lane_model, 'lane_lost', False))

        msg.lane_lost = lane_lost
        msg.localization_degraded = self.loc_status == 4
        msg.active_waypoint_id = int(wp.id) if wp else 0
        msg.distance_to_goal = self._distance_to_active_goal()
        msg.planner_mode = int(self.mode_handler.current_mode)

        msg.age_ms = 0
        msg.valid_until_ms = self.valid_until_ms

        if hasattr(msg, 'warning_flags'):
            msg.warning_flags = []

            if not self.map_origin_locked:
                msg.warning_flags.append('MAP_ORIGIN_NOT_LOCKED')

            if not self.mode_handler.mission_active:
                msg.warning_flags.append('MISSION_INACTIVE')

            if lane_lost:
                msg.warning_flags.append('LANE_LOST')

            if self.loc_status == 4:
                msg.warning_flags.append('LOCALIZATION_DEGRADED')

            if self.loc_status == 6:
                msg.warning_flags.append('LOCALIZATION_LOST')

        self.status_pub.publish(msg)

    def publish_route_context(self):
        now = self.get_clock().now()
        wp = self.waypoint_manager.active_waypoint

        route_context_valid = (
            self.map_origin_locked
            and wp is not None
            and self.mode_handler.mission_active
        )

        ctx_data = self.route_ctx_pub.build(
            ego_x=self.ego_x,
            ego_y=self.ego_y,
            ego_yaw=self.ego_yaw,
            ego_speed=self.ego_speed,
            waypoint_manager=self.waypoint_manager,
            trajectory=self.current_trajectory,
            planner_mode=self.mode_handler.current_mode,
            in_stop_zone=False,
            localization_confidence=self.loc_confidence,
            route_context_valid=route_context_valid,
            lookahead_distance=1.5,
        )

        msg = ActiveRouteContext()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'base_link'

        msg.active_waypoint_id = int(ctx_data.get('active_waypoint_id', 0))
        msg.target_x = float(ctx_data.get('target_x', 0.0))
        msg.target_y = float(ctx_data.get('target_y', 0.0))

        if hasattr(msg, 'target_heading'):
            msg.target_heading = float(ctx_data.get('target_heading', 0.0))

        msg.planner_mode = int(
            ctx_data.get('planner_mode', self.mode_handler.current_mode)
        )

        if hasattr(msg, 'route_direction'):
            msg.route_direction = str(
                ctx_data.get('route_direction', 'UNKNOWN')
            )

        if hasattr(msg, 'lookahead_distance'):
            msg.lookahead_distance = float(
                ctx_data.get('lookahead_distance', 1.5)
            )

        msg.in_stop_zone = bool(ctx_data.get('in_stop_zone', False))

        if hasattr(msg, 'distance_to_stop_zone'):
            msg.distance_to_stop_zone = float(
                ctx_data.get('distance_to_stop_zone', -1.0)
            )

        if hasattr(msg, 'localization_confidence'):
            msg.localization_confidence = float(
                ctx_data.get('localization_confidence', self.loc_confidence)
            )

        msg.ego_speed_mps = float(ctx_data.get('ego_speed_mps', self.ego_speed))
        msg.route_context_valid = bool(
            ctx_data.get('route_context_valid', False)
        )

        msg.age_ms = 0
        msg.valid_until_ms = self.valid_until_ms

        if hasattr(msg, 'warning_flags'):
            msg.warning_flags = list(ctx_data.get('warning_flags', []))

        for pt_dict in ctx_data.get('planned_trajectory', []):
            pt = Point()
            pt.x = float(pt_dict.get('x', 0.0))
            pt.y = float(pt_dict.get('y', 0.0))
            pt.z = 0.0
            msg.planned_trajectory.append(pt)

        self.context_pub.publish(msg)

    # ───────────────────────────────────────────────────────────────────────
    # HELPERS
    # ───────────────────────────────────────────────────────────────────────

    def _distance_to_active_goal(self) -> float:
        wp = self.waypoint_manager.active_waypoint

        if wp is None:
            return 0.0

        return math.hypot(
            float(wp.x) - self.ego_x,
            float(wp.y) - self.ego_y,
        )

    def _load_mission(self):
        if not self.mission_file:
            self.get_logger().warn(
                'mission_file parametresi boş — GeoJSON yüklenmedi.'
            )
            return

        if not os.path.exists(self.mission_file):
            self.get_logger().error(
                f'Mission dosyası bulunamadı: {self.mission_file}'
            )
            return

        try:
            waypoints = self.geojson_loader.load(self.mission_file)
            self.waypoint_manager.reload(waypoints)

            self.get_logger().info(
                f'{len(waypoints)} waypoint yüklendi: {self.mission_file}'
            )

        except Exception as exc:
            self.get_logger().error(f'Mission yükleme hatası: {exc}')


def main(args=None):
    rclpy.init(args=args)

    node = PlannerNode()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
