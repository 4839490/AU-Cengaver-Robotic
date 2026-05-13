// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from planning_msgs:msg/TargetSpeed.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "planning_msgs/msg/detail/target_speed__rosidl_typesupport_introspection_c.h"
#include "planning_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "planning_msgs/msg/detail/target_speed__functions.h"
#include "planning_msgs/msg/detail/target_speed__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  planning_msgs__msg__TargetSpeed__init(message_memory);
}

void TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_fini_function(void * message_memory)
{
  planning_msgs__msg__TargetSpeed__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_member_array[7] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "jerk_limit",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, jerk_limit),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "reason",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, reason),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "valid_until_ms",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, valid_until_ms),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "age_ms",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, age_ms),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "warning_flags",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(planning_msgs__msg__TargetSpeed, warning_flags),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_members = {
  "planning_msgs__msg",  // message namespace
  "TargetSpeed",  // message name
  7,  // number of fields
  sizeof(planning_msgs__msg__TargetSpeed),
  TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_member_array,  // message members
  TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_init_function,  // function to initialize message memory (memory has to be allocated)
  TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_type_support_handle = {
  0,
  &TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_planning_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, planning_msgs, msg, TargetSpeed)() {
  TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_type_support_handle.typesupport_identifier) {
    TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TargetSpeed__rosidl_typesupport_introspection_c__TargetSpeed_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
