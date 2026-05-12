# localization_msgs/RawGps.msg
# =============================================================================
# GPS → debug/rosbag
# Topic: /localization/raw_gps — 10 Hz
#
# PLANNER BU MESAJI OKUMAZ.
# Sadece debug, rosbag ve localization health için kullanılır.
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

float64 latitude
float64 longitude
float64 altitude

float64 speed
float64 heading_deg

float64 hdop
float64 vdop

uint8 FIX_NONE=0
uint8 FIX_GPS=1
uint8 FIX_DGPS=2
uint8 FIX_RTK_FLOAT=4
uint8 FIX_RTK_FIXED=5

uint8 fix_type