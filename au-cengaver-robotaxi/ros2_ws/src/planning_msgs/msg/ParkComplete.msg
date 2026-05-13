# planning_msgs/ParkComplete.msg
# =============================================================================
# Planner → FSM park tamamlandı bildirimi
# Topic: /planning/park_complete — event-driven
# =============================================================================

# planning_msgs/ParkComplete.msg

std_msgs/Header header

bool success

float32 final_cross_track_error
float32 final_heading_error
uint8 iterations_used

uint32 waypoint_id
uint32 age_ms
uint32 valid_until_ms
string[] warning_flags
