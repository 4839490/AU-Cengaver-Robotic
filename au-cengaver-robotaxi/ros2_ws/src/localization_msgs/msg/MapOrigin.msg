# localization_msgs/MapOrigin.msg
# =============================================================================
# map_origin_publisher → Planner harita referans noktası
# Topic: /localization/map_origin — TRANSIENT_LOCAL QoS
#
# locked=false iken planner waypoint işlemez.
# =============================================================================

std_msgs/Header header

float64 lat_ref
float64 lon_ref
float64 alt_ref
float64 yaw_ref

bool locked