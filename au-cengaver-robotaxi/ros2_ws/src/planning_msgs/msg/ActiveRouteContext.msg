# planning_msgs/ActiveRouteContext.msg
# =============================================================================
# Planner → Controller/Perception aktif rota bağlamı
# Topic: /planning/active_route_context — 10-20Hz — BASE_LINK frame
#
# ⚠️ Koordinatlar base_link frame — map frame değil!
# ego_speed_mps → controller_feedback.actual_speed'den gelir (TTC için zorunlu)
# =============================================================================

std_msgs/Header header

float32 target_x
float32 target_y
uint8 planner_mode
bool in_stop_zone
float32 ego_speed_mps
bool route_context_valid

TrajectoryPoint[] planned_trajectory

uint32 age_ms
uint32 valid_until_ms
string[] warning_flags