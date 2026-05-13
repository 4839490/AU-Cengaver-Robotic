// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__TRAITS_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__TRAITS_HPP_

#include "planning_msgs/msg/detail/trajectory_point__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<planning_msgs::msg::TrajectoryPoint>()
{
  return "planning_msgs::msg::TrajectoryPoint";
}

template<>
inline const char * name<planning_msgs::msg::TrajectoryPoint>()
{
  return "planning_msgs/msg/TrajectoryPoint";
}

template<>
struct has_fixed_size<planning_msgs::msg::TrajectoryPoint>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<planning_msgs::msg::TrajectoryPoint>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<planning_msgs::msg::TrajectoryPoint>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__TRAITS_HPP_
