// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from localization_msgs:msg/RawGps.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'FIX_NONE'.
enum
{
  localization_msgs__msg__RawGps__FIX_NONE = 0
};

/// Constant 'FIX_GPS'.
enum
{
  localization_msgs__msg__RawGps__FIX_GPS = 1
};

/// Constant 'FIX_DGPS'.
enum
{
  localization_msgs__msg__RawGps__FIX_DGPS = 2
};

/// Constant 'FIX_RTK_FLOAT'.
enum
{
  localization_msgs__msg__RawGps__FIX_RTK_FLOAT = 4
};

/// Constant 'FIX_RTK_FIXED'.
enum
{
  localization_msgs__msg__RawGps__FIX_RTK_FIXED = 5
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

// Struct defined in msg/RawGps in the package localization_msgs.
typedef struct localization_msgs__msg__RawGps
{
  std_msgs__msg__Header header;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  double latitude;
  double longitude;
  double altitude;
  double speed;
  double heading_deg;
  double hdop;
  double vdop;
  uint8_t fix_type;
} localization_msgs__msg__RawGps;

// Struct for a sequence of localization_msgs__msg__RawGps.
typedef struct localization_msgs__msg__RawGps__Sequence
{
  localization_msgs__msg__RawGps * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} localization_msgs__msg__RawGps__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_H_
