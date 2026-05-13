// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from common_msgs:msg/AutonomyMode.idl
// generated code does not contain a copyright notice
#include "common_msgs/msg/detail/autonomy_mode__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
common_msgs__msg__AutonomyMode__init(common_msgs__msg__AutonomyMode * msg)
{
  if (!msg) {
    return false;
  }
  // mode
  return true;
}

void
common_msgs__msg__AutonomyMode__fini(common_msgs__msg__AutonomyMode * msg)
{
  if (!msg) {
    return;
  }
  // mode
}

bool
common_msgs__msg__AutonomyMode__are_equal(const common_msgs__msg__AutonomyMode * lhs, const common_msgs__msg__AutonomyMode * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // mode
  if (lhs->mode != rhs->mode) {
    return false;
  }
  return true;
}

bool
common_msgs__msg__AutonomyMode__copy(
  const common_msgs__msg__AutonomyMode * input,
  common_msgs__msg__AutonomyMode * output)
{
  if (!input || !output) {
    return false;
  }
  // mode
  output->mode = input->mode;
  return true;
}

common_msgs__msg__AutonomyMode *
common_msgs__msg__AutonomyMode__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__AutonomyMode * msg = (common_msgs__msg__AutonomyMode *)allocator.allocate(sizeof(common_msgs__msg__AutonomyMode), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(common_msgs__msg__AutonomyMode));
  bool success = common_msgs__msg__AutonomyMode__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
common_msgs__msg__AutonomyMode__destroy(common_msgs__msg__AutonomyMode * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    common_msgs__msg__AutonomyMode__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
common_msgs__msg__AutonomyMode__Sequence__init(common_msgs__msg__AutonomyMode__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__AutonomyMode * data = NULL;

  if (size) {
    data = (common_msgs__msg__AutonomyMode *)allocator.zero_allocate(size, sizeof(common_msgs__msg__AutonomyMode), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = common_msgs__msg__AutonomyMode__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        common_msgs__msg__AutonomyMode__fini(&data[i - 1]);
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
common_msgs__msg__AutonomyMode__Sequence__fini(common_msgs__msg__AutonomyMode__Sequence * array)
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
      common_msgs__msg__AutonomyMode__fini(&array->data[i]);
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

common_msgs__msg__AutonomyMode__Sequence *
common_msgs__msg__AutonomyMode__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  common_msgs__msg__AutonomyMode__Sequence * array = (common_msgs__msg__AutonomyMode__Sequence *)allocator.allocate(sizeof(common_msgs__msg__AutonomyMode__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = common_msgs__msg__AutonomyMode__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
common_msgs__msg__AutonomyMode__Sequence__destroy(common_msgs__msg__AutonomyMode__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    common_msgs__msg__AutonomyMode__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
common_msgs__msg__AutonomyMode__Sequence__are_equal(const common_msgs__msg__AutonomyMode__Sequence * lhs, const common_msgs__msg__AutonomyMode__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!common_msgs__msg__AutonomyMode__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
common_msgs__msg__AutonomyMode__Sequence__copy(
  const common_msgs__msg__AutonomyMode__Sequence * input,
  common_msgs__msg__AutonomyMode__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(common_msgs__msg__AutonomyMode);
    common_msgs__msg__AutonomyMode * data =
      (common_msgs__msg__AutonomyMode *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!common_msgs__msg__AutonomyMode__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          common_msgs__msg__AutonomyMode__fini(&data[i]);
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
    if (!common_msgs__msg__AutonomyMode__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
