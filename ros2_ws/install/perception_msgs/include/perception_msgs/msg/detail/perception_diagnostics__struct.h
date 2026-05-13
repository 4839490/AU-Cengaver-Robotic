// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from perception_msgs:msg/PerceptionDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_H_
#define PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_H_

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
// Member 'node_name'
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/PerceptionDiagnostics in the package perception_msgs.
typedef struct perception_msgs__msg__PerceptionDiagnostics
{
  std_msgs__msg__Header header;
  rosidl_runtime_c__String node_name;
  float input_hz;
  float output_hz;
  float latency_ms;
  uint32_t last_msg_age_ms;
  float mean_confidence;
  uint32_t num_outputs;
  float gpu_utilization;
  rosidl_runtime_c__String__Sequence warning_flags;
} perception_msgs__msg__PerceptionDiagnostics;

// Struct for a sequence of perception_msgs__msg__PerceptionDiagnostics.
typedef struct perception_msgs__msg__PerceptionDiagnostics__Sequence
{
  perception_msgs__msg__PerceptionDiagnostics * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} perception_msgs__msg__PerceptionDiagnostics__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_H_
