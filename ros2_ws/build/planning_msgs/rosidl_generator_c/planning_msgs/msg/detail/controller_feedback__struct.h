// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_H_

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

// Struct defined in msg/ControllerFeedback in the package planning_msgs.
typedef struct planning_msgs__msg__ControllerFeedback
{
  std_msgs__msg__Header header;
  float actual_speed;
  float actual_steering_deg;
  float cross_track_error;
  float heading_error;
  bool brake_active;
  bool full_brake_active;
  uint32_t age_ms;
  uint32_t valid_until_ms;
} planning_msgs__msg__ControllerFeedback;

// Struct for a sequence of planning_msgs__msg__ControllerFeedback.
typedef struct planning_msgs__msg__ControllerFeedback__Sequence
{
  planning_msgs__msg__ControllerFeedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__ControllerFeedback__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_H_
