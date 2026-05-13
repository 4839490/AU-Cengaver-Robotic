// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from localization_msgs:msg/LocalizationOdometry.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_H_

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

// Struct defined in msg/LocalizationOdometry in the package localization_msgs.
typedef struct localization_msgs__msg__LocalizationOdometry
{
  std_msgs__msg__Header header;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  double x;
  double y;
  double yaw;
  double linear_velocity;
  double angular_velocity;
  double position_covariance;
  double heading_covariance;
  double velocity_covariance;
  rosidl_runtime_c__String__Sequence warning_flags;
} localization_msgs__msg__LocalizationOdometry;

// Struct for a sequence of localization_msgs__msg__LocalizationOdometry.
typedef struct localization_msgs__msg__LocalizationOdometry__Sequence
{
  localization_msgs__msg__LocalizationOdometry * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} localization_msgs__msg__LocalizationOdometry__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_H_
