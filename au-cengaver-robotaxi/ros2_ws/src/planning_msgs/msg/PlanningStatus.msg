# planning_msgs/PlanningStatus.msg
# =============================================================================
# Planner → Controller/FSM sağlık raporu
# Topic: /planning/status — 10Hz
#
# Controller davranışları:
#   STATUS_LOCALIZATION_DEGRADED → hızı %50 düşür
#   STATUS_EMERGENCY             → TAM FREN
#   STATUS_MISSION_COMPLETE      → dur + el freni
# =============================================================================

std_msgs/Header header

uint8 STATUS_ACTIVE=0
uint8 STATUS_WAITING_FSM=1
uint8 STATUS_OBSTACLE_BLOCKED=2
uint8 STATUS_LANE_LOST=3
uint8 STATUS_LOCALIZATION_DEGRADED=4
uint8 STATUS_EMERGENCY=5
uint8 STATUS_MISSION_COMPLETE=6

uint8 status
bool trajectory_valid
bool goal_reached
bool parking_entry_reached
bool obstacle_blocking
bool lane_lost
bool localization_degraded
uint8 active_waypoint_id
float32 distance_to_goal
uint8 planner_mode
uint32 age_ms
uint32 valid_until_ms
string[] warning_flags