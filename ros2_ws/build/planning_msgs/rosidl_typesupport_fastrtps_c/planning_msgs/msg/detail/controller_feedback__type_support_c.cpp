// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/controller_feedback__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "planning_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "planning_msgs/msg/detail/controller_feedback__struct.h"
#include "planning_msgs/msg/detail/controller_feedback__functions.h"
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


using _ControllerFeedback__ros_msg_type = planning_msgs__msg__ControllerFeedback;

static bool _ControllerFeedback__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ControllerFeedback__ros_msg_type * ros_message = static_cast<const _ControllerFeedback__ros_msg_type *>(untyped_ros_message);
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

  // Field name: actual_speed
  {
    cdr << ros_message->actual_speed;
  }

  // Field name: actual_steering_deg
  {
    cdr << ros_message->actual_steering_deg;
  }

  // Field name: cross_track_error
  {
    cdr << ros_message->cross_track_error;
  }

  // Field name: heading_error
  {
    cdr << ros_message->heading_error;
  }

  // Field name: brake_active
  {
    cdr << (ros_message->brake_active ? true : false);
  }

  // Field name: full_brake_active
  {
    cdr << (ros_message->full_brake_active ? true : false);
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

static bool _ControllerFeedback__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ControllerFeedback__ros_msg_type * ros_message = static_cast<_ControllerFeedback__ros_msg_type *>(untyped_ros_message);
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

  // Field name: actual_speed
  {
    cdr >> ros_message->actual_speed;
  }

  // Field name: actual_steering_deg
  {
    cdr >> ros_message->actual_steering_deg;
  }

  // Field name: cross_track_error
  {
    cdr >> ros_message->cross_track_error;
  }

  // Field name: heading_error
  {
    cdr >> ros_message->heading_error;
  }

  // Field name: brake_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->brake_active = tmp ? true : false;
  }

  // Field name: full_brake_active
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->full_brake_active = tmp ? true : false;
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

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_planning_msgs
size_t get_serialized_size_planning_msgs__msg__ControllerFeedback(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ControllerFeedback__ros_msg_type * ros_message = static_cast<const _ControllerFeedback__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name actual_speed
  {
    size_t item_size = sizeof(ros_message->actual_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name actual_steering_deg
  {
    size_t item_size = sizeof(ros_message->actual_steering_deg);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cross_track_error
  {
    size_t item_size = sizeof(ros_message->cross_track_error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name heading_error
  {
    size_t item_size = sizeof(ros_message->heading_error);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name brake_active
  {
    size_t item_size = sizeof(ros_message->brake_active);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name full_brake_active
  {
    size_t item_size = sizeof(ros_message->full_brake_active);
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

static uint32_t _ControllerFeedback__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_planning_msgs__msg__ControllerFeedback(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_planning_msgs
size_t max_serialized_size_planning_msgs__msg__ControllerFeedback(
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
  // member: actual_speed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: actual_steering_deg
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: cross_track_error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: heading_error
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: brake_active
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: full_brake_active
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

static size_t _ControllerFeedback__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_planning_msgs__msg__ControllerFeedback(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_ControllerFeedback = {
  "planning_msgs::msg",
  "ControllerFeedback",
  _ControllerFeedback__cdr_serialize,
  _ControllerFeedback__cdr_deserialize,
  _ControllerFeedback__get_serialized_size,
  _ControllerFeedback__max_serialized_size
};

static rosidl_message_type_support_t _ControllerFeedback__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ControllerFeedback,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, planning_msgs, msg, ControllerFeedback)() {
  return &_ControllerFeedback__type_support;
}

#if defined(__cplusplus)
}
#endif
