// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/localization_status__functions.h"

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
localization_msgs__msg__LocalizationStatus__init(localization_msgs__msg__LocalizationStatus * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    localization_msgs__msg__LocalizationStatus__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // status
  // localization_confidence
  // position_covariance
  // heading_covariance
  // ndt_healthy
  // ndt_quality
  // map_odom_stable
  // map_odom_drift
  // gps_available
  // imu_available
  // lidar_available
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    localization_msgs__msg__LocalizationStatus__fini(msg);
    return false;
  }
  return true;
}

void
localization_msgs__msg__LocalizationStatus__fini(localization_msgs__msg__LocalizationStatus * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // age_ms
  // valid_until_ms
  // status
  // localization_confidence
  // position_covariance
  // heading_covariance
  // ndt_healthy
  // ndt_quality
  // map_odom_stable
  // map_odom_drift
  // gps_available
  // imu_available
  // lidar_available
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
localization_msgs__msg__LocalizationStatus__are_equal(const localization_msgs__msg__LocalizationStatus * lhs, const localization_msgs__msg__LocalizationStatus * rhs)
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
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // localization_confidence
  if (lhs->localization_confidence != rhs->localization_confidence) {
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
  // ndt_healthy
  if (lhs->ndt_healthy != rhs->ndt_healthy) {
    return false;
  }
  // ndt_quality
  if (lhs->ndt_quality != rhs->ndt_quality) {
    return false;
  }
  // map_odom_stable
  if (lhs->map_odom_stable != rhs->map_odom_stable) {
    return false;
  }
  // map_odom_drift
  if (lhs->map_odom_drift != rhs->map_odom_drift) {
    return false;
  }
  // gps_available
  if (lhs->gps_available != rhs->gps_available) {
    return false;
  }
  // imu_available
  if (lhs->imu_available != rhs->imu_available) {
    return false;
  }
  // lidar_available
  if (lhs->lidar_available != rhs->lidar_available) {
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
localization_msgs__msg__LocalizationStatus__copy(
  const localization_msgs__msg__LocalizationStatus * input,
  localization_msgs__msg__LocalizationStatus * output)
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
  // status
  output->status = input->status;
  // localization_confidence
  output->localization_confidence = input->localization_confidence;
  // position_covariance
  output->position_covariance = input->position_covariance;
  // heading_covariance
  output->heading_covariance = input->heading_covariance;
  // ndt_healthy
  output->ndt_healthy = input->ndt_healthy;
  // ndt_quality
  output->ndt_quality = input->ndt_quality;
  // map_odom_stable
  output->map_odom_stable = input->map_odom_stable;
  // map_odom_drift
  output->map_odom_drift = input->map_odom_drift;
  // gps_available
  output->gps_available = input->gps_available;
  // imu_available
  output->imu_available = input->imu_available;
  // lidar_available
  output->lidar_available = input->lidar_available;
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

localization_msgs__msg__LocalizationStatus *
localization_msgs__msg__LocalizationStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationStatus * msg = (localization_msgs__msg__LocalizationStatus *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(localization_msgs__msg__LocalizationStatus));
  bool success = localization_msgs__msg__LocalizationStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
localization_msgs__msg__LocalizationStatus__destroy(localization_msgs__msg__LocalizationStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    localization_msgs__msg__LocalizationStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
localization_msgs__msg__LocalizationStatus__Sequence__init(localization_msgs__msg__LocalizationStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationStatus * data = NULL;

  if (size) {
    data = (localization_msgs__msg__LocalizationStatus *)allocator.zero_allocate(size, sizeof(localization_msgs__msg__LocalizationStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = localization_msgs__msg__LocalizationStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        localization_msgs__msg__LocalizationStatus__fini(&data[i - 1]);
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
localization_msgs__msg__LocalizationStatus__Sequence__fini(localization_msgs__msg__LocalizationStatus__Sequence * array)
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
      localization_msgs__msg__LocalizationStatus__fini(&array->data[i]);
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

localization_msgs__msg__LocalizationStatus__Sequence *
localization_msgs__msg__LocalizationStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationStatus__Sequence * array = (localization_msgs__msg__LocalizationStatus__Sequence *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = localization_msgs__msg__LocalizationStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
localization_msgs__msg__LocalizationStatus__Sequence__destroy(localization_msgs__msg__LocalizationStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    localization_msgs__msg__LocalizationStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
localization_msgs__msg__LocalizationStatus__Sequence__are_equal(const localization_msgs__msg__LocalizationStatus__Sequence * lhs, const localization_msgs__msg__LocalizationStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!localization_msgs__msg__LocalizationStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
localization_msgs__msg__LocalizationStatus__Sequence__copy(
  const localization_msgs__msg__LocalizationStatus__Sequence * input,
  localization_msgs__msg__LocalizationStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(localization_msgs__msg__LocalizationStatus);
    localization_msgs__msg__LocalizationStatus * data =
      (localization_msgs__msg__LocalizationStatus *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!localization_msgs__msg__LocalizationStatus__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          localization_msgs__msg__LocalizationStatus__fini(&data[i]);
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
    if (!localization_msgs__msg__LocalizationStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
