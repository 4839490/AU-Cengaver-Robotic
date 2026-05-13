// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_H_

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
// Member 'route_direction'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"
// Member 'planned_trajectory'
#include "geometry_msgs/msg/detail/point__struct.h"

// Struct defined in msg/ActiveRouteContext in the package planning_msgs.
typedef struct planning_msgs__msg__ActiveRouteContext
{
  std_msgs__msg__Header header;
  uint32_t active_waypoint_id;
  float target_x;
  float target_y;
  float target_heading;
  uint8_t planner_mode;
  rosidl_runtime_c__String route_direction;
  geometry_msgs__msg__Point__Sequence planned_trajectory;
  float lookahead_distance;
  bool in_stop_zone;
  float distance_to_stop_zone;
  float localization_confidence;
  float ego_speed_mps;
  bool route_context_valid;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__ActiveRouteContext;

// Struct for a sequence of planning_msgs__msg__ActiveRouteContext.
typedef struct planning_msgs__msg__ActiveRouteContext__Sequence
{
  planning_msgs__msg__ActiveRouteContext * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__ActiveRouteContext__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_H_
