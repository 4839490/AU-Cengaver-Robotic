// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__FSM_EVENT__TRAITS_HPP_
#define FSM_MSGS__MSG__DETAIL__FSM_EVENT__TRAITS_HPP_

#include "fsm_msgs/msg/detail/fsm_event__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<fsm_msgs::msg::FSMEvent>()
{
  return "fsm_msgs::msg::FSMEvent";
}

template<>
inline const char * name<fsm_msgs::msg::FSMEvent>()
{
  return "fsm_msgs/msg/FSMEvent";
}

template<>
struct has_fixed_size<fsm_msgs::msg::FSMEvent>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<fsm_msgs::msg::FSMEvent>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<fsm_msgs::msg::FSMEvent>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // FSM_MSGS__MSG__DETAIL__FSM_EVENT__TRAITS_HPP_
