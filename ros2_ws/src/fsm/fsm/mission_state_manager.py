"""
AU Cengaver Robotics — Mission State Manager
TEKNOFEST 2026

Görev durumu takibi burada.
fsm_node.py bu sınıfı kullanır.
"""

import rclpy.logging

logger = rclpy.logging.get_logger('mission_state_manager')


class MissionStateManager:

    def __init__(self):
        self.mission_active        = False
        self.total_waypoints       = 0
        self.completed_waypoints   = 0
        self.current_waypoint_id   = 0
        self.current_waypoint_type = 0
        self.next_waypoint_id      = 0
        self.next_waypoint_type    = 0
        self.pickup_complete       = False
        self.dropoff_complete      = False

    def gorevi_baslat(self, total_waypoints):
        """Görevi başlat."""
        self.mission_active        = True
        self.total_waypoints       = total_waypoints
        self.completed_waypoints   = 0
        self.pickup_complete       = False
        self.dropoff_complete      = False
        logger.info(f"Görev başladı — {total_waypoints} waypoint")

    def gorevi_bitir(self):
        """Görevi tamamla."""
        self.mission_active = False
        logger.info("Görev tamamlandı")

    def waypoint_tamamla(self, waypoint_id, waypoint_type):
        """Bir waypoint tamamlandı."""
        self.completed_waypoints  += 1
        self.current_waypoint_id   = waypoint_id
        self.current_waypoint_type = waypoint_type
        logger.info(
            f"Waypoint tamamlandı: {waypoint_id} "
            f"({self.completed_waypoints}/{self.total_waypoints})"
        )

    def pickup_tamamla(self, waypoint_id):
        self.pickup_complete = True
        self.waypoint_tamamla(waypoint_id, 0)

    def dropoff_tamamla(self, waypoint_id):
        self.dropoff_complete = True
        self.waypoint_tamamla(waypoint_id, 1)

    def sonraki_waypoint_ayarla(self, next_id, next_type):
        self.next_waypoint_id   = next_id
        self.next_waypoint_type = next_type
        # FIX: yeni waypoint'e geçerken önceki pickup/dropoff sinyallerini sıfırla.
        # Eski kodda True kalıyordu — planner bir sonraki waypointte de tamamlandı sanıyordu.
        self.pickup_complete  = False
        self.dropoff_complete = False

    def gorev_bitti_mi(self):
        """Tüm waypointler tamamlandı mı?"""
        if self.total_waypoints == 0:
            return False
        return self.completed_waypoints >= self.total_waypoints
