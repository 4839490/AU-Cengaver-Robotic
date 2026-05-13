// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from localization_msgs:msg/LocalizationOdometry.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/localization_odometry__functions.h"

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
localization_msgs__msg__LocalizationOdometry__init(localization_msgs__msg__LocalizationOdometry * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    localization_msgs__msg__LocalizationOdometry__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // x
  // y
  // yaw
  // linear_velocity
  // angular_velocity
  // position_covariance
  // heading_covariance
  // velocity_covariance
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    localization_msgs__msg__LocalizationOdometry__fini(msg);
    return false;
  }
  return true;
}

void
localization_msgs__msg__LocalizationOdometry__fini(localization_msgs__msg__LocalizationOdometry * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // age_ms
  // valid_until_ms
  // x
  // y
  // yaw
  // linear_velocity
  // angular_velocity
  // position_covariance
  // heading_covariance
  // velocity_covariance
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
localization_msgs__msg__LocalizationOdometry__are_equal(const localization_msgs__msg__LocalizationOdometry * lhs, const localization_msgs__msg__LocalizationOdometry * rhs)
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
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // linear_velocity
  if (lhs->linear_velocity != rhs->linear_velocity) {
    return false;
  }
  // angular_velocity
  if (lhs->angular_velocity != rhs->angular_velocity) {
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
  // velocity_covariance
  if (lhs->velocity_covariance != rhs->velocity_covariance) {
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
localization_msgs__msg__LocalizationOdometry__copy(
  const localization_msgs__msg__LocalizationOdometry * input,
  localization_msgs__msg__LocalizationOdometry * output)
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
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // yaw
  output->yaw = input->yaw;
  // linear_velocity
  output->linear_velocity = input->linear_velocity;
  // angular_velocity
  output->angular_velocity = input->angular_velocity;
  // position_covariance
  output->position_covariance = input->position_covariance;
  // heading_covariance
  output->heading_covariance = input->heading_covariance;
  // velocity_covariance
  output->velocity_covariance = input->velocity_covariance;
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

localization_msgs__msg__LocalizationOdometry *
localization_msgs__msg__LocalizationOdometry__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationOdometry * msg = (localization_msgs__msg__LocalizationOdometry *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationOdometry), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(localization_msgs__msg__LocalizationOdometry));
  bool success = localization_msgs__msg__LocalizationOdometry__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
localization_msgs__msg__LocalizationOdometry__destroy(localization_msgs__msg__LocalizationOdometry * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    localization_msgs__msg__LocalizationOdometry__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
localization_msgs__msg__LocalizationOdometry__Sequence__init(localization_msgs__msg__LocalizationOdometry__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationOdometry * data = NULL;

  if (size) {
    data = (localization_msgs__msg__LocalizationOdometry *)allocator.zero_allocate(size, sizeof(localization_msgs__msg__LocalizationOdometry), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = localization_msgs__msg__LocalizationOdometry__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        localization_msgs__msg__LocalizationOdometry__fini(&data[i - 1]);
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
localization_msgs__msg__LocalizationOdometry__Sequence__fini(localization_msgs__msg__LocalizationOdometry__Sequence * array)
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
      localization_msgs__msg__LocalizationOdometry__fini(&array->data[i]);
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

localization_msgs__msg__LocalizationOdometry__Sequence *
localization_msgs__msg__LocalizationOdometry__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__LocalizationOdometry__Sequence * array = (localization_msgs__msg__LocalizationOdometry__Sequence *)allocator.allocate(sizeof(localization_msgs__msg__LocalizationOdometry__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = localization_msgs__msg__LocalizationOdometry__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
localization_msgs__msg__LocalizationOdometry__Sequence__destroy(localization_msgs__msg__LocalizationOdometry__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    localization_msgs__msg__LocalizationOdometry__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
localization_msgs__msg__LocalizationOdometry__Sequence__are_equal(const localization_msgs__msg__LocalizationOdometry__Sequence * lhs, const localization_msgs__msg__LocalizationOdometry__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!localization_msgs__msg__LocalizationOdometry__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
localization_msgs__msg__LocalizationOdometry__Sequence__copy(
  const localization_msgs__msg__LocalizationOdometry__Sequence * input,
  localization_msgs__msg__LocalizationOdometry__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(localization_msgs__msg__LocalizationOdometry);
    localization_msgs__msg__LocalizationOdometry * data =
      (localization_msgs__msg__LocalizationOdometry *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!localization_msgs__msg__LocalizationOdometry__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          localization_msgs__msg__LocalizationOdometry__fini(&data[i]);
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
    if (!localization_msgs__msg__LocalizationOdometry__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
