# common_msgs/AutonomyMode.msg
# =============================================================================
# AU Cengaver Robotics — TEKNOFEST 2026
# TEK MOD ENUM — tüm paketler bunu kullanır
#
# ⚠️ PlannerMode.msg ve FSMMode.msg YOKTUR
# ⚠️ JUNCTION ve TUNNEL mod değildir — TargetSpeed.reason olarak kullanılır
# =============================================================================

uint8 LANE_FOLLOW      = 0   # Normal şerit takibi
uint8 STOP_APPROACH    = 1   # Dur noktasına yaklaşım
uint8 PICKUP_APPROACH  = 2   # Yolcu alma yaklaşımı
uint8 DROPOFF_APPROACH = 3   # Yolcu bırakma yaklaşımı
uint8 OBSTACLE_AVOID   = 4   # Engel kaçınma
uint8 PARK_APPROACH    = 5   # Park yaklaşımı
uint8 PARK_MANEUVER    = 6   # Park manevrası (≤3 km/h)
uint8 MISSION_COMPLETE = 7   # Görev tamamlandı

uint8 mode             # Mevcut mod değeri
