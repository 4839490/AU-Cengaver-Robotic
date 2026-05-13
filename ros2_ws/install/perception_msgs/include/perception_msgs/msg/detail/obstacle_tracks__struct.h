// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/ObstacleTracks.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_H_

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
// Member 'tracks'
#include "perception_msgs/msg/detail/obstacle_track__struct.h"

// Struct defined in msg/ObstacleTracks in the package perception_msgs.
typedef struct perception_msgs__msg__ObstacleTracks
{
  std_msgs__msg__Header header;
  perception_msgs__msg__ObstacleTrack__Sequence tracks;
} perception_msgs__msg__ObstacleTracks;

// Struct for a sequence of perception_msgs__msg__ObstacleTracks.
typedef struct perception_msgs__msg__ObstacleTracks__Sequence
{
  perception_msgs__msg__ObstacleTracks * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__ObstacleTracks__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_H_
