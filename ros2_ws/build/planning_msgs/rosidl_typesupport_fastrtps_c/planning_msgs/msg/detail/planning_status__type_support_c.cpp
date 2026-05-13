// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/planning_status__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "planning_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "planning_msgs/msg/detail/planning_status__struct.h"
#include "planning_msgs/msg/detail/planning_status__functions.h"
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

#include "rosidl_runtime_c/string.h"  // warning_flags
#include "rosidl_runtime_c/string_functions.h"  // warning_flags
#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_planning_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_planning_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_planning_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _PlanningStatus__ros_msg_type = planning_msgs__msg__PlanningStatus;

static bool _PlanningStatus__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _PlanningStatus__ros_msg_type * ros_message = static_cast<const _PlanningStatus__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->header, cdr))
    {
      return false;
    }
  }

  // Field name: status
  {
    cdr << ros_message->status;
  }

  // Field name: trajectory_valid
  {
    cdr << (ros_message->trajectory_valid ? true : false);
  }

  // Field name: goal_reached
  {
    cdr << (ros_message->goal_reached ? true : false);
  }

  // Field name: parking_entry_reached
  {
    cdr << (ros_message->parking_entry_reached ? true : false);
  }

  // Field name: obstacle_blocking
  {
    cdr << (ros_message->obstacle_blocking ? true : false);
  }

  // Field name: lane_lost
  {
    cdr << (ros_message->lane_lost ? true : false);
  }

  // Field name: localization_degraded
  {
    cdr << (ros_message->localization_degraded ? true : false);
  }

  // Field name: active_waypoint_id
  {
    cdr << ros_message->active_waypoint_id;
  }

  // Field name: distance_to_goal
  {
    cdr << ros_message->distance_to_goal;
  }

  // Field name: planner_mode
  {
    cdr << ros_message->planner_mode;
  }

  // Field name: age_ms
  {
    cdr << ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr << ros_message->valid_until_ms;
  }

  // Field name: warning_flags
  {
    size_t size = ros_message->warning_flags.size;
    auto array_ptr = ros_message->warning_flags.data;
    cdr << static_cast<uint32_t>(size);
    for (size_t i = 0; i < size; ++i) {
      const rosidl_runtime_c__String * str = &array_ptr[i];
      if (str->capacity == 0 || str->capacity <= str->size) {
        fprintf(stderr, "string capacity not greater than size\n");
        return false;
      }
      if (str->data[str->size] != '\0') {
        fprintf(stderr, "string not null-terminated\n");
        return false;
      }
      cdr << str->data;
    }
  }

  return true;
}

static bool _PlanningStatus__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _PlanningStatus__ros_msg_type * ros_message = static_cast<_PlanningStatus__ros_msg_type *>(untyped_ros_message);
  // Field name: header
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, Header
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->header))
    {
      return false;
    }
  }

  // Field name: status
  {
    cdr >> ros_message->status;
  }

  // Field name: trajectory_valid
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->trajectory_valid = tmp ? true : false;
  }

  // Field name: goal_reached
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->goal_reached = tmp ? true : false;
  }

  // Field name: parking_entry_reached
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->parking_entry_reached = tmp ? true : false;
  }

  // Field name: obstacle_blocking
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->obstacle_blocking = tmp ? true : false;
  }

  // Field name: lane_lost
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->lane_lost = tmp ? true : false;
  }

  // Field name: localization_degraded
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->localization_degraded = tmp ? true : false;
  }

  // Field name: active_waypoint_id
  {
    cdr >> ros_message->active_waypoint_id;
  }

  // Field name: distance_to_goal
  {
    cdr >> ros_message->distance_to_goal;
  }

  // Field name: planner_mode
  {
    cdr >> ros_message->planner_mode;
  }

  // Field name: age_ms
  {
    cdr >> ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr >> ros_message->valid_until_ms;
  }

  // Field name: warning_flags
  {
    uint32_t cdrSize;
    cdr >> cdrSize;
    size_t size = static_cast<size_t>(cdrSize);
    if (ros_message->warning_flags.data) {
      rosidl_runtime_c__String__Sequence__fini(&ros_message->warning_flags);
    }
    if (!rosidl_runtime_c__String__Sequence__init(&ros_message->warning_flags, size)) {
      return "failed to create array for field 'warning_flags'";
    }
    auto array_ptr = ros_message->warning_flags.data;
    for (size_t i = 0; i < size; ++i) {
      std::string tmp;
      cdr >> tmp;
      auto & ros_i = array_ptr[i];
      if (!ros_i.data) {
        rosidl_runtime_c__String__init(&ros_i);
      }
      bool succeeded = rosidl_runtime_c__String__assign(
        &ros_i,
        tmp.c_str());
      if (!succeeded) {
        fprintf(stderr, "failed to assign string into field 'warning_flags'\n");
        return false;
      }
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_planning_msgs
size_t get_serialized_size_planning_msgs__msg__PlanningStatus(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _PlanningStatus__ros_msg_type * ros_message = static_cast<const _PlanningStatus__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name status
  {
    size_t item_size = sizeof(ros_message->status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name trajectory_valid
  {
    size_t item_size = sizeof(ros_message->trajectory_valid);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name goal_reached
  {
    size_t item_size = sizeof(ros_message->goal_reached);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name parking_entry_reached
  {
    size_t item_size = sizeof(ros_message->parking_entry_reached);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name obstacle_blocking
  {
    size_t item_size = sizeof(ros_message->obstacle_blocking);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lane_lost
  {
    size_t item_size = sizeof(ros_message->lane_lost);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name localization_degraded
  {
    size_t item_size = sizeof(ros_message->localization_degraded);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name active_waypoint_id
  {
    size_t item_size = sizeof(ros_message->active_waypoint_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name distance_to_goal
  {
    size_t item_size = sizeof(ros_message->distance_to_goal);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name planner_mode
  {
    size_t item_size = sizeof(ros_message->planner_mode);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name age_ms
  {
    size_t item_size = sizeof(ros_message->age_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name valid_until_ms
  {
    size_t item_size = sizeof(ros_message->valid_until_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name warning_flags
  {
    size_t array_size = ros_message->warning_flags.size;
    auto array_ptr = ros_message->warning_flags.data;
    current_alignment += padding +
      eprosima::fastcdr::Cdr::alignment(current_alignment, padding);
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        (array_ptr[index].size + 1);
    }
  }

  return current_alignment - initial_alignment;
}

static uint32_t _PlanningStatus__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_planning_msgs__msg__PlanningStatus(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_planning_msgs
size_t max_serialized_size_planning_msgs__msg__PlanningStatus(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: header
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__Header(
        full_bounded, current_alignment);
    }
  }
  // member: status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: trajectory_valid
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: goal_reached
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: parking_entry_reached
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: obstacle_blocking
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: lane_lost
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: localization_degraded
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: active_waypoint_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: distance_to_goal
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: planner_mode
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: age_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: valid_until_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: warning_flags
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

static size_t _PlanningStatus__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_planning_msgs__msg__PlanningStatus(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_PlanningStatus = {
  "planning_msgs::msg",
  "PlanningStatus",
  _PlanningStatus__cdr_serialize,
  _PlanningStatus__cdr_deserialize,
  _PlanningStatus__get_serialized_size,
  _PlanningStatus__max_serialized_size
};

static rosidl_message_type_support_t _PlanningStatus__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_PlanningStatus,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, planning_msgs, msg, PlanningStatus)() {
  return &_PlanningStatus__type_support;
}

#if defined(__cplusplus)
}
#endif
