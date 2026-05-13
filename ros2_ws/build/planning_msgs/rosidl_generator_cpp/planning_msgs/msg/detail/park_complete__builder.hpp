// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/ParkComplete.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__BUILDER_HPP_

#include "planning_msgs/msg/detail/park_complete__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_ParkComplete_warning_flags
{
public:
  explicit Init_ParkComplete_warning_flags(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::ParkComplete warning_flags(::planning_msgs::msg::ParkComplete::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_valid_until_ms
{
public:
  explicit Init_ParkComplete_valid_until_ms(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_warning_flags valid_until_ms(::planning_msgs::msg::ParkComplete::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_ParkComplete_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_age_ms
{
public:
  explicit Init_ParkComplete_age_ms(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_valid_until_ms age_ms(::planning_msgs::msg::ParkComplete::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_ParkComplete_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_waypoint_id
{
public:
  explicit Init_ParkComplete_waypoint_id(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_age_ms waypoint_id(::planning_msgs::msg::ParkComplete::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_ParkComplete_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_iterations_used
{
public:
  explicit Init_ParkComplete_iterations_used(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_waypoint_id iterations_used(::planning_msgs::msg::ParkComplete::_iterations_used_type arg)
  {
    msg_.iterations_used = std::move(arg);
    return Init_ParkComplete_waypoint_id(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_final_heading_error
{
public:
  explicit Init_ParkComplete_final_heading_error(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_iterations_used final_heading_error(::planning_msgs::msg::ParkComplete::_final_heading_error_type arg)
  {
    msg_.final_heading_error = std::move(arg);
    return Init_ParkComplete_iterations_used(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_final_cross_track_error
{
public:
  explicit Init_ParkComplete_final_cross_track_error(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_final_heading_error final_cross_track_error(::planning_msgs::msg::ParkComplete::_final_cross_track_error_type arg)
  {
    msg_.final_cross_track_error = std::move(arg);
    return Init_ParkComplete_final_heading_error(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_success
{
public:
  explicit Init_ParkComplete_success(::planning_msgs::msg::ParkComplete & msg)
  : msg_(msg)
  {}
  Init_ParkComplete_final_cross_track_error success(::planning_msgs::msg::ParkComplete::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_ParkComplete_final_cross_track_error(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

class Init_ParkComplete_header
{
public:
  Init_ParkComplete_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ParkComplete_success header(::planning_msgs::msg::ParkComplete::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ParkComplete_success(msg_);
  }

private:
  ::planning_msgs::msg::ParkComplete msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::ParkComplete>()
{
  return planning_msgs::msg::builder::Init_ParkComplete_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__BUILDER_HPP_
