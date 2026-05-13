// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/obstacle_track__rosidl_typesupport_fastrtps_cpp.hpp"
#include "perception_msgs/msg/detail/obstacle_track__struct.hpp"

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

namespace perception_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_perception_msgs
cdr_serialize(
  const perception_msgs::msg::ObstacleTrack & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: track_id
  cdr << ros_message.track_id;
  // Member: class_label
  cdr << ros_message.class_label;
  // Member: confidence
  cdr << ros_message.confidence;
  // Member: position_x
  cdr << ros_message.position_x;
  // Member: position_y
  cdr << ros_message.position_y;
  // Member: distance
  cdr << ros_message.distance;
  // Member: velocity_x
  cdr << ros_message.velocity_x;
  // Member: velocity_y
  cdr << ros_message.velocity_y;
  // Member: ttc
  cdr << ros_message.ttc;
  // Member: width
  cdr << ros_message.width;
  // Member: length
  cdr << ros_message.length;
  // Member: height
  cdr << ros_message.height;
  // Member: is_static
  cdr << (ros_message.is_static ? true : false);
  // Member: source_sensor
  cdr << ros_message.source_sensor;
  // Member: semantic_source
  cdr << ros_message.semantic_source;
  // Member: geometry_source
  cdr << ros_message.geometry_source;
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
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_perception_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  perception_msgs::msg::ObstacleTrack & ros_message)
{
  // Member: track_id
  cdr >> ros_message.track_id;

  // Member: class_label
  cdr >> ros_message.class_label;

  // Member: confidence
  cdr >> ros_message.confidence;

  // Member: position_x
  cdr >> ros_message.position_x;

  // Member: position_y
  cdr >> ros_message.position_y;

  // Member: distance
  cdr >> ros_message.distance;

  // Member: velocity_x
  cdr >> ros_message.velocity_x;

  // Member: velocity_y
  cdr >> ros_message.velocity_y;

  // Member: ttc
  cdr >> ros_message.ttc;

  // Member: width
  cdr >> ros_message.width;

  // Member: length
  cdr >> ros_message.length;

  // Member: height
  cdr >> ros_message.height;

  // Member: is_static
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.is_static = tmp ? true : false;
  }

  // Member: source_sensor
  cdr >> ros_message.source_sensor;

  // Member: semantic_source
  cdr >> ros_message.semantic_source;

  // Member: geometry_source
  cdr >> ros_message.geometry_source;

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
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_perception_msgs
get_serialized_size(
  const perception_msgs::msg::ObstacleTrack & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: track_id
  {
    size_t item_size = sizeof(ros_message.track_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: class_label
  {
    size_t item_size = sizeof(ros_message.class_label);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: confidence
  {
    size_t item_size = sizeof(ros_message.confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position_x
  {
    size_t item_size = sizeof(ros_message.position_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position_y
  {
    size_t item_size = sizeof(ros_message.position_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance
  {
    size_t item_size = sizeof(ros_message.distance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity_x
  {
    size_t item_size = sizeof(ros_message.velocity_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: velocity_y
  {
    size_t item_size = sizeof(ros_message.velocity_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ttc
  {
    size_t item_size = sizeof(ros_message.ttc);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: width
  {
    size_t item_size = sizeof(ros_message.width);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: length
  {
    size_t item_size = sizeof(ros_message.length);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: height
  {
    size_t item_size = sizeof(ros_message.height);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: is_static
  {
    size_t item_size = sizeof(ros_message.is_static);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: source_sensor
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.source_sensor.size() + 1);
  // Member: semantic_source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.semantic_source.size() + 1);
  // Member: geometry_source
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.geometry_source.size() + 1);
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
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_perception_msgs
max_serialized_size_ObstacleTrack(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: track_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: class_label
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: confidence
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: position_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: position_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: distance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: velocity_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: velocity_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: ttc
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: width
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: length
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: height
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: is_static
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: source_sensor
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: semantic_source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
  }

  // Member: geometry_source
  {
    size_t array_size = 1;

    full_bounded = false;
    for (size_t index = 0; index < array_size; ++index) {
      current_alignment += padding +
        eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
        1;
    }
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

static bool _ObstacleTrack__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const perception_msgs::msg::ObstacleTrack *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ObstacleTrack__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<perception_msgs::msg::ObstacleTrack *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ObstacleTrack__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const perception_msgs::msg::ObstacleTrack *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ObstacleTrack__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ObstacleTrack(full_bounded, 0);
}

static message_type_support_callbacks_t _ObstacleTrack__callbacks = {
  "perception_msgs::msg",
  "ObstacleTrack",
  _ObstacleTrack__cdr_serialize,
  _ObstacleTrack__cdr_deserialize,
  _ObstacleTrack__get_serialized_size,
  _ObstacleTrack__max_serialized_size
};

static rosidl_message_type_support_t _ObstacleTrack__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ObstacleTrack__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace perception_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_perception_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<perception_msgs::msg::ObstacleTrack>()
{
  return &perception_msgs::msg::typesupport_fastrtps_cpp::_ObstacleTrack__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, perception_msgs, msg, ObstacleTrack)() {
  return &perception_msgs::msg::typesupport_fastrtps_cpp::_ObstacleTrack__handle;
}

#ifdef __cplusplus
}
#endif
