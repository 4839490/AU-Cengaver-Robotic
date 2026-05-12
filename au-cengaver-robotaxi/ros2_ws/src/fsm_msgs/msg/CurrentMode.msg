# fsm_msgs/CurrentMode.msg
# =============================================================================
# FSM → Planner / Controller / Perception  |  mevcut mod bilgisi
# Topic: /fsm/current_mode — 10 Hz  |  valid_until: 500 ms
# Contract: FSM↔Planner v1.1
# =============================================================================

# --- Mode constants (common_msgs/AutonomyMode ile aynı) ---
uint8 LANE_FOLLOW=0
uint8 STOP_APPROACH=1
uint8 PICKUP_APPROACH=2
uint8 DROPOFF_APPROACH=3
uint8 OBSTACLE_AVOID=4
uint8 PARK_APPROACH=5
uint8 PARK_MANEUVER=6
uint8 MISSION_COMPLETE=7

# --- stop_reason constants (STOP_APPROACH modunda geçerli) ---
uint8 STOP_NONE=0
uint8 STOP_RED_LIGHT=1
uint8 STOP_STOP_SIGN=2
uint8 STOP_OBSTACLE_TTC=3
uint8 STOP_LOCALIZATION_LOST=4
uint8 STOP_STALE_SENSOR=5
uint8 STOP_MISSION_ABORT=6
uint8 STOP_PEDESTRIAN=7

# --- Fields ---
std_msgs/Header header

uint8   mode           # AutonomyMode constant — aktif mod
uint8   previous_mode  # AutonomyMode constant — bir önceki mod

string  reason         # mod değişim nedeni (debug): "RED_LIGHT", "OBSTACLE_DETECTED" vb.

uint8   stop_reason    # STOP_APPROACH modunda geçerli — diğer modlarda STOP_NONE=0

uint32  waypoint_id    # aktif GeoJSON nokta ID'si

uint32  age_ms
uint32  valid_until_ms # 500 ms

string[] warning_flags # TRANSITION_FAILED | UNKNOWN_MODE | TIMEOUT
