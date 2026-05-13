// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from common_msgs:msg/AutonomyMode.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_H_
#define COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'LANE_FOLLOW'.
enum
{
  common_msgs__msg__AutonomyMode__LANE_FOLLOW = 0
};

/// Constant 'STOP_APPROACH'.
enum
{
  common_msgs__msg__AutonomyMode__STOP_APPROACH = 1
};

/// Constant 'PICKUP_APPROACH'.
enum
{
  common_msgs__msg__AutonomyMode__PICKUP_APPROACH = 2
};

/// Constant 'DROPOFF_APPROACH'.
enum
{
  common_msgs__msg__AutonomyMode__DROPOFF_APPROACH = 3
};

/// Constant 'OBSTACLE_AVOID'.
enum
{
  common_msgs__msg__AutonomyMode__OBSTACLE_AVOID = 4
};

/// Constant 'PARK_APPROACH'.
enum
{
  common_msgs__msg__AutonomyMode__PARK_APPROACH = 5
};

/// Constant 'PARK_MANEUVER'.
enum
{
  common_msgs__msg__AutonomyMode__PARK_MANEUVER = 6
};

/// Constant 'MISSION_COMPLETE'.
enum
{
  common_msgs__msg__AutonomyMode__MISSION_COMPLETE = 7
};

// Struct defined in msg/AutonomyMode in the package common_msgs.
typedef struct common_msgs__msg__AutonomyMode
{
  uint8_t mode;
} common_msgs__msg__AutonomyMode;

// Struct for a sequence of common_msgs__msg__AutonomyMode.
typedef struct common_msgs__msg__AutonomyMode__Sequence
{
  common_msgs__msg__AutonomyMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} common_msgs__msg__AutonomyMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_H_
