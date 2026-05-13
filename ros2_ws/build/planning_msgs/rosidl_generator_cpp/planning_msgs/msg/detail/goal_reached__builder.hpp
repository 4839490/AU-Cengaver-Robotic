// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/GoalReached.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__BUILDER_HPP_

#include "planning_msgs/msg/detail/goal_reached__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_GoalReached_warning_flags
{
public:
  explicit Init_GoalReached_warning_flags(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::GoalReached warning_flags(::planning_msgs::msg::GoalReached::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_valid_until_ms
{
public:
  explicit Init_GoalReached_valid_until_ms(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_warning_flags valid_until_ms(::planning_msgs::msg::GoalReached::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_GoalReached_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_age_ms
{
public:
  explicit Init_GoalReached_age_ms(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_valid_until_ms age_ms(::planning_msgs::msg::GoalReached::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_GoalReached_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_heading_error
{
public:
  explicit Init_GoalReached_heading_error(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_age_ms heading_error(::planning_msgs::msg::GoalReached::_heading_error_type arg)
  {
    msg_.heading_error = std::move(arg);
    return Init_GoalReached_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_distance_error
{
public:
  explicit Init_GoalReached_distance_error(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_heading_error distance_error(::planning_msgs::msg::GoalReached::_distance_error_type arg)
  {
    msg_.distance_error = std::move(arg);
    return Init_GoalReached_heading_error(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_success
{
public:
  explicit Init_GoalReached_success(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_distance_error success(::planning_msgs::msg::GoalReached::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_GoalReached_distance_error(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_waypoint_type
{
public:
  explicit Init_GoalReached_waypoint_type(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_success waypoint_type(::planning_msgs::msg::GoalReached::_waypoint_type_type arg)
  {
    msg_.waypoint_type = std::move(arg);
    return Init_GoalReached_success(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_waypoint_id
{
public:
  explicit Init_GoalReached_waypoint_id(::planning_msgs::msg::GoalReached & msg)
  : msg_(msg)
  {}
  Init_GoalReached_waypoint_type waypoint_id(::planning_msgs::msg::GoalReached::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_GoalReached_waypoint_type(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

class Init_GoalReached_header
{
public:
  Init_GoalReached_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GoalReached_waypoint_id header(::planning_msgs::msg::GoalReached::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_GoalReached_waypoint_id(msg_);
  }

private:
  ::planning_msgs::msg::GoalReached msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::GoalReached>()
{
  return planning_msgs::msg::builder::Init_GoalReached_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__BUILDER_HPP_
