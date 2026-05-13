// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fsm_msgs:msg/CurrentMode.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_H_
#define FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_H_

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
  fsm_msgs__msg__CurrentMode__LANE_FOLLOW = 0
};

/// Constant 'STOP_APPROACH'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_APPROACH = 1
};

/// Constant 'PICKUP_APPROACH'.
enum
{
  fsm_msgs__msg__CurrentMode__PICKUP_APPROACH = 2
};

/// Constant 'DROPOFF_APPROACH'.
enum
{
  fsm_msgs__msg__CurrentMode__DROPOFF_APPROACH = 3
};

/// Constant 'OBSTACLE_AVOID'.
enum
{
  fsm_msgs__msg__CurrentMode__OBSTACLE_AVOID = 4
};

/// Constant 'PARK_APPROACH'.
enum
{
  fsm_msgs__msg__CurrentMode__PARK_APPROACH = 5
};

/// Constant 'PARK_MANEUVER'.
enum
{
  fsm_msgs__msg__CurrentMode__PARK_MANEUVER = 6
};

/// Constant 'MISSION_COMPLETE'.
enum
{
  fsm_msgs__msg__CurrentMode__MISSION_COMPLETE = 7
};

/// Constant 'STOP_NONE'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_NONE = 0
};

/// Constant 'STOP_RED_LIGHT'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_RED_LIGHT = 1
};

/// Constant 'STOP_STOP_SIGN'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_STOP_SIGN = 2
};

/// Constant 'STOP_OBSTACLE_TTC'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_OBSTACLE_TTC = 3
};

/// Constant 'STOP_LOCALIZATION_LOST'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_LOCALIZATION_LOST = 4
};

/// Constant 'STOP_STALE_SENSOR'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_STALE_SENSOR = 5
};

/// Constant 'STOP_MISSION_ABORT'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_MISSION_ABORT = 6
};

/// Constant 'STOP_PEDESTRIAN'.
enum
{
  fsm_msgs__msg__CurrentMode__STOP_PEDESTRIAN = 7
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'reason'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/CurrentMode in the package fsm_msgs.
typedef struct fsm_msgs__msg__CurrentMode
{
  std_msgs__msg__Header header;
  uint8_t mode;
  uint8_t previous_mode;
  rosidl_runtime_c__String reason;
  uint8_t stop_reason;
  uint32_t waypoint_id;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} fsm_msgs__msg__CurrentMode;

// Struct for a sequence of fsm_msgs__msg__CurrentMode.
typedef struct fsm_msgs__msg__CurrentMode__Sequence
{
  fsm_msgs__msg__CurrentMode * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fsm_msgs__msg__CurrentMode__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_H_
