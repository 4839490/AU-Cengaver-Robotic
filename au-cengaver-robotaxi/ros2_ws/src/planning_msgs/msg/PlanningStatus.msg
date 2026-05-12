# planning_msgs/PlanningStatus.msg
# =============================================================================
# Planner → Controller sağlık raporu
# Topic: /planning/status — 10Hz
#
# status sabitleri:
#   0 = ACTIVE               → normal çalışıyor
#   1 = WAITING_FSM          → FSM onayı bekliyor
#   2 = OBSTACLE_BLOCKED     → engel yolu bloke etti
#   3 = LANE_LOST            → şerit kaybı
#   4 = LOCALIZATION_DEGRADED → GPS/lokalizasyon zayıf
#   5 = EMERGENCY            → acil durum
#   6 = MISSION_COMPLETE     → görev tamamlandı
#
# Controller davranışları:
#   status=4 (LOCALIZATION_DEGRADED) → hızı %50 düşür
#   status=5 (EMERGENCY)             → TAM FREN
#   status=6 (MISSION_COMPLETE)      → dur + el freni
# =============================================================================

std_msgs/Header header          # Zaman damgası

uint8  status                   # Planner genel durumu (yukarıdaki sabitler)
bool   trajectory_valid         # Mevcut trajectory geçerli mi?
bool   goal_reached             # Hedefe ulaşıldı mı?
bool   parking_entry_reached    # Park girişine ulaşıldı mı?
bool   obstacle_blocking        # Engel yolu bloklıyor mu?
bool   lane_lost                # Şerit kaybı var mı?
bool   localization_degraded    # Lokalizasyon zayıf mı?
uint8  active_waypoint_id       # Şu an hangi waypoint hedefi
float32 distance_to_goal        # Hedefe kalan mesafe (m)
uint8  planner_mode             # Mevcut mod — common_msgs/AutonomyMode
uint32 age_ms                   # Mesajın yaşı (ms)
uint32 valid_until_ms           # Geçerlilik süresi (ms)
string[] warning_flags          # Uyarı mesajları

# status sabitleri
uint8 STATUS_ACTIVE               = 0
uint8 STATUS_WAITING_FSM          = 1
uint8 STATUS_OBSTACLE_BLOCKED     = 2
uint8 STATUS_LANE_LOST            = 3
uint8 STATUS_LOCALIZATION_DEGRADED = 4
uint8 STATUS_EMERGENCY            = 5
uint8 STATUS_MISSION_COMPLETE     = 6
