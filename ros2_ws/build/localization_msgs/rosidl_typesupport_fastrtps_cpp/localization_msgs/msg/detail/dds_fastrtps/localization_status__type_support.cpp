// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/localization_status__rosidl_typesupport_fastrtps_cpp.hpp"
#include "localization_msgs/msg/detail/localization_status__struct.hpp"

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


namespace localization_msgs
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
cdr_serialize(
  const localization_msgs::msg::LocalizationStatus & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.header,
    cdr);
  // Member: age_ms
  cdr << ros_message.age_ms;
  // Member: valid_until_ms
  cdr << ros_message.valid_until_ms;
  // Member: status
  cdr << ros_message.status;
  // Member: localization_confidence
  cdr << ros_message.localization_confidence;
  // Member: position_covariance
  cdr << ros_message.position_covariance;
  // Member: heading_covariance
  cdr << ros_message.heading_covariance;
  // Member: ndt_healthy
  cdr << (ros_message.ndt_healthy ? true : false);
  // Member: ndt_quality
  cdr << ros_message.ndt_quality;
  // Member: map_odom_stable
  cdr << (ros_message.map_odom_stable ? true : false);
  // Member: map_odom_drift
  cdr << ros_message.map_odom_drift;
  // Member: gps_available
  cdr << (ros_message.gps_available ? true : false);
  // Member: imu_available
  cdr << (ros_message.imu_available ? true : false);
  // Member: lidar_available
  cdr << (ros_message.lidar_available ? true : false);
  // Member: warning_flags
  {
    cdr << ros_message.warning_flags;
  }
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  localization_msgs::msg::LocalizationStatus & ros_message)
{
  // Member: header
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.header);

  // Member: age_ms
  cdr >> ros_message.age_ms;

  // Member: valid_until_ms
  cdr >> ros_message.valid_until_ms;

  // Member: status
  cdr >> ros_message.status;

  // Member: localization_confidence
  cdr >> ros_message.localization_confidence;

  // Member: position_covariance
  cdr >> ros_message.position_covariance;

  // Member: heading_covariance
  cdr >> ros_message.heading_covariance;

  // Member: ndt_healthy
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.ndt_healthy = tmp ? true : false;
  }

  // Member: ndt_quality
  cdr >> ros_message.ndt_quality;

  // Member: map_odom_stable
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.map_odom_stable = tmp ? true : false;
  }

  // Member: map_odom_drift
  cdr >> ros_message.map_odom_drift;

  // Member: gps_available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.gps_available = tmp ? true : false;
  }

  // Member: imu_available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.imu_available = tmp ? true : false;
  }

  // Member: lidar_available
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.lidar_available = tmp ? true : false;
  }

  // Member: warning_flags
  {
    cdr >> ros_message.warning_flags;
  }

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
get_serialized_size(
  const localization_msgs::msg::LocalizationStatus & ros_message,
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
  // Member: status
  {
    size_t item_size = sizeof(ros_message.status);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: localization_confidence
  {
    size_t item_size = sizeof(ros_message.localization_confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: position_covariance
  {
    size_t item_size = sizeof(ros_message.position_covariance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: heading_covariance
  {
    size_t item_size = sizeof(ros_message.heading_covariance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ndt_healthy
  {
    size_t item_size = sizeof(ros_message.ndt_healthy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: ndt_quality
  {
    size_t item_size = sizeof(ros_message.ndt_quality);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: map_odom_stable
  {
    size_t item_size = sizeof(ros_message.map_odom_stable);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: map_odom_drift
  {
    size_t item_size = sizeof(ros_message.map_odom_drift);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: gps_available
  {
    size_t item_size = sizeof(ros_message.gps_available);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: imu_available
  {
    size_t item_size = sizeof(ros_message.imu_available);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: lidar_available
  {
    size_t item_size = sizeof(ros_message.lidar_available);
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
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_localization_msgs
max_serialized_size_LocalizationStatus(
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

  // Member: status
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: localization_confidence
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: position_covariance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: heading_covariance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: ndt_healthy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: ndt_quality
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: map_odom_stable
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: map_odom_drift
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }

  // Member: gps_available
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: imu_available
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: lidar_available
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
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

static bool _LocalizationStatus__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const localization_msgs::msg::LocalizationStatus *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _LocalizationStatus__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<localization_msgs::msg::LocalizationStatus *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _LocalizationStatus__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const localization_msgs::msg::LocalizationStatus *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _LocalizationStatus__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_LocalizationStatus(full_bounded, 0);
}

static message_type_support_callbacks_t _LocalizationStatus__callbacks = {
  "localization_msgs::msg",
  "LocalizationStatus",
  _LocalizationStatus__cdr_serialize,
  _LocalizationStatus__cdr_deserialize,
  _LocalizationStatus__get_serialized_size,
  _LocalizationStatus__max_serialized_size
};

static rosidl_message_type_support_t _LocalizationStatus__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_LocalizationStatus__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace localization_msgs

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_localization_msgs
const rosidl_message_type_support_t *
get_message_type_support_handle<localization_msgs::msg::LocalizationStatus>()
{
  return &localization_msgs::msg::typesupport_fastrtps_cpp::_LocalizationStatus__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, localization_msgs, msg, LocalizationStatus)() {
  return &localization_msgs::msg::typesupport_fastrtps_cpp::_LocalizationStatus__handle;
}

#ifdef __cplusplus
}
#endif
