// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_

#include "planning_msgs/msg/detail/trajectory_point__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_TrajectoryPoint_distance_from_start
{
public:
  explicit Init_TrajectoryPoint_distance_from_start(::planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::TrajectoryPoint distance_from_start(::planning_msgs::msg::TrajectoryPoint::_distance_from_start_type arg)
  {
    msg_.distance_from_start = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_curvature
{
public:
  explicit Init_TrajectoryPoint_curvature(::planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  Init_TrajectoryPoint_distance_from_start curvature(::planning_msgs::msg::TrajectoryPoint::_curvature_type arg)
  {
    msg_.curvature = std::move(arg);
    return Init_TrajectoryPoint_distance_from_start(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_speed
{
public:
  explicit Init_TrajectoryPoint_speed(::planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  Init_TrajectoryPoint_curvature speed(::planning_msgs::msg::TrajectoryPoint::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_TrajectoryPoint_curvature(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_yaw
{
public:
  explicit Init_TrajectoryPoint_yaw(::planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  Init_TrajectoryPoint_speed yaw(::planning_msgs::msg::TrajectoryPoint::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_TrajectoryPoint_speed(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_y
{
public:
  explicit Init_TrajectoryPoint_y(::planning_msgs::msg::TrajectoryPoint & msg)
  : msg_(msg)
  {}
  Init_TrajectoryPoint_yaw y(::planning_msgs::msg::TrajectoryPoint::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_TrajectoryPoint_yaw(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

class Init_TrajectoryPoint_x
{
public:
  Init_TrajectoryPoint_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrajectoryPoint_y x(::planning_msgs::msg::TrajectoryPoint::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_TrajectoryPoint_y(msg_);
  }

private:
  ::planning_msgs::msg::TrajectoryPoint msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::TrajectoryPoint>()
{
  return planning_msgs::msg::builder::Init_TrajectoryPoint_x();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__BUILDER_HPP_
