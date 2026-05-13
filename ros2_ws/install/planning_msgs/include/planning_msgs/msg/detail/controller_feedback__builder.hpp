// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__BUILDER_HPP_

#include "planning_msgs/msg/detail/controller_feedback__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_ControllerFeedback_valid_until_ms
{
public:
  explicit Init_ControllerFeedback_valid_until_ms(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::ControllerFeedback valid_until_ms(::planning_msgs::msg::ControllerFeedback::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_age_ms
{
public:
  explicit Init_ControllerFeedback_age_ms(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_valid_until_ms age_ms(::planning_msgs::msg::ControllerFeedback::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_ControllerFeedback_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_full_brake_active
{
public:
  explicit Init_ControllerFeedback_full_brake_active(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_age_ms full_brake_active(::planning_msgs::msg::ControllerFeedback::_full_brake_active_type arg)
  {
    msg_.full_brake_active = std::move(arg);
    return Init_ControllerFeedback_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_brake_active
{
public:
  explicit Init_ControllerFeedback_brake_active(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_full_brake_active brake_active(::planning_msgs::msg::ControllerFeedback::_brake_active_type arg)
  {
    msg_.brake_active = std::move(arg);
    return Init_ControllerFeedback_full_brake_active(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_heading_error
{
public:
  explicit Init_ControllerFeedback_heading_error(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_brake_active heading_error(::planning_msgs::msg::ControllerFeedback::_heading_error_type arg)
  {
    msg_.heading_error = std::move(arg);
    return Init_ControllerFeedback_brake_active(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_cross_track_error
{
public:
  explicit Init_ControllerFeedback_cross_track_error(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_heading_error cross_track_error(::planning_msgs::msg::ControllerFeedback::_cross_track_error_type arg)
  {
    msg_.cross_track_error = std::move(arg);
    return Init_ControllerFeedback_heading_error(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_actual_steering_deg
{
public:
  explicit Init_ControllerFeedback_actual_steering_deg(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_cross_track_error actual_steering_deg(::planning_msgs::msg::ControllerFeedback::_actual_steering_deg_type arg)
  {
    msg_.actual_steering_deg = std::move(arg);
    return Init_ControllerFeedback_cross_track_error(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_actual_speed
{
public:
  explicit Init_ControllerFeedback_actual_speed(::planning_msgs::msg::ControllerFeedback & msg)
  : msg_(msg)
  {}
  Init_ControllerFeedback_actual_steering_deg actual_speed(::planning_msgs::msg::ControllerFeedback::_actual_speed_type arg)
  {
    msg_.actual_speed = std::move(arg);
    return Init_ControllerFeedback_actual_steering_deg(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

class Init_ControllerFeedback_header
{
public:
  Init_ControllerFeedback_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControllerFeedback_actual_speed header(::planning_msgs::msg::ControllerFeedback::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ControllerFeedback_actual_speed(msg_);
  }

private:
  ::planning_msgs::msg::ControllerFeedback msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::ControllerFeedback>()
{
  return planning_msgs::msg::builder::Init_ControllerFeedback_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__BUILDER_HPP_
