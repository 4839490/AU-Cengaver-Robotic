// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from localization_msgs:msg/LocalizationDiagnostics.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/localization_diagnostics__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
localization_msgs__msg__LocalizationDiagnostics__init(localization_msgs__msg__LocalizationDiagnostics * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    localization_msgs__msg__LocalizationDiagnostics__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // ekf_output_hz
  // gps_input_hz
  // imu_input_hz
  // ndt_output_hz
  // ekf_latency_ms
  // ndt_latency_ms
  // position_covariance
  // heading_covariance
  // ndt_quality
  // ekf_healthy
  // gps_healthy
  // imu_healthy
  // ndt_healthy
  // map_odom_stable
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    localization_msgs__msg__LocalizationDiagnostics__fini(msg);
    return false;
  }
  return true;
}

void
localization_msgs__msg__LocalizationDiagnostics__fini(localization_msgs__msg__LocalizationDiagnostics * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // age_ms
  // valid_until_ms
  // ekf_output_hz
  // gps_input_hz
  // imu_input_hz
  // ndt_output_hz
  // ekf_latency_ms
  // ndt_latency_ms
  // position_covariance
  // heading_covariance
  // ndt_quality
  // ekf_healthy
  // gps_healthy
  // imu_healthy
  // ndt_healthy
  // map_odom_stable
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
localization_msgs__msg__LocalizationDiagnostics__are_equal(const localization_msgs__msg__LocalizationDiagnostics * lhs, const localization_msgs__msg__LocalizationDiagnostics * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // age_ms
  if (lhs->age_ms != rhs->age_ms) {
    return false;
  }
  // valid_until_ms
  if (lhs->valid_until_ms != rhs->valid_until_ms) {
    return false;
  }
  // ekf_output_hz
  if (lhs->ekf_output_hz != rhs->ekf_output_hz) {
    return false;
  }
  // gps_input_hz
  if (lhs->gps_input_hz != rhs->gps_input_hz) {
    return false;
  }
  // imu_input_hz
  if (lhs->imu_input_hz != rhs->imu_input_hz) {
    return false;
  }
  // ndt_output_hz
  if (lhs->ndt_output_hz != rhs->ndt_output_hz) {
    return false;
  }
  // ekf_latency_ms
  if (lhs->ekf_latency_ms != rhs->ekf_latency_ms) {
    return false;
  }
  // ndt_latency_ms
  if (lhs->ndt_latency_ms != rhs->ndt_latency_ms) {
    return false;
  }
  // position_covariance
  if (lhs->position_covariance != rhs->position_covariance) {
    return false;
  }
  // heading_covariance
  if (lhs->heading_covariance != rhs->heading_covariance) {
    return false;
  }
  // ndt_quality
  if (lhs->ndt_quality != rhs->ndt_quality) {
    return false;
  }
  // ekf_healthy
  if (lhs->ekf_healthy != rhs->ekf_healthy) {
    return false;
  }
  // gps_healthy
  if (lhs->gps_healthy != rhs->gps_healthy) {
    return false;
  }
  // imu_healthy
  if (lhs->imu_healthy != rhs->imu_healthy) {
    return false;
  }
  // ndt_healthy
  if (lhs->ndt_healthy != rhs->ndt_healthy) {
    return false;
  }
  // map_odom_stable
  if (lhs->map_odom_stable != rhs->map_odom_stable) {
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->warning_flags), &(rhs->warning_flags)))
  {
    return false;
  }
  return true;
}

bool
localization_msgs__msg__LocalizationDiagnostics__copy(
  const localization_msgs__msg__LocalizationDiagnostics * input,
  localization_msgs__msg__LocalizationDiagnostics * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  // ekf_output_hz
  output->ekf_output_hz = input->ekf_output_hz;
  // gps_input_hz
  output->gps_input_hz = input->gps_input_hz;
  // imu_input_hz
  output->imu_input_hz = input->imu_input_hz;
  // ndt_output_hz
  output->ndt_output_hz = input->ndt_output_hz;
  // ekf_latency_ms
  output->ekf_latency_ms = input->ekf_latency_ms;
  // ndt_latency_ms
  output->ndt_latency_ms = input->ndt_latency_ms;
  // position_covariance
  output->position_covariance = input->position_covariance;
  // heading_covariance
  output->heading_covariance = input->heading_covariance;
  // ndt_quality
  output->ndt_quality = input->ndt_quality;
  // ekf_healthy
  output->ekf_healthy = input->ekf_healthy;
  // gps_healthy
  output->gps_healthy = input->gps_healthy;
  // imu_healthy
  output->imu_healthy = input->imu_healthy;
  // ndt_healthy
  output->ndt_healthy = input->ndt_healthy;
  // map_odom_stable
  output->map_odom_stable = input->map_odom_stable;
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

localization_msgs__msg__LocalizationDiagnostics *
localization_msgs__msg__LocalizationDiagnostics__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationDiagnostics * msg = (localization_msgs__msg__LocalizationDiagnostics *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationDiagnostics), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(localization_msgs__msg__LocalizationDiagnostics));
  bool success = localization_msgs__msg__LocalizationDiagnostics__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
localization_msgs__msg__LocalizationDiagnostics__destroy(localization_msgs__msg__LocalizationDiagnostics * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    localization_msgs__msg__LocalizationDiagnostics__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
localization_msgs__msg__LocalizationDiagnostics__Sequence__init(localization_msgs__msg__LocalizationDiagnostics__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationDiagnostics * data = NULL;

  if (size) {
    data = (localization_msgs__msg__LocalizationDiagnostics *)allocator.zero_allocate(size, sizeof(localization_msgs__msg__LocalizationDiagnostics), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = localization_msgs__msg__LocalizationDiagnostics__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        localization_msgs__msg__LocalizationDiagnostics__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
localization_msgs__msg__LocalizationDiagnostics__Sequence__fini(localization_msgs__msg__LocalizationDiagnostics__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      localization_msgs__msg__LocalizationDiagnostics__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

localization_msgs__msg__LocalizationDiagnostics__Sequence *
localization_msgs__msg__LocalizationDiagnostics__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationDiagnostics__Sequence * array = (localization_msgs__msg__LocalizationDiagnostics__Sequence *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationDiagnostics__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = localization_msgs__msg__LocalizationDiagnostics__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
localization_msgs__msg__LocalizationDiagnostics__Sequence__destroy(localization_msgs__msg__LocalizationDiagnostics__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    localization_msgs__msg__LocalizationDiagnostics__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
localization_msgs__msg__LocalizationDiagnostics__Sequence__are_equal(const localization_msgs__msg__LocalizationDiagnostics__Sequence * lhs, const localization_msgs__msg__LocalizationDiagnostics__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!localization_msgs__msg__LocalizationDiagnostics__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
localization_msgs__msg__LocalizationDiagnostics__Sequence__copy(
  const localization_msgs__msg__LocalizationDiagnostics__Sequence * input,
  localization_msgs__msg__LocalizationDiagnostics__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(localization_msgs__msg__LocalizationDiagnostics);
    localization_msgs__msg__LocalizationDiagnostics * data =
      (localization_msgs__msg__LocalizationDiagnostics *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!localization_msgs__msg__LocalizationDiagnostics__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          localization_msgs__msg__LocalizationDiagnostics__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!localization_msgs__msg__LocalizationDiagnostics__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
