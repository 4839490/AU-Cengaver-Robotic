// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from localization_msgs:msg/RawGps.idl
// generated code does not contain a copyright notice
#include "localization_msgs/msg/detail/raw_gps__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
localization_msgs__msg__RawGps__init(localization_msgs__msg__RawGps * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    localization_msgs__msg__RawGps__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // latitude
  // longitude
  // altitude
  // speed
  // heading_deg
  // hdop
  // vdop
  // fix_type
  return true;
}

void
localization_msgs__msg__RawGps__fini(localization_msgs__msg__RawGps * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // age_ms
  // valid_until_ms
  // latitude
  // longitude
  // altitude
  // speed
  // heading_deg
  // hdop
  // vdop
  // fix_type
}

bool
localization_msgs__msg__RawGps__are_equal(const localization_msgs__msg__RawGps * lhs, const localization_msgs__msg__RawGps * rhs)
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
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // altitude
  if (lhs->altitude != rhs->altitude) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // heading_deg
  if (lhs->heading_deg != rhs->heading_deg) {
    return false;
  }
  // hdop
  if (lhs->hdop != rhs->hdop) {
    return false;
  }
  // vdop
  if (lhs->vdop != rhs->vdop) {
    return false;
  }
  // fix_type
  if (lhs->fix_type != rhs->fix_type) {
    return false;
  }
  return true;
}

bool
localization_msgs__msg__RawGps__copy(
  const localization_msgs__msg__RawGps * input,
  localization_msgs__msg__RawGps * output)
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
  // latitude
  output->latitude = input->latitude;
  // longitude
  output->longitude = input->longitude;
  // altitude
  output->altitude = input->altitude;
  // speed
  output->speed = input->speed;
  // heading_deg
  output->heading_deg = input->heading_deg;
  // hdop
  output->hdop = input->hdop;
  // vdop
  output->vdop = input->vdop;
  // fix_type
  output->fix_type = input->fix_type;
  return true;
}

localization_msgs__msg__RawGps *
localization_msgs__msg__RawGps__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__RawGps * msg = (localization_msgs__msg__RawGps *)allocator.allocate(sizeof(localization_msgs__msg__RawGps), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(localization_msgs__msg__RawGps));
  bool success = localization_msgs__msg__RawGps__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
localization_msgs__msg__RawGps__destroy(localization_msgs__msg__RawGps * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    localization_msgs__msg__RawGps__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
localization_msgs__msg__RawGps__Sequence__init(localization_msgs__msg__RawGps__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__RawGps * data = NULL;

  if (size) {
    data = (localization_msgs__msg__RawGps *)allocator.zero_allocate(size, sizeof(localization_msgs__msg__RawGps), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = localization_msgs__msg__RawGps__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        localization_msgs__msg__RawGps__fini(&data[i - 1]);
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
localization_msgs__msg__RawGps__Sequence__fini(localization_msgs__msg__RawGps__Sequence * array)
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
      localization_msgs__msg__RawGps__fini(&array->data[i]);
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

localization_msgs__msg__RawGps__Sequence *
localization_msgs__msg__RawGps__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  localization_msgs__msg__RawGps__Sequence * array = (localization_msgs__msg__RawGps__Sequence *)allocator.allocate(sizeof(localization_msgs__msg__RawGps__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = localization_msgs__msg__RawGps__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
localization_msgs__msg__RawGps__Sequence__destroy(localization_msgs__msg__RawGps__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    localization_msgs__msg__RawGps__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
localization_msgs__msg__RawGps__Sequence__are_equal(const localization_msgs__msg__RawGps__Sequence * lhs, const localization_msgs__msg__RawGps__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!localization_msgs__msg__RawGps__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
localization_msgs__msg__RawGps__Sequence__copy(
  const localization_msgs__msg__RawGps__Sequence * input,
  localization_msgs__msg__RawGps__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(localization_msgs__msg__RawGps);
    localization_msgs__msg__RawGps * data =
      (localization_msgs__msg__RawGps *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!localization_msgs__msg__RawGps__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          localization_msgs__msg__RawGps__fini(&data[i]);
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
    if (!localization_msgs__msg__RawGps__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
