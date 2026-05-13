// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice
#include "common_msgs/msg/detail/stop_reason__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "common_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "common_msgs/msg/detail/stop_reason__struct.h"
#include "common_msgs/msg/detail/stop_reason__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _StopReason__ros_msg_type = common_msgs__msg__StopReason;

static bool _StopReason__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _StopReason__ros_msg_type * ros_message = static_cast<const _StopReason__ros_msg_type *>(untyped_ros_message);
  // Field name: reason
  {
    cdr << ros_message->reason;
  }

  return true;
}

static bool _StopReason__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _StopReason__ros_msg_type * ros_message = static_cast<_StopReason__ros_msg_type *>(untyped_ros_message);
  // Field name: reason
  {
    cdr >> ros_message->reason;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_common_msgs
size_t get_serialized_size_common_msgs__msg__StopReason(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _StopReason__ros_msg_type * ros_message = static_cast<const _StopReason__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name reason
  {
    size_t item_size = sizeof(ros_message->reason);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _StopReason__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_common_msgs__msg__StopReason(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_common_msgs
size_t max_serialized_size_common_msgs__msg__StopReason(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: reason
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _StopReason__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_common_msgs__msg__StopReason(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_StopReason = {
  "common_msgs::msg",
  "StopReason",
  _StopReason__cdr_serialize,
  _StopReason__cdr_deserialize,
  _StopReason__get_serialized_size,
  _StopReason__max_serialized_size
};

static rosidl_message_type_support_t _StopReason__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_StopReason,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, common_msgs, msg, StopReason)() {
  return &_StopReason__type_support;
}

#if defined(__cplusplus)
}
#endif
