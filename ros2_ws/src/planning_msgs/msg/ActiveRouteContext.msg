# planning_msgs/ActiveRouteContext.msg

std_msgs/Header header          # frame_id="base_link"

uint32  active_waypoint_id

float32 target_x
float32 target_y
float32 target_heading

uint8   planner_mode
string  route_direction         # STRAIGHT | LEFT | RIGHT | ROUNDABOUT | UNKNOWN

geometry_msgs/Point[] planned_trajectory

float32 lookahead_distance

bool    in_stop_zone
float32 distance_to_stop_zone

float32 localization_confidence
float32 ego_speed_mps

bool    route_context_valid

uint32  age_ms
uint32  valid_until_ms
string[] warning_flags
