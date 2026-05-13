#!/usr/bin/env python3
"""
AU Cengaver Robotics — TEKNOFEST 2026
planner_node.py

Ana Planner Koordinatörü
  Tüm modülleri bir araya getirir, topic'leri subscribe/publish eder

Algoritma Uygulama Önceliği (Algo Tablosu v2.0 §5):
  1. Algo 17 — Timeout Denetleyici (timeout_checker)
  2. Algo 3  — Hedef Doğrulama (waypoint_manager)
  3. Algo 6  — Adaptif Lookahead Trajectory (trajectory_builder)
  4. Algo 9  — Dinamik Hız Profili (speed_profile)
  5. Algo 11 — Reaktif Engel Kaçınma (obstacle_decision)
  6. Algo 15 — Stop Profili (stop_decision)
  7. Algo 13 — Dubins Park (parking_planner)

Sözleşmeler:
  - Planner ↔ Controller Contract v1.3
  - FSM ↔ Planner Contract v1.1
  - Perception ↔ Planner Contract v1.4
  - Localization ↔ Planner Contract v1.2
"""

import os
import math
import rclpy
from rclpy.node import Node
from rclpy.qos import (
    QoSProfile, ReliabilityPolicy,
    DurabilityPolicy, HistoryPolicy
)

from std_msgs.msg import Header
from geometry_msgs.msg import Point

from common_msgs.msg import AutonomyMode
from planning_msgs.msg import (
    Trajectory, TrajectoryPoint as TrajPointMsg,
    TargetSpeed, PlanningStatus,
    ActiveRouteContext, GoalReached,
    ParkComplete, ControllerFeedback,
    FSMRequest
)
from localization_msgs.msg import (
    LocalizationPose, LocalizationOdometry,
    LocalizationStatus, MapOrigin
)
from perception_msgs.msg import (
    LaneModel, TrafficLightState,
    ObstacleTracks, StopTarget
)
from fsm_msgs.msg import CurrentMode, MissionState, FSMEvent

from .timeout_checker import TimeoutChecker
from .coordinate_transform import CoordinateTransform
from .geojson_loader import GeoJsonLoader
from .waypoint_manager import WaypointManager
from .trajectory_builder import TrajectoryBuilder, TrajectoryPoint
from .speed_profile import SpeedProfile
from .obstacle_decision import ObstacleDecision, ObstacleTrack
from .stop_decision import (
    StopDecision, TrafficLightInfo, StopTargetInfo
)
from .parking_planner import ParkingPlanner, ParkSlot
from .route_context_publisher import RouteContextPublisher
from .mode_handler import (
    ModeHandler,
    MODE_LANE_FOLLOW, MODE_STOP_APPROACH,
    MODE_PICKUP_APPROACH, MODE_DROPOFF_APPROACH,
    MODE_OBSTACLE_AVOID, MODE_PARK_APPROACH,
    MODE_PARK_MANEUVER, MODE_MISSION_COMPLETE,
    REQUEST_GOAL_CONFIRMED, REQUEST_OBSTACLE_BLOCKED,
    REQUEST_PARK_READY
)


# ─── QoS ───────────────────────────────────────────────────────────────────
RELIABLE_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.VOLATILE,
    history=HistoryPolicy.KEEP_LAST,
    depth=10
)

TRANSIENT_QOS = QoSProfile(
    reliability=ReliabilityPolicy.RELIABLE,
    durability=DurabilityPolicy.TRANSIENT_LOCAL,
    history=HistoryPolicy.KEEP_LAST,
    depth=1
)


class PlannerNode(Node):
    """
    Ana Planner Node — tüm modülleri koordine eder.
    """

    def __init__(self):
        super().__init__('planner_node')

        # ─── Parametreler ──────────────────────────────────────────────────
        self.declare_parameter('mission_file', '')
        self.declare_parameter('publish_hz',   20.0)
        self.declare_parameter('status_hz',    10.0)
        self.declare_parameter('context_hz',   10.0)
        self.declare_parameter('valid_until_ms', 500)

        self.mission_file    = self.get_parameter('mission_file').value
        self.publish_hz      = self.get_parameter('publish_hz').value
        self.status_hz       = self.get_parameter('status_hz').value
        self.context_hz      = self.get_parameter('context_hz').value
        self.valid_until_ms  = self.get_parameter('valid_until_ms').value

        # ─── Modüller ──────────────────────────────────────────────────────
        self.timeout_checker  = TimeoutChecker()
        self.coord_transform  = CoordinateTransform()
        self.geojson_loader   = GeoJsonLoader(self.coord_transform)
        self.waypoint_manager = WaypointManager([])
        self.traj_builder     = TrajectoryBuilder()
        self.speed_profile    = SpeedProfile()
        self.obstacle_decision = ObstacleDecision()
        self.stop_decision    = StopDecision()
        self.parking_planner  = ParkingPlanner()
        self.route_ctx_pub    = RouteContextPublisher(self.coord_transform)
        self.mode_handler     = ModeHandler()

        # ─── Durum ─────────────────────────────────────────────────────────
        # Lokalizasyon
        self.ego_x    = 0.0
        self.ego_y    = 0.0
        self.ego_yaw  = 0.0
        self.ego_speed = 0.0
        self.loc_confidence  = 0.0
        self.loc_status      = 0
        self.heading_cov     = 1.0
        self.position_cov    = 1.0
        self.map_origin_locked = False

        # Perception
        self.latest_lane_model    = None
        self.latest_traffic_light = None
        self.latest_obstacles     = None
        self.latest_stop_target   = None

        # Controller feedback
        self.actual_speed         = 0.0
        self.cross_track_error    = 0.0
        self.heading_error        = 0.0
        self.full_brake_active    = False

        # Trajectory
        self.current_trajectory: list = []

        # ─── Publishers ────────────────────────────────────────────────────
        self.traj_pub = self.create_publisher(
            Trajectory, '/planning/trajectory', RELIABLE_QOS
        )
        self.speed_pub = self.create_publisher(
            TargetSpeed, '/planning/target_speed', RELIABLE_QOS
        )
        self.status_pub = self.create_publisher(
            PlanningStatus, '/planning/status', RELIABLE_QOS
        )
        self.context_pub = self.create_publisher(
            ActiveRouteContext, '/planning/active_route_context', RELIABLE_QOS
        )
        self.goal_pub = self.create_publisher(
            GoalReached, '/planning/goal_reached', RELIABLE_QOS
        )
        self.park_pub = self.create_publisher(
            ParkComplete, '/planning/park_complete', RELIABLE_QOS
        )
        self.fsm_req_pub = self.create_publisher(
            FSMRequest, '/planning/fsm_request', RELIABLE_QOS
        )

        # ─── Subscribers ───────────────────────────────────────────────────
        # Localization
        self.create_subscription(
            LocalizationPose, '/localization/pose',
            self.pose_callback, RELIABLE_QOS
        )
        self.create_subscription(
            LocalizationOdometry, '/localization/odometry',
            self.odom_callback, RELIABLE_QOS
        )
        self.create_subscription(
            LocalizationStatus, '/localization/status',
            self.loc_status_callback, RELIABLE_QOS
        )
        self.create_subscription(
            MapOrigin, '/localization/map_origin',
            self.map_origin_callback, TRANSIENT_QOS
        )

        # Perception
        self.create_subscription(
            LaneModel, '/perception/lane_model',
            self.lane_callback, RELIABLE_QOS
        )
        self.create_subscription(
            TrafficLightState, '/perception/traffic_light_state',
            self.traffic_light_callback, RELIABLE_QOS
        )
        self.create_subscription(
            ObstacleTracks, '/perception/obstacle_tracks',
            self.obstacle_callback, RELIABLE_QOS
        )
        self.create_subscription(
            StopTarget, '/perception/stop_target',
            self.stop_target_callback, RELIABLE_QOS
        )

        # FSM
        self.create_subscription(
            CurrentMode, '/fsm/current_mode',
            self.fsm_mode_callback, RELIABLE_QOS
        )
        self.create_subscription(
            MissionState, '/fsm/mission_state',
            self.mission_state_callback, RELIABLE_QOS
        )
        self.create_subscription(
            FSMEvent, '/fsm/event',
            self.fsm_event_callback, RELIABLE_QOS
        )

        # Controller feedback
        self.create_subscription(
            ControllerFeedback, '/controller/feedback',
            self.feedback_callback, RELIABLE_QOS
        )

        # ─── Timer'lar ─────────────────────────────────────────────────────
        self.create_timer(
            1.0 / self.publish_hz, self.planning_loop
        )
        self.create_timer(
            1.0 / self.status_hz, self.publish_status
        )
        self.create_timer(
            1.0 / self.context_hz, self.publish_route_context
        )

        self.get_logger().info('planner_node başlatıldı.')

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — Localization
    # ───────────────────────────────────────────────────────────────────────

    def pose_callback(self, msg: LocalizationPose):
        self.timeout_checker.update('/localization/pose')
        self.ego_x           = msg.x
        self.ego_y           = msg.y
        self.ego_yaw         = msg.yaw
        self.loc_confidence  = msg.localization_confidence
        self.position_cov    = msg.position_covariance
        self.heading_cov     = msg.heading_covariance

    def odom_callback(self, msg: LocalizationOdometry):
        self.timeout_checker.update('/localization/odometry')
        self.ego_speed = msg.linear_velocity

    def loc_status_callback(self, msg: LocalizationStatus):
        self.timeout_checker.update('/localization/status')
        self.loc_status = msg.status

    def map_origin_callback(self, msg: MapOrigin):
        if msg.locked and not self.map_origin_locked:
            self.coord_transform.set_origin(
                msg.lat_ref, msg.lon_ref, msg.yaw_ref
            )
            self.map_origin_locked = True
            self.get_logger().info(
                f'Map origin kilitlendi: '
                f'lat={msg.lat_ref:.6f}, lon={msg.lon_ref:.6f}'
            )
            # Mission dosyasını yükle
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
            mode=msg.mode,
            stop_reason=msg.stop_reason,
            mission_active=True,
            waypoint_id=msg.waypoint_id
        )

    def mission_state_callback(self, msg: MissionState):
        self.timeout_checker.update('/fsm/mission_state')
        self.mode_handler.update_mode(
            mode=self.mode_handler.current_mode,
            mission_active=msg.mission_active,
            waypoint_id=msg.current_waypoint_id
        )

    def fsm_event_callback(self, msg: FSMEvent):
        """FSM olaylarını işle."""
        if msg.event_type == 2:   # OBSTACLE_CLEARED
            self.get_logger().info('Engel kalktı — LANE_FOLLOW\'a dön')
        elif msg.event_type == 3:  # REPLANNING
            self.get_logger().info('Yeniden planlama isteği')
            self.current_trajectory = []
        elif msg.event_type == 4:  # MISSION_ABORT
            self.get_logger().warn('Görev iptal edildi!')
            self.current_trajectory = []

    # ───────────────────────────────────────────────────────────────────────
    # CALLBACKS — Controller
    # ───────────────────────────────────────────────────────────────────────

    def feedback_callback(self, msg: ControllerFeedback):
        self.timeout_checker.update('/controller/feedback')
        self.actual_speed      = msg.actual_speed
        self.cross_track_error = msg.cross_track_error
        self.heading_error     = msg.heading_error
        self.full_brake_active = msg.full_brake_active

        # ego_speed güncelle — controller feedback'ten
        # Perception TTC hesabı için active_route_context'e aktarılır
        self.ego_speed = msg.actual_speed

    # ───────────────────────────────────────────────────────────────────────
    # ANA PLANLAMA DÖNGÜSÜ — 20Hz
    # ───────────────────────────────────────────────────────────────────────

    def planning_loop(self):
        """
        Ana planlama döngüsü — 20Hz.
        Algoritma öncelik sırası: 17 → 3 → 6 → 9 → 11 → 15 → 13
        """
        now = self.get_clock().now()

        # ── 1. Algo 17: Timeout kontrolü ────────────────────────────────
        timeout_result = self.timeout_checker.check_all()

        if timeout_result['emergency']:
            self._publish_emergency_stop()
            return

        # ── 2. mission_active kontrolü (FSM Contract FIX-3) ─────────────
        if not self.mode_handler.should_produce_trajectory():
            return

        # ── 3. full_brake_active → trajectory üretme beklet ─────────────
        if self.full_brake_active:
            return

        # ── 4. Waypoint doğrulama (Algo 3) ──────────────────────────────
        wp_result = self.waypoint_manager.update(
            self.ego_x, self.ego_y, self.ego_yaw,
            localization_degraded=(self.loc_status == 4),
            position_covariance=self.position_cov
        )

        if wp_result.reached:
            self._handle_waypoint_reached(wp_result)

        # ── 5. Hız profili (Algo 9) ──────────────────────────────────────
        speed_output = self.speed_profile.compute(
            mode=self.mode_handler.current_mode,
            curvature=self._get_curvature(),
            localization_confidence=self.loc_confidence,
            loc_status=self.loc_status,
            emergency=timeout_result['emergency'],
        )

        # ── 6. Engel kararı (Algo 11) ────────────────────────────────────
        obs_result = self._check_obstacles()
        if obs_result is not None and obs_result.action == 'EMERGENCY':
            self._publish_emergency_stop()
            return

        # ── 7. Dur kararı (Algo 15) ──────────────────────────────────────
        stop_result = self._check_stop()

        # ── 8. Trajectory üret (Algo 6 veya 13) ─────────────────────────
        trajectory = self._build_trajectory(speed_output.speed)

        if trajectory is None:
            return

        # ── 9. Hız override — dur veya engel ────────────────────────────
        final_speed = speed_output.speed
        if stop_result is not None and stop_result.should_stop:
            final_speed = stop_result.target_speed
        if obs_result is not None:
            final_speed *= obs_result.speed_factor

        # ── 10. Yayınla ─────────────────────────────────────────────────
        self._publish_trajectory(trajectory, final_speed, now)
        self._publish_target_speed(
            final_speed,
            speed_output.jerk_limit,
            speed_output.reason,
            now
        )

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI — Trajectory
    # ───────────────────────────────────────────────────────────────────────

    def _build_trajectory(self, target_speed: float):
        """Moda göre trajectory üret."""
        mode = self.mode_handler.current_mode

        # Park modu → Dubins Path (Algo 13)
        if mode == MODE_PARK_APPROACH and \
                self.latest_stop_target is not None:
            slot = ParkSlot(
                slot_x=self.latest_stop_target.stop_x,
                slot_y=self.latest_stop_target.stop_y,
                slot_heading=0.0,
                slot_available=True
            )
            traj = self.parking_planner.plan_dubins(
                self.ego_x, self.ego_y, self.ego_yaw,
                slot, self.heading_cov
            )
            if traj:
                self.current_trajectory = traj
                return traj

        # Şerit bazlı trajectory (Algo 6)
        if self.latest_lane_model is not None:
            centerline = [
                (pt.x, pt.y)
                for pt in self.latest_lane_model.centerline
            ] if hasattr(
                self.latest_lane_model.centerline[0], 'x'
            ) else list(zip(
                self.latest_lane_model.centerline[::2],
                self.latest_lane_model.centerline[1::2]
            )) if self.latest_lane_model.centerline else []

            if centerline:
                traj = self.traj_builder.build(
                    centerline=centerline,
                    curvature=self.latest_lane_model.curvature,
                    ego_x=self.ego_x,
                    ego_y=self.ego_y,
                    ego_yaw=self.ego_yaw,
                    ego_speed=self.ego_speed,
                    target_speed=target_speed,
                    loc_status=self.loc_status,
                )
                if traj:
                    self.current_trajectory = traj
                    return traj

        # Waypoint'e doğru fallback trajectory
        wp = self.waypoint_manager.active_waypoint
        if wp is not None:
            traj = self.traj_builder.build_from_waypoints(
                wp_x=wp.x, wp_y=wp.y,
                ego_x=self.ego_x, ego_y=self.ego_y,
                ego_yaw=self.ego_yaw,
                target_speed=target_speed,
                loc_status=self.loc_status,
            )
            if traj:
                self.current_trajectory = traj
                return traj

        return None

    def _check_obstacles(self):
        """Engel kontrolü."""
        if self.latest_obstacles is None:
            return None

        tracks = [
            ObstacleTrack(
                track_id=t.track_id,
                class_label=t.class_label,
                position_x=t.position_x,
                position_y=t.position_y,
                distance=t.distance,
                ttc=t.ttc,
                is_static=t.is_static,
            )
            for t in self.latest_obstacles.tracks
        ]

        return self.obstacle_decision.decide(
            tracks=tracks,
            trajectory=self.current_trajectory,
            ego_speed=self.ego_speed,
            loc_status=self.loc_status
        )

    def _check_stop(self):
        """Dur kararı kontrolü."""
        light_info  = None
        stop_info   = None

        if self.latest_traffic_light is not None:
            tl = self.latest_traffic_light
            light_info = TrafficLightInfo(
                state=tl.state,
                confidence=tl.confidence,
                relevant_to_route=tl.relevant_to_route,
                confirmed=tl.confirmed,
                in_stop_zone=tl.in_stop_zone,
                distance_to_stop=tl.distance_to_stop
            )

        if self.latest_stop_target is not None:
            st = self.latest_stop_target
            stop_info = StopTargetInfo(
                distance_from_front_bumper=math.sqrt(
                    st.stop_x**2 + st.stop_y**2
                ),
                reason=st.reason,
                confidence=st.confidence
            )

        return self.stop_decision.decide(
            light=light_info,
            stop_target=stop_info,
            current_speed=self.ego_speed
        )

    def _get_curvature(self) -> float:
        """Anlık yol eğriliği."""
        if self.latest_lane_model is not None:
            return self.latest_lane_model.curvature
        return 0.0

    def _handle_waypoint_reached(self, wp_result):
        """Waypoint'e ulaşıldı — FSM'e bildir."""
        now = self.get_clock().now()

        # GoalReached yayınla
        msg              = GoalReached()
        msg.header.stamp = now.to_msg()
        msg.waypoint_id  = wp_result.waypoint_id
        msg.waypoint_type = wp_result.waypoint_type
        msg.success      = True
        self.goal_pub.publish(msg)

        # FSMRequest yayınla
        req_msg              = FSMRequest()
        req_msg.header.stamp = now.to_msg()
        req_msg.request_type = REQUEST_GOAL_CONFIRMED
        req_msg.waypoint_id  = wp_result.waypoint_id
        req_msg.reason       = 'WAYPOINT_REACHED'
        self.fsm_req_pub.publish(req_msg)

        # Sonraki waypoint'e geç
        has_next = self.waypoint_manager.advance()
        if not has_next:
            self.get_logger().info('Tüm waypointler tamamlandı!')

    # ───────────────────────────────────────────────────────────────────────
    # PUBLISH
    # ───────────────────────────────────────────────────────────────────────

    def _publish_trajectory(self, trajectory, speed: float, now):
        """Trajectory yayınla."""
        msg              = Trajectory()
        msg.header.stamp = now.to_msg()
        msg.header.frame_id = 'map'
        msg.planner_mode = self.mode_handler.current_mode
        msg.age_ms       = 0
        msg.valid_until_ms = self.valid_until_ms

        for pt in trajectory:
            tp              = TrajPointMsg()
            tp.x            = float(pt.x)
            tp.y            = float(pt.y)
            tp.yaw          = float(pt.yaw)
            tp.speed        = float(speed)
            tp.curvature    = float(pt.curvature)
            tp.distance_from_start = float(pt.distance_from_start)
            msg.points.append(tp)

        self.traj_pub.publish(msg)

    def _publish_target_speed(
        self, speed: float, jerk: float, reason: int, now
    ):
        """Target speed yayınla."""
        msg              = TargetSpeed()
        msg.header.stamp = now.to_msg()
        msg.speed        = float(speed)
        msg.jerk_limit   = float(jerk)
        msg.reason       = reason
        msg.age_ms       = 0
        msg.valid_until_ms = self.valid_until_ms
        self.speed_pub.publish(msg)

    def _publish_emergency_stop(self):
        """EMERGENCY_STOP yayınla."""
        now = self.get_clock().now()
        msg              = TargetSpeed()
        msg.header.stamp = now.to_msg()
        msg.speed        = 0.0
        msg.jerk_limit   = 10.0
        msg.reason       = 8   # EMERGENCY_STOP
        msg.age_ms       = 0
        msg.valid_until_ms = self.valid_until_ms
        self.speed_pub.publish(msg)
        self.get_logger().warn('EMERGENCY_STOP yayınlandı!')

    def publish_status(self):
        """10Hz planning status yayınla."""
        now = self.get_clock().now()
        wp  = self.waypoint_manager.active_waypoint

        msg                    = PlanningStatus()
        msg.header.stamp       = now.to_msg()
        msg.status             = 0   # ACTIVE
        msg.trajectory_valid   = len(self.current_trajectory) > 0
        msg.goal_reached       = False
        msg.obstacle_blocking  = False
        msg.lane_lost          = (
            self.latest_lane_model is not None and
            self.latest_lane_model.lane_lost
        )
        msg.localization_degraded = (self.loc_status == 4)
        msg.active_waypoint_id = wp.id if wp else 0
        msg.distance_to_goal   = 0.0
        msg.planner_mode       = self.mode_handler.current_mode
        msg.age_ms             = 0
        msg.valid_until_ms     = self.valid_until_ms
        self.status_pub.publish(msg)

    def publish_route_context(self):
        """10Hz active_route_context yayınla."""
        now = self.get_clock().now()

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
            route_context_valid=self.map_origin_locked,
            lookahead_distance=1.5,
        )

        msg                  = ActiveRouteContext()
        msg.header.stamp     = now.to_msg()
        msg.header.frame_id  = 'base_link'
        msg.active_waypoint_id = ctx_data['active_waypoint_id']
        msg.target_x         = float(ctx_data['target_x'])
        msg.target_y         = float(ctx_data['target_y'])
        msg.planner_mode     = ctx_data['planner_mode']
        msg.in_stop_zone     = ctx_data['in_stop_zone']
        msg.ego_speed_mps    = float(ctx_data['ego_speed_mps'])
        msg.route_context_valid = ctx_data['route_context_valid']
        msg.age_ms           = 0
        msg.valid_until_ms   = self.valid_until_ms

        for pt_dict in ctx_data['planned_trajectory']:
            pt   = Point()
            pt.x = float(pt_dict['x'])
            pt.y = float(pt_dict['y'])
            pt.z = 0.0
            msg.planned_trajectory.append(pt)

        self.context_pub.publish(msg)

    # ───────────────────────────────────────────────────────────────────────
    # YARDIMCI
    # ───────────────────────────────────────────────────────────────────────

    def _load_mission(self):
        """Mission dosyasını yükle."""
        if not self.mission_file:
            self.get_logger().warn(
                'mission_file parametresi boş — '
                'GeoJSON yüklenmedi.'
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
                f'{len(waypoints)} waypoint yüklendi: '
                f'{self.mission_file}'
            )
        except Exception as e:
            self.get_logger().error(f'Mission yükleme hatası: {e}')


# ───────────────────────────────────────────────────────────────────────────
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