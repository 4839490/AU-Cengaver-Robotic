// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/LaneModel.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_H_

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
// Member 'centerline'
// Member 'left_boundary'
// Member 'right_boundary'
#include "geometry_msgs/msg/detail/point__struct.h"
// Member 'source_sensor'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/LaneModel in the package perception_msgs.
typedef struct perception_msgs__msg__LaneModel
{
  std_msgs__msg__Header header;
  geometry_msgs__msg__Point__Sequence centerline;
  geometry_msgs__msg__Point__Sequence left_boundary;
  geometry_msgs__msg__Point__Sequence right_boundary;
  float lane_confidence;
  bool lane_lost;
  float curvature;
  float lane_width_estimate;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String source_sensor;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__LaneModel;

// Struct for a sequence of perception_msgs__msg__LaneModel.
typedef struct perception_msgs__msg__LaneModel__Sequence
{
  perception_msgs__msg__LaneModel * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__LaneModel__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_H_
