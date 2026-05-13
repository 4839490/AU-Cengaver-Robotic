// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from common_msgs:msg/AutonomyMode.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__BUILDER_HPP_
#define COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__BUILDER_HPP_

#include "common_msgs/msg/detail/autonomy_mode__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace common_msgs
{

namespace msg
{

namespace builder
{

class Init_AutonomyMode_mode
{
public:
  Init_AutonomyMode_mode()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::common_msgs::msg::AutonomyMode mode(::common_msgs::msg::AutonomyMode::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return std::move(msg_);
  }

private:
  ::common_msgs::msg::AutonomyMode msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::common_msgs::msg::AutonomyMode>()
{
  return common_msgs::msg::builder::Init_AutonomyMode_mode();
}

}  // namespace common_msgs

#endif  // COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__BUILDER_HPP_
