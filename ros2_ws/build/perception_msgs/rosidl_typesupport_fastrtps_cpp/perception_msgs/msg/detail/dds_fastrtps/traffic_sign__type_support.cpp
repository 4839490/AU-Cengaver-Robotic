// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/traffic_sign__rosidl_typesupport_fastrtps_cpp.hpp"
#include "perception_msgs/msg/detail/traffic_sign__struct.hpp"

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
  const perception_msgs::msg::TrafficSign & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: sign_id
  cdr << ros_message.sign_id;
  // Member: type
  cdr << ros_message.type;
  // Member: confidence
  cdr << ros_message.confidence;
  // Member: relevant_to_route
  cdr << (ros_message.relevant_to_route ? true : false);
  // Member: distance
  cdr << ros_message.distance;
  // Member: event_status
  cdr << ros_message.event_status;
  // Member: confirmed
  cdr << (ros_message.confirmed ? true : false);
  // Member: bbox_x
  cdr << ros_message.bbox_x;
  // Member: bbox_y
  cdr << ros_message.bbox_y;
  // Member: bbox_w
  cdr << ros_message.bbox_w;
  // Member: bbox_h
  cdr << ros_message.bbox_h;
  // Member: age_ms
  cdr << ros_message.age_ms;
  // Member: valid_until_ms
  cdr << ros_message.valid_until_ms;
  // Member: event_memory_ttl_ms
  cdr << ros_message.event_memory_ttl_ms;
  // Member: source_sensor
  cdr << ros_message.source_sensor;
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
  perception_msgs::msg::TrafficSign & ros_message)
{
  // Member: sign_id
  cdr >> ros_message.sign_id;

  // Member: type
  cdr >> ros_message.type;

  // Member: confidence
  cdr >> ros_message.confidence;

  // Member: relevant_to_route
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.relevant_to_route = tmp ? true : false;
  }

  // Member: distance
  cdr >> ros_message.distance;

  // Member: event_status
  cdr >> ros_message.event_status;

  // Member: confirmed
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.confirmed = tmp ? true : false;
  }

  // Member: bbox_x
  cdr >> ros_message.bbox_x;

  // Member: bbox_y
  cdr >> ros_message.bbox_y;

  // Member: bbox_w
  cdr >> ros_message.bbox_w;

  // Member: bbox_h
  cdr >> ros_message.bbox_h;

  // Member: age_ms
  cdr >> ros_message.age_ms;

  // Member: valid_until_ms
  cdr >> ros_message.valid_until_ms;

  // Member: event_memory_ttl_ms
  cdr >> ros_message.event_memory_ttl_ms;

  // Member: source_sensor
  cdr >> ros_message.source_sensor;

  // Member: warning_flags
  {
    cdr >> ros_message.warning_flags;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_perception_msgs
get_serialized_size(
  const perception_msgs::msg::TrafficSign & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: sign_id
  {
    size_t item_size = sizeof(ros_message.sign_id);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: type
  {
    size_t item_size = sizeof(ros_message.type);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: confidence
  {
    size_t item_size = sizeof(ros_message.confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: relevant_to_route
  {
    size_t item_size = sizeof(ros_message.relevant_to_route);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: distance
  {
    size_t item_size = sizeof(ros_message.distance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: event_status
  {
    size_t item_size = sizeof(ros_message.event_status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: confirmed
  {
    size_t item_size = sizeof(ros_message.confirmed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bbox_x
  {
    size_t item_size = sizeof(ros_message.bbox_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bbox_y
  {
    size_t item_size = sizeof(ros_message.bbox_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bbox_w
  {
    size_t item_size = sizeof(ros_message.bbox_w);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: bbox_h
  {
    size_t item_size = sizeof(ros_message.bbox_h);
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
  // Member: event_memory_ttl_ms
  {
    size_t item_size = sizeof(ros_message.event_memory_ttl_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: source_sensor
  current_alignment += padding +
    eprosima::fastcdr::Cdr::alignment(current_alignment, padding) +
    (ros_message.source_sensor.size() + 1);
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
max_serialized_size_TrafficSign(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: sign_id
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: type
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

  // Member: relevant_to_route
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: distance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: event_status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: confirmed
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: bbox_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: bbox_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: bbox_w
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: bbox_h
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

  // Member: event_memory_ttl_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
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

static bool _TrafficSign__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const perception_msgs::msg::TrafficSign *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _TrafficSign__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<perception_msgs::msg::TrafficSign *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _TrafficSign__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const perception_msgs::msg::TrafficSign *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _TrafficSign__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_TrafficSign(full_bounded, 0);
}

static message_type_support_callbacks_t _TrafficSign__callbacks = {
  "perception_msgs::msg",
  "TrafficSign",
  _TrafficSign__cdr_serialize,
  _TrafficSign__cdr_deserialize,
  _TrafficSign__get_serialized_size,
  _TrafficSign__max_serialized_size
};

static rosidl_message_type_support_t _TrafficSign__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_TrafficSign__callbacks,
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
get_message_type_support_handle<perception_msgs::msg::TrafficSign>()
{
  return &perception_msgs::msg::typesupport_fastrtps_cpp::_TrafficSign__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, perception_msgs, msg, TrafficSign)() {
  return &perception_msgs::msg::typesupport_fastrtps_cpp::_TrafficSign__handle;
}

#ifdef __cplusplus
}
#endif
