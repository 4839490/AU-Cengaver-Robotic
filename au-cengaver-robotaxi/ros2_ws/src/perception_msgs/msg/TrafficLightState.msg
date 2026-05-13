# perception_msgs/TrafficLightState.msg
# =============================================================================
# Perception → FSM trafik ışığı durumu
# Topic: /perception/traffic_light_state — 10-30Hz
#
# FSM kuralı: confirmed=true VE relevant_to_route=true zorunlu
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms
uint8 STATE_RED=0
uint8 STATE_YELLOW=1
uint8 STATE_GREEN=2
uint8 STATE_STALE=3
uint8 state
float64 confidence
bool relevant_to_route
bool confirmed
bool in_stop_zone
string[] warning_flags
