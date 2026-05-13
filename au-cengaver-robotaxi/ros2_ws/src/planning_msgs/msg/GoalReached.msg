# planning_msgs/GoalReached.msg
# =============================================================================
# Planner → FSM hedef noktasına ulaşıldı bildirimi
# Topic: /planning/goal_reached — event-driven
# =============================================================================

# planning_msgs/GoalReached.msg

uint8 PICKUP=0
uint8 DROPOFF=1
uint8 WAYPOINT=2
uint8 PARK_ENTRY=3

std_msgs/Header header

uint32 waypoint_id
uint8  waypoint_type
bool   success

float32 distance_error
float32 heading_error

uint32 age_ms
uint32 valid_until_ms
string[] warning_flags
