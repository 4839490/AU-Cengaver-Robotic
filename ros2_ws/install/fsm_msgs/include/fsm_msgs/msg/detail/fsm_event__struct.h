// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_H_
#define FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'PICKUP_COMPLETE'.
enum
{
  fsm_msgs__msg__FSMEvent__PICKUP_COMPLETE = 0
};

/// Constant 'DROPOFF_COMPLETE'.
enum
{
  fsm_msgs__msg__FSMEvent__DROPOFF_COMPLETE = 1
};

/// Constant 'OBSTACLE_CLEARED'.
enum
{
  fsm_msgs__msg__FSMEvent__OBSTACLE_CLEARED = 2
};

/// Constant 'REPLANNING_REQUEST'.
enum
{
  fsm_msgs__msg__FSMEvent__REPLANNING_REQUEST = 3
};

/// Constant 'MISSION_ABORT'.
enum
{
  fsm_msgs__msg__FSMEvent__MISSION_ABORT = 4
};

/// Constant 'RESUME'.
enum
{
  fsm_msgs__msg__FSMEvent__RESUME = 5
};

/// Constant 'PARK_SLOT_CHANGE'.
enum
{
  fsm_msgs__msg__FSMEvent__PARK_SLOT_CHANGE = 6
};

/// Constant 'EMERGENCY_STOP_REQUEST'.
enum
{
  fsm_msgs__msg__FSMEvent__EMERGENCY_STOP_REQUEST = 7
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'data'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/FSMEvent in the package fsm_msgs.
typedef struct fsm_msgs__msg__FSMEvent
{
  std_msgs__msg__Header header;
  uint8_t event_type;
  uint32_t waypoint_id;
  rosidl_runtime_c__String data;
  uint32_t age_ms;
} fsm_msgs__msg__FSMEvent;

// Struct for a sequence of fsm_msgs__msg__FSMEvent.
typedef struct fsm_msgs__msg__FSMEvent__Sequence
{
  fsm_msgs__msg__FSMEvent * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fsm_msgs__msg__FSMEvent__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_H_
