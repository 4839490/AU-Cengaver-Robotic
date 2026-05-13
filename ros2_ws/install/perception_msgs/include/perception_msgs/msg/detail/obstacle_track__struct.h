// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'UNKNOWN_OBSTACLE'.
enum
{
  perception_msgs__msg__ObstacleTrack__UNKNOWN_OBSTACLE = 0
};

/// Constant 'VEHICLE'.
enum
{
  perception_msgs__msg__ObstacleTrack__VEHICLE = 1
};

/// Constant 'PEDESTRIAN'.
enum
{
  perception_msgs__msg__ObstacleTrack__PEDESTRIAN = 2
};

/// Constant 'CONE'.
enum
{
  perception_msgs__msg__ObstacleTrack__CONE = 3
};

/// Constant 'BARRIER'.
enum
{
  perception_msgs__msg__ObstacleTrack__BARRIER = 4
};

/// Constant 'SIGN_POLE'.
enum
{
  perception_msgs__msg__ObstacleTrack__SIGN_POLE = 5
};

// Include directives for member types
// Member 'source_sensor'
// Member 'semantic_source'
// Member 'geometry_source'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/ObstacleTrack in the package perception_msgs.
typedef struct perception_msgs__msg__ObstacleTrack
{
  uint32_t track_id;
  uint8_t class_label;
  float confidence;
  float position_x;
  float position_y;
  float distance;
  float velocity_x;
  float velocity_y;
  float ttc;
  float width;
  float length;
  float height;
  bool is_static;
  rosidl_runtime_c__String source_sensor;
  rosidl_runtime_c__String semantic_source;
  rosidl_runtime_c__String geometry_source;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__ObstacleTrack;

// Struct for a sequence of perception_msgs__msg__ObstacleTrack.
typedef struct perception_msgs__msg__ObstacleTrack__Sequence
{
  perception_msgs__msg__ObstacleTrack * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__ObstacleTrack__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_H_
