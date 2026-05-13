# planning_msgs/FSMRequest.msg
# =============================================================================
# Planner → FSM mod değişiklik isteği
# Topic: /planning/fsm_request — event-driven
# =============================================================================

std_msgs/Header header

uint8 REQUEST_MODE_CHANGE=0
uint8 REQUEST_STOP=1
uint8 REQUEST_RESUME=2
uint8 REQUEST_REPLAN=3
uint8 REQUEST_MISSION_COMPLETE=4
uint8 REQUEST_PARK_READY=5

uint8 request_type
uint8 requested_mode
string waypoint_id
string reason