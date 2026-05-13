// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__FSM_EVENT__FUNCTIONS_H_
#define FSM_MSGS__MSG__DETAIL__FSM_EVENT__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "fsm_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "fsm_msgs/msg/detail/fsm_event__struct.h"

/// Initialize msg/FSMEvent message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * fsm_msgs__msg__FSMEvent
 * )) before or use
 * fsm_msgs__msg__FSMEvent__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__FSMEvent__init(fsm_msgs__msg__FSMEvent * msg);

/// Finalize msg/FSMEvent message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__FSMEvent__fini(fsm_msgs__msg__FSMEvent * msg);

/// Create msg/FSMEvent message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * fsm_msgs__msg__FSMEvent__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
fsm_msgs__msg__FSMEvent *
fsm_msgs__msg__FSMEvent__create();

/// Destroy msg/FSMEvent message.
/**
 * It calls
 * fsm_msgs__msg__FSMEvent__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__FSMEvent__destroy(fsm_msgs__msg__FSMEvent * msg);

/// Check for msg/FSMEvent message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__FSMEvent__are_equal(const fsm_msgs__msg__FSMEvent * lhs, const fsm_msgs__msg__FSMEvent * rhs);

/// Copy a msg/FSMEvent message.
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
fsm_msgs__msg__FSMEvent__copy(
  const fsm_msgs__msg__FSMEvent * input,
  fsm_msgs__msg__FSMEvent * output);

/// Initialize array of msg/FSMEvent messages.
/**
 * It allocates the memory for the number of elements and calls
 * fsm_msgs__msg__FSMEvent__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__FSMEvent__Sequence__init(fsm_msgs__msg__FSMEvent__Sequence * array, size_t size);

/// Finalize array of msg/FSMEvent messages.
/**
 * It calls
 * fsm_msgs__msg__FSMEvent__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__FSMEvent__Sequence__fini(fsm_msgs__msg__FSMEvent__Sequence * array);

/// Create array of msg/FSMEvent messages.
/**
 * It allocates the memory for the array and calls
 * fsm_msgs__msg__FSMEvent__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
fsm_msgs__msg__FSMEvent__Sequence *
fsm_msgs__msg__FSMEvent__Sequence__create(size_t size);

/// Destroy array of msg/FSMEvent messages.
/**
 * It calls
 * fsm_msgs__msg__FSMEvent__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
void
fsm_msgs__msg__FSMEvent__Sequence__destroy(fsm_msgs__msg__FSMEvent__Sequence * array);

/// Check for msg/FSMEvent message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_fsm_msgs
bool
fsm_msgs__msg__FSMEvent__Sequence__are_equal(const fsm_msgs__msg__FSMEvent__Sequence * lhs, const fsm_msgs__msg__FSMEvent__Sequence * rhs);

/// Copy an array of msg/FSMEvent messages.
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
fsm_msgs__msg__FSMEvent__Sequence__copy(
  const fsm_msgs__msg__FSMEvent__Sequence * input,
  fsm_msgs__msg__FSMEvent__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // FSM_MSGS__MSG__DETAIL__FSM_EVENT__FUNCTIONS_H_
