# perception_msgs/TrafficSigns.msg
# =============================================================================
# Perception → FSM/Planner trafik tabelaları listesi
# Topic: /perception/traffic_signs — 10-30Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms
TrafficSign[] signs
string[] warning_flags
