// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__BUILDER_HPP_

#include "planning_msgs/msg/detail/planning_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_PlanningStatus_warning_flags
{
public:
  explicit Init_PlanningStatus_warning_flags(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::PlanningStatus warning_flags(::planning_msgs::msg::PlanningStatus::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_valid_until_ms
{
public:
  explicit Init_PlanningStatus_valid_until_ms(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_warning_flags valid_until_ms(::planning_msgs::msg::PlanningStatus::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_PlanningStatus_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_age_ms
{
public:
  explicit Init_PlanningStatus_age_ms(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_valid_until_ms age_ms(::planning_msgs::msg::PlanningStatus::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_PlanningStatus_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_planner_mode
{
public:
  explicit Init_PlanningStatus_planner_mode(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_age_ms planner_mode(::planning_msgs::msg::PlanningStatus::_planner_mode_type arg)
  {
    msg_.planner_mode = std::move(arg);
    return Init_PlanningStatus_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_distance_to_goal
{
public:
  explicit Init_PlanningStatus_distance_to_goal(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_planner_mode distance_to_goal(::planning_msgs::msg::PlanningStatus::_distance_to_goal_type arg)
  {
    msg_.distance_to_goal = std::move(arg);
    return Init_PlanningStatus_planner_mode(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_active_waypoint_id
{
public:
  explicit Init_PlanningStatus_active_waypoint_id(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_distance_to_goal active_waypoint_id(::planning_msgs::msg::PlanningStatus::_active_waypoint_id_type arg)
  {
    msg_.active_waypoint_id = std::move(arg);
    return Init_PlanningStatus_distance_to_goal(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_localization_degraded
{
public:
  explicit Init_PlanningStatus_localization_degraded(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_active_waypoint_id localization_degraded(::planning_msgs::msg::PlanningStatus::_localization_degraded_type arg)
  {
    msg_.localization_degraded = std::move(arg);
    return Init_PlanningStatus_active_waypoint_id(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_lane_lost
{
public:
  explicit Init_PlanningStatus_lane_lost(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_localization_degraded lane_lost(::planning_msgs::msg::PlanningStatus::_lane_lost_type arg)
  {
    msg_.lane_lost = std::move(arg);
    return Init_PlanningStatus_localization_degraded(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_obstacle_blocking
{
public:
  explicit Init_PlanningStatus_obstacle_blocking(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_lane_lost obstacle_blocking(::planning_msgs::msg::PlanningStatus::_obstacle_blocking_type arg)
  {
    msg_.obstacle_blocking = std::move(arg);
    return Init_PlanningStatus_lane_lost(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_parking_entry_reached
{
public:
  explicit Init_PlanningStatus_parking_entry_reached(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_obstacle_blocking parking_entry_reached(::planning_msgs::msg::PlanningStatus::_parking_entry_reached_type arg)
  {
    msg_.parking_entry_reached = std::move(arg);
    return Init_PlanningStatus_obstacle_blocking(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_goal_reached
{
public:
  explicit Init_PlanningStatus_goal_reached(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_parking_entry_reached goal_reached(::planning_msgs::msg::PlanningStatus::_goal_reached_type arg)
  {
    msg_.goal_reached = std::move(arg);
    return Init_PlanningStatus_parking_entry_reached(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_trajectory_valid
{
public:
  explicit Init_PlanningStatus_trajectory_valid(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_goal_reached trajectory_valid(::planning_msgs::msg::PlanningStatus::_trajectory_valid_type arg)
  {
    msg_.trajectory_valid = std::move(arg);
    return Init_PlanningStatus_goal_reached(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_status
{
public:
  explicit Init_PlanningStatus_status(::planning_msgs::msg::PlanningStatus & msg)
  : msg_(msg)
  {}
  Init_PlanningStatus_trajectory_valid status(::planning_msgs::msg::PlanningStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_PlanningStatus_trajectory_valid(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

class Init_PlanningStatus_header
{
public:
  Init_PlanningStatus_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PlanningStatus_status header(::planning_msgs::msg::PlanningStatus::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_PlanningStatus_status(msg_);
  }

private:
  ::planning_msgs::msg::PlanningStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::PlanningStatus>()
{
  return planning_msgs::msg::builder::Init_PlanningStatus_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__BUILDER_HPP_
