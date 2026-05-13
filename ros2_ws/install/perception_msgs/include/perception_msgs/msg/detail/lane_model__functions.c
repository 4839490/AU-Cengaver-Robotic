// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/LaneModel.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/lane_model__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `centerline`
// Member `left_boundary`
// Member `right_boundary`
#include "geometry_msgs/msg/detail/point__functions.h"
// Member `source_sensor`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__LaneModel__init(perception_msgs__msg__LaneModel * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  // centerline
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->centerline, 0)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  // left_boundary
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->left_boundary, 0)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  // right_boundary
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->right_boundary, 0)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  // lane_confidence
  // lane_lost
  // curvature
  // lane_width_estimate
  // age_ms
  // valid_until_ms
  // source_sensor
  if (!rosidl_runtime_c__String__init(&msg->source_sensor)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__LaneModel__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__LaneModel__fini(perception_msgs__msg__LaneModel * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // centerline
  geometry_msgs__msg__Point__Sequence__fini(&msg->centerline);
  // left_boundary
  geometry_msgs__msg__Point__Sequence__fini(&msg->left_boundary);
  // right_boundary
  geometry_msgs__msg__Point__Sequence__fini(&msg->right_boundary);
  // lane_confidence
  // lane_lost
  // curvature
  // lane_width_estimate
  // age_ms
  // valid_until_ms
  // source_sensor
  rosidl_runtime_c__String__fini(&msg->source_sensor);
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__LaneModel__are_equal(const perception_msgs__msg__LaneModel * lhs, const perception_msgs__msg__LaneModel * rhs)
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
  // centerline
  if (!geometry_msgs__msg__Point__Sequence__are_equal(
      &(lhs->centerline), &(rhs->centerline)))
  {
    return false;
  }
  // left_boundary
  if (!geometry_msgs__msg__Point__Sequence__are_equal(
      &(lhs->left_boundary), &(rhs->left_boundary)))
  {
    return false;
  }
  // right_boundary
  if (!geometry_msgs__msg__Point__Sequence__are_equal(
      &(lhs->right_boundary), &(rhs->right_boundary)))
  {
    return false;
  }
  // lane_confidence
  if (lhs->lane_confidence != rhs->lane_confidence) {
    return false;
  }
  // lane_lost
  if (lhs->lane_lost != rhs->lane_lost) {
    return false;
  }
  // curvature
  if (lhs->curvature != rhs->curvature) {
    return false;
  }
  // lane_width_estimate
  if (lhs->lane_width_estimate != rhs->lane_width_estimate) {
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
perception_msgs__msg__LaneModel__copy(
  const perception_msgs__msg__LaneModel * input,
  perception_msgs__msg__LaneModel * output)
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
  // centerline
  if (!geometry_msgs__msg__Point__Sequence__copy(
      &(input->centerline), &(output->centerline)))
  {
    return false;
  }
  // left_boundary
  if (!geometry_msgs__msg__Point__Sequence__copy(
      &(input->left_boundary), &(output->left_boundary)))
  {
    return false;
  }
  // right_boundary
  if (!geometry_msgs__msg__Point__Sequence__copy(
      &(input->right_boundary), &(output->right_boundary)))
  {
    return false;
  }
  // lane_confidence
  output->lane_confidence = input->lane_confidence;
  // lane_lost
  output->lane_lost = input->lane_lost;
  // curvature
  output->curvature = input->curvature;
  // lane_width_estimate
  output->lane_width_estimate = input->lane_width_estimate;
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

perception_msgs__msg__LaneModel *
perception_msgs__msg__LaneModel__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__LaneModel * msg = (perception_msgs__msg__LaneModel *)allocator.allocate(sizeof(perception_msgs__msg__LaneModel), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__LaneModel));
  bool success = perception_msgs__msg__LaneModel__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__LaneModel__destroy(perception_msgs__msg__LaneModel * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__LaneModel__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__LaneModel__Sequence__init(perception_msgs__msg__LaneModel__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__LaneModel * data = NULL;

  if (size) {
    data = (perception_msgs__msg__LaneModel *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__LaneModel), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__LaneModel__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__LaneModel__fini(&data[i - 1]);
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
perception_msgs__msg__LaneModel__Sequence__fini(perception_msgs__msg__LaneModel__Sequence * array)
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
      perception_msgs__msg__LaneModel__fini(&array->data[i]);
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

perception_msgs__msg__LaneModel__Sequence *
perception_msgs__msg__LaneModel__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__LaneModel__Sequence * array = (perception_msgs__msg__LaneModel__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__LaneModel__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__LaneModel__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__LaneModel__Sequence__destroy(perception_msgs__msg__LaneModel__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__LaneModel__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__LaneModel__Sequence__are_equal(const perception_msgs__msg__LaneModel__Sequence * lhs, const perception_msgs__msg__LaneModel__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__LaneModel__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__LaneModel__Sequence__copy(
  const perception_msgs__msg__LaneModel__Sequence * input,
  perception_msgs__msg__LaneModel__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__LaneModel);
    perception_msgs__msg__LaneModel * data =
      (perception_msgs__msg__LaneModel *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__LaneModel__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__LaneModel__fini(&data[i]);
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
    if (!perception_msgs__msg__LaneModel__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
