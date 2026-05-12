# planning_msgs/ParkComplete.msg
# =============================================================================
# Planner → FSM park tamamlandı bildirimi
# Topic: /planning/park_complete — event-driven
# =============================================================================

std_msgs/Header header

string waypoint_id
bool success
float32 lateral_error
float32 heading_error
string[] warning_flags