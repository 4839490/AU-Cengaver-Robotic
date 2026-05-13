// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/traffic_sign__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `source_sensor`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__TrafficSign__init(perception_msgs__msg__TrafficSign * msg)
{
  if (!msg) {
    return false;
  }
  // sign_id
  // type
  // confidence
  // relevant_to_route
  // distance
  // event_status
  // confirmed
  // bbox_x
  // bbox_y
  // bbox_w
  // bbox_h
  // age_ms
  // valid_until_ms
  // event_memory_ttl_ms
  // source_sensor
  if (!rosidl_runtime_c__String__init(&msg->source_sensor)) {
    perception_msgs__msg__TrafficSign__fini(msg);
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__TrafficSign__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__TrafficSign__fini(perception_msgs__msg__TrafficSign * msg)
{
  if (!msg) {
    return;
  }
  // sign_id
  // type
  // confidence
  // relevant_to_route
  // distance
  // event_status
  // confirmed
  // bbox_x
  // bbox_y
  // bbox_w
  // bbox_h
  // age_ms
  // valid_until_ms
  // event_memory_ttl_ms
  // source_sensor
  rosidl_runtime_c__String__fini(&msg->source_sensor);
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__TrafficSign__are_equal(const perception_msgs__msg__TrafficSign * lhs, const perception_msgs__msg__TrafficSign * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sign_id
  if (lhs->sign_id != rhs->sign_id) {
    return false;
  }
  // type
  if (lhs->type != rhs->type) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // relevant_to_route
  if (lhs->relevant_to_route != rhs->relevant_to_route) {
    return false;
  }
  // distance
  if (lhs->distance != rhs->distance) {
    return false;
  }
  // event_status
  if (lhs->event_status != rhs->event_status) {
    return false;
  }
  // confirmed
  if (lhs->confirmed != rhs->confirmed) {
    return false;
  }
  // bbox_x
  if (lhs->bbox_x != rhs->bbox_x) {
    return false;
  }
  // bbox_y
  if (lhs->bbox_y != rhs->bbox_y) {
    return false;
  }
  // bbox_w
  if (lhs->bbox_w != rhs->bbox_w) {
    return false;
  }
  // bbox_h
  if (lhs->bbox_h != rhs->bbox_h) {
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
  // event_memory_ttl_ms
  if (lhs->event_memory_ttl_ms != rhs->event_memory_ttl_ms) {
    return false;
  }
  // source_sensor
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source_sensor), &(rhs->source_sensor)))
  {
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
perception_msgs__msg__TrafficSign__copy(
  const perception_msgs__msg__TrafficSign * input,
  perception_msgs__msg__TrafficSign * output)
{
  if (!input || !output) {
    return false;
  }
  // sign_id
  output->sign_id = input->sign_id;
  // type
  output->type = input->type;
  // confidence
  output->confidence = input->confidence;
  // relevant_to_route
  output->relevant_to_route = input->relevant_to_route;
  // distance
  output->distance = input->distance;
  // event_status
  output->event_status = input->event_status;
  // confirmed
  output->confirmed = input->confirmed;
  // bbox_x
  output->bbox_x = input->bbox_x;
  // bbox_y
  output->bbox_y = input->bbox_y;
  // bbox_w
  output->bbox_w = input->bbox_w;
  // bbox_h
  output->bbox_h = input->bbox_h;
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  // event_memory_ttl_ms
  output->event_memory_ttl_ms = input->event_memory_ttl_ms;
  // source_sensor
  if (!rosidl_runtime_c__String__copy(
      &(input->source_sensor), &(output->source_sensor)))
  {
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

perception_msgs__msg__TrafficSign *
perception_msgs__msg__TrafficSign__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficSign * msg = (perception_msgs__msg__TrafficSign *)allocator.allocate(sizeof(perception_msgs__msg__TrafficSign), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__TrafficSign));
  bool success = perception_msgs__msg__TrafficSign__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__TrafficSign__destroy(perception_msgs__msg__TrafficSign * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__TrafficSign__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__TrafficSign__Sequence__init(perception_msgs__msg__TrafficSign__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficSign * data = NULL;

  if (size) {
    data = (perception_msgs__msg__TrafficSign *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__TrafficSign), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__TrafficSign__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__TrafficSign__fini(&data[i - 1]);
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
perception_msgs__msg__TrafficSign__Sequence__fini(perception_msgs__msg__TrafficSign__Sequence * array)
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
      perception_msgs__msg__TrafficSign__fini(&array->data[i]);
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

perception_msgs__msg__TrafficSign__Sequence *
perception_msgs__msg__TrafficSign__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficSign__Sequence * array = (perception_msgs__msg__TrafficSign__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__TrafficSign__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__TrafficSign__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__TrafficSign__Sequence__destroy(perception_msgs__msg__TrafficSign__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__TrafficSign__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__TrafficSign__Sequence__are_equal(const perception_msgs__msg__TrafficSign__Sequence * lhs, const perception_msgs__msg__TrafficSign__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__TrafficSign__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__TrafficSign__Sequence__copy(
  const perception_msgs__msg__TrafficSign__Sequence * input,
  perception_msgs__msg__TrafficSign__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__TrafficSign);
    perception_msgs__msg__TrafficSign * data =
      (perception_msgs__msg__TrafficSign *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__TrafficSign__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__TrafficSign__fini(&data[i]);
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
    if (!perception_msgs__msg__TrafficSign__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
