// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/FSMRequest.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/fsm_request__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `reason`
#include "rosidl_runtime_c/string_functions.h"

bool
planning_msgs__msg__FSMRequest__init(planning_msgs__msg__FSMRequest * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    planning_msgs__msg__FSMRequest__fini(msg);
    return false;
  }
  // request_type
  // requested_mode
  // waypoint_id
  // reason
  if (!rosidl_runtime_c__String__init(&msg->reason)) {
    planning_msgs__msg__FSMRequest__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  return true;
}

void
planning_msgs__msg__FSMRequest__fini(planning_msgs__msg__FSMRequest * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // request_type
  // requested_mode
  // waypoint_id
  // reason
  rosidl_runtime_c__String__fini(&msg->reason);
  // age_ms
  // valid_until_ms
}

bool
planning_msgs__msg__FSMRequest__are_equal(const planning_msgs__msg__FSMRequest * lhs, const planning_msgs__msg__FSMRequest * rhs)
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
  // request_type
  if (lhs->request_type != rhs->request_type) {
    return false;
  }
  // requested_mode
  if (lhs->requested_mode != rhs->requested_mode) {
    return false;
  }
  // waypoint_id
  if (lhs->waypoint_id != rhs->waypoint_id) {
    return false;
  }
  // reason
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->reason), &(rhs->reason)))
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
  return true;
}

bool
planning_msgs__msg__FSMRequest__copy(
  const planning_msgs__msg__FSMRequest * input,
  planning_msgs__msg__FSMRequest * output)
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
  // request_type
  output->request_type = input->request_type;
  // requested_mode
  output->requested_mode = input->requested_mode;
  // waypoint_id
  output->waypoint_id = input->waypoint_id;
  // reason
  if (!rosidl_runtime_c__String__copy(
      &(input->reason), &(output->reason)))
  {
    return false;
  }
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  return true;
}

planning_msgs__msg__FSMRequest *
planning_msgs__msg__FSMRequest__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__FSMRequest * msg = (planning_msgs__msg__FSMRequest *)allocator.allocate(sizeof(planning_msgs__msg__FSMRequest), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__FSMRequest));
  bool success = planning_msgs__msg__FSMRequest__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__FSMRequest__destroy(planning_msgs__msg__FSMRequest * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__FSMRequest__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__FSMRequest__Sequence__init(planning_msgs__msg__FSMRequest__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__FSMRequest * data = NULL;

  if (size) {
    data = (planning_msgs__msg__FSMRequest *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__FSMRequest), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__FSMRequest__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__FSMRequest__fini(&data[i - 1]);
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
planning_msgs__msg__FSMRequest__Sequence__fini(planning_msgs__msg__FSMRequest__Sequence * array)
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
      planning_msgs__msg__FSMRequest__fini(&array->data[i]);
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

planning_msgs__msg__FSMRequest__Sequence *
planning_msgs__msg__FSMRequest__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__FSMRequest__Sequence * array = (planning_msgs__msg__FSMRequest__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__FSMRequest__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__FSMRequest__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__FSMRequest__Sequence__destroy(planning_msgs__msg__FSMRequest__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__FSMRequest__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__FSMRequest__Sequence__are_equal(const planning_msgs__msg__FSMRequest__Sequence * lhs, const planning_msgs__msg__FSMRequest__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__FSMRequest__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__FSMRequest__Sequence__copy(
  const planning_msgs__msg__FSMRequest__Sequence * input,
  planning_msgs__msg__FSMRequest__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__FSMRequest);
    planning_msgs__msg__FSMRequest * data =
      (planning_msgs__msg__FSMRequest *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__FSMRequest__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__FSMRequest__fini(&data[i]);
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
    if (!planning_msgs__msg__FSMRequest__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
