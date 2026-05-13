# perception_msgs/msg/ObstacleTrack.msg
# Nested element of /perception/obstacle_tracks. NO own header; uses parent header.
# NO `in_path` field — path-membership is computed planner-side.

uint8 UNKNOWN_OBSTACLE=0
uint8 VEHICLE=1
uint8 PEDESTRIAN=2
uint8 CONE=3
uint8 BARRIER=4
uint8 SIGN_POLE=5

uint32  track_id
uint8   class_label
float32 confidence
float32 position_x
float32 position_y
float32 distance
float32 velocity_x
float32 velocity_y
float32 ttc
float32 width
float32 length
float32 height
bool    is_static
string  source_sensor
string  semantic_source
string  geometry_source
uint32  age_ms
uint32  valid_until_ms
string[] warning_flags
