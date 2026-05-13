// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fsm_msgs:msg/CurrentMode.idl
// generated code does not contain a copyright notice
#include "fsm_msgs/msg/detail/current_mode__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `reason`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
fsm_msgs__msg__CurrentMode__init(fsm_msgs__msg__CurrentMode * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    fsm_msgs__msg__CurrentMode__fini(msg);
    return false;
  }
  // mode
  // previous_mode
  // reason
  if (!rosidl_runtime_c__String__init(&msg->reason)) {
    fsm_msgs__msg__CurrentMode__fini(msg);
    return false;
  }
  // stop_reason
  // waypoint_id
  // age_ms
  // valid_until_ms
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    fsm_msgs__msg__CurrentMode__fini(msg);
    return false;
  }
  return true;
}

void
fsm_msgs__msg__CurrentMode__fini(fsm_msgs__msg__CurrentMode * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // mode
  // previous_mode
  // reason
  rosidl_runtime_c__String__fini(&msg->reason);
  // stop_reason
  // waypoint_id
  // age_ms
  // valid_until_ms
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
fsm_msgs__msg__CurrentMode__are_equal(const fsm_msgs__msg__CurrentMode * lhs, const fsm_msgs__msg__CurrentMode * rhs)
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
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  // previous_mode
  if (lhs->previous_mode != rhs->previous_mode) {
    return false;
  }
  // reason
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->reason), &(rhs->reason)))
  {
    return false;
  }
  // stop_reason
  if (lhs->stop_reason != rhs->stop_reason) {
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
fsm_msgs__msg__CurrentMode__copy(
  const fsm_msgs__msg__CurrentMode * input,
  fsm_msgs__msg__CurrentMode * output)
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
  // mode
  output->mode = input->mode;
  // previous_mode
  output->previous_mode = input->previous_mode;
  // reason
  if (!rosidl_runtime_c__String__copy(
      &(input->reason), &(output->reason)))
  {
    return false;
  }
  // stop_reason
  output->stop_reason = input->stop_reason;
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

fsm_msgs__msg__CurrentMode *
fsm_msgs__msg__CurrentMode__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__CurrentMode * msg = (fsm_msgs__msg__CurrentMode *)allocator.allocate(sizeof(fsm_msgs__msg__CurrentMode), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fsm_msgs__msg__CurrentMode));
  bool success = fsm_msgs__msg__CurrentMode__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fsm_msgs__msg__CurrentMode__destroy(fsm_msgs__msg__CurrentMode * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fsm_msgs__msg__CurrentMode__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fsm_msgs__msg__CurrentMode__Sequence__init(fsm_msgs__msg__CurrentMode__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__CurrentMode * data = NULL;

  if (size) {
    data = (fsm_msgs__msg__CurrentMode *)allocator.zero_allocate(size, sizeof(fsm_msgs__msg__CurrentMode), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fsm_msgs__msg__CurrentMode__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fsm_msgs__msg__CurrentMode__fini(&data[i - 1]);
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
fsm_msgs__msg__CurrentMode__Sequence__fini(fsm_msgs__msg__CurrentMode__Sequence * array)
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
      fsm_msgs__msg__CurrentMode__fini(&array->data[i]);
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

fsm_msgs__msg__CurrentMode__Sequence *
fsm_msgs__msg__CurrentMode__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__CurrentMode__Sequence * array = (fsm_msgs__msg__CurrentMode__Sequence *)allocator.allocate(sizeof(fsm_msgs__msg__CurrentMode__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fsm_msgs__msg__CurrentMode__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fsm_msgs__msg__CurrentMode__Sequence__destroy(fsm_msgs__msg__CurrentMode__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fsm_msgs__msg__CurrentMode__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fsm_msgs__msg__CurrentMode__Sequence__are_equal(const fsm_msgs__msg__CurrentMode__Sequence * lhs, const fsm_msgs__msg__CurrentMode__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fsm_msgs__msg__CurrentMode__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fsm_msgs__msg__CurrentMode__Sequence__copy(
  const fsm_msgs__msg__CurrentMode__Sequence * input,
  fsm_msgs__msg__CurrentMode__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fsm_msgs__msg__CurrentMode);
    fsm_msgs__msg__CurrentMode * data =
      (fsm_msgs__msg__CurrentMode *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fsm_msgs__msg__CurrentMode__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          fsm_msgs__msg__CurrentMode__fini(&data[i]);
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
    if (!fsm_msgs__msg__CurrentMode__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
