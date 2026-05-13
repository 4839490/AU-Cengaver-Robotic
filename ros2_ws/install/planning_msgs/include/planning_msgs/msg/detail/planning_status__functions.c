// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice
#include "planning_msgs/msg/detail/planning_status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
planning_msgs__msg__PlanningStatus__init(planning_msgs__msg__PlanningStatus * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    planning_msgs__msg__PlanningStatus__fini(msg);
    return false;
  }
  // status
  // trajectory_valid
  // goal_reached
  // parking_entry_reached
  // obstacle_blocking
  // lane_lost
  // localization_degraded
  // active_waypoint_id
  // distance_to_goal
  // planner_mode
  // age_ms
  // valid_until_ms
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    planning_msgs__msg__PlanningStatus__fini(msg);
    return false;
  }
  return true;
}

void
planning_msgs__msg__PlanningStatus__fini(planning_msgs__msg__PlanningStatus * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // status
  // trajectory_valid
  // goal_reached
  // parking_entry_reached
  // obstacle_blocking
  // lane_lost
  // localization_degraded
  // active_waypoint_id
  // distance_to_goal
  // planner_mode
  // age_ms
  // valid_until_ms
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
planning_msgs__msg__PlanningStatus__are_equal(const planning_msgs__msg__PlanningStatus * lhs, const planning_msgs__msg__PlanningStatus * rhs)
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
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // trajectory_valid
  if (lhs->trajectory_valid != rhs->trajectory_valid) {
    return false;
  }
  // goal_reached
  if (lhs->goal_reached != rhs->goal_reached) {
    return false;
  }
  // parking_entry_reached
  if (lhs->parking_entry_reached != rhs->parking_entry_reached) {
    return false;
  }
  // obstacle_blocking
  if (lhs->obstacle_blocking != rhs->obstacle_blocking) {
    return false;
  }
  // lane_lost
  if (lhs->lane_lost != rhs->lane_lost) {
    return false;
  }
  // localization_degraded
  if (lhs->localization_degraded != rhs->localization_degraded) {
    return false;
  }
  // active_waypoint_id
  if (lhs->active_waypoint_id != rhs->active_waypoint_id) {
    return false;
  }
  // distance_to_goal
  if (lhs->distance_to_goal != rhs->distance_to_goal) {
    return false;
  }
  // planner_mode
  if (lhs->planner_mode != rhs->planner_mode) {
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
planning_msgs__msg__PlanningStatus__copy(
  const planning_msgs__msg__PlanningStatus * input,
  planning_msgs__msg__PlanningStatus * output)
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
  // status
  output->status = input->status;
  // trajectory_valid
  output->trajectory_valid = input->trajectory_valid;
  // goal_reached
  output->goal_reached = input->goal_reached;
  // parking_entry_reached
  output->parking_entry_reached = input->parking_entry_reached;
  // obstacle_blocking
  output->obstacle_blocking = input->obstacle_blocking;
  // lane_lost
  output->lane_lost = input->lane_lost;
  // localization_degraded
  output->localization_degraded = input->localization_degraded;
  // active_waypoint_id
  output->active_waypoint_id = input->active_waypoint_id;
  // distance_to_goal
  output->distance_to_goal = input->distance_to_goal;
  // planner_mode
  output->planner_mode = input->planner_mode;
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

planning_msgs__msg__PlanningStatus *
planning_msgs__msg__PlanningStatus__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__PlanningStatus * msg = (planning_msgs__msg__PlanningStatus *)allocator.allocate(sizeof(planning_msgs__msg__PlanningStatus), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(planning_msgs__msg__PlanningStatus));
  bool success = planning_msgs__msg__PlanningStatus__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
planning_msgs__msg__PlanningStatus__destroy(planning_msgs__msg__PlanningStatus * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    planning_msgs__msg__PlanningStatus__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
planning_msgs__msg__PlanningStatus__Sequence__init(planning_msgs__msg__PlanningStatus__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__PlanningStatus * data = NULL;

  if (size) {
    data = (planning_msgs__msg__PlanningStatus *)allocator.zero_allocate(size, sizeof(planning_msgs__msg__PlanningStatus), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = planning_msgs__msg__PlanningStatus__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        planning_msgs__msg__PlanningStatus__fini(&data[i - 1]);
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
planning_msgs__msg__PlanningStatus__Sequence__fini(planning_msgs__msg__PlanningStatus__Sequence * array)
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
      planning_msgs__msg__PlanningStatus__fini(&array->data[i]);
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

planning_msgs__msg__PlanningStatus__Sequence *
planning_msgs__msg__PlanningStatus__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  planning_msgs__msg__PlanningStatus__Sequence * array = (planning_msgs__msg__PlanningStatus__Sequence *)allocator.allocate(sizeof(planning_msgs__msg__PlanningStatus__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = planning_msgs__msg__PlanningStatus__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
planning_msgs__msg__PlanningStatus__Sequence__destroy(planning_msgs__msg__PlanningStatus__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    planning_msgs__msg__PlanningStatus__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
planning_msgs__msg__PlanningStatus__Sequence__are_equal(const planning_msgs__msg__PlanningStatus__Sequence * lhs, const planning_msgs__msg__PlanningStatus__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!planning_msgs__msg__PlanningStatus__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
planning_msgs__msg__PlanningStatus__Sequence__copy(
  const planning_msgs__msg__PlanningStatus__Sequence * input,
  planning_msgs__msg__PlanningStatus__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(planning_msgs__msg__PlanningStatus);
    planning_msgs__msg__PlanningStatus * data =
      (planning_msgs__msg__PlanningStatus *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!planning_msgs__msg__PlanningStatus__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          planning_msgs__msg__PlanningStatus__fini(&data[i]);
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
    if (!planning_msgs__msg__PlanningStatus__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
