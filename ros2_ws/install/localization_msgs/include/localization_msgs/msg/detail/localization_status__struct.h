// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'OK'.
enum
{
  localization_msgs__msg__LocalizationStatus__OK = 0
};

/// Constant 'GNSS_LOST'.
enum
{
  localization_msgs__msg__LocalizationStatus__GNSS_LOST = 1
};

/// Constant 'IMU_ONLY'.
enum
{
  localization_msgs__msg__LocalizationStatus__IMU_ONLY = 2
};

/// Constant 'LIDAR_ONLY'.
enum
{
  localization_msgs__msg__LocalizationStatus__LIDAR_ONLY = 3
};

/// Constant 'DEGRADED'.
enum
{
  localization_msgs__msg__LocalizationStatus__DEGRADED = 4
};

/// Constant 'RELOCALIZING'.
enum
{
  localization_msgs__msg__LocalizationStatus__RELOCALIZING = 5
};

/// Constant 'LOST'.
enum
{
  localization_msgs__msg__LocalizationStatus__LOST = 6
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/LocalizationStatus in the package localization_msgs.
typedef struct localization_msgs__msg__LocalizationStatus
{
  std_msgs__msg__Header header;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  uint8_t status;
  double localization_confidence;
  double position_covariance;
  double heading_covariance;
  bool ndt_healthy;
  double ndt_quality;
  bool map_odom_stable;
  double map_odom_drift;
  bool gps_available;
  bool imu_available;
  bool lidar_available;
  rosidl_runtime_c__String__Sequence warning_flags;
} localization_msgs__msg__LocalizationStatus;

// Struct for a sequence of localization_msgs__msg__LocalizationStatus.
typedef struct localization_msgs__msg__LocalizationStatus__Sequence
{
  localization_msgs__msg__LocalizationStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} localization_msgs__msg__LocalizationStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_H_
