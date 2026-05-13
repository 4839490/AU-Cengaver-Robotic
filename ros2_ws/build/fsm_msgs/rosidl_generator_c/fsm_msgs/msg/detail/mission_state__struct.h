// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_H_
#define FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_H_

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
  fsm_msgs__msg__MissionState__PICKUP = 0
};

/// Constant 'DROPOFF'.
enum
{
  fsm_msgs__msg__MissionState__DROPOFF = 1
};

/// Constant 'WAYPOINT'.
enum
{
  fsm_msgs__msg__MissionState__WAYPOINT = 2
};

/// Constant 'PARK_ENTRY'.
enum
{
  fsm_msgs__msg__MissionState__PARK_ENTRY = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/MissionState in the package fsm_msgs.
typedef struct fsm_msgs__msg__MissionState
{
  std_msgs__msg__Header header;
  bool mission_active;
  uint8_t total_waypoints;
  uint8_t completed_waypoints;
  uint32_t current_waypoint_id;
  uint8_t current_waypoint_type;
  uint32_t next_waypoint_id;
  uint8_t next_waypoint_type;
  bool pickup_complete;
  bool dropoff_complete;
  uint32_t age_ms;
  uint32_t valid_until_ms;
} fsm_msgs__msg__MissionState;

// Struct for a sequence of fsm_msgs__msg__MissionState.
typedef struct fsm_msgs__msg__MissionState__Sequence
{
  fsm_msgs__msg__MissionState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} fsm_msgs__msg__MissionState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_H_
