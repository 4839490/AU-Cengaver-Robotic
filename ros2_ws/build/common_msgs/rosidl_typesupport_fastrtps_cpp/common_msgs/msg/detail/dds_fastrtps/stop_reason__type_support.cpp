// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice
#include "common_msgs/msg/detail/stop_reason__rosidl_typesupport_fastrtps_cpp.hpp"
#include "common_msgs/msg/detail/stop_reason__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

namespace common_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_common_msgs
cdr_serialize(
  const common_msgs::msg::StopReason & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: reason
  cdr << ros_message.reason;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_common_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  common_msgs::msg::StopReason & ros_message)
{
  // Member: reason
  cdr >> ros_message.reason;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_common_msgs
get_serialized_size(
  const common_msgs::msg::StopReason & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: reason
  {
    size_t item_size = sizeof(ros_message.reason);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_common_msgs
max_serialized_size_StopReason(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: reason
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _StopReason__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const common_msgs::msg::StopReason *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _StopReason__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<common_msgs::msg::StopReason *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _StopReason__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const common_msgs::msg::StopReason *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _StopReason__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_StopReason(full_bounded, 0);
}

static message_type_support_callbacks_t _StopReason__callbacks = {
  "common_msgs::msg",
  "StopReason",
  _StopReason__cdr_serialize,
  _StopReason__cdr_deserialize,
  _StopReason__get_serialized_size,
  _StopReason__max_serialized_size
};

static rosidl_message_type_support_t _StopReason__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_StopReason__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace common_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_common_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<common_msgs::msg::StopReason>()
{
  return &common_msgs::msg::typesupport_fastrtps_cpp::_StopReason__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, common_msgs, msg, StopReason)() {
  return &common_msgs::msg::typesupport_fastrtps_cpp::_StopReason__handle;
}

#ifdef __cplusplus
}
#endif
