// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/controller_feedback__rosidl_typesupport_fastrtps_cpp.hpp"
#include "planning_msgs/msg/detail/controller_feedback__struct.hpp"

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


namespace planning_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
cdr_serialize(
  const planning_msgs::msg::ControllerFeedback & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: actual_speed
  cdr << ros_message.actual_speed;
  // Member: actual_steering_deg
  cdr << ros_message.actual_steering_deg;
  // Member: cross_track_error
  cdr << ros_message.cross_track_error;
  // Member: heading_error
  cdr << ros_message.heading_error;
  // Member: brake_active
  cdr << (ros_message.brake_active ? true : false);
  // Member: full_brake_active
  cdr << (ros_message.full_brake_active ? true : false);
  // Member: age_ms
  cdr << ros_message.age_ms;
  // Member: valid_until_ms
  cdr << ros_message.valid_until_ms;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  planning_msgs::msg::ControllerFeedback & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: actual_speed
  cdr >> ros_message.actual_speed;

  // Member: actual_steering_deg
  cdr >> ros_message.actual_steering_deg;

  // Member: cross_track_error
  cdr >> ros_message.cross_track_error;

  // Member: heading_error
  cdr >> ros_message.heading_error;

  // Member: brake_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.brake_active = tmp ? true : false;
  }

  // Member: full_brake_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.full_brake_active = tmp ? true : false;
  }

  // Member: age_ms
  cdr >> ros_message.age_ms;

  // Member: valid_until_ms
  cdr >> ros_message.valid_until_ms;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
get_serialized_size(
  const planning_msgs::msg::ControllerFeedback & ros_message,
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
  // Member: actual_speed
  {
    size_t item_size = sizeof(ros_message.actual_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: actual_steering_deg
  {
    size_t item_size = sizeof(ros_message.actual_steering_deg);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cross_track_error
  {
    size_t item_size = sizeof(ros_message.cross_track_error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: heading_error
  {
    size_t item_size = sizeof(ros_message.heading_error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: brake_active
  {
    size_t item_size = sizeof(ros_message.brake_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: full_brake_active
  {
    size_t item_size = sizeof(ros_message.full_brake_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: age_ms
  {
    size_t item_size = sizeof(ros_message.age_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: valid_until_ms
  {
    size_t item_size = sizeof(ros_message.valid_until_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
max_serialized_size_ControllerFeedback(
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

  // Member: actual_speed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: actual_steering_deg
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: cross_track_error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: heading_error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: brake_active
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: full_brake_active
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: age_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: valid_until_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _ControllerFeedback__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::ControllerFeedback *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ControllerFeedback__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<planning_msgs::msg::ControllerFeedback *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ControllerFeedback__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::ControllerFeedback *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ControllerFeedback__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ControllerFeedback(full_bounded, 0);
}

static message_type_support_callbacks_t _ControllerFeedback__callbacks = {
  "planning_msgs::msg",
  "ControllerFeedback",
  _ControllerFeedback__cdr_serialize,
  _ControllerFeedback__cdr_deserialize,
  _ControllerFeedback__get_serialized_size,
  _ControllerFeedback__max_serialized_size
};

static rosidl_message_type_support_t _ControllerFeedback__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ControllerFeedback__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace planning_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_planning_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<planning_msgs::msg::ControllerFeedback>()
{
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_ControllerFeedback__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, planning_msgs, msg, ControllerFeedback)() {
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_ControllerFeedback__handle;
}

#ifdef __cplusplus
}
#endif
