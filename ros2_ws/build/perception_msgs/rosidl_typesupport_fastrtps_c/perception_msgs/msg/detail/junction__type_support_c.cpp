// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from perception_msgs:msg/Junction.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/junction__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "perception_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "perception_msgs/msg/detail/junction__struct.h"
#include "perception_msgs/msg/detail/junction__functions.h"
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
#include "std_msgs/msg/detail/header__functions.h"  // header

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_perception_msgs
size_t get_serialized_size_std_msgs__msg__Header(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_perception_msgs
size_t max_serialized_size_std_msgs__msg__Header(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_perception_msgs
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, Header)();


using _Junction__ros_msg_type = perception_msgs__msg__Junction;

static bool _Junction__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _Junction__ros_msg_type * ros_message = static_cast<const _Junction__ros_msg_type *>(untyped_ros_message);
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

  // Field name: detected
  {
    cdr << (ros_message->detected ? true : false);
  }

  // Field name: junction_type
  {
    cdr << ros_message->junction_type;
  }

  // Field name: arm_count
  {
    cdr << ros_message->arm_count;
  }

  // Field name: distance_to_entry
  {
    cdr << ros_message->distance_to_entry;
  }

  // Field name: confidence
  {
    cdr << ros_message->confidence;
  }

  // Field name: age_ms
  {
    cdr << ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr << ros_message->valid_until_ms;
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

static bool _Junction__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _Junction__ros_msg_type * ros_message = static_cast<_Junction__ros_msg_type *>(untyped_ros_message);
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

  // Field name: detected
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->detected = tmp ? true : false;
  }

  // Field name: junction_type
  {
    cdr >> ros_message->junction_type;
  }

  // Field name: arm_count
  {
    cdr >> ros_message->arm_count;
  }

  // Field name: distance_to_entry
  {
    cdr >> ros_message->distance_to_entry;
  }

  // Field name: confidence
  {
    cdr >> ros_message->confidence;
  }

  // Field name: age_ms
  {
    cdr >> ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr >> ros_message->valid_until_ms;
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
size_t get_serialized_size_perception_msgs__msg__Junction(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _Junction__ros_msg_type * ros_message = static_cast<const _Junction__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
  // field.name detected
  {
    size_t item_size = sizeof(ros_message->detected);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name junction_type
  {
    size_t item_size = sizeof(ros_message->junction_type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name arm_count
  {
    size_t item_size = sizeof(ros_message->arm_count);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name distance_to_entry
  {
    size_t item_size = sizeof(ros_message->distance_to_entry);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name confidence
  {
    size_t item_size = sizeof(ros_message->confidence);
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

static uint32_t _Junction__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_perception_msgs__msg__Junction(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_perception_msgs
size_t max_serialized_size_perception_msgs__msg__Junction(
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
  // member: detected
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: junction_type
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: arm_count
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: distance_to_entry
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: confidence
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

static size_t _Junction__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_perception_msgs__msg__Junction(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_Junction = {
  "perception_msgs::msg",
  "Junction",
  _Junction__cdr_serialize,
  _Junction__cdr_deserialize,
  _Junction__get_serialized_size,
  _Junction__max_serialized_size
};

static rosidl_message_type_support_t _Junction__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_Junction,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, perception_msgs, msg, Junction)() {
  return &_Junction__type_support;
}

#if defined(__cplusplus)
}
#endif
