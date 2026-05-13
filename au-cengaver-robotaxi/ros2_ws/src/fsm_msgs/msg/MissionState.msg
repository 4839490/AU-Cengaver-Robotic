# fsm_msgs/MissionState.msg
# =============================================================================
# FSM → Planner görev durumu
# Topic: /fsm/mission_state — 5Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

bool mission_active
uint32 total_waypoints
uint32 completed_waypoints
string current_waypoint_id
string current_waypoint_type
string next_waypoint_id
string next_waypoint_type
string[] warning_flags