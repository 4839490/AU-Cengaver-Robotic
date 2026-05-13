// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/Trajectory.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_H_

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
// Member 'points'
#include "planning_msgs/msg/detail/trajectory_point__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/Trajectory in the package planning_msgs.
typedef struct planning_msgs__msg__Trajectory
{
  std_msgs__msg__Header header;
  planning_msgs__msg__TrajectoryPoint__Sequence points;
  uint8_t planner_mode;
  uint32_t valid_until_ms;
  uint32_t age_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__Trajectory;

// Struct for a sequence of planning_msgs__msg__Trajectory.
typedef struct planning_msgs__msg__Trajectory__Sequence
{
  planning_msgs__msg__Trajectory * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__Trajectory__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_H_
