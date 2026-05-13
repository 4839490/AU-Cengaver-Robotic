// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/Junction.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'NORMAL'.
enum
{
  perception_msgs__msg__Junction__NORMAL = 0
};

/// Constant 'ROUNDABOUT'.
enum
{
  perception_msgs__msg__Junction__ROUNDABOUT = 1
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'source_sensor'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/Junction in the package perception_msgs.
typedef struct perception_msgs__msg__Junction
{
  std_msgs__msg__Header header;
  bool detected;
  uint8_t junction_type;
  uint8_t arm_count;
  float distance_to_entry;
  float confidence;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String source_sensor;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__Junction;

// Struct for a sequence of perception_msgs__msg__Junction.
typedef struct perception_msgs__msg__Junction__Sequence
{
  perception_msgs__msg__Junction * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__Junction__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_H_
