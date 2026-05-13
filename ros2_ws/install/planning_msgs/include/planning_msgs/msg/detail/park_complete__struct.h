// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/ParkComplete.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_H_

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

// Struct defined in msg/ParkComplete in the package planning_msgs.
typedef struct planning_msgs__msg__ParkComplete
{
  std_msgs__msg__Header header;
  bool success;
  float final_cross_track_error;
  float final_heading_error;
  uint8_t iterations_used;
  uint32_t waypoint_id;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__ParkComplete;

// Struct for a sequence of planning_msgs__msg__ParkComplete.
typedef struct planning_msgs__msg__ParkComplete__Sequence
{
  planning_msgs__msg__ParkComplete * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__ParkComplete__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_H_
