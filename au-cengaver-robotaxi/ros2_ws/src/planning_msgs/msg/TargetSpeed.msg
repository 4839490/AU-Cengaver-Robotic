# planning_msgs/TargetSpeed.msg
# =============================================================================
# Planner → Controller güvenlik hızı
# Topic: /planning/target_speed — 20Hz
#
# Hız öncelik kuralı (Sözleşme v1.2 FIX-5):
#   final_speed = min(target_speed.speed, trajectory_point.speed)
#
# reason sabitleri:
#   0 = LANE_FOLLOW     → normal sürüş
#   1 = APPROACH_STOP   → dur noktasına yaklaşım
#   2 = PICKUP_DROPOFF  → yolcu işlemi (max 3 km/h)
#   3 = OBSTACLE_SLOW   → engel yavaşlaması
#   4 = JUNCTION        → kavşak (mod değil, reason!)
#   5 = TUNNEL          → tünel (mod değil, reason!)
#   6 = PARK_APPROACH   → park yaklaşımı
#   7 = PARK_MANEUVER   → park manevrası (max 3 km/h)
#   8 = EMERGENCY_STOP  → yazılımsal tam fren (güç kesilmez)
# =============================================================================

std_msgs/Header header   # Zaman damgası

float32 speed            # Güvenlik hız limiti (m/s) — 0.0=dur
float32 jerk_limit       # Hız geçişi yumuşatma (m/s³)
                         #   Normal: 2.0 | Park: 1.0 | Acil: 10.0
uint8   reason           # Neden bu hız? (yukarıdaki sabitler)
uint32  valid_until_ms   # Geçerlilik süresi (ms) — varsayılan 200ms
uint32  age_ms           # Mesajın yaşı (ms)
string[] warning_flags   # Uyarı mesajları

# reason sabitleri
uint8 REASON_LANE_FOLLOW    = 0
uint8 REASON_APPROACH_STOP  = 1
uint8 REASON_PICKUP_DROPOFF = 2
uint8 REASON_OBSTACLE_SLOW  = 3
uint8 REASON_JUNCTION       = 4
uint8 REASON_TUNNEL         = 5
uint8 REASON_PARK_APPROACH  = 6
uint8 REASON_PARK_MANEUVER  = 7
uint8 REASON_EMERGENCY_STOP = 8
