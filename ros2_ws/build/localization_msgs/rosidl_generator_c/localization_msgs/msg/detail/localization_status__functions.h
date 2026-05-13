// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__FUNCTIONS_H_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "localization_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "localization_msgs/msg/detail/localization_status__struct.h"

/// Initialize msg/LocalizationStatus message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * localization_msgs__msg__LocalizationStatus
 * )) before or use
 * localization_msgs__msg__LocalizationStatus__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__init(localization_msgs__msg__LocalizationStatus * msg);

/// Finalize msg/LocalizationStatus message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
void
localization_msgs__msg__LocalizationStatus__fini(localization_msgs__msg__LocalizationStatus * msg);

/// Create msg/LocalizationStatus message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * localization_msgs__msg__LocalizationStatus__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
localization_msgs__msg__LocalizationStatus *
localization_msgs__msg__LocalizationStatus__create();

/// Destroy msg/LocalizationStatus message.
/**
 * It calls
 * localization_msgs__msg__LocalizationStatus__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
void
localization_msgs__msg__LocalizationStatus__destroy(localization_msgs__msg__LocalizationStatus * msg);

/// Check for msg/LocalizationStatus message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__are_equal(const localization_msgs__msg__LocalizationStatus * lhs, const localization_msgs__msg__LocalizationStatus * rhs);

/// Copy a msg/LocalizationStatus message.
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
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__copy(
  const localization_msgs__msg__LocalizationStatus * input,
  localization_msgs__msg__LocalizationStatus * output);

/// Initialize array of msg/LocalizationStatus messages.
/**
 * It allocates the memory for the number of elements and calls
 * localization_msgs__msg__LocalizationStatus__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__Sequence__init(localization_msgs__msg__LocalizationStatus__Sequence * array, size_t size);

/// Finalize array of msg/LocalizationStatus messages.
/**
 * It calls
 * localization_msgs__msg__LocalizationStatus__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
void
localization_msgs__msg__LocalizationStatus__Sequence__fini(localization_msgs__msg__LocalizationStatus__Sequence * array);

/// Create array of msg/LocalizationStatus messages.
/**
 * It allocates the memory for the array and calls
 * localization_msgs__msg__LocalizationStatus__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
localization_msgs__msg__LocalizationStatus__Sequence *
localization_msgs__msg__LocalizationStatus__Sequence__create(size_t size);

/// Destroy array of msg/LocalizationStatus messages.
/**
 * It calls
 * localization_msgs__msg__LocalizationStatus__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
void
localization_msgs__msg__LocalizationStatus__Sequence__destroy(localization_msgs__msg__LocalizationStatus__Sequence * array);

/// Check for msg/LocalizationStatus message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__Sequence__are_equal(const localization_msgs__msg__LocalizationStatus__Sequence * lhs, const localization_msgs__msg__LocalizationStatus__Sequence * rhs);

/// Copy an array of msg/LocalizationStatus messages.
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
ROSIDL_GENERATOR_C_PUBLIC_localization_msgs
bool
localization_msgs__msg__LocalizationStatus__Sequence__copy(
  const localization_msgs__msg__LocalizationStatus__Sequence * input,
  localization_msgs__msg__LocalizationStatus__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__FUNCTIONS_H_
