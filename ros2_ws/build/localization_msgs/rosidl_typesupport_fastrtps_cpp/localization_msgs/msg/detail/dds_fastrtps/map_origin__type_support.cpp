// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/map_origin__rosidl_typesupport_fastrtps_cpp.hpp"
#include "localization_msgs/msg/detail/map_origin__struct.hpp"

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
namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::Header &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::Header &);
size_t get_serialized_size(
  const std_msgs::msg::Header &,
  size_t current_alignment);
size_t
max_serialized_size_Header(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs


namespace localization_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
cdr_serialize(
  const localization_msgs::msg::MapOrigin & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: lat_ref
  cdr << ros_message.lat_ref;
  // Member: lon_ref
  cdr << ros_message.lon_ref;
  // Member: alt_ref
  cdr << ros_message.alt_ref;
  // Member: yaw_ref
  cdr << ros_message.yaw_ref;
  // Member: source
  cdr << ros_message.source;
  // Member: locked
  cdr << (ros_message.locked ? true : false);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  localization_msgs::msg::MapOrigin & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: lat_ref
  cdr >> ros_message.lat_ref;

  // Member: lon_ref
  cdr >> ros_message.lon_ref;

  // Member: alt_ref
  cdr >> ros_message.alt_ref;

  // Member: yaw_ref
  cdr >> ros_message.yaw_ref;

  // Member: source
  cdr >> ros_message.source;

  // Member: locked
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.locked = tmp ? true : false;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
get_serialized_size(
  const localization_msgs::msg::MapOrigin & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: header

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.header, current_alignment);
  // Member: lat_ref
  {
    size_t item_size = sizeof(ros_message.lat_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lon_ref
  {
    size_t item_size = sizeof(ros_message.lon_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: alt_ref
  {
    size_t item_size = sizeof(ros_message.alt_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: yaw_ref
  {
    size_t item_size = sizeof(ros_message.yaw_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.source.size() + 1);
  // Member: locked
  {
    size_t item_size = sizeof(ros_message.locked);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
max_serialized_size_MapOrigin(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: header
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_Header(
        full_bounded, current_alignment);
    }
  }

  // Member: lat_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: lon_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: alt_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: yaw_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: locked
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static bool _MapOrigin__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const localization_msgs::msg::MapOrigin *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _MapOrigin__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<localization_msgs::msg::MapOrigin *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _MapOrigin__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const localization_msgs::msg::MapOrigin *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _MapOrigin__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_MapOrigin(full_bounded, 0);
}

static message_type_support_callbacks_t _MapOrigin__callbacks = {
  "localization_msgs::msg",
  "MapOrigin",
  _MapOrigin__cdr_serialize,
  _MapOrigin__cdr_deserialize,
  _MapOrigin__get_serialized_size,
  _MapOrigin__max_serialized_size
};

static rosidl_message_type_support_t _MapOrigin__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_MapOrigin__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace localization_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_localization_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<localization_msgs::msg::MapOrigin>()
{
  return &localization_msgs::msg::typesupport_fastrtps_cpp::_MapOrigin__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, localization_msgs, msg, MapOrigin)() {
  return &localization_msgs::msg::typesupport_fastrtps_cpp::_MapOrigin__handle;
}

#ifdef __cplusplus
}
#endif
