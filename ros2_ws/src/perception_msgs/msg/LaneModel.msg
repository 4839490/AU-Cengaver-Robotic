# perception_msgs/msg/LaneModel.msg
# Topic: /perception/lane_model | 20-30 Hz | frame_id: base_link | valid_until_ms: 500

std_msgs/Header header
geometry_msgs/Point[] centerline
geometry_msgs/Point[] left_boundary
geometry_msgs/Point[] right_boundary
float32 lane_confidence
bool    lane_lost
float32 curvature
float32 lane_width_estimate
uint32  age_ms
uint32  valid_until_ms
string  source_sensor
string[] warning_flags
