// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/TargetSpeed.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__BUILDER_HPP_

#include "planning_msgs/msg/detail/target_speed__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_TargetSpeed_warning_flags
{
public:
  explicit Init_TargetSpeed_warning_flags(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::TargetSpeed warning_flags(::planning_msgs::msg::TargetSpeed::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_age_ms
{
public:
  explicit Init_TargetSpeed_age_ms(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  Init_TargetSpeed_warning_flags age_ms(::planning_msgs::msg::TargetSpeed::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_TargetSpeed_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_valid_until_ms
{
public:
  explicit Init_TargetSpeed_valid_until_ms(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  Init_TargetSpeed_age_ms valid_until_ms(::planning_msgs::msg::TargetSpeed::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_TargetSpeed_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_reason
{
public:
  explicit Init_TargetSpeed_reason(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  Init_TargetSpeed_valid_until_ms reason(::planning_msgs::msg::TargetSpeed::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return Init_TargetSpeed_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_jerk_limit
{
public:
  explicit Init_TargetSpeed_jerk_limit(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  Init_TargetSpeed_reason jerk_limit(::planning_msgs::msg::TargetSpeed::_jerk_limit_type arg)
  {
    msg_.jerk_limit = std::move(arg);
    return Init_TargetSpeed_reason(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_speed
{
public:
  explicit Init_TargetSpeed_speed(::planning_msgs::msg::TargetSpeed & msg)
  : msg_(msg)
  {}
  Init_TargetSpeed_jerk_limit speed(::planning_msgs::msg::TargetSpeed::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_TargetSpeed_jerk_limit(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

class Init_TargetSpeed_header
{
public:
  Init_TargetSpeed_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TargetSpeed_speed header(::planning_msgs::msg::TargetSpeed::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TargetSpeed_speed(msg_);
  }

private:
  ::planning_msgs::msg::TargetSpeed msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::TargetSpeed>()
{
  return planning_msgs::msg::builder::Init_TargetSpeed_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__BUILDER_HPP_
