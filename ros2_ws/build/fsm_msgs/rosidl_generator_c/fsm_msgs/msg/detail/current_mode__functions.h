// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fsm_msgs:msg/CurrentMode.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__CURRENT_MODE__FUNCTIONS_H_
#define FSM_MSGS__MSG__DETAIL__CURRENT_MODE__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fsm_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "fsm_msgs/msg/detail/current_mode__struct.h"

/// Initialize msg/CurrentMode message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fsm_msgs__msg__CurrentMode
 * )) before or use
 * fsm_msgs__msg__CurrentMode__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__init(fsm_msgs__msg__CurrentMode * msg);

/// Finalize msg/CurrentMode message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__CurrentMode__fini(fsm_msgs__msg__CurrentMode * msg);

/// Create msg/CurrentMode message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fsm_msgs__msg__CurrentMode__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
fsm_msgs__msg__CurrentMode *
fsm_msgs__msg__CurrentMode__create();

/// Destroy msg/CurrentMode message.
/**
 * It calls
 * fsm_msgs__msg__CurrentMode__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__CurrentMode__destroy(fsm_msgs__msg__CurrentMode * msg);

/// Check for msg/CurrentMode message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__are_equal(const fsm_msgs__msg__CurrentMode * lhs, const fsm_msgs__msg__CurrentMode * rhs);

/// Copy a msg/CurrentMode message.
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
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__copy(
  const fsm_msgs__msg__CurrentMode * input,
  fsm_msgs__msg__CurrentMode * output);

/// Initialize array of msg/CurrentMode messages.
/**
 * It allocates the memory for the number of elements and calls
 * fsm_msgs__msg__CurrentMode__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__Sequence__init(fsm_msgs__msg__CurrentMode__Sequence * array, size_t size);

/// Finalize array of msg/CurrentMode messages.
/**
 * It calls
 * fsm_msgs__msg__CurrentMode__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__CurrentMode__Sequence__fini(fsm_msgs__msg__CurrentMode__Sequence * array);

/// Create array of msg/CurrentMode messages.
/**
 * It allocates the memory for the array and calls
 * fsm_msgs__msg__CurrentMode__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
fsm_msgs__msg__CurrentMode__Sequence *
fsm_msgs__msg__CurrentMode__Sequence__create(size_t size);

/// Destroy array of msg/CurrentMode messages.
/**
 * It calls
 * fsm_msgs__msg__CurrentMode__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__CurrentMode__Sequence__destroy(fsm_msgs__msg__CurrentMode__Sequence * array);

/// Check for msg/CurrentMode message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__Sequence__are_equal(const fsm_msgs__msg__CurrentMode__Sequence * lhs, const fsm_msgs__msg__CurrentMode__Sequence * rhs);

/// Copy an array of msg/CurrentMode messages.
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
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__CurrentMode__Sequence__copy(
  const fsm_msgs__msg__CurrentMode__Sequence * input,
  fsm_msgs__msg__CurrentMode__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FSM_MSGS__MSG__DETAIL__CURRENT_MODE__FUNCTIONS_H_
