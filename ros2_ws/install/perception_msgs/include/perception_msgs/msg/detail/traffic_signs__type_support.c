// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from perception_msgs:msg/TrafficSigns.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "perception_msgs/msg/detail/traffic_signs__rosidl_typesupport_introspection_c.h"
#include "perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "perception_msgs/msg/detail/traffic_signs__functions.h"
#include "perception_msgs/msg/detail/traffic_signs__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `signs`
#include "perception_msgs/msg/traffic_sign.h"
// Member `signs`
#include "perception_msgs/msg/detail/traffic_sign__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  perception_msgs__msg__TrafficSigns__init(message_memory);
}

void TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_fini_function(void * message_memory)
{
  perception_msgs__msg__TrafficSigns__fini(message_memory);
}

size_t TrafficSigns__rosidl_typesupport_introspection_c__size_function__TrafficSign__signs(
  const void * untyped_member)
{
  const perception_msgs__msg__TrafficSign__Sequence * member =
    (const perception_msgs__msg__TrafficSign__Sequence *)(untyped_member);
  return member->size;
}

const void * TrafficSigns__rosidl_typesupport_introspection_c__get_const_function__TrafficSign__signs(
  const void * untyped_member, size_t index)
{
  const perception_msgs__msg__TrafficSign__Sequence * member =
    (const perception_msgs__msg__TrafficSign__Sequence *)(untyped_member);
  return &member->data[index];
}

void * TrafficSigns__rosidl_typesupport_introspection_c__get_function__TrafficSign__signs(
  void * untyped_member, size_t index)
{
  perception_msgs__msg__TrafficSign__Sequence * member =
    (perception_msgs__msg__TrafficSign__Sequence *)(untyped_member);
  return &member->data[index];
}

bool TrafficSigns__rosidl_typesupport_introspection_c__resize_function__TrafficSign__signs(
  void * untyped_member, size_t size)
{
  perception_msgs__msg__TrafficSign__Sequence * member =
    (perception_msgs__msg__TrafficSign__Sequence *)(untyped_member);
  perception_msgs__msg__TrafficSign__Sequence__fini(member);
  return perception_msgs__msg__TrafficSign__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__TrafficSigns, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "signs",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__TrafficSigns, signs),  // bytes offset in struct
    NULL,  // default value
    TrafficSigns__rosidl_typesupport_introspection_c__size_function__TrafficSign__signs,  // size() function pointer
    TrafficSigns__rosidl_typesupport_introspection_c__get_const_function__TrafficSign__signs,  // get_const(index) function pointer
    TrafficSigns__rosidl_typesupport_introspection_c__get_function__TrafficSign__signs,  // get(index) function pointer
    TrafficSigns__rosidl_typesupport_introspection_c__resize_function__TrafficSign__signs  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_members = {
  "perception_msgs__msg",  // message namespace
  "TrafficSigns",  // message name
  2,  // number of fields
  sizeof(perception_msgs__msg__TrafficSigns),
  TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_member_array,  // message members
  TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_init_function,  // function to initialize message memory (memory has to be allocated)
  TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_type_support_handle = {
  0,
  &TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, perception_msgs, msg, TrafficSigns)() {
  TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, perception_msgs, msg, TrafficSign)();
  if (!TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_type_support_handle.typesupport_identifier) {
    TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &TrafficSigns__rosidl_typesupport_introspection_c__TrafficSigns_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
