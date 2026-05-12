# planning_msgs/Trajectory.msg
# =============================================================================
# Planner → Controller yörünge mesajı
# Topic: /planning/trajectory — 20Hz — map frame
#
# Timeout kuralı (Yol Haritası v1.1):
#   0-500ms   → normal
#   500-1000ms → hız %50 düşür
#   >1000ms   → TAM FREN
# =============================================================================

std_msgs/Header header        # Zaman damgası + frame_id="map"

TrajectoryPoint[] points      # Yörünge noktaları listesi (en az 5 nokta beklenir)

uint8 planner_mode            # Mevcut mod — common_msgs/AutonomyMode sabitlerini kullan
uint32 valid_until_ms         # Geçerlilik süresi (ms) — varsayılan 200ms
uint32 age_ms                 # Mesajın yaşı (ms) — üretildiğinden bu yana
string[] warning_flags        # Uyarı mesajları
