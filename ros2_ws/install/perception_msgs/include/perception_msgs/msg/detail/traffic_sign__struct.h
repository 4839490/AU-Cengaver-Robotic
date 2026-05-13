// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'UNKNOWN_SIGN'.
enum
{
  perception_msgs__msg__TrafficSign__UNKNOWN_SIGN = 0
};

/// Constant 'STOP'.
enum
{
  perception_msgs__msg__TrafficSign__STOP = 1
};

/// Constant 'SPEED_LIMIT'.
enum
{
  perception_msgs__msg__TrafficSign__SPEED_LIMIT = 2
};

/// Constant 'NO_ENTRY'.
enum
{
  perception_msgs__msg__TrafficSign__NO_ENTRY = 3
};

/// Constant 'MANDATORY_LEFT'.
enum
{
  perception_msgs__msg__TrafficSign__MANDATORY_LEFT = 4
};

/// Constant 'MANDATORY_RIGHT'.
enum
{
  perception_msgs__msg__TrafficSign__MANDATORY_RIGHT = 5
};

/// Constant 'MANDATORY_STRAIGHT'.
enum
{
  perception_msgs__msg__TrafficSign__MANDATORY_STRAIGHT = 6
};

/// Constant 'MANDATORY_LEFT_STRAIGHT'.
enum
{
  perception_msgs__msg__TrafficSign__MANDATORY_LEFT_STRAIGHT = 7
};

/// Constant 'MANDATORY_RIGHT_STRAIGHT'.
enum
{
  perception_msgs__msg__TrafficSign__MANDATORY_RIGHT_STRAIGHT = 8
};

/// Constant 'ROUNDABOUT'.
enum
{
  perception_msgs__msg__TrafficSign__ROUNDABOUT = 9
};

/// Constant 'PARKING'.
enum
{
  perception_msgs__msg__TrafficSign__PARKING = 10
};

/// Constant 'NO_PARKING'.
enum
{
  perception_msgs__msg__TrafficSign__NO_PARKING = 11
};

/// Constant 'TUNNEL'.
enum
{
  perception_msgs__msg__TrafficSign__TUNNEL = 12
};

/// Constant 'PEDESTRIAN_CROSSING'.
enum
{
  perception_msgs__msg__TrafficSign__PEDESTRIAN_CROSSING = 13
};

/// Constant 'NEW'.
enum
{
  perception_msgs__msg__TrafficSign__NEW = 0
};

/// Constant 'TRACKED'.
enum
{
  perception_msgs__msg__TrafficSign__TRACKED = 1
};

/// Constant 'ALREADY_HANDLED'.
enum
{
  perception_msgs__msg__TrafficSign__ALREADY_HANDLED = 2
};

/// Constant 'STALE'.
enum
{
  perception_msgs__msg__TrafficSign__STALE = 3
};

// Include directives for member types
// Member 'source_sensor'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/TrafficSign in the package perception_msgs.
typedef struct perception_msgs__msg__TrafficSign
{
  uint32_t sign_id;
  uint8_t type;
  float confidence;
  bool relevant_to_route;
  float distance;
  uint8_t event_status;
  bool confirmed;
  float bbox_x;
  float bbox_y;
  float bbox_w;
  float bbox_h;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  uint32_t event_memory_ttl_ms;
  rosidl_runtime_c__String source_sensor;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__TrafficSign;

// Struct for a sequence of perception_msgs__msg__TrafficSign.
typedef struct perception_msgs__msg__TrafficSign__Sequence
{
  perception_msgs__msg__TrafficSign * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__TrafficSign__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_H_
