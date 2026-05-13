# perception_msgs/msg/StopTarget.msg
# Topic: /perception/stop_target | 10-20 Hz | frame_id: base_link | valid_until_ms: 300
# Per contract §15 raw .msg block: NO warning_flags field.

uint8 TRAFFIC_LIGHT_STOP=0
uint8 STOP_SIGN=1
uint8 PICKUP=2
uint8 DROPOFF=3

uint8 LOW=0
uint8 NORMAL=1
uint8 HIGH=2
uint8 CRITICAL=3

std_msgs/Header header
uint8   target_type
float32 distance_from_front_bumper
float32 target_x
float32 target_y
float32 confidence
string  source
uint32  age_ms
uint32  valid_until_ms
int32   waypoint_id
float32 heading_at_stop
uint8   priority
uint32  required_stop_duration_ms
uint32  stop_reason_id
string  source_topic
