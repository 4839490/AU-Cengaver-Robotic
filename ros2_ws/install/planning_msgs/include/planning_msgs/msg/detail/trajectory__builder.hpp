// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/Trajectory.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__BUILDER_HPP_

#include "planning_msgs/msg/detail/trajectory__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_Trajectory_warning_flags
{
public:
  explicit Init_Trajectory_warning_flags(::planning_msgs::msg::Trajectory & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::Trajectory warning_flags(::planning_msgs::msg::Trajectory::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

class Init_Trajectory_age_ms
{
public:
  explicit Init_Trajectory_age_ms(::planning_msgs::msg::Trajectory & msg)
  : msg_(msg)
  {}
  Init_Trajectory_warning_flags age_ms(::planning_msgs::msg::Trajectory::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_Trajectory_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

class Init_Trajectory_valid_until_ms
{
public:
  explicit Init_Trajectory_valid_until_ms(::planning_msgs::msg::Trajectory & msg)
  : msg_(msg)
  {}
  Init_Trajectory_age_ms valid_until_ms(::planning_msgs::msg::Trajectory::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_Trajectory_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

class Init_Trajectory_planner_mode
{
public:
  explicit Init_Trajectory_planner_mode(::planning_msgs::msg::Trajectory & msg)
  : msg_(msg)
  {}
  Init_Trajectory_valid_until_ms planner_mode(::planning_msgs::msg::Trajectory::_planner_mode_type arg)
  {
    msg_.planner_mode = std::move(arg);
    return Init_Trajectory_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

class Init_Trajectory_points
{
public:
  explicit Init_Trajectory_points(::planning_msgs::msg::Trajectory & msg)
  : msg_(msg)
  {}
  Init_Trajectory_planner_mode points(::planning_msgs::msg::Trajectory::_points_type arg)
  {
    msg_.points = std::move(arg);
    return Init_Trajectory_planner_mode(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

class Init_Trajectory_header
{
public:
  Init_Trajectory_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Trajectory_points header(::planning_msgs::msg::Trajectory::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Trajectory_points(msg_);
  }

private:
  ::planning_msgs::msg::Trajectory msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::Trajectory>()
{
  return planning_msgs::msg::builder::Init_Trajectory_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__BUILDER_HPP_
