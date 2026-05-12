# localization_msgs/LocalizationStatus.msg
# =============================================================================
# Localization → FSM/Planner/Safety sağlık durumu
# Topic: /localization/status — 10 Hz
# =============================================================================

uint8 OK=0
uint8 GNSS_LOST=1
uint8 IMU_ONLY=2
uint8 LIDAR_ONLY=3
uint8 DEGRADED=4
uint8 RELOCALIZING=5
uint8 LOST=6

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

uint8 status

float64 localization_confidence
float64 position_covariance
float64 heading_covariance

bool ndt_healthy
float64 ndt_quality

bool map_odom_stable
float64 map_odom_drift

bool gps_available
bool imu_available
bool lidar_available

string[] warning_flags