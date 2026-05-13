// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_H_

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
// Member 'source'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/MapOrigin in the package localization_msgs.
typedef struct localization_msgs__msg__MapOrigin
{
  std_msgs__msg__Header header;
  double lat_ref;
  double lon_ref;
  double alt_ref;
  double yaw_ref;
  rosidl_runtime_c__String source;
  bool locked;
} localization_msgs__msg__MapOrigin;

// Struct for a sequence of localization_msgs__msg__MapOrigin.
typedef struct localization_msgs__msg__MapOrigin__Sequence
{
  localization_msgs__msg__MapOrigin * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} localization_msgs__msg__MapOrigin__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_H_
