// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice
#include "fsm_msgs/msg/detail/fsm_event__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `data`
#include "rosidl_runtime_c/string_functions.h"

bool
fsm_msgs__msg__FSMEvent__init(fsm_msgs__msg__FSMEvent * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    fsm_msgs__msg__FSMEvent__fini(msg);
    return false;
  }
  // event_type
  // waypoint_id
  // data
  if (!rosidl_runtime_c__String__init(&msg->data)) {
    fsm_msgs__msg__FSMEvent__fini(msg);
    return false;
  }
  // age_ms
  return true;
}

void
fsm_msgs__msg__FSMEvent__fini(fsm_msgs__msg__FSMEvent * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // event_type
  // waypoint_id
  // data
  rosidl_runtime_c__String__fini(&msg->data);
  // age_ms
}

bool
fsm_msgs__msg__FSMEvent__are_equal(const fsm_msgs__msg__FSMEvent * lhs, const fsm_msgs__msg__FSMEvent * rhs)
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
  // event_type
  if (lhs->event_type != rhs->event_type) {
    return false;
  }
  // waypoint_id
  if (lhs->waypoint_id != rhs->waypoint_id) {
    return false;
  }
  // data
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->data), &(rhs->data)))
  {
    return false;
  }
  // age_ms
  if (lhs->age_ms != rhs->age_ms) {
    return false;
  }
  return true;
}

bool
fsm_msgs__msg__FSMEvent__copy(
  const fsm_msgs__msg__FSMEvent * input,
  fsm_msgs__msg__FSMEvent * output)
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
  // event_type
  output->event_type = input->event_type;
  // waypoint_id
  output->waypoint_id = input->waypoint_id;
  // data
  if (!rosidl_runtime_c__String__copy(
      &(input->data), &(output->data)))
  {
    return false;
  }
  // age_ms
  output->age_ms = input->age_ms;
  return true;
}

fsm_msgs__msg__FSMEvent *
fsm_msgs__msg__FSMEvent__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__FSMEvent * msg = (fsm_msgs__msg__FSMEvent *)allocator.allocate(sizeof(fsm_msgs__msg__FSMEvent), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fsm_msgs__msg__FSMEvent));
  bool success = fsm_msgs__msg__FSMEvent__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fsm_msgs__msg__FSMEvent__destroy(fsm_msgs__msg__FSMEvent * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fsm_msgs__msg__FSMEvent__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fsm_msgs__msg__FSMEvent__Sequence__init(fsm_msgs__msg__FSMEvent__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__FSMEvent * data = NULL;

  if (size) {
    data = (fsm_msgs__msg__FSMEvent *)allocator.zero_allocate(size, sizeof(fsm_msgs__msg__FSMEvent), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fsm_msgs__msg__FSMEvent__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fsm_msgs__msg__FSMEvent__fini(&data[i - 1]);
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
fsm_msgs__msg__FSMEvent__Sequence__fini(fsm_msgs__msg__FSMEvent__Sequence * array)
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
      fsm_msgs__msg__FSMEvent__fini(&array->data[i]);
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

fsm_msgs__msg__FSMEvent__Sequence *
fsm_msgs__msg__FSMEvent__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__FSMEvent__Sequence * array = (fsm_msgs__msg__FSMEvent__Sequence *)allocator.allocate(sizeof(fsm_msgs__msg__FSMEvent__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fsm_msgs__msg__FSMEvent__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fsm_msgs__msg__FSMEvent__Sequence__destroy(fsm_msgs__msg__FSMEvent__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fsm_msgs__msg__FSMEvent__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fsm_msgs__msg__FSMEvent__Sequence__are_equal(const fsm_msgs__msg__FSMEvent__Sequence * lhs, const fsm_msgs__msg__FSMEvent__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fsm_msgs__msg__FSMEvent__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fsm_msgs__msg__FSMEvent__Sequence__copy(
  const fsm_msgs__msg__FSMEvent__Sequence * input,
  fsm_msgs__msg__FSMEvent__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fsm_msgs__msg__FSMEvent);
    fsm_msgs__msg__FSMEvent * data =
      (fsm_msgs__msg__FSMEvent *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fsm_msgs__msg__FSMEvent__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          fsm_msgs__msg__FSMEvent__fini(&data[i]);
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
    if (!fsm_msgs__msg__FSMEvent__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
