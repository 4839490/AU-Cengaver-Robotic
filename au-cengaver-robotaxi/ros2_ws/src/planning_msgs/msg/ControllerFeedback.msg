# planning_msgs/ControllerFeedback.msg
# =============================================================================
# Controller → Planner geri bildirim
# Topic: /controller/feedback — 20Hz
#
# ⚠️ 200ms içinde gelmezse planner status=EMERGENCY yayınlar
#
# Planner kullanım kuralları:
#   cross_track_error > 0.3m  → trajectory yeniden hesapla
#   cross_track_error > 0.5m  → şerit kaybı uyarısı, hız düşür
#   heading_error > 0.2 rad   → yönelim önceliklendir
#   full_brake_active = true  → yeni trajectory üretmeyi beklet
#   actual_speed → ActiveRouteContext.ego_speed_mps olarak iletilir
# =============================================================================

std_msgs/Header header

float32 actual_speed
float32 actual_steering_deg
float32 cross_track_error
float32 heading_error
bool brake_active
bool full_brake_active

uint32 valid_until_ms