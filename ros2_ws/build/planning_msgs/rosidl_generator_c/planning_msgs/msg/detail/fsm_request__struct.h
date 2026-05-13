// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/FSMRequest.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'MODE_CHANGE'.
enum
{
  planning_msgs__msg__FSMRequest__MODE_CHANGE = 0
};

/// Constant 'REPLANNING_NEEDED'.
enum
{
  planning_msgs__msg__FSMRequest__REPLANNING_NEEDED = 1
};

/// Constant 'GOAL_CONFIRMED'.
enum
{
  planning_msgs__msg__FSMRequest__GOAL_CONFIRMED = 2
};

/// Constant 'OBSTACLE_BLOCKED'.
enum
{
  planning_msgs__msg__FSMRequest__OBSTACLE_BLOCKED = 3
};

/// Constant 'LOCALIZATION_DEGRADED'.
enum
{
  planning_msgs__msg__FSMRequest__LOCALIZATION_DEGRADED = 4
};

/// Constant 'PARK_READY'.
enum
{
  planning_msgs__msg__FSMRequest__PARK_READY = 5
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'reason'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/FSMRequest in the package planning_msgs.
typedef struct planning_msgs__msg__FSMRequest
{
  std_msgs__msg__Header header;
  uint8_t request_type;
  uint8_t requested_mode;
  uint32_t waypoint_id;
  rosidl_runtime_c__String reason;
  uint32_t age_ms;
  uint32_t valid_until_ms;
} planning_msgs__msg__FSMRequest;

// Struct for a sequence of planning_msgs__msg__FSMRequest.
typedef struct planning_msgs__msg__FSMRequest__Sequence
{
  planning_msgs__msg__FSMRequest * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__FSMRequest__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_H_
