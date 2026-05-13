// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__MISSION_STATE__TRAITS_HPP_
#define FSM_MSGS__MSG__DETAIL__MISSION_STATE__TRAITS_HPP_

#include "fsm_msgs/msg/detail/mission_state__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fsm_msgs::msg::MissionState>()
{
  return "fsm_msgs::msg::MissionState";
}

template<>
inline const char * name<fsm_msgs::msg::MissionState>()
{
  return "fsm_msgs/msg/MissionState";
}

template<>
struct has_fixed_size<fsm_msgs::msg::MissionState>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<fsm_msgs::msg::MissionState>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<fsm_msgs::msg::MissionState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FSM_MSGS__MSG__DETAIL__MISSION_STATE__TRAITS_HPP_
