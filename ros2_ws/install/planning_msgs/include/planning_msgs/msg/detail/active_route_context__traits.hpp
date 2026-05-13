// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__TRAITS_HPP_
#define PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__TRAITS_HPP_

#include "planning_msgs/msg/detail/active_route_context__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<planning_msgs::msg::ActiveRouteContext>()
{
  return "planning_msgs::msg::ActiveRouteContext";
}

template<>
inline const char * name<planning_msgs::msg::ActiveRouteContext>()
{
  return "planning_msgs/msg/ActiveRouteContext";
}

template<>
struct has_fixed_size<planning_msgs::msg::ActiveRouteContext>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<planning_msgs::msg::ActiveRouteContext>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<planning_msgs::msg::ActiveRouteContext>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__TRAITS_HPP_
