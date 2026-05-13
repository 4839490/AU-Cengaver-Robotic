// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__FSM_EVENT__BUILDER_HPP_
#define FSM_MSGS__MSG__DETAIL__FSM_EVENT__BUILDER_HPP_

#include "fsm_msgs/msg/detail/fsm_event__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace fsm_msgs
{

namespace msg
{

namespace builder
{

class Init_FSMEvent_age_ms
{
public:
  explicit Init_FSMEvent_age_ms(::fsm_msgs::msg::FSMEvent & msg)
  : msg_(msg)
  {}
  ::fsm_msgs::msg::FSMEvent age_ms(::fsm_msgs::msg::FSMEvent::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fsm_msgs::msg::FSMEvent msg_;
};

class Init_FSMEvent_data
{
public:
  explicit Init_FSMEvent_data(::fsm_msgs::msg::FSMEvent & msg)
  : msg_(msg)
  {}
  Init_FSMEvent_age_ms data(::fsm_msgs::msg::FSMEvent::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_FSMEvent_age_ms(msg_);
  }

private:
  ::fsm_msgs::msg::FSMEvent msg_;
};

class Init_FSMEvent_waypoint_id
{
public:
  explicit Init_FSMEvent_waypoint_id(::fsm_msgs::msg::FSMEvent & msg)
  : msg_(msg)
  {}
  Init_FSMEvent_data waypoint_id(::fsm_msgs::msg::FSMEvent::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_FSMEvent_data(msg_);
  }

private:
  ::fsm_msgs::msg::FSMEvent msg_;
};

class Init_FSMEvent_event_type
{
public:
  explicit Init_FSMEvent_event_type(::fsm_msgs::msg::FSMEvent & msg)
  : msg_(msg)
  {}
  Init_FSMEvent_waypoint_id event_type(::fsm_msgs::msg::FSMEvent::_event_type_type arg)
  {
    msg_.event_type = std::move(arg);
    return Init_FSMEvent_waypoint_id(msg_);
  }

private:
  ::fsm_msgs::msg::FSMEvent msg_;
};

class Init_FSMEvent_header
{
public:
  Init_FSMEvent_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FSMEvent_event_type header(::fsm_msgs::msg::FSMEvent::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_FSMEvent_event_type(msg_);
  }

private:
  ::fsm_msgs::msg::FSMEvent msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fsm_msgs::msg::FSMEvent>()
{
  return fsm_msgs::msg::builder::Init_FSMEvent_header();
}

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__FSM_EVENT__BUILDER_HPP_
