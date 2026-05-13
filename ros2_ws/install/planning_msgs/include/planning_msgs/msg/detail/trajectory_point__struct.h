// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/TrajectoryPoint in the package planning_msgs.
typedef struct planning_msgs__msg__TrajectoryPoint
{
  double x;
  double y;
  double yaw;
  float speed;
  float curvature;
  float distance_from_start;
} planning_msgs__msg__TrajectoryPoint;

// Struct for a sequence of planning_msgs__msg__TrajectoryPoint.
typedef struct planning_msgs__msg__TrajectoryPoint__Sequence
{
  planning_msgs__msg__TrajectoryPoint * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__TrajectoryPoint__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_H_
