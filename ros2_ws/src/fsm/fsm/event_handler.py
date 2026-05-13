"""
AU Cengaver Robotics — Event Handler
TEKNOFEST 2026

Event gönderme mantığı burada.
fsm_node.py bu sınıfı kullanır.

Sözleşme: FSM_Planner_Contract_v1.1, Bölüm 7 — /fsm/event
FSMEvent.event_type sabitleri:
  PICKUP_COMPLETE=0, DROPOFF_COMPLETE=1, OBSTACLE_CLEARED=2,
  REPLANNING_REQUEST=3, MISSION_ABORT=4, RESUME=5,
  PARK_SLOT_CHANGE=6, EMERGENCY_STOP_REQUEST=7
"""

from fsm_msgs.msg import FSMEvent
import rclpy.logging

logger = rclpy.logging.get_logger('event_handler')


class EventHandler:

    def __init__(self, publisher, clock):
        """
        publisher: /fsm/event publisher'ı
        clock: node'un saati
        """
        self.publisher = publisher
        self.clock     = clock

    def gonder(self, event_type, waypoint_id, data=""):
        """
        Planner'a anlık olay bildir.
        """
        msg = FSMEvent()
        msg.header.stamp = self.clock.now().to_msg()
        msg.event_type   = event_type
        msg.waypoint_id  = waypoint_id
        msg.data         = data
        self.publisher.publish(msg)

        logger.info(f"EVENT: tip={event_type}, wp={waypoint_id}, data={data}")

    def pickup_complete(self, waypoint_id):
        self.gonder(FSMEvent.PICKUP_COMPLETE, waypoint_id)

    def dropoff_complete(self, waypoint_id):
        self.gonder(FSMEvent.DROPOFF_COMPLETE, waypoint_id)

    def obstacle_cleared(self, waypoint_id):
        self.gonder(FSMEvent.OBSTACLE_CLEARED, waypoint_id)

    def replanning_request(self, waypoint_id, sebep=""):
        self.gonder(FSMEvent.REPLANNING_REQUEST, waypoint_id, sebep)

    def mission_abort(self):
        self.gonder(FSMEvent.MISSION_ABORT, 0)

    def resume(self, waypoint_id):
        self.gonder(FSMEvent.RESUME, waypoint_id)

    def park_slot_change(self, new_slot_id):
        self.gonder(FSMEvent.PARK_SLOT_CHANGE, 0, f"new_slot_id:{new_slot_id}")

    def emergency_stop(self, sebep=""):
        self.gonder(FSMEvent.EMERGENCY_STOP_REQUEST, 0, sebep)

    # FIX: REQUEST_REJECTED sözleşmede tanımlı bir FSMEvent değil — kaldırıldı.
    # Bilinmeyen istek tipi geldiğinde fsm_node.py sadece log atar.
