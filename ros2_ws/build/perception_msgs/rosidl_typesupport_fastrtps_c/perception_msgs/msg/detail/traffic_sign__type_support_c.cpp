// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/traffic_sign__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "perception_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "perception_msgs/msg/detail/traffic_sign__struct.h"
#include "perception_msgs/msg/detail/traffic_sign__functions.h"
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

#include "rosidl_runtime_c/string.h"  // source_sensor, warning_flags
#include "rosidl_runtime_c/string_functions.h"  // source_sensor, warning_flags

// forward declare type support functions


using _TrafficSign__ros_msg_type = perception_msgs__msg__TrafficSign;

static bool _TrafficSign__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _TrafficSign__ros_msg_type * ros_message = static_cast<const _TrafficSign__ros_msg_type *>(untyped_ros_message);
  // Field name: sign_id
  {
    cdr << ros_message->sign_id;
  }

  // Field name: type
  {
    cdr << ros_message->type;
  }

  // Field name: confidence
  {
    cdr << ros_message->confidence;
  }

  // Field name: relevant_to_route
  {
    cdr << (ros_message->relevant_to_route ? true : false);
  }

  // Field name: distance
  {
    cdr << ros_message->distance;
  }

  // Field name: event_status
  {
    cdr << ros_message->event_status;
  }

  // Field name: confirmed
  {
    cdr << (ros_message->confirmed ? true : false);
  }

  // Field name: bbox_x
  {
    cdr << ros_message->bbox_x;
  }

  // Field name: bbox_y
  {
    cdr << ros_message->bbox_y;
  }

  // Field name: bbox_w
  {
    cdr << ros_message->bbox_w;
  }

  // Field name: bbox_h
  {
    cdr << ros_message->bbox_h;
  }

  // Field name: age_ms
  {
    cdr << ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr << ros_message->valid_until_ms;
  }

  // Field name: event_memory_ttl_ms
  {
    cdr << ros_message->event_memory_ttl_ms;
  }

  // Field name: source_sensor
  {
    const rosidl_runtime_c__String * str = &ros_message->source_sensor;
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

static bool _TrafficSign__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _TrafficSign__ros_msg_type * ros_message = static_cast<_TrafficSign__ros_msg_type *>(untyped_ros_message);
  // Field name: sign_id
  {
    cdr >> ros_message->sign_id;
  }

  // Field name: type
  {
    cdr >> ros_message->type;
  }

  // Field name: confidence
  {
    cdr >> ros_message->confidence;
  }

  // Field name: relevant_to_route
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->relevant_to_route = tmp ? true : false;
  }

  // Field name: distance
  {
    cdr >> ros_message->distance;
  }

  // Field name: event_status
  {
    cdr >> ros_message->event_status;
  }

  // Field name: confirmed
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->confirmed = tmp ? true : false;
  }

  // Field name: bbox_x
  {
    cdr >> ros_message->bbox_x;
  }

  // Field name: bbox_y
  {
    cdr >> ros_message->bbox_y;
  }

  // Field name: bbox_w
  {
    cdr >> ros_message->bbox_w;
  }

  // Field name: bbox_h
  {
    cdr >> ros_message->bbox_h;
  }

  // Field name: age_ms
  {
    cdr >> ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr >> ros_message->valid_until_ms;
  }

  // Field name: event_memory_ttl_ms
  {
    cdr >> ros_message->event_memory_ttl_ms;
  }

  // Field name: source_sensor
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->source_sensor.data) {
      rosidl_runtime_c__String__init(&ros_message->source_sensor);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->source_sensor,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'source_sensor'\n");
      return false;
    }
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

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_perception_msgs
size_t get_serialized_size_perception_msgs__msg__TrafficSign(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _TrafficSign__ros_msg_type * ros_message = static_cast<const _TrafficSign__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name sign_id
  {
    size_t item_size = sizeof(ros_message->sign_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name type
  {
    size_t item_size = sizeof(ros_message->type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name confidence
  {
    size_t item_size = sizeof(ros_message->confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name relevant_to_route
  {
    size_t item_size = sizeof(ros_message->relevant_to_route);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name distance
  {
    size_t item_size = sizeof(ros_message->distance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name event_status
  {
    size_t item_size = sizeof(ros_message->event_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name confirmed
  {
    size_t item_size = sizeof(ros_message->confirmed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bbox_x
  {
    size_t item_size = sizeof(ros_message->bbox_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bbox_y
  {
    size_t item_size = sizeof(ros_message->bbox_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bbox_w
  {
    size_t item_size = sizeof(ros_message->bbox_w);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name bbox_h
  {
    size_t item_size = sizeof(ros_message->bbox_h);
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
  // field.name event_memory_ttl_ms
  {
    size_t item_size = sizeof(ros_message->event_memory_ttl_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name source_sensor
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->source_sensor.size + 1);
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

static uint32_t _TrafficSign__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_perception_msgs__msg__TrafficSign(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_perception_msgs
size_t max_serialized_size_perception_msgs__msg__TrafficSign(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: sign_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: confidence
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: relevant_to_route
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: distance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: event_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: confirmed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: bbox_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: bbox_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: bbox_w
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: bbox_h
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
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
  // member: event_memory_ttl_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: source_sensor
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
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

static size_t _TrafficSign__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_perception_msgs__msg__TrafficSign(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_TrafficSign = {
  "perception_msgs::msg",
  "TrafficSign",
  _TrafficSign__cdr_serialize,
  _TrafficSign__cdr_deserialize,
  _TrafficSign__get_serialized_size,
  _TrafficSign__max_serialized_size
};

static rosidl_message_type_support_t _TrafficSign__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_TrafficSign,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, perception_msgs, msg, TrafficSign)() {
  return &_TrafficSign__type_support;
}

#if defined(__cplusplus)
}
#endif
