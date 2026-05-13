// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/controller_feedback__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
planning_msgs__msg__ControllerFeedback__init(planning_msgs__msg__ControllerFeedback * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    planning_msgs__msg__ControllerFeedback__fini(msg);
    return false;
  }
  // actual_speed
  // actual_steering_deg
  // cross_track_error
  // heading_error
  // brake_active
  // full_brake_active
  // age_ms
  // valid_until_ms
  return true;
}

void
planning_msgs__msg__ControllerFeedback__fini(planning_msgs__msg__ControllerFeedback * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // actual_speed
  // actual_steering_deg
  // cross_track_error
  // heading_error
  // brake_active
  // full_brake_active
  // age_ms
  // valid_until_ms
}

bool
planning_msgs__msg__ControllerFeedback__are_equal(const planning_msgs__msg__ControllerFeedback * lhs, const planning_msgs__msg__ControllerFeedback * rhs)
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
  // actual_speed
  if (lhs->actual_speed != rhs->actual_speed) {
    return false;
  }
  // actual_steering_deg
  if (lhs->actual_steering_deg != rhs->actual_steering_deg) {
    return false;
  }
  // cross_track_error
  if (lhs->cross_track_error != rhs->cross_track_error) {
    return false;
  }
  // heading_error
  if (lhs->heading_error != rhs->heading_error) {
    return false;
  }
  // brake_active
  if (lhs->brake_active != rhs->brake_active) {
    return false;
  }
  // full_brake_active
  if (lhs->full_brake_active != rhs->full_brake_active) {
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
  return true;
}

bool
planning_msgs__msg__ControllerFeedback__copy(
  const planning_msgs__msg__ControllerFeedback * input,
  planning_msgs__msg__ControllerFeedback * output)
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
  // actual_speed
  output->actual_speed = input->actual_speed;
  // actual_steering_deg
  output->actual_steering_deg = input->actual_steering_deg;
  // cross_track_error
  output->cross_track_error = input->cross_track_error;
  // heading_error
  output->heading_error = input->heading_error;
  // brake_active
  output->brake_active = input->brake_active;
  // full_brake_active
  output->full_brake_active = input->full_brake_active;
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  return true;
}

planning_msgs__msg__ControllerFeedback *
planning_msgs__msg__ControllerFeedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ControllerFeedback * msg = (planning_msgs__msg__ControllerFeedback *)allocator.allocate(sizeof(planning_msgs__msg__ControllerFeedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__ControllerFeedback));
  bool success = planning_msgs__msg__ControllerFeedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__ControllerFeedback__destroy(planning_msgs__msg__ControllerFeedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__ControllerFeedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__ControllerFeedback__Sequence__init(planning_msgs__msg__ControllerFeedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ControllerFeedback * data = NULL;

  if (size) {
    data = (planning_msgs__msg__ControllerFeedback *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__ControllerFeedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__ControllerFeedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__ControllerFeedback__fini(&data[i - 1]);
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
planning_msgs__msg__ControllerFeedback__Sequence__fini(planning_msgs__msg__ControllerFeedback__Sequence * array)
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
      planning_msgs__msg__ControllerFeedback__fini(&array->data[i]);
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

planning_msgs__msg__ControllerFeedback__Sequence *
planning_msgs__msg__ControllerFeedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ControllerFeedback__Sequence * array = (planning_msgs__msg__ControllerFeedback__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__ControllerFeedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__ControllerFeedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__ControllerFeedback__Sequence__destroy(planning_msgs__msg__ControllerFeedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__ControllerFeedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__ControllerFeedback__Sequence__are_equal(const planning_msgs__msg__ControllerFeedback__Sequence * lhs, const planning_msgs__msg__ControllerFeedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__ControllerFeedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__ControllerFeedback__Sequence__copy(
  const planning_msgs__msg__ControllerFeedback__Sequence * input,
  planning_msgs__msg__ControllerFeedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__ControllerFeedback);
    planning_msgs__msg__ControllerFeedback * data =
      (planning_msgs__msg__ControllerFeedback *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__ControllerFeedback__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__ControllerFeedback__fini(&data[i]);
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
    if (!planning_msgs__msg__ControllerFeedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
