// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from perception_msgs:msg/PerceptionDiagnostics.idl
// generated code does not contain a copyright notice
#include "perception_msgs/msg/detail/perception_diagnostics__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `node_name`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

bool
perception_msgs__msg__PerceptionDiagnostics__init(perception_msgs__msg__PerceptionDiagnostics * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    perception_msgs__msg__PerceptionDiagnostics__fini(msg);
    return false;
  }
  // node_name
  if (!rosidl_runtime_c__String__init(&msg->node_name)) {
    perception_msgs__msg__PerceptionDiagnostics__fini(msg);
    return false;
  }
  // input_hz
  // output_hz
  // latency_ms
  // last_msg_age_ms
  // mean_confidence
  // num_outputs
  // gpu_utilization
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__init(&msg->warning_flags, 0)) {
    perception_msgs__msg__PerceptionDiagnostics__fini(msg);
    return false;
  }
  return true;
}

void
perception_msgs__msg__PerceptionDiagnostics__fini(perception_msgs__msg__PerceptionDiagnostics * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // node_name
  rosidl_runtime_c__String__fini(&msg->node_name);
  // input_hz
  // output_hz
  // latency_ms
  // last_msg_age_ms
  // mean_confidence
  // num_outputs
  // gpu_utilization
  // warning_flags
  rosidl_runtime_c__String__Sequence__fini(&msg->warning_flags);
}

bool
perception_msgs__msg__PerceptionDiagnostics__are_equal(const perception_msgs__msg__PerceptionDiagnostics * lhs, const perception_msgs__msg__PerceptionDiagnostics * rhs)
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
  // node_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->node_name), &(rhs->node_name)))
  {
    return false;
  }
  // input_hz
  if (lhs->input_hz != rhs->input_hz) {
    return false;
  }
  // output_hz
  if (lhs->output_hz != rhs->output_hz) {
    return false;
  }
  // latency_ms
  if (lhs->latency_ms != rhs->latency_ms) {
    return false;
  }
  // last_msg_age_ms
  if (lhs->last_msg_age_ms != rhs->last_msg_age_ms) {
    return false;
  }
  // mean_confidence
  if (lhs->mean_confidence != rhs->mean_confidence) {
    return false;
  }
  // num_outputs
  if (lhs->num_outputs != rhs->num_outputs) {
    return false;
  }
  // gpu_utilization
  if (lhs->gpu_utilization != rhs->gpu_utilization) {
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
perception_msgs__msg__PerceptionDiagnostics__copy(
  const perception_msgs__msg__PerceptionDiagnostics * input,
  perception_msgs__msg__PerceptionDiagnostics * output)
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
  // node_name
  if (!rosidl_runtime_c__String__copy(
      &(input->node_name), &(output->node_name)))
  {
    return false;
  }
  // input_hz
  output->input_hz = input->input_hz;
  // output_hz
  output->output_hz = input->output_hz;
  // latency_ms
  output->latency_ms = input->latency_ms;
  // last_msg_age_ms
  output->last_msg_age_ms = input->last_msg_age_ms;
  // mean_confidence
  output->mean_confidence = input->mean_confidence;
  // num_outputs
  output->num_outputs = input->num_outputs;
  // gpu_utilization
  output->gpu_utilization = input->gpu_utilization;
  // warning_flags
  if (!rosidl_runtime_c__String__Sequence__copy(
      &(input->warning_flags), &(output->warning_flags)))
  {
    return false;
  }
  return true;
}

perception_msgs__msg__PerceptionDiagnostics *
perception_msgs__msg__PerceptionDiagnostics__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__PerceptionDiagnostics * msg = (perception_msgs__msg__PerceptionDiagnostics *)allocator.allocate(sizeof(perception_msgs__msg__PerceptionDiagnostics), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(perception_msgs__msg__PerceptionDiagnostics));
  bool success = perception_msgs__msg__PerceptionDiagnostics__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
perception_msgs__msg__PerceptionDiagnostics__destroy(perception_msgs__msg__PerceptionDiagnostics * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    perception_msgs__msg__PerceptionDiagnostics__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
perception_msgs__msg__PerceptionDiagnostics__Sequence__init(perception_msgs__msg__PerceptionDiagnostics__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__PerceptionDiagnostics * data = NULL;

  if (size) {
    data = (perception_msgs__msg__PerceptionDiagnostics *)allocator.zero_allocate(size, sizeof(perception_msgs__msg__PerceptionDiagnostics), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = perception_msgs__msg__PerceptionDiagnostics__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        perception_msgs__msg__PerceptionDiagnostics__fini(&data[i - 1]);
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
perception_msgs__msg__PerceptionDiagnostics__Sequence__fini(perception_msgs__msg__PerceptionDiagnostics__Sequence * array)
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
      perception_msgs__msg__PerceptionDiagnostics__fini(&array->data[i]);
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

perception_msgs__msg__PerceptionDiagnostics__Sequence *
perception_msgs__msg__PerceptionDiagnostics__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  perception_msgs__msg__PerceptionDiagnostics__Sequence * array = (perception_msgs__msg__PerceptionDiagnostics__Sequence *)allocator.allocate(sizeof(perception_msgs__msg__PerceptionDiagnostics__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = perception_msgs__msg__PerceptionDiagnostics__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
perception_msgs__msg__PerceptionDiagnostics__Sequence__destroy(perception_msgs__msg__PerceptionDiagnostics__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    perception_msgs__msg__PerceptionDiagnostics__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
perception_msgs__msg__PerceptionDiagnostics__Sequence__are_equal(const perception_msgs__msg__PerceptionDiagnostics__Sequence * lhs, const perception_msgs__msg__PerceptionDiagnostics__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!perception_msgs__msg__PerceptionDiagnostics__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
perception_msgs__msg__PerceptionDiagnostics__Sequence__copy(
  const perception_msgs__msg__PerceptionDiagnostics__Sequence * input,
  perception_msgs__msg__PerceptionDiagnostics__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(perception_msgs__msg__PerceptionDiagnostics);
    perception_msgs__msg__PerceptionDiagnostics * data =
      (perception_msgs__msg__PerceptionDiagnostics *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!perception_msgs__msg__PerceptionDiagnostics__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          perception_msgs__msg__PerceptionDiagnostics__fini(&data[i]);
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
    if (!perception_msgs__msg__PerceptionDiagnostics__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
