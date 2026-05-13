// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from perception_msgs:msg/TrafficSigns.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "perception_msgs/msg/detail/traffic_signs__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace perception_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void TrafficSigns_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) perception_msgs::msg::TrafficSigns(_init);
}

void TrafficSigns_fini_function(void * message_memory)
{
  auto typed_message = static_cast<perception_msgs::msg::TrafficSigns *>(message_memory);
  typed_message->~TrafficSigns();
}

size_t size_function__TrafficSigns__signs(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<perception_msgs::msg::TrafficSign> *>(untyped_member);
  return member->size();
}

const void * get_const_function__TrafficSigns__signs(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<perception_msgs::msg::TrafficSign> *>(untyped_member);
  return &member[index];
}

void * get_function__TrafficSigns__signs(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<perception_msgs::msg::TrafficSign> *>(untyped_member);
  return &member[index];
}

void resize_function__TrafficSigns__signs(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<perception_msgs::msg::TrafficSign> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember TrafficSigns_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs::msg::TrafficSigns, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "signs",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<perception_msgs::msg::TrafficSign>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs::msg::TrafficSigns, signs),  // bytes offset in struct
    nullptr,  // default value
    size_function__TrafficSigns__signs,  // size() function pointer
    get_const_function__TrafficSigns__signs,  // get_const(index) function pointer
    get_function__TrafficSigns__signs,  // get(index) function pointer
    resize_function__TrafficSigns__signs  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers TrafficSigns_message_members = {
  "perception_msgs::msg",  // message namespace
  "TrafficSigns",  // message name
  2,  // number of fields
  sizeof(perception_msgs::msg::TrafficSigns),
  TrafficSigns_message_member_array,  // message members
  TrafficSigns_init_function,  // function to initialize message memory (memory has to be allocated)
  TrafficSigns_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t TrafficSigns_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &TrafficSigns_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace perception_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<perception_msgs::msg::TrafficSigns>()
{
  return &::perception_msgs::msg::rosidl_typesupport_introspection_cpp::TrafficSigns_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, perception_msgs, msg, TrafficSigns)() {
  return &::perception_msgs::msg::rosidl_typesupport_introspection_cpp::TrafficSigns_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
