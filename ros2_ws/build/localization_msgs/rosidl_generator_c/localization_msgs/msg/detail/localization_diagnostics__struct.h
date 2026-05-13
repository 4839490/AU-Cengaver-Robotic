// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from localization_msgs:msg/LocalizationDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/LocalizationDiagnostics in the package localization_msgs.
typedef struct localization_msgs__msg__LocalizationDiagnostics
{
  std_msgs__msg__Header header;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  double ekf_output_hz;
  double gps_input_hz;
  double imu_input_hz;
  double ndt_output_hz;
  double ekf_latency_ms;
  double ndt_latency_ms;
  double position_covariance;
  double heading_covariance;
  double ndt_quality;
  bool ekf_healthy;
  bool gps_healthy;
  bool imu_healthy;
  bool ndt_healthy;
  bool map_odom_stable;
  rosidl_runtime_c__String__Sequence warning_flags;
} localization_msgs__msg__LocalizationDiagnostics;

// Struct for a sequence of localization_msgs__msg__LocalizationDiagnostics.
typedef struct localization_msgs__msg__LocalizationDiagnostics__Sequence
{
  localization_msgs__msg__LocalizationDiagnostics * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} localization_msgs__msg__LocalizationDiagnostics__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_H_
