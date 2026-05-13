// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from perception_msgs:msg/TrafficSigns.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__TRAITS_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__TRAITS_HPP_

#include "perception_msgs/msg/detail/traffic_signs__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<perception_msgs::msg::TrafficSigns>()
{
  return "perception_msgs::msg::TrafficSigns";
}

template<>
inline const char * name<perception_msgs::msg::TrafficSigns>()
{
  return "perception_msgs/msg/TrafficSigns";
}

template<>
struct has_fixed_size<perception_msgs::msg::TrafficSigns>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<perception_msgs::msg::TrafficSigns>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<perception_msgs::msg::TrafficSigns>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__TRAITS_HPP_
