// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'UNKNOWN'.
enum
{
  perception_msgs__msg__TrafficLightState__UNKNOWN = 0
};

/// Constant 'RED'.
enum
{
  perception_msgs__msg__TrafficLightState__RED = 1
};

/// Constant 'YELLOW'.
enum
{
  perception_msgs__msg__TrafficLightState__YELLOW = 2
};

/// Constant 'GREEN'.
enum
{
  perception_msgs__msg__TrafficLightState__GREEN = 3
};

/// Constant 'STALE'.
enum
{
  perception_msgs__msg__TrafficLightState__STALE = 4
};

/// Constant 'CONFLICT'.
enum
{
  perception_msgs__msg__TrafficLightState__CONFLICT = 5
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'source_sensor'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/TrafficLightState in the package perception_msgs.
typedef struct perception_msgs__msg__TrafficLightState
{
  std_msgs__msg__Header header;
  uint8_t state;
  float confidence;
  bool relevant_to_route;
  float distance_to_stop;
  bool confirmed;
  bool in_stop_zone;
  float bbox_x;
  float bbox_y;
  float bbox_w;
  float bbox_h;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String source_sensor;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__TrafficLightState;

// Struct for a sequence of perception_msgs__msg__TrafficLightState.
typedef struct perception_msgs__msg__TrafficLightState__Sequence
{
  perception_msgs__msg__TrafficLightState * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__TrafficLightState__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_H_
