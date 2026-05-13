// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "common_msgs/msg/detail/stop_reason__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace common_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void StopReason_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) common_msgs::msg::StopReason(_init);
}

void StopReason_fini_function(void * message_memory)
{
  auto typed_message = static_cast<common_msgs::msg::StopReason *>(message_memory);
  typed_message->~StopReason();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember StopReason_message_member_array[1] = {
  {
    "reason",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(common_msgs::msg::StopReason, reason),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers StopReason_message_members = {
  "common_msgs::msg",  // message namespace
  "StopReason",  // message name
  1,  // number of fields
  sizeof(common_msgs::msg::StopReason),
  StopReason_message_member_array,  // message members
  StopReason_init_function,  // function to initialize message memory (memory has to be allocated)
  StopReason_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t StopReason_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &StopReason_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace common_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<common_msgs::msg::StopReason>()
{
  return &::common_msgs::msg::rosidl_typesupport_introspection_cpp::StopReason_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, common_msgs, msg, StopReason)() {
  return &::common_msgs::msg::rosidl_typesupport_introspection_cpp::StopReason_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
