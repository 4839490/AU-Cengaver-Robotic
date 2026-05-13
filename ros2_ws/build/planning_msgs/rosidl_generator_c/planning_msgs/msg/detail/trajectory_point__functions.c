// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/trajectory_point__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
planning_msgs__msg__TrajectoryPoint__init(planning_msgs__msg__TrajectoryPoint * msg)
{
  if (!msg) {
    return false;
  }
  // x
  // y
  // yaw
  // speed
  // curvature
  // distance_from_start
  return true;
}

void
planning_msgs__msg__TrajectoryPoint__fini(planning_msgs__msg__TrajectoryPoint * msg)
{
  if (!msg) {
    return;
  }
  // x
  // y
  // yaw
  // speed
  // curvature
  // distance_from_start
}

bool
planning_msgs__msg__TrajectoryPoint__are_equal(const planning_msgs__msg__TrajectoryPoint * lhs, const planning_msgs__msg__TrajectoryPoint * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x
  if (lhs->x != rhs->x) {
    return false;
  }
  // y
  if (lhs->y != rhs->y) {
    return false;
  }
  // yaw
  if (lhs->yaw != rhs->yaw) {
    return false;
  }
  // speed
  if (lhs->speed != rhs->speed) {
    return false;
  }
  // curvature
  if (lhs->curvature != rhs->curvature) {
    return false;
  }
  // distance_from_start
  if (lhs->distance_from_start != rhs->distance_from_start) {
    return false;
  }
  return true;
}

bool
planning_msgs__msg__TrajectoryPoint__copy(
  const planning_msgs__msg__TrajectoryPoint * input,
  planning_msgs__msg__TrajectoryPoint * output)
{
  if (!input || !output) {
    return false;
  }
  // x
  output->x = input->x;
  // y
  output->y = input->y;
  // yaw
  output->yaw = input->yaw;
  // speed
  output->speed = input->speed;
  // curvature
  output->curvature = input->curvature;
  // distance_from_start
  output->distance_from_start = input->distance_from_start;
  return true;
}

planning_msgs__msg__TrajectoryPoint *
planning_msgs__msg__TrajectoryPoint__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__TrajectoryPoint * msg = (planning_msgs__msg__TrajectoryPoint *)allocator.allocate(sizeof(planning_msgs__msg__TrajectoryPoint), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__TrajectoryPoint));
  bool success = planning_msgs__msg__TrajectoryPoint__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__TrajectoryPoint__destroy(planning_msgs__msg__TrajectoryPoint * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__TrajectoryPoint__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__TrajectoryPoint__Sequence__init(planning_msgs__msg__TrajectoryPoint__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__TrajectoryPoint * data = NULL;

  if (size) {
    data = (planning_msgs__msg__TrajectoryPoint *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__TrajectoryPoint), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__TrajectoryPoint__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__TrajectoryPoint__fini(&data[i - 1]);
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
planning_msgs__msg__TrajectoryPoint__Sequence__fini(planning_msgs__msg__TrajectoryPoint__Sequence * array)
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
      planning_msgs__msg__TrajectoryPoint__fini(&array->data[i]);
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

planning_msgs__msg__TrajectoryPoint__Sequence *
planning_msgs__msg__TrajectoryPoint__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__TrajectoryPoint__Sequence * array = (planning_msgs__msg__TrajectoryPoint__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__TrajectoryPoint__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__TrajectoryPoint__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__TrajectoryPoint__Sequence__destroy(planning_msgs__msg__TrajectoryPoint__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__TrajectoryPoint__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__TrajectoryPoint__Sequence__are_equal(const planning_msgs__msg__TrajectoryPoint__Sequence * lhs, const planning_msgs__msg__TrajectoryPoint__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__TrajectoryPoint__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__TrajectoryPoint__Sequence__copy(
  const planning_msgs__msg__TrajectoryPoint__Sequence * input,
  planning_msgs__msg__TrajectoryPoint__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__TrajectoryPoint);
    planning_msgs__msg__TrajectoryPoint * data =
      (planning_msgs__msg__TrajectoryPoint *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__TrajectoryPoint__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__TrajectoryPoint__fini(&data[i]);
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
    if (!planning_msgs__msg__TrajectoryPoint__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
