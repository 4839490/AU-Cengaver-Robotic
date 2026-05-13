// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fsm_msgs:msg/CurrentMode.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__CURRENT_MODE__BUILDER_HPP_
#define FSM_MSGS__MSG__DETAIL__CURRENT_MODE__BUILDER_HPP_

#include "fsm_msgs/msg/detail/current_mode__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace fsm_msgs
{

namespace msg
{

namespace builder
{

class Init_CurrentMode_warning_flags
{
public:
  explicit Init_CurrentMode_warning_flags(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  ::fsm_msgs::msg::CurrentMode warning_flags(::fsm_msgs::msg::CurrentMode::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_valid_until_ms
{
public:
  explicit Init_CurrentMode_valid_until_ms(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_warning_flags valid_until_ms(::fsm_msgs::msg::CurrentMode::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_CurrentMode_warning_flags(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_age_ms
{
public:
  explicit Init_CurrentMode_age_ms(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_valid_until_ms age_ms(::fsm_msgs::msg::CurrentMode::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_CurrentMode_valid_until_ms(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_waypoint_id
{
public:
  explicit Init_CurrentMode_waypoint_id(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_age_ms waypoint_id(::fsm_msgs::msg::CurrentMode::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_CurrentMode_age_ms(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_stop_reason
{
public:
  explicit Init_CurrentMode_stop_reason(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_waypoint_id stop_reason(::fsm_msgs::msg::CurrentMode::_stop_reason_type arg)
  {
    msg_.stop_reason = std::move(arg);
    return Init_CurrentMode_waypoint_id(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_reason
{
public:
  explicit Init_CurrentMode_reason(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_stop_reason reason(::fsm_msgs::msg::CurrentMode::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return Init_CurrentMode_stop_reason(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_previous_mode
{
public:
  explicit Init_CurrentMode_previous_mode(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_reason previous_mode(::fsm_msgs::msg::CurrentMode::_previous_mode_type arg)
  {
    msg_.previous_mode = std::move(arg);
    return Init_CurrentMode_reason(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_mode
{
public:
  explicit Init_CurrentMode_mode(::fsm_msgs::msg::CurrentMode & msg)
  : msg_(msg)
  {}
  Init_CurrentMode_previous_mode mode(::fsm_msgs::msg::CurrentMode::_mode_type arg)
  {
    msg_.mode = std::move(arg);
    return Init_CurrentMode_previous_mode(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

class Init_CurrentMode_header
{
public:
  Init_CurrentMode_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CurrentMode_mode header(::fsm_msgs::msg::CurrentMode::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_CurrentMode_mode(msg_);
  }

private:
  ::fsm_msgs::msg::CurrentMode msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fsm_msgs::msg::CurrentMode>()
{
  return fsm_msgs::msg::builder::Init_CurrentMode_header();
}

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__CURRENT_MODE__BUILDER_HPP_
