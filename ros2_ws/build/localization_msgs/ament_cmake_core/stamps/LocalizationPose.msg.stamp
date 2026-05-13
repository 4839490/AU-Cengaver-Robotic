# localization_msgs/LocalizationPose.msg
# =============================================================================
# Localization → Planner/FSM konum bilgisi
# Topic: /localization/pose — 30-50 Hz — map frame (ENU)
#
# ENU yaw standardı:
# yaw=0 → +x / Doğu
# yaw=pi/2 → +y / Kuzey
# yaw pozitif → CCW
# yaw aralığı → [-pi, pi]
# =============================================================================

uint8 SOURCE_GPS_IMU_LIDAR=0
uint8 SOURCE_IMU_LIDAR=1
uint8 SOURCE_IMU_ONLY=2
uint8 SOURCE_LIDAR_ONLY=3
uint8 SOURCE_DEAD_RECKONING=4

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

float64 x
float64 y
float64 yaw

float64 linear_velocity
float64 angular_velocity

uint8 source

float64 localization_confidence
float64 position_covariance
float64 heading_covariance
float64 velocity_covariance

string[] warning_flags