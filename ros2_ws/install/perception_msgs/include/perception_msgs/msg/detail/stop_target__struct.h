// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/StopTarget.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'TRAFFIC_LIGHT_STOP'.
enum
{
  perception_msgs__msg__StopTarget__TRAFFIC_LIGHT_STOP = 0
};

/// Constant 'STOP_SIGN'.
enum
{
  perception_msgs__msg__StopTarget__STOP_SIGN = 1
};

/// Constant 'PICKUP'.
enum
{
  perception_msgs__msg__StopTarget__PICKUP = 2
};

/// Constant 'DROPOFF'.
enum
{
  perception_msgs__msg__StopTarget__DROPOFF = 3
};

/// Constant 'LOW'.
enum
{
  perception_msgs__msg__StopTarget__LOW = 0
};

/// Constant 'NORMAL'.
enum
{
  perception_msgs__msg__StopTarget__NORMAL = 1
};

/// Constant 'HIGH'.
enum
{
  perception_msgs__msg__StopTarget__HIGH = 2
};

/// Constant 'CRITICAL'.
enum
{
  perception_msgs__msg__StopTarget__CRITICAL = 3
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'source'
// Member 'source_topic'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/StopTarget in the package perception_msgs.
typedef struct perception_msgs__msg__StopTarget
{
  std_msgs__msg__Header header;
  uint8_t target_type;
  float distance_from_front_bumper;
  float target_x;
  float target_y;
  float confidence;
  rosidl_runtime_c__String source;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  int32_t waypoint_id;
  float heading_at_stop;
  uint8_t priority;
  uint32_t required_stop_duration_ms;
  uint32_t stop_reason_id;
  rosidl_runtime_c__String source_topic;
} perception_msgs__msg__StopTarget;

// Struct for a sequence of perception_msgs__msg__StopTarget.
typedef struct perception_msgs__msg__StopTarget__Sequence
{
  perception_msgs__msg__StopTarget * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__StopTarget__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_H_
