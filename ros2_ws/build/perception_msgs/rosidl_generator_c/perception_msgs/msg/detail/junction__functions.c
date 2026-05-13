// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/Junction.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/junction__functions.h"

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
perception_msgs__msg__Junction__init(perception_msgs__msg__Junction * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    perception_msgs__msg__Junction__fini(msg);
    return false;
  }
  // detected
  // junction_type
  // arm_count
  // distance_to_entry
  // confidence
  // age_ms
  // valid_until_ms
  // source_sensor
  if (!rosidl_runtime_c__String__init(&msg->source_sensor)) {
    perception_msgs__msg__Junction__fini(msg);
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__Junction__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__Junction__fini(perception_msgs__msg__Junction * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // detected
  // junction_type
  // arm_count
  // distance_to_entry
  // confidence
  // age_ms
  // valid_until_ms
  // source_sensor
  rosidl_runtime_c__String__fini(&msg->source_sensor);
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__Junction__are_equal(const perception_msgs__msg__Junction * lhs, const perception_msgs__msg__Junction * rhs)
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
  // detected
  if (lhs->detected != rhs->detected) {
    return false;
  }
  // junction_type
  if (lhs->junction_type != rhs->junction_type) {
    return false;
  }
  // arm_count
  if (lhs->arm_count != rhs->arm_count) {
    return false;
  }
  // distance_to_entry
  if (lhs->distance_to_entry != rhs->distance_to_entry) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
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
perception_msgs__msg__Junction__copy(
  const perception_msgs__msg__Junction * input,
  perception_msgs__msg__Junction * output)
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
  // detected
  output->detected = input->detected;
  // junction_type
  output->junction_type = input->junction_type;
  // arm_count
  output->arm_count = input->arm_count;
  // distance_to_entry
  output->distance_to_entry = input->distance_to_entry;
  // confidence
  output->confidence = input->confidence;
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

perception_msgs__msg__Junction *
perception_msgs__msg__Junction__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__Junction * msg = (perception_msgs__msg__Junction *)allocator.allocate(sizeof(perception_msgs__msg__Junction), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__Junction));
  bool success = perception_msgs__msg__Junction__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__Junction__destroy(perception_msgs__msg__Junction * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__Junction__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__Junction__Sequence__init(perception_msgs__msg__Junction__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__Junction * data = NULL;

  if (size) {
    data = (perception_msgs__msg__Junction *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__Junction), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__Junction__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__Junction__fini(&data[i - 1]);
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
perception_msgs__msg__Junction__Sequence__fini(perception_msgs__msg__Junction__Sequence * array)
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
      perception_msgs__msg__Junction__fini(&array->data[i]);
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

perception_msgs__msg__Junction__Sequence *
perception_msgs__msg__Junction__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__Junction__Sequence * array = (perception_msgs__msg__Junction__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__Junction__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__Junction__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__Junction__Sequence__destroy(perception_msgs__msg__Junction__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__Junction__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__Junction__Sequence__are_equal(const perception_msgs__msg__Junction__Sequence * lhs, const perception_msgs__msg__Junction__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__Junction__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__Junction__Sequence__copy(
  const perception_msgs__msg__Junction__Sequence * input,
  perception_msgs__msg__Junction__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__Junction);
    perception_msgs__msg__Junction * data =
      (perception_msgs__msg__Junction *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__Junction__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__Junction__fini(&data[i]);
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
    if (!perception_msgs__msg__Junction__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
