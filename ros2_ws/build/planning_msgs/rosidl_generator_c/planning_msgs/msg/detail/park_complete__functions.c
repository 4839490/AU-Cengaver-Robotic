// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/ParkComplete.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/park_complete__functions.h"

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
planning_msgs__msg__ParkComplete__init(planning_msgs__msg__ParkComplete * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    planning_msgs__msg__ParkComplete__fini(msg);
    return false;
  }
  // success
  // final_cross_track_error
  // final_heading_error
  // iterations_used
  // waypoint_id
  // age_ms
  // valid_until_ms
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    planning_msgs__msg__ParkComplete__fini(msg);
    return false;
  }
  return true;
}

void
planning_msgs__msg__ParkComplete__fini(planning_msgs__msg__ParkComplete * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // success
  // final_cross_track_error
  // final_heading_error
  // iterations_used
  // waypoint_id
  // age_ms
  // valid_until_ms
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
planning_msgs__msg__ParkComplete__are_equal(const planning_msgs__msg__ParkComplete * lhs, const planning_msgs__msg__ParkComplete * rhs)
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
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  // final_cross_track_error
  if (lhs->final_cross_track_error != rhs->final_cross_track_error) {
    return false;
  }
  // final_heading_error
  if (lhs->final_heading_error != rhs->final_heading_error) {
    return false;
  }
  // iterations_used
  if (lhs->iterations_used != rhs->iterations_used) {
    return false;
  }
  // waypoint_id
  if (lhs->waypoint_id != rhs->waypoint_id) {
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
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->warning_flags), &(rhs->warning_flags)))
  {
    return false;
  }
  return true;
}

bool
planning_msgs__msg__ParkComplete__copy(
  const planning_msgs__msg__ParkComplete * input,
  planning_msgs__msg__ParkComplete * output)
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
  // success
  output->success = input->success;
  // final_cross_track_error
  output->final_cross_track_error = input->final_cross_track_error;
  // final_heading_error
  output->final_heading_error = input->final_heading_error;
  // iterations_used
  output->iterations_used = input->iterations_used;
  // waypoint_id
  output->waypoint_id = input->waypoint_id;
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

planning_msgs__msg__ParkComplete *
planning_msgs__msg__ParkComplete__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ParkComplete * msg = (planning_msgs__msg__ParkComplete *)allocator.allocate(sizeof(planning_msgs__msg__ParkComplete), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__ParkComplete));
  bool success = planning_msgs__msg__ParkComplete__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__ParkComplete__destroy(planning_msgs__msg__ParkComplete * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__ParkComplete__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__ParkComplete__Sequence__init(planning_msgs__msg__ParkComplete__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ParkComplete * data = NULL;

  if (size) {
    data = (planning_msgs__msg__ParkComplete *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__ParkComplete), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__ParkComplete__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__ParkComplete__fini(&data[i - 1]);
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
planning_msgs__msg__ParkComplete__Sequence__fini(planning_msgs__msg__ParkComplete__Sequence * array)
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
      planning_msgs__msg__ParkComplete__fini(&array->data[i]);
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

planning_msgs__msg__ParkComplete__Sequence *
planning_msgs__msg__ParkComplete__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ParkComplete__Sequence * array = (planning_msgs__msg__ParkComplete__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__ParkComplete__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__ParkComplete__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__ParkComplete__Sequence__destroy(planning_msgs__msg__ParkComplete__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__ParkComplete__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__ParkComplete__Sequence__are_equal(const planning_msgs__msg__ParkComplete__Sequence * lhs, const planning_msgs__msg__ParkComplete__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__ParkComplete__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__ParkComplete__Sequence__copy(
  const planning_msgs__msg__ParkComplete__Sequence * input,
  planning_msgs__msg__ParkComplete__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__ParkComplete);
    planning_msgs__msg__ParkComplete * data =
      (planning_msgs__msg__ParkComplete *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__ParkComplete__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__ParkComplete__fini(&data[i]);
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
    if (!planning_msgs__msg__ParkComplete__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
