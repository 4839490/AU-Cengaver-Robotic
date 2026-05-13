// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/planning_status__rosidl_typesupport_fastrtps_cpp.hpp"
#include "planning_msgs/msg/detail/planning_status__struct.hpp"

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
  const planning_msgs::msg::PlanningStatus & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: status
  cdr << ros_message.status;
  // Member: trajectory_valid
  cdr << (ros_message.trajectory_valid ? true : false);
  // Member: goal_reached
  cdr << (ros_message.goal_reached ? true : false);
  // Member: parking_entry_reached
  cdr << (ros_message.parking_entry_reached ? true : false);
  // Member: obstacle_blocking
  cdr << (ros_message.obstacle_blocking ? true : false);
  // Member: lane_lost
  cdr << (ros_message.lane_lost ? true : false);
  // Member: localization_degraded
  cdr << (ros_message.localization_degraded ? true : false);
  // Member: active_waypoint_id
  cdr << ros_message.active_waypoint_id;
  // Member: distance_to_goal
  cdr << ros_message.distance_to_goal;
  // Member: planner_mode
  cdr << ros_message.planner_mode;
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
  planning_msgs::msg::PlanningStatus & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: status
  cdr >> ros_message.status;

  // Member: trajectory_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.trajectory_valid = tmp ? true : false;
  }

  // Member: goal_reached
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.goal_reached = tmp ? true : false;
  }

  // Member: parking_entry_reached
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.parking_entry_reached = tmp ? true : false;
  }

  // Member: obstacle_blocking
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.obstacle_blocking = tmp ? true : false;
  }

  // Member: lane_lost
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.lane_lost = tmp ? true : false;
  }

  // Member: localization_degraded
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.localization_degraded = tmp ? true : false;
  }

  // Member: active_waypoint_id
  cdr >> ros_message.active_waypoint_id;

  // Member: distance_to_goal
  cdr >> ros_message.distance_to_goal;

  // Member: planner_mode
  cdr >> ros_message.planner_mode;

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
  const planning_msgs::msg::PlanningStatus & ros_message,
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
  // Member: status
  {
    size_t item_size = sizeof(ros_message.status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: trajectory_valid
  {
    size_t item_size = sizeof(ros_message.trajectory_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: goal_reached
  {
    size_t item_size = sizeof(ros_message.goal_reached);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: parking_entry_reached
  {
    size_t item_size = sizeof(ros_message.parking_entry_reached);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: obstacle_blocking
  {
    size_t item_size = sizeof(ros_message.obstacle_blocking);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lane_lost
  {
    size_t item_size = sizeof(ros_message.lane_lost);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: localization_degraded
  {
    size_t item_size = sizeof(ros_message.localization_degraded);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: active_waypoint_id
  {
    size_t item_size = sizeof(ros_message.active_waypoint_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance_to_goal
  {
    size_t item_size = sizeof(ros_message.distance_to_goal);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: planner_mode
  {
    size_t item_size = sizeof(ros_message.planner_mode);
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
max_serialized_size_PlanningStatus(
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

  // Member: status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: trajectory_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: goal_reached
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: parking_entry_reached
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: obstacle_blocking
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: lane_lost
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: localization_degraded
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: active_waypoint_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance_to_goal
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: planner_mode
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

static bool _PlanningStatus__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::PlanningStatus *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _PlanningStatus__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<planning_msgs::msg::PlanningStatus *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _PlanningStatus__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const planning_msgs::msg::PlanningStatus *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _PlanningStatus__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_PlanningStatus(full_bounded, 0);
}

static message_type_support_callbacks_t _PlanningStatus__callbacks = {
  "planning_msgs::msg",
  "PlanningStatus",
  _PlanningStatus__cdr_serialize,
  _PlanningStatus__cdr_deserialize,
  _PlanningStatus__get_serialized_size,
  _PlanningStatus__max_serialized_size
};

static rosidl_message_type_support_t _PlanningStatus__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_PlanningStatus__callbacks,
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
get_message_type_support_handle<planning_msgs::msg::PlanningStatus>()
{
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_PlanningStatus__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, planning_msgs, msg, PlanningStatus)() {
  return &planning_msgs::msg::typesupport_fastrtps_cpp::_PlanningStatus__handle;
}

#ifdef __cplusplus
}
#endif
