# planning_msgs/Trajectory.msg
# =============================================================================
# Planner → Controller yörünge
# Topic: /planning/trajectory — 20Hz — map frame
#
# Timeout kuralı:
#   0-500ms    → normal
#   500-1000ms → hız %50 düşür
#   >1000ms    → TAM FREN
# =============================================================================

std_msgs/Header header

TrajectoryPoint[] points
uint8 planner_mode
uint32 valid_until_ms
uint32 age_ms
string[] warning_flags