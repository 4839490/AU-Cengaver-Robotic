// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from perception_msgs:msg/ObstacleTracks.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "perception_msgs/msg/detail/obstacle_tracks__struct.hpp"
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

void ObstacleTracks_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) perception_msgs::msg::ObstacleTracks(_init);
}

void ObstacleTracks_fini_function(void * message_memory)
{
  auto typed_message = static_cast<perception_msgs::msg::ObstacleTracks *>(message_memory);
  typed_message->~ObstacleTracks();
}

size_t size_function__ObstacleTracks__tracks(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<perception_msgs::msg::ObstacleTrack> *>(untyped_member);
  return member->size();
}

const void * get_const_function__ObstacleTracks__tracks(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<perception_msgs::msg::ObstacleTrack> *>(untyped_member);
  return &member[index];
}

void * get_function__ObstacleTracks__tracks(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<perception_msgs::msg::ObstacleTrack> *>(untyped_member);
  return &member[index];
}

void resize_function__ObstacleTracks__tracks(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<perception_msgs::msg::ObstacleTrack> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ObstacleTracks_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs::msg::ObstacleTracks, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "tracks",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<perception_msgs::msg::ObstacleTrack>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(perception_msgs::msg::ObstacleTracks, tracks),  // bytes offset in struct
    nullptr,  // default value
    size_function__ObstacleTracks__tracks,  // size() function pointer
    get_const_function__ObstacleTracks__tracks,  // get_const(index) function pointer
    get_function__ObstacleTracks__tracks,  // get(index) function pointer
    resize_function__ObstacleTracks__tracks  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ObstacleTracks_message_members = {
  "perception_msgs::msg",  // message namespace
  "ObstacleTracks",  // message name
  2,  // number of fields
  sizeof(perception_msgs::msg::ObstacleTracks),
  ObstacleTracks_message_member_array,  // message members
  ObstacleTracks_init_function,  // function to initialize message memory (memory has to be allocated)
  ObstacleTracks_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ObstacleTracks_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ObstacleTracks_message_members,
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
get_message_type_support_handle<perception_msgs::msg::ObstacleTracks>()
{
  return &::perception_msgs::msg::rosidl_typesupport_introspection_cpp::ObstacleTracks_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, perception_msgs, msg, ObstacleTracks)() {
  return &::perception_msgs::msg::rosidl_typesupport_introspection_cpp::ObstacleTracks_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
