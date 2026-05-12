# planning_msgs/ActiveRouteContext.msg
# =============================================================================
# Planner → Controller/Perception aktif rota bağlamı
# Topic: /planning/active_route_context — 10-20Hz — BASE_LINK frame
#
# ⚠️ Koordinatlar base_link frame'inde — map frame değil!
#    target_x/y: aracın önündeki hedef nokta (araç merkezine göre)
#
# ego_speed_mps TTC hesabı için zorunludur:
#   controller_feedback.actual_speed → bu alana kopyalanır
# =============================================================================

std_msgs/Header header          # frame_id="base_link"

float32 target_x                # Hedef nokta x — base_link frame (m)
float32 target_y                # Hedef nokta y — base_link frame (m)
uint8   planner_mode            # Mevcut mod — common_msgs/AutonomyMode
bool    in_stop_zone            # Dur bölgesinde miyiz?
float32 ego_speed_mps           # Araç hızı (m/s) — controller_feedback'ten gelir
bool    route_context_valid     # Bağlam geçerli mi?
                                # false = algıyı yoksaymak değil, konservatif davran

TrajectoryPoint[] planned_trajectory  # Planlanan kısa yörünge — base_link frame
                                      # Engel in_path hesabı için planner kullanır

uint32 age_ms                   # Mesajın yaşı (ms)
uint32 valid_until_ms           # Geçerlilik süresi (ms)
string[] warning_flags          # Uyarı mesajları
