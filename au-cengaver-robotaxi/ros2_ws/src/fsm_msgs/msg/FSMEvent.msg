# fsm_msgs/FSMEvent.msg
# =============================================================================
# FSM → Planner  |  olay bildirimleri
# Topic: /fsm/event — event-driven  |  valid_until: 500 ms
# Contract: FSM↔Planner v1.1
#
# EMERGENCY_STOP_REQUEST → yazılımsal tam fren isteği
# AUTONOMOUS_EMERGENCY   → donanımsal güç kesme — safety supervisor sorumluluğu
# =============================================================================

# --- Event type constants ---
uint8 PICKUP_COMPLETE=0
uint8 DROPOFF_COMPLETE=1
uint8 OBSTACLE_CLEARED=2
uint8 REPLANNING_REQUEST=3
uint8 MISSION_ABORT=4
uint8 RESUME=5
uint8 PARK_SLOT_CHANGE=6
uint8 EMERGENCY_STOP_REQUEST=7

# --- Fields ---
std_msgs/Header header

uint8   event_type
uint32  waypoint_id  # ilgili waypoint ID (varsa)
string  data         # ek bilgi — debug (ör: 'new_slot_id:3')

uint32  age_ms
