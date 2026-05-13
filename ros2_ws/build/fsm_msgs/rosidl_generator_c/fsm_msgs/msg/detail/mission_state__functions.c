// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice
#include "fsm_msgs/msg/detail/mission_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
fsm_msgs__msg__MissionState__init(fsm_msgs__msg__MissionState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    fsm_msgs__msg__MissionState__fini(msg);
    return false;
  }
  // mission_active
  // total_waypoints
  // completed_waypoints
  // current_waypoint_id
  // current_waypoint_type
  // next_waypoint_id
  // next_waypoint_type
  // pickup_complete
  // dropoff_complete
  // age_ms
  // valid_until_ms
  return true;
}

void
fsm_msgs__msg__MissionState__fini(fsm_msgs__msg__MissionState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // mission_active
  // total_waypoints
  // completed_waypoints
  // current_waypoint_id
  // current_waypoint_type
  // next_waypoint_id
  // next_waypoint_type
  // pickup_complete
  // dropoff_complete
  // age_ms
  // valid_until_ms
}

bool
fsm_msgs__msg__MissionState__are_equal(const fsm_msgs__msg__MissionState * lhs, const fsm_msgs__msg__MissionState * rhs)
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
  // mission_active
  if (lhs->mission_active != rhs->mission_active) {
    return false;
  }
  // total_waypoints
  if (lhs->total_waypoints != rhs->total_waypoints) {
    return false;
  }
  // completed_waypoints
  if (lhs->completed_waypoints != rhs->completed_waypoints) {
    return false;
  }
  // current_waypoint_id
  if (lhs->current_waypoint_id != rhs->current_waypoint_id) {
    return false;
  }
  // current_waypoint_type
  if (lhs->current_waypoint_type != rhs->current_waypoint_type) {
    return false;
  }
  // next_waypoint_id
  if (lhs->next_waypoint_id != rhs->next_waypoint_id) {
    return false;
  }
  // next_waypoint_type
  if (lhs->next_waypoint_type != rhs->next_waypoint_type) {
    return false;
  }
  // pickup_complete
  if (lhs->pickup_complete != rhs->pickup_complete) {
    return false;
  }
  // dropoff_complete
  if (lhs->dropoff_complete != rhs->dropoff_complete) {
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
  return true;
}

bool
fsm_msgs__msg__MissionState__copy(
  const fsm_msgs__msg__MissionState * input,
  fsm_msgs__msg__MissionState * output)
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
  // mission_active
  output->mission_active = input->mission_active;
  // total_waypoints
  output->total_waypoints = input->total_waypoints;
  // completed_waypoints
  output->completed_waypoints = input->completed_waypoints;
  // current_waypoint_id
  output->current_waypoint_id = input->current_waypoint_id;
  // current_waypoint_type
  output->current_waypoint_type = input->current_waypoint_type;
  // next_waypoint_id
  output->next_waypoint_id = input->next_waypoint_id;
  // next_waypoint_type
  output->next_waypoint_type = input->next_waypoint_type;
  // pickup_complete
  output->pickup_complete = input->pickup_complete;
  // dropoff_complete
  output->dropoff_complete = input->dropoff_complete;
  // age_ms
  output->age_ms = input->age_ms;
  // valid_until_ms
  output->valid_until_ms = input->valid_until_ms;
  return true;
}

fsm_msgs__msg__MissionState *
fsm_msgs__msg__MissionState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__MissionState * msg = (fsm_msgs__msg__MissionState *)allocator.allocate(sizeof(fsm_msgs__msg__MissionState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(fsm_msgs__msg__MissionState));
  bool success = fsm_msgs__msg__MissionState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
fsm_msgs__msg__MissionState__destroy(fsm_msgs__msg__MissionState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    fsm_msgs__msg__MissionState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
fsm_msgs__msg__MissionState__Sequence__init(fsm_msgs__msg__MissionState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__MissionState * data = NULL;

  if (size) {
    data = (fsm_msgs__msg__MissionState *)allocator.zero_allocate(size, sizeof(fsm_msgs__msg__MissionState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = fsm_msgs__msg__MissionState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        fsm_msgs__msg__MissionState__fini(&data[i - 1]);
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
fsm_msgs__msg__MissionState__Sequence__fini(fsm_msgs__msg__MissionState__Sequence * array)
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
      fsm_msgs__msg__MissionState__fini(&array->data[i]);
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

fsm_msgs__msg__MissionState__Sequence *
fsm_msgs__msg__MissionState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  fsm_msgs__msg__MissionState__Sequence * array = (fsm_msgs__msg__MissionState__Sequence *)allocator.allocate(sizeof(fsm_msgs__msg__MissionState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = fsm_msgs__msg__MissionState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
fsm_msgs__msg__MissionState__Sequence__destroy(fsm_msgs__msg__MissionState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    fsm_msgs__msg__MissionState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
fsm_msgs__msg__MissionState__Sequence__are_equal(const fsm_msgs__msg__MissionState__Sequence * lhs, const fsm_msgs__msg__MissionState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!fsm_msgs__msg__MissionState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
fsm_msgs__msg__MissionState__Sequence__copy(
  const fsm_msgs__msg__MissionState__Sequence * input,
  fsm_msgs__msg__MissionState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(fsm_msgs__msg__MissionState);
    fsm_msgs__msg__MissionState * data =
      (fsm_msgs__msg__MissionState *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!fsm_msgs__msg__MissionState__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          fsm_msgs__msg__MissionState__fini(&data[i]);
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
    if (!fsm_msgs__msg__MissionState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
