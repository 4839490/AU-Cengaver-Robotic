// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/traffic_light_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `source_sensor`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__TrafficLightState__init(perception_msgs__msg__TrafficLightState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    perception_msgs__msg__TrafficLightState__fini(msg);
    return false;
  }
  // state
  // confidence
  // relevant_to_route
  // distance_to_stop
  // confirmed
  // in_stop_zone
  // bbox_x
  // bbox_y
  // bbox_w
  // bbox_h
  // age_ms
  // valid_until_ms
  // source_sensor
  if (!rosidl_runtime_c__String__init(&msg->source_sensor)) {
    perception_msgs__msg__TrafficLightState__fini(msg);
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__TrafficLightState__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__TrafficLightState__fini(perception_msgs__msg__TrafficLightState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // state
  // confidence
  // relevant_to_route
  // distance_to_stop
  // confirmed
  // in_stop_zone
  // bbox_x
  // bbox_y
  // bbox_w
  // bbox_h
  // age_ms
  // valid_until_ms
  // source_sensor
  rosidl_runtime_c__String__fini(&msg->source_sensor);
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__TrafficLightState__are_equal(const perception_msgs__msg__TrafficLightState * lhs, const perception_msgs__msg__TrafficLightState * rhs)
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
  // state
  if (lhs->state != rhs->state) {
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
  // distance_to_stop
  if (lhs->distance_to_stop != rhs->distance_to_stop) {
    return false;
  }
  // confirmed
  if (lhs->confirmed != rhs->confirmed) {
    return false;
  }
  // in_stop_zone
  if (lhs->in_stop_zone != rhs->in_stop_zone) {
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
perception_msgs__msg__TrafficLightState__copy(
  const perception_msgs__msg__TrafficLightState * input,
  perception_msgs__msg__TrafficLightState * output)
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
  // state
  output->state = input->state;
  // confidence
  output->confidence = input->confidence;
  // relevant_to_route
  output->relevant_to_route = input->relevant_to_route;
  // distance_to_stop
  output->distance_to_stop = input->distance_to_stop;
  // confirmed
  output->confirmed = input->confirmed;
  // in_stop_zone
  output->in_stop_zone = input->in_stop_zone;
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

perception_msgs__msg__TrafficLightState *
perception_msgs__msg__TrafficLightState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficLightState * msg = (perception_msgs__msg__TrafficLightState *)allocator.allocate(sizeof(perception_msgs__msg__TrafficLightState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__TrafficLightState));
  bool success = perception_msgs__msg__TrafficLightState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__TrafficLightState__destroy(perception_msgs__msg__TrafficLightState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__TrafficLightState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__TrafficLightState__Sequence__init(perception_msgs__msg__TrafficLightState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficLightState * data = NULL;

  if (size) {
    data = (perception_msgs__msg__TrafficLightState *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__TrafficLightState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__TrafficLightState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__TrafficLightState__fini(&data[i - 1]);
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
perception_msgs__msg__TrafficLightState__Sequence__fini(perception_msgs__msg__TrafficLightState__Sequence * array)
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
      perception_msgs__msg__TrafficLightState__fini(&array->data[i]);
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

perception_msgs__msg__TrafficLightState__Sequence *
perception_msgs__msg__TrafficLightState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__TrafficLightState__Sequence * array = (perception_msgs__msg__TrafficLightState__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__TrafficLightState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__TrafficLightState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__TrafficLightState__Sequence__destroy(perception_msgs__msg__TrafficLightState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__TrafficLightState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__TrafficLightState__Sequence__are_equal(const perception_msgs__msg__TrafficLightState__Sequence * lhs, const perception_msgs__msg__TrafficLightState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__TrafficLightState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__TrafficLightState__Sequence__copy(
  const perception_msgs__msg__TrafficLightState__Sequence * input,
  perception_msgs__msg__TrafficLightState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__TrafficLightState);
    perception_msgs__msg__TrafficLightState * data =
      (perception_msgs__msg__TrafficLightState *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__TrafficLightState__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__TrafficLightState__fini(&data[i]);
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
    if (!perception_msgs__msg__TrafficLightState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
