# planning_msgs/FSMRequest.msg
# =============================================================================
# Planner → FSM mod değişiklik isteği
# Topic: /planning/fsm_request — event-driven
# =============================================================================

# planning_msgs/FSMRequest.msg

uint8 MODE_CHANGE=0
uint8 REPLANNING_NEEDED=1
uint8 GOAL_CONFIRMED=2
uint8 OBSTACLE_BLOCKED=3
uint8 LOCALIZATION_DEGRADED=4
uint8 PARK_READY=5

std_msgs/Header header

uint8 request_type
uint8 requested_mode
uint32 waypoint_id
string reason

uint32 age_ms
uint32 valid_until_ms
