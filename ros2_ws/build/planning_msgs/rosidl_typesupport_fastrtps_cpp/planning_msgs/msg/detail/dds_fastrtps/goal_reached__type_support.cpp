// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from planning_msgs:msg/GoalReached.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/goal_reached__rosidl_typesupport_fastrtps_cpp.hpp"
#include "planning_msgs/msg/detail/goal_reached__struct.hpp"

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
  const planning_msgs::msg::GoalReached & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: waypoint_id
  cdr << ros_message.waypoint_id;
  // Member: waypoint_type
  cdr << ros_message.waypoint_type;
  // Member: success
  cdr << (ros_message.success ? true : false);
  // Member: distance_error
  cdr << ros_message.distance_error;
  // Member: heading_error
  cdr << ros_message.heading_error;
  // Member: age_ms
  cdr << ros_message.age_ms;
  // Member: valid_until_ms
  cdr << ros_message.valid_until_ms;
  // Member: warning_flags
  {
    cdr << ros_message.warning_flags;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  planning_msgs::msg::GoalReached & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: waypoint_id
  cdr >> ros_message.waypoint_id;

  // Member: waypoint_type
  cdr >> ros_message.waypoint_type;

  // Member: success
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.success = tmp ? true : false;
  }

  // Member: distance_error
  cdr >> ros_message.distance_error;

  // Member: heading_error
  cdr >> ros_message.heading_error;

  // Member: age_ms
  cdr >> ros_message.age_ms;

  // Member: valid_until_ms
  cdr >> ros_message.valid_until_ms;

  // Member: warning_flags
  {
    cdr >> ros_message.warning_flags;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
get_serialized_size(
  const planning_msgs::msg::GoalReached & ros_message,
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
  // Member: waypoint_id
  {
    size_t item_size = sizeof(ros_message.waypoint_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: waypoint_type
  {
    size_t item_size = sizeof(ros_message.waypoint_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: success
  {
    size_t item_size = sizeof(ros_message.success);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance_error
  {
    size_t item_size = sizeof(ros_message.distance_error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: heading_error
  {
    size_t item_size = sizeof(ros_message.heading_error);
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
  // Member: warning_flags
  {
    size_t array_size = ros_message.warning_flags.size();

    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (ros_message.warning_flags[index].size() + 1);
    }
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_planning_msgs
max_serialized_size_GoalReached(
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

  // Member: waypoint_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: waypoint_type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: success
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: distance_error
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

  // Member: warning_flags
  {
    size_t array_size = 0;
    full_bounded = false;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  return current_alignment - initial_alignment;
}

static bool _GoalReached__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::GoalReached *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _GoalReached__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<planning_msgs::msg::GoalReached *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _GoalReached__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::GoalReached *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _GoalReached__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_GoalReached(full_bounded, 0);
}

static message_type_support_callbacks_t _GoalReached__callbacks = {
  "planning_msgs::msg",
  "GoalReached",
  _GoalReached__cdr_serialize,
  _GoalReached__cdr_deserialize,
  _GoalReached__get_serialized_size,
  _GoalReached__max_serialized_size
};

static rosidl_message_type_support_t _GoalReached__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_GoalReached__callbacks,
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
get_message_type_support_handle<planning_msgs::msg::GoalReached>()
{
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_GoalReached__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, planning_msgs, msg, GoalReached)() {
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_GoalReached__handle;
}

#ifdef __cplusplus
}
#endif
