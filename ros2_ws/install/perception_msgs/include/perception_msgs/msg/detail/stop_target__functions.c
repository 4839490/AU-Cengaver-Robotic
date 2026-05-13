// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/StopTarget.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/stop_target__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `source`
// Member `source_topic`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__StopTarget__init(perception_msgs__msg__StopTarget * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    perception_msgs__msg__StopTarget__fini(msg);
    return false;
  }
  // target_type
  // distance_from_front_bumper
  // target_x
  // target_y
  // confidence
  // source
  if (!rosidl_runtime_c__String__init(&msg->source)) {
    perception_msgs__msg__StopTarget__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // waypoint_id
  // heading_at_stop
  // priority
  // required_stop_duration_ms
  // stop_reason_id
  // source_topic
  if (!rosidl_runtime_c__String__init(&msg->source_topic)) {
    perception_msgs__msg__StopTarget__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__StopTarget__fini(perception_msgs__msg__StopTarget * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // target_type
  // distance_from_front_bumper
  // target_x
  // target_y
  // confidence
  // source
  rosidl_runtime_c__String__fini(&msg->source);
  // age_ms
  // valid_until_ms
  // waypoint_id
  // heading_at_stop
  // priority
  // required_stop_duration_ms
  // stop_reason_id
  // source_topic
  rosidl_runtime_c__String__fini(&msg->source_topic);
}

bool
perception_msgs__msg__StopTarget__are_equal(const perception_msgs__msg__StopTarget * lhs, const perception_msgs__msg__StopTarget * rhs)
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
  // target_type
  if (lhs->target_type != rhs->target_type) {
    return false;
  }
  // distance_from_front_bumper
  if (lhs->distance_from_front_bumper != rhs->distance_from_front_bumper) {
    return false;
  }
  // target_x
  if (lhs->target_x != rhs->target_x) {
    return false;
  }
  // target_y
  if (lhs->target_y != rhs->target_y) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // source
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source), &(rhs->source)))
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
  // waypoint_id
  if (lhs->waypoint_id != rhs->waypoint_id) {
    return false;
  }
  // heading_at_stop
  if (lhs->heading_at_stop != rhs->heading_at_stop) {
    return false;
  }
  // priority
  if (lhs->priority != rhs->priority) {
    return false;
  }
  // required_stop_duration_ms
  if (lhs->required_stop_duration_ms != rhs->required_stop_duration_ms) {
    return false;
  }
  // stop_reason_id
  if (lhs->stop_reason_id != rhs->stop_reason_id) {
    return false;
  }
  // source_topic
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source_topic), &(rhs->source_topic)))
  {
    return false;
  }
  return true;
}

bool
perception_msgs__msg__StopTarget__copy(
  const perception_msgs__msg__StopTarget * input,
  perception_msgs__msg__StopTarget * output)
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
  // target_type
  output->target_type = input->target_type;
  // distance_from_front_bumper
  output->distance_from_front_bumper = input->distance_from_front_bumper;
  // target_x
  output->target_x = input->target_x;
  // target_y
  output->target_y = input->target_y;
  // confidence
  output->confidence = input->confidence;
  // source
  if (!rosidl_runtime_c__String__copy(
      &(input->source), &(output->source)))
  {
    return false;
  }
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  // waypoint_id
  output->waypoint_id = input->waypoint_id;
  // heading_at_stop
  output->heading_at_stop = input->heading_at_stop;
  // priority
  output->priority = input->priority;
  // required_stop_duration_ms
  output->required_stop_duration_ms = input->required_stop_duration_ms;
  // stop_reason_id
  output->stop_reason_id = input->stop_reason_id;
  // source_topic
  if (!rosidl_runtime_c__String__copy(
      &(input->source_topic), &(output->source_topic)))
  {
    return false;
  }
  return true;
}

perception_msgs__msg__StopTarget *
perception_msgs__msg__StopTarget__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__StopTarget * msg = (perception_msgs__msg__StopTarget *)allocator.allocate(sizeof(perception_msgs__msg__StopTarget), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__StopTarget));
  bool success = perception_msgs__msg__StopTarget__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__StopTarget__destroy(perception_msgs__msg__StopTarget * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__StopTarget__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__StopTarget__Sequence__init(perception_msgs__msg__StopTarget__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__StopTarget * data = NULL;

  if (size) {
    data = (perception_msgs__msg__StopTarget *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__StopTarget), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__StopTarget__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__StopTarget__fini(&data[i - 1]);
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
perception_msgs__msg__StopTarget__Sequence__fini(perception_msgs__msg__StopTarget__Sequence * array)
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
      perception_msgs__msg__StopTarget__fini(&array->data[i]);
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

perception_msgs__msg__StopTarget__Sequence *
perception_msgs__msg__StopTarget__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__StopTarget__Sequence * array = (perception_msgs__msg__StopTarget__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__StopTarget__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__StopTarget__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__StopTarget__Sequence__destroy(perception_msgs__msg__StopTarget__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__StopTarget__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__StopTarget__Sequence__are_equal(const perception_msgs__msg__StopTarget__Sequence * lhs, const perception_msgs__msg__StopTarget__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__StopTarget__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__StopTarget__Sequence__copy(
  const perception_msgs__msg__StopTarget__Sequence * input,
  perception_msgs__msg__StopTarget__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__StopTarget);
    perception_msgs__msg__StopTarget * data =
      (perception_msgs__msg__StopTarget *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__StopTarget__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__StopTarget__fini(&data[i]);
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
    if (!perception_msgs__msg__StopTarget__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
