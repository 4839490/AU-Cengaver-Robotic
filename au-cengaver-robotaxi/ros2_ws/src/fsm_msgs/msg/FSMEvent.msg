# fsm_msgs/FSMEvent.msg
# =============================================================================
# Planner/Controller → FSM olay bildirimi
# Topic: /fsm/event — event-driven
#
# ⚠️ FSM EMERGENCY_STOP isteği üretebilir
#    AUTONOMOUS_EMERGENCY safety supervisor sorumluluğundadır
#    FSM bu sinyali sadece izler ve loglar
# =============================================================================

std_msgs/Header header

uint8 PICKUP_COMPLETE=0
uint8 DROPOFF_COMPLETE=1
uint8 OBSTACLE_CLEARED=2
uint8 PARK_COMPLETE=3
uint8 MISSION_START=4
uint8 MISSION_ABORT=5
uint8 LOC_LOST=6
uint8 EMERGENCY_STOP_REQUEST=7

uint8 event_type
string waypoint_id
string data