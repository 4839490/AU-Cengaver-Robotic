# localization_msgs/LocalizationDiagnostics.msg
# =============================================================================
# Localization → izleme/debug diagnostik bilgisi
# Topic: /localization/diagnostics — 1-2 Hz
# =============================================================================

std_msgs/Header header
uint32 age_ms
uint32 valid_until_ms

float64 ekf_output_hz
float64 gps_input_hz
float64 imu_input_hz
float64 ndt_output_hz

float64 ekf_latency_ms
float64 ndt_latency_ms

float64 position_covariance
float64 heading_covariance
float64 ndt_quality

bool ekf_healthy
bool gps_healthy
bool imu_healthy
bool ndt_healthy
bool map_odom_stable

string[] warning_flags