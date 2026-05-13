// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/obstacle_track__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "perception_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "perception_msgs/msg/detail/obstacle_track__struct.h"
#include "perception_msgs/msg/detail/obstacle_track__functions.h"
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

#include "rosidl_runtime_c/string.h"  // geometry_source, semantic_source, source_sensor, warning_flags
#include "rosidl_runtime_c/string_functions.h"  // geometry_source, semantic_source, source_sensor, warning_flags

// forward declare type support functions


using _ObstacleTrack__ros_msg_type = perception_msgs__msg__ObstacleTrack;

static bool _ObstacleTrack__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ObstacleTrack__ros_msg_type * ros_message = static_cast<const _ObstacleTrack__ros_msg_type *>(untyped_ros_message);
  // Field name: track_id
  {
    cdr << ros_message->track_id;
  }

  // Field name: class_label
  {
    cdr << ros_message->class_label;
  }

  // Field name: confidence
  {
    cdr << ros_message->confidence;
  }

  // Field name: position_x
  {
    cdr << ros_message->position_x;
  }

  // Field name: position_y
  {
    cdr << ros_message->position_y;
  }

  // Field name: distance
  {
    cdr << ros_message->distance;
  }

  // Field name: velocity_x
  {
    cdr << ros_message->velocity_x;
  }

  // Field name: velocity_y
  {
    cdr << ros_message->velocity_y;
  }

  // Field name: ttc
  {
    cdr << ros_message->ttc;
  }

  // Field name: width
  {
    cdr << ros_message->width;
  }

  // Field name: length
  {
    cdr << ros_message->length;
  }

  // Field name: height
  {
    cdr << ros_message->height;
  }

  // Field name: is_static
  {
    cdr << (ros_message->is_static ? true : false);
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

  // Field name: semantic_source
  {
    const rosidl_runtime_c__String * str = &ros_message->semantic_source;
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

  // Field name: geometry_source
  {
    const rosidl_runtime_c__String * str = &ros_message->geometry_source;
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

static bool _ObstacleTrack__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ObstacleTrack__ros_msg_type * ros_message = static_cast<_ObstacleTrack__ros_msg_type *>(untyped_ros_message);
  // Field name: track_id
  {
    cdr >> ros_message->track_id;
  }

  // Field name: class_label
  {
    cdr >> ros_message->class_label;
  }

  // Field name: confidence
  {
    cdr >> ros_message->confidence;
  }

  // Field name: position_x
  {
    cdr >> ros_message->position_x;
  }

  // Field name: position_y
  {
    cdr >> ros_message->position_y;
  }

  // Field name: distance
  {
    cdr >> ros_message->distance;
  }

  // Field name: velocity_x
  {
    cdr >> ros_message->velocity_x;
  }

  // Field name: velocity_y
  {
    cdr >> ros_message->velocity_y;
  }

  // Field name: ttc
  {
    cdr >> ros_message->ttc;
  }

  // Field name: width
  {
    cdr >> ros_message->width;
  }

  // Field name: length
  {
    cdr >> ros_message->length;
  }

  // Field name: height
  {
    cdr >> ros_message->height;
  }

  // Field name: is_static
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->is_static = tmp ? true : false;
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

  // Field name: semantic_source
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->semantic_source.data) {
      rosidl_runtime_c__String__init(&ros_message->semantic_source);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->semantic_source,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'semantic_source'\n");
      return false;
    }
  }

  // Field name: geometry_source
  {
    std::string tmp;
    cdr >> tmp;
    if (!ros_message->geometry_source.data) {
      rosidl_runtime_c__String__init(&ros_message->geometry_source);
    }
    bool succeeded = rosidl_runtime_c__String__assign(
      &ros_message->geometry_source,
      tmp.c_str());
    if (!succeeded) {
      fprintf(stderr, "failed to assign string into field 'geometry_source'\n");
      return false;
    }
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

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_perception_msgs
size_t get_serialized_size_perception_msgs__msg__ObstacleTrack(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ObstacleTrack__ros_msg_type * ros_message = static_cast<const _ObstacleTrack__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name track_id
  {
    size_t item_size = sizeof(ros_message->track_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name class_label
  {
    size_t item_size = sizeof(ros_message->class_label);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name confidence
  {
    size_t item_size = sizeof(ros_message->confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position_x
  {
    size_t item_size = sizeof(ros_message->position_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position_y
  {
    size_t item_size = sizeof(ros_message->position_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name distance
  {
    size_t item_size = sizeof(ros_message->distance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity_x
  {
    size_t item_size = sizeof(ros_message->velocity_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name velocity_y
  {
    size_t item_size = sizeof(ros_message->velocity_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ttc
  {
    size_t item_size = sizeof(ros_message->ttc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name width
  {
    size_t item_size = sizeof(ros_message->width);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name length
  {
    size_t item_size = sizeof(ros_message->length);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name height
  {
    size_t item_size = sizeof(ros_message->height);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name is_static
  {
    size_t item_size = sizeof(ros_message->is_static);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name source_sensor
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->source_sensor.size + 1);
  // field.name semantic_source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->semantic_source.size + 1);
  // field.name geometry_source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message->geometry_source.size + 1);
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

static uint32_t _ObstacleTrack__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_perception_msgs__msg__ObstacleTrack(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_perception_msgs
size_t max_serialized_size_perception_msgs__msg__ObstacleTrack(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: track_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: class_label
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
  // member: position_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: position_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: distance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: velocity_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: velocity_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: ttc
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: width
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: length
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: height
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: is_static
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
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
  // member: semantic_source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }
  // member: geometry_source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
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

static size_t _ObstacleTrack__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_perception_msgs__msg__ObstacleTrack(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_ObstacleTrack = {
  "perception_msgs::msg",
  "ObstacleTrack",
  _ObstacleTrack__cdr_serialize,
  _ObstacleTrack__cdr_deserialize,
  _ObstacleTrack__get_serialized_size,
  _ObstacleTrack__max_serialized_size
};

static rosidl_message_type_support_t _ObstacleTrack__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ObstacleTrack,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, perception_msgs, msg, ObstacleTrack)() {
  return &_ObstacleTrack__type_support;
}

#if defined(__cplusplus)
}
#endif
