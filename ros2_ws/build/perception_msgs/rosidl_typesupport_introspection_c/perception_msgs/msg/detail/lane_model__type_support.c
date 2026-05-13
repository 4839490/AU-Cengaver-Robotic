// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from perception_msgs:msg/LaneModel.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "perception_msgs/msg/detail/lane_model__rosidl_typesupport_introspection_c.h"
#include "perception_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "perception_msgs/msg/detail/lane_model__functions.h"
#include "perception_msgs/msg/detail/lane_model__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `centerline`
// Member `left_boundary`
// Member `right_boundary`
#include "geometry_msgs/msg/point.h"
// Member `centerline`
// Member `left_boundary`
// Member `right_boundary`
#include "geometry_msgs/msg/detail/point__rosidl_typesupport_introspection_c.h"
// Member `source_sensor`
// Member `warning_flags`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void LaneModel__rosidl_typesupport_introspection_c__LaneModel_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  perception_msgs__msg__LaneModel__init(message_memory);
}

void LaneModel__rosidl_typesupport_introspection_c__LaneModel_fini_function(void * message_memory)
{
  perception_msgs__msg__LaneModel__fini(message_memory);
}

size_t LaneModel__rosidl_typesupport_introspection_c__size_function__Point__centerline(
  const void * untyped_member)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return member->size;
}

const void * LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__centerline(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

void * LaneModel__rosidl_typesupport_introspection_c__get_function__Point__centerline(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

bool LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__centerline(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  geometry_msgs__msg__Point__Sequence__fini(member);
  return geometry_msgs__msg__Point__Sequence__init(member, size);
}

size_t LaneModel__rosidl_typesupport_introspection_c__size_function__Point__left_boundary(
  const void * untyped_member)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return member->size;
}

const void * LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__left_boundary(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

void * LaneModel__rosidl_typesupport_introspection_c__get_function__Point__left_boundary(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

bool LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__left_boundary(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  geometry_msgs__msg__Point__Sequence__fini(member);
  return geometry_msgs__msg__Point__Sequence__init(member, size);
}

size_t LaneModel__rosidl_typesupport_introspection_c__size_function__Point__right_boundary(
  const void * untyped_member)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return member->size;
}

const void * LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__right_boundary(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point__Sequence * member =
    (const geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

void * LaneModel__rosidl_typesupport_introspection_c__get_function__Point__right_boundary(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  return &member->data[index];
}

bool LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__right_boundary(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Point__Sequence * member =
    (geometry_msgs__msg__Point__Sequence *)(untyped_member);
  geometry_msgs__msg__Point__Sequence__fini(member);
  return geometry_msgs__msg__Point__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array[12] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "centerline",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, centerline),  // bytes offset in struct
    NULL,  // default value
    LaneModel__rosidl_typesupport_introspection_c__size_function__Point__centerline,  // size() function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__centerline,  // get_const(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_function__Point__centerline,  // get(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__centerline  // resize(index) function pointer
  },
  {
    "left_boundary",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, left_boundary),  // bytes offset in struct
    NULL,  // default value
    LaneModel__rosidl_typesupport_introspection_c__size_function__Point__left_boundary,  // size() function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__left_boundary,  // get_const(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_function__Point__left_boundary,  // get(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__left_boundary  // resize(index) function pointer
  },
  {
    "right_boundary",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, right_boundary),  // bytes offset in struct
    NULL,  // default value
    LaneModel__rosidl_typesupport_introspection_c__size_function__Point__right_boundary,  // size() function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_const_function__Point__right_boundary,  // get_const(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__get_function__Point__right_boundary,  // get(index) function pointer
    LaneModel__rosidl_typesupport_introspection_c__resize_function__Point__right_boundary  // resize(index) function pointer
  },
  {
    "lane_confidence",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, lane_confidence),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "lane_lost",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, lane_lost),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "curvature",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, curvature),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "lane_width_estimate",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, lane_width_estimate),  // bytes offset in struct
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
    offsetof(perception_msgs__msg__LaneModel, age_ms),  // bytes offset in struct
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
    offsetof(perception_msgs__msg__LaneModel, valid_until_ms),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "source_sensor",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs__msg__LaneModel, source_sensor),  // bytes offset in struct
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
    offsetof(perception_msgs__msg__LaneModel, warning_flags),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_members = {
  "perception_msgs__msg",  // message namespace
  "LaneModel",  // message name
  12,  // number of fields
  sizeof(perception_msgs__msg__LaneModel),
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array,  // message members
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_init_function,  // function to initialize message memory (memory has to be allocated)
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_type_support_handle = {
  0,
  &LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_perception_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, perception_msgs, msg, LaneModel)() {
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array[2].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point)();
  if (!LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_type_support_handle.typesupport_identifier) {
    LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &LaneModel__rosidl_typesupport_introspection_c__LaneModel_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
