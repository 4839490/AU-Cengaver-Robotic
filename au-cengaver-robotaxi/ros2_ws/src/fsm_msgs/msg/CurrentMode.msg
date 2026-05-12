# fsm_msgs/CurrentMode.msg
# =============================================================================
# FSM → Planner/Controller mevcut mod bilgisi
# Topic: /fsm/current_mode — 10Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

uint8 mode
uint8 previous_mode

uint8 stop_reason
string waypoint_id
string[] warning_flags