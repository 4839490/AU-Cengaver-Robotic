# perception_msgs/StopTarget.msg
# =============================================================================
# Perception → Planner dur noktası
# Topic: /perception/stop_target — 10-20Hz
# Kaynak: trafik ışığı + STOP tabela + PICKUP/DROPOFF birleşimi
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms
float64 stop_x      # Dur noktası x — base_link frame
float64 stop_y      # Dur noktası y — base_link frame
string reason       # "RED_LIGHT", "STOP_SIGN", "PICKUP", "DROPOFF"
float64 confidence  # 0.0-1.0
string[] warning_flags
