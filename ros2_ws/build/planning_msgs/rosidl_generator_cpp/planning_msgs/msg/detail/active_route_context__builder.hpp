// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__BUILDER_HPP_

#include "planning_msgs/msg/detail/active_route_context__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_ActiveRouteContext_warning_flags
{
public:
  explicit Init_ActiveRouteContext_warning_flags(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::ActiveRouteContext warning_flags(::planning_msgs::msg::ActiveRouteContext::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_valid_until_ms
{
public:
  explicit Init_ActiveRouteContext_valid_until_ms(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_warning_flags valid_until_ms(::planning_msgs::msg::ActiveRouteContext::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_ActiveRouteContext_warning_flags(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_age_ms
{
public:
  explicit Init_ActiveRouteContext_age_ms(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_valid_until_ms age_ms(::planning_msgs::msg::ActiveRouteContext::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_ActiveRouteContext_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_route_context_valid
{
public:
  explicit Init_ActiveRouteContext_route_context_valid(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_age_ms route_context_valid(::planning_msgs::msg::ActiveRouteContext::_route_context_valid_type arg)
  {
    msg_.route_context_valid = std::move(arg);
    return Init_ActiveRouteContext_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_ego_speed_mps
{
public:
  explicit Init_ActiveRouteContext_ego_speed_mps(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_route_context_valid ego_speed_mps(::planning_msgs::msg::ActiveRouteContext::_ego_speed_mps_type arg)
  {
    msg_.ego_speed_mps = std::move(arg);
    return Init_ActiveRouteContext_route_context_valid(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_localization_confidence
{
public:
  explicit Init_ActiveRouteContext_localization_confidence(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_ego_speed_mps localization_confidence(::planning_msgs::msg::ActiveRouteContext::_localization_confidence_type arg)
  {
    msg_.localization_confidence = std::move(arg);
    return Init_ActiveRouteContext_ego_speed_mps(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_distance_to_stop_zone
{
public:
  explicit Init_ActiveRouteContext_distance_to_stop_zone(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_localization_confidence distance_to_stop_zone(::planning_msgs::msg::ActiveRouteContext::_distance_to_stop_zone_type arg)
  {
    msg_.distance_to_stop_zone = std::move(arg);
    return Init_ActiveRouteContext_localization_confidence(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_in_stop_zone
{
public:
  explicit Init_ActiveRouteContext_in_stop_zone(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_distance_to_stop_zone in_stop_zone(::planning_msgs::msg::ActiveRouteContext::_in_stop_zone_type arg)
  {
    msg_.in_stop_zone = std::move(arg);
    return Init_ActiveRouteContext_distance_to_stop_zone(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_lookahead_distance
{
public:
  explicit Init_ActiveRouteContext_lookahead_distance(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_in_stop_zone lookahead_distance(::planning_msgs::msg::ActiveRouteContext::_lookahead_distance_type arg)
  {
    msg_.lookahead_distance = std::move(arg);
    return Init_ActiveRouteContext_in_stop_zone(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_planned_trajectory
{
public:
  explicit Init_ActiveRouteContext_planned_trajectory(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_lookahead_distance planned_trajectory(::planning_msgs::msg::ActiveRouteContext::_planned_trajectory_type arg)
  {
    msg_.planned_trajectory = std::move(arg);
    return Init_ActiveRouteContext_lookahead_distance(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_route_direction
{
public:
  explicit Init_ActiveRouteContext_route_direction(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_planned_trajectory route_direction(::planning_msgs::msg::ActiveRouteContext::_route_direction_type arg)
  {
    msg_.route_direction = std::move(arg);
    return Init_ActiveRouteContext_planned_trajectory(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_planner_mode
{
public:
  explicit Init_ActiveRouteContext_planner_mode(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_route_direction planner_mode(::planning_msgs::msg::ActiveRouteContext::_planner_mode_type arg)
  {
    msg_.planner_mode = std::move(arg);
    return Init_ActiveRouteContext_route_direction(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_target_heading
{
public:
  explicit Init_ActiveRouteContext_target_heading(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_planner_mode target_heading(::planning_msgs::msg::ActiveRouteContext::_target_heading_type arg)
  {
    msg_.target_heading = std::move(arg);
    return Init_ActiveRouteContext_planner_mode(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_target_y
{
public:
  explicit Init_ActiveRouteContext_target_y(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_target_heading target_y(::planning_msgs::msg::ActiveRouteContext::_target_y_type arg)
  {
    msg_.target_y = std::move(arg);
    return Init_ActiveRouteContext_target_heading(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_target_x
{
public:
  explicit Init_ActiveRouteContext_target_x(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_target_y target_x(::planning_msgs::msg::ActiveRouteContext::_target_x_type arg)
  {
    msg_.target_x = std::move(arg);
    return Init_ActiveRouteContext_target_y(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_active_waypoint_id
{
public:
  explicit Init_ActiveRouteContext_active_waypoint_id(::planning_msgs::msg::ActiveRouteContext & msg)
  : msg_(msg)
  {}
  Init_ActiveRouteContext_target_x active_waypoint_id(::planning_msgs::msg::ActiveRouteContext::_active_waypoint_id_type arg)
  {
    msg_.active_waypoint_id = std::move(arg);
    return Init_ActiveRouteContext_target_x(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

class Init_ActiveRouteContext_header
{
public:
  Init_ActiveRouteContext_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ActiveRouteContext_active_waypoint_id header(::planning_msgs::msg::ActiveRouteContext::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ActiveRouteContext_active_waypoint_id(msg_);
  }

private:
  ::planning_msgs::msg::ActiveRouteContext msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::ActiveRouteContext>()
{
  return planning_msgs::msg::builder::Init_ActiveRouteContext_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__BUILDER_HPP_
