# perception_msgs/LaneModel.msg
# =============================================================================
# Perception → Planner şerit modeli
# Topic: /perception/lane_model — 20-30Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms
float64[] centerline        # Merkez çizgi noktaları [x0,y0,x1,y1,...]
float64[] left_boundary     # Sol sınır noktaları
float64[] right_boundary    # Sağ sınır noktaları
float64 lane_confidence     # 0.0-1.0
bool lane_lost              # Şerit kaybı var mı?
float64 curvature           # Yol eğriliği (1/metre)
string[] warning_flags
