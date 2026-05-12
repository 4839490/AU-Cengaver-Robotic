# controller_msgs/ControllerFeedback.msg
# =============================================================================
# AU Cengaver Robotics — TEKNOFEST 2026
# Controller → Planner geri bildirim
# Topic: /controller/feedback — 20Hz
# Sorumlu: Muhammed Durmaz
#
# Sözleşme: Planner↔Controller v1.2, Bölüm 6.3
#
# ⚠️ 200ms içinde gelmezse → planner status=EMERGENCY yayınlar
# ⚠️ actual_speed → ActiveRouteContext.ego_speed_mps olarak iletilir (TTC için)
#
# Planner kullanım kuralları:
#   cross_track_error > 0.3m  → trajectory yeniden hesapla
#   cross_track_error > 0.5m  → şerit kaybı uyarısı, hız düşür
#   heading_error > 0.2 rad   → yönelim önceliklendir
#   full_brake_active = true  → yeni trajectory üretmeyi beklet
# =============================================================================

std_msgs/Header header

# ── Araç Durumu ───────────────────────────────────────────────────────────────
float32 actual_speed            # Gerçek hız (m/s) — odometri/encoder
float32 actual_steering_deg     # Gerçek direksiyon açısı (derece)
                                # CAN steering_center_byte offset uygulanmış fiziksel değer

# ── Hata Değerleri ────────────────────────────────────────────────────────────
float32 cross_track_error       # Trajectory'den yanal sapma (m)
                                # + = sola sapma | - = sağa sapma

float32 heading_error           # Hedef yönden açısal sapma (radyan)
                                # + = sola bakıyor | - = sağa bakıyor

# ── Fren Durumu ───────────────────────────────────────────────────────────────
bool    brake_active            # Fren komutu aktif mi?
bool    full_brake_active       # Tam fren (emergency) aktif mi?

# ── Zaman ─────────────────────────────────────────────────────────────────────
uint32  age_ms                  # Mesajın yaşı (ms)                   ← [DÜZELTİLDİ] eklendi
uint32  valid_until_ms          # Geçerlilik süresi = 200ms
                                # Aşılırsa planner status=EMERGENCY yayınlar
