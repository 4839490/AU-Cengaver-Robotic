// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/TrafficSigns.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__BUILDER_HPP_

#include "perception_msgs/msg/detail/traffic_signs__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficSigns_signs
{
public:
  explicit Init_TrafficSigns_signs(::perception_msgs::msg::TrafficSigns & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::TrafficSigns signs(::perception_msgs::msg::TrafficSigns::_signs_type arg)
  {
    msg_.signs = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSigns msg_;
};

class Init_TrafficSigns_header
{
public:
  Init_TrafficSigns_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficSigns_signs header(::perception_msgs::msg::TrafficSigns::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TrafficSigns_signs(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSigns msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::TrafficSigns>()
{
  return perception_msgs::msg::builder::Init_TrafficSigns_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__BUILDER_HPP_
