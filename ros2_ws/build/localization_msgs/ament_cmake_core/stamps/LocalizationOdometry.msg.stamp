# localization_msgs/LocalizationOdometry.msg
# =============================================================================
# local_ekf_node → Planner/Controller odometri
# Topic: /localization/odometry — 50 Hz
# Frame: odom
# TF: odom → base_link
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

float64 x
float64 y
float64 yaw

float64 linear_velocity
float64 angular_velocity

float64 position_covariance
float64 heading_covariance
float64 velocity_covariance

string[] warning_flags