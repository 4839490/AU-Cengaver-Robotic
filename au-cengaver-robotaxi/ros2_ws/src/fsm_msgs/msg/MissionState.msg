# fsm_msgs/MissionState.msg
# =============================================================================
# FSM → Planner  |  görev durumu
# Topic: /fsm/mission_state — 5 Hz  |  valid_until: 1000 ms
# Contract: FSM↔Planner v1.1
# =============================================================================

# --- Waypoint type constants ---
uint8 PICKUP=0
uint8 DROPOFF=1
uint8 WAYPOINT=2
uint8 PARK_ENTRY=3

# --- Fields ---
std_msgs/Header header

bool    mission_active

uint8   total_waypoints       # toplam waypoint sayısı
uint8   completed_waypoints   # tamamlanan waypoint sayısı

uint32  current_waypoint_id   # aktif GeoJSON nokta ID'si
uint8   current_waypoint_type # waypoint type constant

uint32  next_waypoint_id      # sonraki waypoint ID — planner önceden hazırlanabilir
uint8   next_waypoint_type    # sonraki waypoint type constant

bool    pickup_complete       # aktif PICKUP tamamlandı sinyali
bool    dropoff_complete      # aktif DROPOFF tamamlandı sinyali

uint32  age_ms
uint32  valid_until_ms        # 1000 ms
