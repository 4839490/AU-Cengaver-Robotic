// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/map_origin__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "localization_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "localization_msgs/msg/detail/map_origin__struct.h"
#include "localization_msgs/msg/detail/map_origin__functions.h"
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

#include "rosidl_runtime_c/string.h"  // source
#include "rosidl_runtime_c/string_functions.h"  // source
#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_localization_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_localization_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_localization_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _MapOrigin__ros_msg_type = localization_msgs__msg__MapOrigin;

static bool _MapOrigin__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _MapOrigin__ros_msg_type * ros_message = static_cast<const _MapOrigin__ros_msg_type *>(untyped_ros_message);
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

  // Field name: lat_ref
  {
    cdr << ros_message->lat_ref;
  }

  // Field name: lon_ref
  {
    cdr << ros_message->lon_ref;
  }

  // Field name: alt_ref
  {
    cdr << ros_message->alt_ref;
  }

  // Field name: yaw_ref
  {
    cdr << ros_message->yaw_ref;
  }

  // Field name: source
  {
    const rosidl_runtime_c__String * str = &ros_message->source;
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

  // Field name: locked
  {
    cdr << (ros_message->locked ? true : false);
  }

  return true;
}

static bool _MapOrigin__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _MapOrigin__ros_msg_type * ros_message = static_cast<_MapOrigin__ros_msg_type *>(untyped_ros_message);
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

  // Field name: lat_ref
  {
    cdr >> ros_message->lat_ref;
  }

  // Field name: lon_ref
  {
    cdr >> ros_message->lon_ref;
  }

  // Field name: alt_ref
  {
    cdr >> ros_message->alt_ref;
  }

  // Field name: yaw_ref
  {
    cdr >> ros_message->yaw_ref;
  }

  // Field name: source
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->source.data) {
      rosidl_runtime_c__String__init(&ros_message->source);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->source,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'source'\n");
      return false;
    }
  }

  // Field name: locked
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->locked = tmp ? true : false;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_localization_msgs
size_t get_serialized_size_localization_msgs__msg__MapOrigin(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _MapOrigin__ros_msg_type * ros_message = static_cast<const _MapOrigin__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name lat_ref
  {
    size_t item_size = sizeof(ros_message->lat_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name lon_ref
  {
    size_t item_size = sizeof(ros_message->lon_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name alt_ref
  {
    size_t item_size = sizeof(ros_message->alt_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name yaw_ref
  {
    size_t item_size = sizeof(ros_message->yaw_ref);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->source.size + 1);
  // field.name locked
  {
    size_t item_size = sizeof(ros_message->locked);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _MapOrigin__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_localization_msgs__msg__MapOrigin(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_localization_msgs
size_t max_serialized_size_localization_msgs__msg__MapOrigin(
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
  // member: lat_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: lon_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: alt_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: yaw_ref
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: locked
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _MapOrigin__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_localization_msgs__msg__MapOrigin(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_MapOrigin = {
  "localization_msgs::msg",
  "MapOrigin",
  _MapOrigin__cdr_serialize,
  _MapOrigin__cdr_deserialize,
  _MapOrigin__get_serialized_size,
  _MapOrigin__max_serialized_size
};

static rosidl_message_type_support_t _MapOrigin__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_MapOrigin,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, localization_msgs, msg, MapOrigin)() {
  return &_MapOrigin__type_support;
}

#if defined(__cplusplus)
}
#endif
