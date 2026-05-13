// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from localization_msgs:msg/LocalizationDiagnostics.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/localization_diagnostics__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "localization_msgs/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "localization_msgs/msg/detail/localization_diagnostics__struct.h"
#include "localization_msgs/msg/detail/localization_diagnostics__functions.h"
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


using _LocalizationDiagnostics__ros_msg_type = localization_msgs__msg__LocalizationDiagnostics;

static bool _LocalizationDiagnostics__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _LocalizationDiagnostics__ros_msg_type * ros_message = static_cast<const _LocalizationDiagnostics__ros_msg_type *>(untyped_ros_message);
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

  // Field name: age_ms
  {
    cdr << ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr << ros_message->valid_until_ms;
  }

  // Field name: ekf_output_hz
  {
    cdr << ros_message->ekf_output_hz;
  }

  // Field name: gps_input_hz
  {
    cdr << ros_message->gps_input_hz;
  }

  // Field name: imu_input_hz
  {
    cdr << ros_message->imu_input_hz;
  }

  // Field name: ndt_output_hz
  {
    cdr << ros_message->ndt_output_hz;
  }

  // Field name: ekf_latency_ms
  {
    cdr << ros_message->ekf_latency_ms;
  }

  // Field name: ndt_latency_ms
  {
    cdr << ros_message->ndt_latency_ms;
  }

  // Field name: position_covariance
  {
    cdr << ros_message->position_covariance;
  }

  // Field name: heading_covariance
  {
    cdr << ros_message->heading_covariance;
  }

  // Field name: ndt_quality
  {
    cdr << ros_message->ndt_quality;
  }

  // Field name: ekf_healthy
  {
    cdr << (ros_message->ekf_healthy ? true : false);
  }

  // Field name: gps_healthy
  {
    cdr << (ros_message->gps_healthy ? true : false);
  }

  // Field name: imu_healthy
  {
    cdr << (ros_message->imu_healthy ? true : false);
  }

  // Field name: ndt_healthy
  {
    cdr << (ros_message->ndt_healthy ? true : false);
  }

  // Field name: map_odom_stable
  {
    cdr << (ros_message->map_odom_stable ? true : false);
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

static bool _LocalizationDiagnostics__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _LocalizationDiagnostics__ros_msg_type * ros_message = static_cast<_LocalizationDiagnostics__ros_msg_type *>(untyped_ros_message);
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

  // Field name: age_ms
  {
    cdr >> ros_message->age_ms;
  }

  // Field name: valid_until_ms
  {
    cdr >> ros_message->valid_until_ms;
  }

  // Field name: ekf_output_hz
  {
    cdr >> ros_message->ekf_output_hz;
  }

  // Field name: gps_input_hz
  {
    cdr >> ros_message->gps_input_hz;
  }

  // Field name: imu_input_hz
  {
    cdr >> ros_message->imu_input_hz;
  }

  // Field name: ndt_output_hz
  {
    cdr >> ros_message->ndt_output_hz;
  }

  // Field name: ekf_latency_ms
  {
    cdr >> ros_message->ekf_latency_ms;
  }

  // Field name: ndt_latency_ms
  {
    cdr >> ros_message->ndt_latency_ms;
  }

  // Field name: position_covariance
  {
    cdr >> ros_message->position_covariance;
  }

  // Field name: heading_covariance
  {
    cdr >> ros_message->heading_covariance;
  }

  // Field name: ndt_quality
  {
    cdr >> ros_message->ndt_quality;
  }

  // Field name: ekf_healthy
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->ekf_healthy = tmp ? true : false;
  }

  // Field name: gps_healthy
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->gps_healthy = tmp ? true : false;
  }

  // Field name: imu_healthy
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->imu_healthy = tmp ? true : false;
  }

  // Field name: ndt_healthy
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->ndt_healthy = tmp ? true : false;
  }

  // Field name: map_odom_stable
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->map_odom_stable = tmp ? true : false;
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

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_localization_msgs
size_t get_serialized_size_localization_msgs__msg__LocalizationDiagnostics(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _LocalizationDiagnostics__ros_msg_type * ros_message = static_cast<const _LocalizationDiagnostics__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name header

  current_alignment += get_serialized_size_std_msgs__msg__Header(
    &(ros_message->header), current_alignment);
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
  // field.name ekf_output_hz
  {
    size_t item_size = sizeof(ros_message->ekf_output_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gps_input_hz
  {
    size_t item_size = sizeof(ros_message->gps_input_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name imu_input_hz
  {
    size_t item_size = sizeof(ros_message->imu_input_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ndt_output_hz
  {
    size_t item_size = sizeof(ros_message->ndt_output_hz);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ekf_latency_ms
  {
    size_t item_size = sizeof(ros_message->ekf_latency_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ndt_latency_ms
  {
    size_t item_size = sizeof(ros_message->ndt_latency_ms);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name position_covariance
  {
    size_t item_size = sizeof(ros_message->position_covariance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name heading_covariance
  {
    size_t item_size = sizeof(ros_message->heading_covariance);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ndt_quality
  {
    size_t item_size = sizeof(ros_message->ndt_quality);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ekf_healthy
  {
    size_t item_size = sizeof(ros_message->ekf_healthy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name gps_healthy
  {
    size_t item_size = sizeof(ros_message->gps_healthy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name imu_healthy
  {
    size_t item_size = sizeof(ros_message->imu_healthy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name ndt_healthy
  {
    size_t item_size = sizeof(ros_message->ndt_healthy);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name map_odom_stable
  {
    size_t item_size = sizeof(ros_message->map_odom_stable);
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

static uint32_t _LocalizationDiagnostics__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_localization_msgs__msg__LocalizationDiagnostics(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_localization_msgs
size_t max_serialized_size_localization_msgs__msg__LocalizationDiagnostics(
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
  // member: ekf_output_hz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: gps_input_hz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: imu_input_hz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ndt_output_hz
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ekf_latency_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ndt_latency_ms
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: position_covariance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: heading_covariance
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ndt_quality
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: ekf_healthy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: gps_healthy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: imu_healthy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: ndt_healthy
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: map_odom_stable
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
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

static size_t _LocalizationDiagnostics__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_localization_msgs__msg__LocalizationDiagnostics(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_LocalizationDiagnostics = {
  "localization_msgs::msg",
  "LocalizationDiagnostics",
  _LocalizationDiagnostics__cdr_serialize,
  _LocalizationDiagnostics__cdr_deserialize,
  _LocalizationDiagnostics__get_serialized_size,
  _LocalizationDiagnostics__max_serialized_size
};

static rosidl_message_type_support_t _LocalizationDiagnostics__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_LocalizationDiagnostics,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, localization_msgs, msg, LocalizationDiagnostics)() {
  return &_LocalizationDiagnostics__type_support;
}

#if defined(__cplusplus)
}
#endif
