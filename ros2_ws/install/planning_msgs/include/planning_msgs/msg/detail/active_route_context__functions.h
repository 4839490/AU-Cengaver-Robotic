// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__FUNCTIONS_H_
#define PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "planning_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "planning_msgs/msg/detail/active_route_context__struct.h"

/// Initialize msg/ActiveRouteContext message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * planning_msgs__msg__ActiveRouteContext
 * )) before or use
 * planning_msgs__msg__ActiveRouteContext__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__init(planning_msgs__msg__ActiveRouteContext * msg);

/// Finalize msg/ActiveRouteContext message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
void
planning_msgs__msg__ActiveRouteContext__fini(planning_msgs__msg__ActiveRouteContext * msg);

/// Create msg/ActiveRouteContext message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * planning_msgs__msg__ActiveRouteContext__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
planning_msgs__msg__ActiveRouteContext *
planning_msgs__msg__ActiveRouteContext__create();

/// Destroy msg/ActiveRouteContext message.
/**
 * It calls
 * planning_msgs__msg__ActiveRouteContext__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
void
planning_msgs__msg__ActiveRouteContext__destroy(planning_msgs__msg__ActiveRouteContext * msg);

/// Check for msg/ActiveRouteContext message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__are_equal(const planning_msgs__msg__ActiveRouteContext * lhs, const planning_msgs__msg__ActiveRouteContext * rhs);

/// Copy a msg/ActiveRouteContext message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__copy(
  const planning_msgs__msg__ActiveRouteContext * input,
  planning_msgs__msg__ActiveRouteContext * output);

/// Initialize array of msg/ActiveRouteContext messages.
/**
 * It allocates the memory for the number of elements and calls
 * planning_msgs__msg__ActiveRouteContext__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__Sequence__init(planning_msgs__msg__ActiveRouteContext__Sequence * array, size_t size);

/// Finalize array of msg/ActiveRouteContext messages.
/**
 * It calls
 * planning_msgs__msg__ActiveRouteContext__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
void
planning_msgs__msg__ActiveRouteContext__Sequence__fini(planning_msgs__msg__ActiveRouteContext__Sequence * array);

/// Create array of msg/ActiveRouteContext messages.
/**
 * It allocates the memory for the array and calls
 * planning_msgs__msg__ActiveRouteContext__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
planning_msgs__msg__ActiveRouteContext__Sequence *
planning_msgs__msg__ActiveRouteContext__Sequence__create(size_t size);

/// Destroy array of msg/ActiveRouteContext messages.
/**
 * It calls
 * planning_msgs__msg__ActiveRouteContext__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
void
planning_msgs__msg__ActiveRouteContext__Sequence__destroy(planning_msgs__msg__ActiveRouteContext__Sequence * array);

/// Check for msg/ActiveRouteContext message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__Sequence__are_equal(const planning_msgs__msg__ActiveRouteContext__Sequence * lhs, const planning_msgs__msg__ActiveRouteContext__Sequence * rhs);

/// Copy an array of msg/ActiveRouteContext messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_planning_msgs
bool
planning_msgs__msg__ActiveRouteContext__Sequence__copy(
  const planning_msgs__msg__ActiveRouteContext__Sequence * input,
  planning_msgs__msg__ActiveRouteContext__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__FUNCTIONS_H_
