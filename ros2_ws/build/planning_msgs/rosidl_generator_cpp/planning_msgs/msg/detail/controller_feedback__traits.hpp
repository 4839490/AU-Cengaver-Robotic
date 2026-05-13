// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__TRAITS_HPP_
#define PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__TRAITS_HPP_

#include "planning_msgs/msg/detail/controller_feedback__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<planning_msgs::msg::ControllerFeedback>()
{
  return "planning_msgs::msg::ControllerFeedback";
}

template<>
inline const char * name<planning_msgs::msg::ControllerFeedback>()
{
  return "planning_msgs/msg/ControllerFeedback";
}

template<>
struct has_fixed_size<planning_msgs::msg::ControllerFeedback>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<planning_msgs::msg::ControllerFeedback>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<planning_msgs::msg::ControllerFeedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__TRAITS_HPP_
