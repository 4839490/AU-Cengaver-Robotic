# common_msgs/StopReason.msg
# =============================================================================
# STOP_APPROACH modunda durma sebebini belirtir.
# FSM, Planner ve Controller tarafından ortak kullanılır.
# =============================================================================

uint8 STOP_NONE=0
uint8 STOP_RED_LIGHT=1
uint8 STOP_STOP_SIGN=2
uint8 STOP_OBSTACLE_TTC=3
uint8 STOP_LOCALIZATION_LOST=4
uint8 STOP_STALE_SENSOR=5
uint8 STOP_MISSION_ABORT=6
uint8 STOP_PEDESTRIAN=7

uint8 reason
