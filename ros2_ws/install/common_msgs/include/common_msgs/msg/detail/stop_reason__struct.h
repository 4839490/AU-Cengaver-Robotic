// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_H_
#define COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'STOP_NONE'.
enum
{
  common_msgs__msg__StopReason__STOP_NONE = 0
};

/// Constant 'STOP_RED_LIGHT'.
enum
{
  common_msgs__msg__StopReason__STOP_RED_LIGHT = 1
};

/// Constant 'STOP_STOP_SIGN'.
enum
{
  common_msgs__msg__StopReason__STOP_STOP_SIGN = 2
};

/// Constant 'STOP_OBSTACLE_TTC'.
enum
{
  common_msgs__msg__StopReason__STOP_OBSTACLE_TTC = 3
};

/// Constant 'STOP_LOCALIZATION_LOST'.
enum
{
  common_msgs__msg__StopReason__STOP_LOCALIZATION_LOST = 4
};

/// Constant 'STOP_STALE_SENSOR'.
enum
{
  common_msgs__msg__StopReason__STOP_STALE_SENSOR = 5
};

/// Constant 'STOP_MISSION_ABORT'.
enum
{
  common_msgs__msg__StopReason__STOP_MISSION_ABORT = 6
};

/// Constant 'STOP_PEDESTRIAN'.
enum
{
  common_msgs__msg__StopReason__STOP_PEDESTRIAN = 7
};

// Struct defined in msg/StopReason in the package common_msgs.
typedef struct common_msgs__msg__StopReason
{
  uint8_t reason;
} common_msgs__msg__StopReason;

// Struct for a sequence of common_msgs__msg__StopReason.
typedef struct common_msgs__msg__StopReason__Sequence
{
  common_msgs__msg__StopReason * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} common_msgs__msg__StopReason__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_H_
