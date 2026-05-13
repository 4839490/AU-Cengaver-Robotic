// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice
#include "fsm_msgs/msg/detail/mission_state__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "fsm_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "fsm_msgs/msg/detail/mission_state__struct.h"
#include "fsm_msgs/msg/detail/mission_state__functions.h"
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

#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fsm_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fsm_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_fsm_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _MissionState__ros_msg_type = fsm_msgs__msg__MissionState;

static bool _MissionState__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MissionState__ros_msg_type * ros_message = static_cast<const _MissionState__ros_msg_type *>(untyped_ros_message);
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

  // Field name: mission_active
  {
    cdr << (ros_message->mission_active ? true : false);
  }

  // Field name: total_waypoints
  {
    cdr << ros_message->total_waypoints;
  }

  // Field name: completed_waypoints
  {
    cdr << ros_message->completed_waypoints;
  }

  // Field name: current_waypoint_id
  {
    cdr << ros_message->current_waypoint_id;
  }

  // Field name: current_waypoint_type
  {
    cdr << ros_message->current_waypoint_type;
  }

  // Field name: next_waypoint_id
  {
    cdr << ros_message->next_waypoint_id;
  }

  // Field name: next_waypoint_type
  {
    cdr << ros_message->next_waypoint_type;
  }

  // Field name: pickup_complete
  {
    cdr << (ros_message->pickup_complete ? true : false);
  }

  // Field name: dropoff_complete
  {
    cdr << (ros_message->dropoff_complete ? true : false);
  }

  // Field name: age_ms
  {
    cdr << ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr << ros_message->valid_until_ms;
  }

  return true;
}

static bool _MissionState__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MissionState__ros_msg_type * ros_message = static_cast<_MissionState__ros_msg_type *>(untyped_ros_message);
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

  // Field name: mission_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->mission_active = tmp ? true : false;
  }

  // Field name: total_waypoints
  {
    cdr >> ros_message->total_waypoints;
  }

  // Field name: completed_waypoints
  {
    cdr >> ros_message->completed_waypoints;
  }

  // Field name: current_waypoint_id
  {
    cdr >> ros_message->current_waypoint_id;
  }

  // Field name: current_waypoint_type
  {
    cdr >> ros_message->current_waypoint_type;
  }

  // Field name: next_waypoint_id
  {
    cdr >> ros_message->next_waypoint_id;
  }

  // Field name: next_waypoint_type
  {
    cdr >> ros_message->next_waypoint_type;
  }

  // Field name: pickup_complete
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->pickup_complete = tmp ? true : false;
  }

  // Field name: dropoff_complete
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->dropoff_complete = tmp ? true : false;
  }

  // Field name: age_ms
  {
    cdr >> ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr >> ros_message->valid_until_ms;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fsm_msgs
size_t get_serialized_size_fsm_msgs__msg__MissionState(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MissionState__ros_msg_type * ros_message = static_cast<const _MissionState__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name mission_active
  {
    size_t item_size = sizeof(ros_message->mission_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name total_waypoints
  {
    size_t item_size = sizeof(ros_message->total_waypoints);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name completed_waypoints
  {
    size_t item_size = sizeof(ros_message->completed_waypoints);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name current_waypoint_id
  {
    size_t item_size = sizeof(ros_message->current_waypoint_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name current_waypoint_type
  {
    size_t item_size = sizeof(ros_message->current_waypoint_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name next_waypoint_id
  {
    size_t item_size = sizeof(ros_message->next_waypoint_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name next_waypoint_type
  {
    size_t item_size = sizeof(ros_message->next_waypoint_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name pickup_complete
  {
    size_t item_size = sizeof(ros_message->pickup_complete);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name dropoff_complete
  {
    size_t item_size = sizeof(ros_message->dropoff_complete);
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

  return current_alignment - initial_alignment;
}

static uint32_t _MissionState__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_fsm_msgs__msg__MissionState(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_fsm_msgs
size_t max_serialized_size_fsm_msgs__msg__MissionState(
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
  // member: mission_active
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: total_waypoints
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: completed_waypoints
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: current_waypoint_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: current_waypoint_type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: next_waypoint_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: next_waypoint_type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: pickup_complete
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: dropoff_complete
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

  return current_alignment - initial_alignment;
}

static size_t _MissionState__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_fsm_msgs__msg__MissionState(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MissionState = {
  "fsm_msgs::msg",
  "MissionState",
  _MissionState__cdr_serialize,
  _MissionState__cdr_deserialize,
  _MissionState__get_serialized_size,
  _MissionState__max_serialized_size
};

static rosidl_message_type_support_t _MissionState__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MissionState,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, fsm_msgs, msg, MissionState)() {
  return &_MissionState__type_support;
}

#if defined(__cplusplus)
}
#endif
