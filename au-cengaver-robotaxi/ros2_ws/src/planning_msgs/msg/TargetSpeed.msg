# planning_msgs/TargetSpeed.msg
# =============================================================================
# Planner → Controller güvenlik hızı
# Topic: /planning/target_speed — 20Hz
#
# Hız öncelik kuralı:
#   final_speed = min(target_speed.speed, trajectory_point.speed)
# =============================================================================

std_msgs/Header header

float32 speed
float32 jerk_limit
uint8 reason
uint32 valid_until_ms
uint32 age_ms
string[] warning_flags

uint8 REASON_LANE_FOLLOW=0
uint8 REASON_APPROACH_STOP=1
uint8 REASON_PICKUP_DROPOFF=2
uint8 REASON_OBSTACLE_SLOW=3
uint8 REASON_JUNCTION=4
uint8 REASON_TUNNEL=5
uint8 REASON_PARK_APPROACH=6
uint8 REASON_PARK_MANEUVER=7
uint8 REASON_EMERGENCY_STOP=8