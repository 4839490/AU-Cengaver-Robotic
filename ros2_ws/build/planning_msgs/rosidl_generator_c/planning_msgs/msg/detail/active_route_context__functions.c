// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/active_route_context__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `route_direction`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"
// Member `planned_trajectory`
#include "geometry_msgs/msg/detail/point__functions.h"

bool
planning_msgs__msg__ActiveRouteContext__init(planning_msgs__msg__ActiveRouteContext * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    planning_msgs__msg__ActiveRouteContext__fini(msg);
    return false;
  }
  // active_waypoint_id
  // target_x
  // target_y
  // target_heading
  // planner_mode
  // route_direction
  if (!rosidl_runtime_c__String__init(&msg->route_direction)) {
    planning_msgs__msg__ActiveRouteContext__fini(msg);
    return false;
  }
  // planned_trajectory
  if (!geometry_msgs__msg__Point__Sequence__init(&msg->planned_trajectory, 0)) {
    planning_msgs__msg__ActiveRouteContext__fini(msg);
    return false;
  }
  // lookahead_distance
  // in_stop_zone
  // distance_to_stop_zone
  // localization_confidence
  // ego_speed_mps
  // route_context_valid
  // age_ms
  // valid_until_ms
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    planning_msgs__msg__ActiveRouteContext__fini(msg);
    return false;
  }
  return true;
}

void
planning_msgs__msg__ActiveRouteContext__fini(planning_msgs__msg__ActiveRouteContext * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // active_waypoint_id
  // target_x
  // target_y
  // target_heading
  // planner_mode
  // route_direction
  rosidl_runtime_c__String__fini(&msg->route_direction);
  // planned_trajectory
  geometry_msgs__msg__Point__Sequence__fini(&msg->planned_trajectory);
  // lookahead_distance
  // in_stop_zone
  // distance_to_stop_zone
  // localization_confidence
  // ego_speed_mps
  // route_context_valid
  // age_ms
  // valid_until_ms
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
planning_msgs__msg__ActiveRouteContext__are_equal(const planning_msgs__msg__ActiveRouteContext * lhs, const planning_msgs__msg__ActiveRouteContext * rhs)
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
  // active_waypoint_id
  if (lhs->active_waypoint_id != rhs->active_waypoint_id) {
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
  // target_heading
  if (lhs->target_heading != rhs->target_heading) {
    return false;
  }
  // planner_mode
  if (lhs->planner_mode != rhs->planner_mode) {
    return false;
  }
  // route_direction
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->route_direction), &(rhs->route_direction)))
  {
    return false;
  }
  // planned_trajectory
  if (!geometry_msgs__msg__Point__Sequence__are_equal(
      &(lhs->planned_trajectory), &(rhs->planned_trajectory)))
  {
    return false;
  }
  // lookahead_distance
  if (lhs->lookahead_distance != rhs->lookahead_distance) {
    return false;
  }
  // in_stop_zone
  if (lhs->in_stop_zone != rhs->in_stop_zone) {
    return false;
  }
  // distance_to_stop_zone
  if (lhs->distance_to_stop_zone != rhs->distance_to_stop_zone) {
    return false;
  }
  // localization_confidence
  if (lhs->localization_confidence != rhs->localization_confidence) {
    return false;
  }
  // ego_speed_mps
  if (lhs->ego_speed_mps != rhs->ego_speed_mps) {
    return false;
  }
  // route_context_valid
  if (lhs->route_context_valid != rhs->route_context_valid) {
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
planning_msgs__msg__ActiveRouteContext__copy(
  const planning_msgs__msg__ActiveRouteContext * input,
  planning_msgs__msg__ActiveRouteContext * output)
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
  // active_waypoint_id
  output->active_waypoint_id = input->active_waypoint_id;
  // target_x
  output->target_x = input->target_x;
  // target_y
  output->target_y = input->target_y;
  // target_heading
  output->target_heading = input->target_heading;
  // planner_mode
  output->planner_mode = input->planner_mode;
  // route_direction
  if (!rosidl_runtime_c__String__copy(
      &(input->route_direction), &(output->route_direction)))
  {
    return false;
  }
  // planned_trajectory
  if (!geometry_msgs__msg__Point__Sequence__copy(
      &(input->planned_trajectory), &(output->planned_trajectory)))
  {
    return false;
  }
  // lookahead_distance
  output->lookahead_distance = input->lookahead_distance;
  // in_stop_zone
  output->in_stop_zone = input->in_stop_zone;
  // distance_to_stop_zone
  output->distance_to_stop_zone = input->distance_to_stop_zone;
  // localization_confidence
  output->localization_confidence = input->localization_confidence;
  // ego_speed_mps
  output->ego_speed_mps = input->ego_speed_mps;
  // route_context_valid
  output->route_context_valid = input->route_context_valid;
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

planning_msgs__msg__ActiveRouteContext *
planning_msgs__msg__ActiveRouteContext__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ActiveRouteContext * msg = (planning_msgs__msg__ActiveRouteContext *)allocator.allocate(sizeof(planning_msgs__msg__ActiveRouteContext), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__ActiveRouteContext));
  bool success = planning_msgs__msg__ActiveRouteContext__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__ActiveRouteContext__destroy(planning_msgs__msg__ActiveRouteContext * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__ActiveRouteContext__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__ActiveRouteContext__Sequence__init(planning_msgs__msg__ActiveRouteContext__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ActiveRouteContext * data = NULL;

  if (size) {
    data = (planning_msgs__msg__ActiveRouteContext *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__ActiveRouteContext), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__ActiveRouteContext__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__ActiveRouteContext__fini(&data[i - 1]);
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
planning_msgs__msg__ActiveRouteContext__Sequence__fini(planning_msgs__msg__ActiveRouteContext__Sequence * array)
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
      planning_msgs__msg__ActiveRouteContext__fini(&array->data[i]);
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

planning_msgs__msg__ActiveRouteContext__Sequence *
planning_msgs__msg__ActiveRouteContext__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__ActiveRouteContext__Sequence * array = (planning_msgs__msg__ActiveRouteContext__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__ActiveRouteContext__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__ActiveRouteContext__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__ActiveRouteContext__Sequence__destroy(planning_msgs__msg__ActiveRouteContext__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__ActiveRouteContext__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__ActiveRouteContext__Sequence__are_equal(const planning_msgs__msg__ActiveRouteContext__Sequence * lhs, const planning_msgs__msg__ActiveRouteContext__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__ActiveRouteContext__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__ActiveRouteContext__Sequence__copy(
  const planning_msgs__msg__ActiveRouteContext__Sequence * input,
  planning_msgs__msg__ActiveRouteContext__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__ActiveRouteContext);
    planning_msgs__msg__ActiveRouteContext * data =
      (planning_msgs__msg__ActiveRouteContext *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__ActiveRouteContext__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__ActiveRouteContext__fini(&data[i]);
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
    if (!planning_msgs__msg__ActiveRouteContext__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
