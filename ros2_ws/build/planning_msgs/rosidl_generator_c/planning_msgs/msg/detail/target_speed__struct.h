// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/TargetSpeed.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'REASON_LANE_FOLLOW'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_LANE_FOLLOW = 0
};

/// Constant 'REASON_APPROACH_STOP'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_APPROACH_STOP = 1
};

/// Constant 'REASON_PICKUP_DROPOFF'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_PICKUP_DROPOFF = 2
};

/// Constant 'REASON_OBSTACLE_SLOW'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_OBSTACLE_SLOW = 3
};

/// Constant 'REASON_JUNCTION'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_JUNCTION = 4
};

/// Constant 'REASON_TUNNEL'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_TUNNEL = 5
};

/// Constant 'REASON_PARK_APPROACH'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_PARK_APPROACH = 6
};

/// Constant 'REASON_PARK_MANEUVER'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_PARK_MANEUVER = 7
};

/// Constant 'REASON_EMERGENCY_STOP'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_EMERGENCY_STOP = 8
};

/// Constant 'REASON_LOCALIZATION_DEGRADED'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_LOCALIZATION_DEGRADED = 9
};

/// Constant 'REASON_LANE_LOST'.
enum
{
  planning_msgs__msg__TargetSpeed__REASON_LANE_LOST = 10
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/TargetSpeed in the package planning_msgs.
typedef struct planning_msgs__msg__TargetSpeed
{
  std_msgs__msg__Header header;
  float speed;
  float jerk_limit;
  uint8_t reason;
  uint32_t valid_until_ms;
  uint32_t age_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__TargetSpeed;

// Struct for a sequence of planning_msgs__msg__TargetSpeed.
typedef struct planning_msgs__msg__TargetSpeed__Sequence
{
  planning_msgs__msg__TargetSpeed * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__TargetSpeed__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_H_
