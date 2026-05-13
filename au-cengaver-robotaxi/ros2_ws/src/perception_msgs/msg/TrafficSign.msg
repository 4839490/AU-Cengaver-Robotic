# perception_msgs/TrafficSign.msg
# =============================================================================
# Tek trafik tabelası — TrafficSigns.msg içinde kullanılır
# =============================================================================

string type           # "STOP", "SPEED_LIMIT", "PARKING", "YIELD" vb.
string event_status   # "DETECTED", "CONFIRMED", "CLEARED"
bool confirmed        # YOLOv8 teyit edildi mi?
float64 distance      # Tabelaya mesafe (metre)
float64 confidence    # 0.0-1.0
