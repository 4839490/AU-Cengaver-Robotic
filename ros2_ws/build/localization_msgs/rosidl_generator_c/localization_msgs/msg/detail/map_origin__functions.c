// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/map_origin__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `source`
#include "rosidl_runtime_c/string_functions.h"

bool
localization_msgs__msg__MapOrigin__init(localization_msgs__msg__MapOrigin * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    localization_msgs__msg__MapOrigin__fini(msg);
    return false;
  }
  // lat_ref
  // lon_ref
  // alt_ref
  // yaw_ref
  // source
  if (!rosidl_runtime_c__String__init(&msg->source)) {
    localization_msgs__msg__MapOrigin__fini(msg);
    return false;
  }
  // locked
  return true;
}

void
localization_msgs__msg__MapOrigin__fini(localization_msgs__msg__MapOrigin * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // lat_ref
  // lon_ref
  // alt_ref
  // yaw_ref
  // source
  rosidl_runtime_c__String__fini(&msg->source);
  // locked
}

bool
localization_msgs__msg__MapOrigin__are_equal(const localization_msgs__msg__MapOrigin * lhs, const localization_msgs__msg__MapOrigin * rhs)
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
  // lat_ref
  if (lhs->lat_ref != rhs->lat_ref) {
    return false;
  }
  // lon_ref
  if (lhs->lon_ref != rhs->lon_ref) {
    return false;
  }
  // alt_ref
  if (lhs->alt_ref != rhs->alt_ref) {
    return false;
  }
  // yaw_ref
  if (lhs->yaw_ref != rhs->yaw_ref) {
    return false;
  }
  // source
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source), &(rhs->source)))
  {
    return false;
  }
  // locked
  if (lhs->locked != rhs->locked) {
    return false;
  }
  return true;
}

bool
localization_msgs__msg__MapOrigin__copy(
  const localization_msgs__msg__MapOrigin * input,
  localization_msgs__msg__MapOrigin * output)
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
  // lat_ref
  output->lat_ref = input->lat_ref;
  // lon_ref
  output->lon_ref = input->lon_ref;
  // alt_ref
  output->alt_ref = input->alt_ref;
  // yaw_ref
  output->yaw_ref = input->yaw_ref;
  // source
  if (!rosidl_runtime_c__String__copy(
      &(input->source), &(output->source)))
  {
    return false;
  }
  // locked
  output->locked = input->locked;
  return true;
}

localization_msgs__msg__MapOrigin *
localization_msgs__msg__MapOrigin__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__MapOrigin * msg = (localization_msgs__msg__MapOrigin *)allocator.allocate(sizeof(localization_msgs__msg__MapOrigin), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(localization_msgs__msg__MapOrigin));
  bool success = localization_msgs__msg__MapOrigin__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
localization_msgs__msg__MapOrigin__destroy(localization_msgs__msg__MapOrigin * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    localization_msgs__msg__MapOrigin__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
localization_msgs__msg__MapOrigin__Sequence__init(localization_msgs__msg__MapOrigin__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__MapOrigin * data = NULL;

  if (size) {
    data = (localization_msgs__msg__MapOrigin *)allocator.zero_allocate(size, sizeof(localization_msgs__msg__MapOrigin), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = localization_msgs__msg__MapOrigin__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        localization_msgs__msg__MapOrigin__fini(&data[i - 1]);
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
localization_msgs__msg__MapOrigin__Sequence__fini(localization_msgs__msg__MapOrigin__Sequence * array)
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
      localization_msgs__msg__MapOrigin__fini(&array->data[i]);
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

localization_msgs__msg__MapOrigin__Sequence *
localization_msgs__msg__MapOrigin__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__MapOrigin__Sequence * array = (localization_msgs__msg__MapOrigin__Sequence *)allocator.allocate(sizeof(localization_msgs__msg__MapOrigin__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = localization_msgs__msg__MapOrigin__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
localization_msgs__msg__MapOrigin__Sequence__destroy(localization_msgs__msg__MapOrigin__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    localization_msgs__msg__MapOrigin__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
localization_msgs__msg__MapOrigin__Sequence__are_equal(const localization_msgs__msg__MapOrigin__Sequence * lhs, const localization_msgs__msg__MapOrigin__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!localization_msgs__msg__MapOrigin__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
localization_msgs__msg__MapOrigin__Sequence__copy(
  const localization_msgs__msg__MapOrigin__Sequence * input,
  localization_msgs__msg__MapOrigin__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(localization_msgs__msg__MapOrigin);
    localization_msgs__msg__MapOrigin * data =
      (localization_msgs__msg__MapOrigin *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!localization_msgs__msg__MapOrigin__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          localization_msgs__msg__MapOrigin__fini(&data[i]);
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
    if (!localization_msgs__msg__MapOrigin__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
