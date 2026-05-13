// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice
#include "common_msgs/msg/detail/stop_reason__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
common_msgs__msg__StopReason__init(common_msgs__msg__StopReason * msg)
{
  if (!msg) {
    return false;
  }
  // reason
  return true;
}

void
common_msgs__msg__StopReason__fini(common_msgs__msg__StopReason * msg)
{
  if (!msg) {
    return;
  }
  // reason
}

bool
common_msgs__msg__StopReason__are_equal(const common_msgs__msg__StopReason * lhs, const common_msgs__msg__StopReason * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // reason
  if (lhs->reason != rhs->reason) {
    return false;
  }
  return true;
}

bool
common_msgs__msg__StopReason__copy(
  const common_msgs__msg__StopReason * input,
  common_msgs__msg__StopReason * output)
{
  if (!input || !output) {
    return false;
  }
  // reason
  output->reason = input->reason;
  return true;
}

common_msgs__msg__StopReason *
common_msgs__msg__StopReason__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__StopReason * msg = (common_msgs__msg__StopReason *)allocator.allocate(sizeof(common_msgs__msg__StopReason), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(common_msgs__msg__StopReason));
  bool success = common_msgs__msg__StopReason__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
common_msgs__msg__StopReason__destroy(common_msgs__msg__StopReason * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    common_msgs__msg__StopReason__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
common_msgs__msg__StopReason__Sequence__init(common_msgs__msg__StopReason__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__StopReason * data = NULL;

  if (size) {
    data = (common_msgs__msg__StopReason *)allocator.zero_allocate(size, sizeof(common_msgs__msg__StopReason), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = common_msgs__msg__StopReason__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        common_msgs__msg__StopReason__fini(&data[i - 1]);
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
common_msgs__msg__StopReason__Sequence__fini(common_msgs__msg__StopReason__Sequence * array)
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
      common_msgs__msg__StopReason__fini(&array->data[i]);
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

common_msgs__msg__StopReason__Sequence *
common_msgs__msg__StopReason__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__StopReason__Sequence * array = (common_msgs__msg__StopReason__Sequence *)allocator.allocate(sizeof(common_msgs__msg__StopReason__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = common_msgs__msg__StopReason__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
common_msgs__msg__StopReason__Sequence__destroy(common_msgs__msg__StopReason__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    common_msgs__msg__StopReason__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
common_msgs__msg__StopReason__Sequence__are_equal(const common_msgs__msg__StopReason__Sequence * lhs, const common_msgs__msg__StopReason__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!common_msgs__msg__StopReason__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
common_msgs__msg__StopReason__Sequence__copy(
  const common_msgs__msg__StopReason__Sequence * input,
  common_msgs__msg__StopReason__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(common_msgs__msg__StopReason);
    common_msgs__msg__StopReason * data =
      (common_msgs__msg__StopReason *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!common_msgs__msg__StopReason__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          common_msgs__msg__StopReason__fini(&data[i]);
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
    if (!common_msgs__msg__StopReason__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
