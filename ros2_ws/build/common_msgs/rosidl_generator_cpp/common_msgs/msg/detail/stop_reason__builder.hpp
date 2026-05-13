// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_
#define COMMON_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_

#include "common_msgs/msg/detail/stop_reason__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace common_msgs
{

namespace msg
{

namespace builder
{

class Init_StopReason_reason
{
public:
  Init_StopReason_reason()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::common_msgs::msg::StopReason reason(::common_msgs::msg::StopReason::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return std::move(msg_);
  }

private:
  ::common_msgs::msg::StopReason msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::common_msgs::msg::StopReason>()
{
  return common_msgs::msg::builder::Init_StopReason_reason();
}

}  // namespace common_msgs

#endif  // COMMON_MSGS__MSG__DETAIL__STOP_REASON__BUILDER_HPP_
