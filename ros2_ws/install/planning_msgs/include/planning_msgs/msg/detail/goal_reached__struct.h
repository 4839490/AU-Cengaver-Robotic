// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/GoalReached.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'PICKUP'.
enum
{
  planning_msgs__msg__GoalReached__PICKUP = 0
};

/// Constant 'DROPOFF'.
enum
{
  planning_msgs__msg__GoalReached__DROPOFF = 1
};

/// Constant 'WAYPOINT'.
enum
{
  planning_msgs__msg__GoalReached__WAYPOINT = 2
};

/// Constant 'PARK_ENTRY'.
enum
{
  planning_msgs__msg__GoalReached__PARK_ENTRY = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/GoalReached in the package planning_msgs.
typedef struct planning_msgs__msg__GoalReached
{
  std_msgs__msg__Header header;
  uint32_t waypoint_id;
  uint8_t waypoint_type;
  bool success;
  float distance_error;
  float heading_error;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__GoalReached;

// Struct for a sequence of planning_msgs__msg__GoalReached.
typedef struct planning_msgs__msg__GoalReached__Sequence
{
  planning_msgs__msg__GoalReached * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__GoalReached__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_H_
