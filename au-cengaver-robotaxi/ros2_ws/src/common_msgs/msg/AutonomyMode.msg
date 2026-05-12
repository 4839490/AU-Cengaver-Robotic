# common_msgs/AutonomyMode.msg
# =============================================================================
# AU Cengaver Robotics — TEKNOFEST 2026
# TEK MOD ENUM — FSM, Planning, Controller tarafından kullanılır
#
# PlannerMode.msg ve FSMMode.msg YOKTUR.
# JUNCTION ve TUNNEL mod değildir — TargetSpeed.reason olarak kullanılır.
# =============================================================================

uint8 LANE_FOLLOW=0
uint8 STOP_APPROACH=1
uint8 PICKUP_APPROACH=2
uint8 DROPOFF_APPROACH=3
uint8 OBSTACLE_AVOID=4
uint8 PARK_APPROACH=5
uint8 PARK_MANEUVER=6
uint8 MISSION_COMPLETE=7

uint8 mode
