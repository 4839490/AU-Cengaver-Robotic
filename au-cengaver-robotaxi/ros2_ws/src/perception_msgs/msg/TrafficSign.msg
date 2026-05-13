# perception_msgs/msg/TrafficSign.msg
# Nested element of /perception/traffic_signs. NO own header; uses parent header.

uint8 UNKNOWN_SIGN=0
uint8 STOP=1
uint8 SPEED_LIMIT=2
uint8 NO_ENTRY=3
uint8 MANDATORY_LEFT=4
uint8 MANDATORY_RIGHT=5
uint8 MANDATORY_STRAIGHT=6
uint8 MANDATORY_LEFT_STRAIGHT=7
uint8 MANDATORY_RIGHT_STRAIGHT=8
uint8 ROUNDABOUT=9
uint8 PARKING=10
uint8 NO_PARKING=11
uint8 TUNNEL=12
uint8 PEDESTRIAN_CROSSING=13

uint8 NEW=0
uint8 TRACKED=1
uint8 ALREADY_HANDLED=2
uint8 STALE=3

uint32  sign_id
uint8   type
float32 confidence
bool    relevant_to_route
float32 distance
uint8   event_status
bool    confirmed
float32 bbox_x
float32 bbox_y
float32 bbox_w
float32 bbox_h
uint32  age_ms
uint32  valid_until_ms
uint32  event_memory_ttl_ms
string  source_sensor
string[] warning_flags
