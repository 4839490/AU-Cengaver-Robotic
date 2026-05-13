// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from localization_msgs:msg/LocalizationOdometry.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__TRAITS_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__TRAITS_HPP_

#include "localization_msgs/msg/detail/localization_odometry__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<localization_msgs::msg::LocalizationOdometry>()
{
  return "localization_msgs::msg::LocalizationOdometry";
}

template<>
inline const char * name<localization_msgs::msg::LocalizationOdometry>()
{
  return "localization_msgs/msg/LocalizationOdometry";
}

template<>
struct has_fixed_size<localization_msgs::msg::LocalizationOdometry>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<localization_msgs::msg::LocalizationOdometry>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<localization_msgs::msg::LocalizationOdometry>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__TRAITS_HPP_
