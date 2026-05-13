# perception_msgs/msg/Junction.msg
# Topic: /perception/junction | 10 Hz | frame_id: base_link | valid_until_ms: 500
# OPTIONAL in MVP — when not published, planner uses active_route_context.route_direction.

uint8 NORMAL=0
uint8 ROUNDABOUT=1

std_msgs/Header header
bool    detected
uint8   junction_type
uint8   arm_count
float32 distance_to_entry
float32 confidence
uint32  age_ms
uint32  valid_until_ms
string  source_sensor
string[] warning_flags
