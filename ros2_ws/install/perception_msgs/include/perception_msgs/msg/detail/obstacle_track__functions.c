// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/obstacle_track__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `source_sensor`
// Member `semantic_source`
// Member `geometry_source`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__ObstacleTrack__init(perception_msgs__msg__ObstacleTrack * msg)
{
  if (!msg) {
    return false;
  }
  // track_id
  // class_label
  // confidence
  // position_x
  // position_y
  // distance
  // velocity_x
  // velocity_y
  // ttc
  // width
  // length
  // height
  // is_static
  // source_sensor
  if (!rosidl_runtime_c__String__init(&msg->source_sensor)) {
    perception_msgs__msg__ObstacleTrack__fini(msg);
    return false;
  }
  // semantic_source
  if (!rosidl_runtime_c__String__init(&msg->semantic_source)) {
    perception_msgs__msg__ObstacleTrack__fini(msg);
    return false;
  }
  // geometry_source
  if (!rosidl_runtime_c__String__init(&msg->geometry_source)) {
    perception_msgs__msg__ObstacleTrack__fini(msg);
    return false;
  }
  // age_ms
  // valid_until_ms
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__ObstacleTrack__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__ObstacleTrack__fini(perception_msgs__msg__ObstacleTrack * msg)
{
  if (!msg) {
    return;
  }
  // track_id
  // class_label
  // confidence
  // position_x
  // position_y
  // distance
  // velocity_x
  // velocity_y
  // ttc
  // width
  // length
  // height
  // is_static
  // source_sensor
  rosidl_runtime_c__String__fini(&msg->source_sensor);
  // semantic_source
  rosidl_runtime_c__String__fini(&msg->semantic_source);
  // geometry_source
  rosidl_runtime_c__String__fini(&msg->geometry_source);
  // age_ms
  // valid_until_ms
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__ObstacleTrack__are_equal(const perception_msgs__msg__ObstacleTrack * lhs, const perception_msgs__msg__ObstacleTrack * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // track_id
  if (lhs->track_id != rhs->track_id) {
    return false;
  }
  // class_label
  if (lhs->class_label != rhs->class_label) {
    return false;
  }
  // confidence
  if (lhs->confidence != rhs->confidence) {
    return false;
  }
  // position_x
  if (lhs->position_x != rhs->position_x) {
    return false;
  }
  // position_y
  if (lhs->position_y != rhs->position_y) {
    return false;
  }
  // distance
  if (lhs->distance != rhs->distance) {
    return false;
  }
  // velocity_x
  if (lhs->velocity_x != rhs->velocity_x) {
    return false;
  }
  // velocity_y
  if (lhs->velocity_y != rhs->velocity_y) {
    return false;
  }
  // ttc
  if (lhs->ttc != rhs->ttc) {
    return false;
  }
  // width
  if (lhs->width != rhs->width) {
    return false;
  }
  // length
  if (lhs->length != rhs->length) {
    return false;
  }
  // height
  if (lhs->height != rhs->height) {
    return false;
  }
  // is_static
  if (lhs->is_static != rhs->is_static) {
    return false;
  }
  // source_sensor
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->source_sensor), &(rhs->source_sensor)))
  {
    return false;
  }
  // semantic_source
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->semantic_source), &(rhs->semantic_source)))
  {
    return false;
  }
  // geometry_source
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->geometry_source), &(rhs->geometry_source)))
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
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__are_equal(
      &(lhs->warning_flags), &(rhs->warning_flags)))
  {
    return false;
  }
  return true;
}

bool
perception_msgs__msg__ObstacleTrack__copy(
  const perception_msgs__msg__ObstacleTrack * input,
  perception_msgs__msg__ObstacleTrack * output)
{
  if (!input || !output) {
    return false;
  }
  // track_id
  output->track_id = input->track_id;
  // class_label
  output->class_label = input->class_label;
  // confidence
  output->confidence = input->confidence;
  // position_x
  output->position_x = input->position_x;
  // position_y
  output->position_y = input->position_y;
  // distance
  output->distance = input->distance;
  // velocity_x
  output->velocity_x = input->velocity_x;
  // velocity_y
  output->velocity_y = input->velocity_y;
  // ttc
  output->ttc = input->ttc;
  // width
  output->width = input->width;
  // length
  output->length = input->length;
  // height
  output->height = input->height;
  // is_static
  output->is_static = input->is_static;
  // source_sensor
  if (!rosidl_runtime_c__String__copy(
      &(input->source_sensor), &(output->source_sensor)))
  {
    return false;
  }
  // semantic_source
  if (!rosidl_runtime_c__String__copy(
      &(input->semantic_source), &(output->semantic_source)))
  {
    return false;
  }
  // geometry_source
  if (!rosidl_runtime_c__String__copy(
      &(input->geometry_source), &(output->geometry_source)))
  {
    return false;
  }
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

perception_msgs__msg__ObstacleTrack *
perception_msgs__msg__ObstacleTrack__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__ObstacleTrack * msg = (perception_msgs__msg__ObstacleTrack *)allocator.allocate(sizeof(perception_msgs__msg__ObstacleTrack), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__ObstacleTrack));
  bool success = perception_msgs__msg__ObstacleTrack__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__ObstacleTrack__destroy(perception_msgs__msg__ObstacleTrack * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__ObstacleTrack__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__ObstacleTrack__Sequence__init(perception_msgs__msg__ObstacleTrack__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__ObstacleTrack * data = NULL;

  if (size) {
    data = (perception_msgs__msg__ObstacleTrack *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__ObstacleTrack), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__ObstacleTrack__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__ObstacleTrack__fini(&data[i - 1]);
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
perception_msgs__msg__ObstacleTrack__Sequence__fini(perception_msgs__msg__ObstacleTrack__Sequence * array)
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
      perception_msgs__msg__ObstacleTrack__fini(&array->data[i]);
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

perception_msgs__msg__ObstacleTrack__Sequence *
perception_msgs__msg__ObstacleTrack__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__ObstacleTrack__Sequence * array = (perception_msgs__msg__ObstacleTrack__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__ObstacleTrack__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__ObstacleTrack__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__ObstacleTrack__Sequence__destroy(perception_msgs__msg__ObstacleTrack__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__ObstacleTrack__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__ObstacleTrack__Sequence__are_equal(const perception_msgs__msg__ObstacleTrack__Sequence * lhs, const perception_msgs__msg__ObstacleTrack__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__ObstacleTrack__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__ObstacleTrack__Sequence__copy(
  const perception_msgs__msg__ObstacleTrack__Sequence * input,
  perception_msgs__msg__ObstacleTrack__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__ObstacleTrack);
    perception_msgs__msg__ObstacleTrack * data =
      (perception_msgs__msg__ObstacleTrack *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__ObstacleTrack__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__ObstacleTrack__fini(&data[i]);
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
    if (!perception_msgs__msg__ObstacleTrack__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
