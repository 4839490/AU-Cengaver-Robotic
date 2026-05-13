# perception_msgs/msg/TrafficLightState.msg
# Topic: /perception/traffic_light_state | 10-30 Hz | frame_id: base_link | valid_until_ms: 300

uint8 UNKNOWN=0
uint8 RED=1
uint8 YELLOW=2
uint8 GREEN=3
uint8 STALE=4
uint8 CONFLICT=5

std_msgs/Header header
uint8   state
float32 confidence
bool    relevant_to_route
float32 distance_to_stop
bool    confirmed
bool    in_stop_zone
float32 bbox_x
float32 bbox_y
float32 bbox_w
float32 bbox_h
uint32  age_ms
uint32  valid_until_ms
string  source_sensor
string[] warning_flags
