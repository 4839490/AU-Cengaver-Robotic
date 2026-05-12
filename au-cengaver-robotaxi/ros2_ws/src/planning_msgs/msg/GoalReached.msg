# planning_msgs/GoalReached.msg
# =============================================================================
# Planner → FSM hedef noktasına ulaşıldı bildirimi
# Topic: /planning/goal_reached — event-driven
# =============================================================================

std_msgs/Header header

string waypoint_id
string waypoint_type
float32 distance_error