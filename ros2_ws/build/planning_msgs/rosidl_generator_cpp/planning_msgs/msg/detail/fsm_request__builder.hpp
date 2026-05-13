// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from planning_msgs:msg/FSMRequest.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__BUILDER_HPP_
#define PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__BUILDER_HPP_

#include "planning_msgs/msg/detail/fsm_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace planning_msgs
{

namespace msg
{

namespace builder
{

class Init_FSMRequest_valid_until_ms
{
public:
  explicit Init_FSMRequest_valid_until_ms(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  ::planning_msgs::msg::FSMRequest valid_until_ms(::planning_msgs::msg::FSMRequest::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_age_ms
{
public:
  explicit Init_FSMRequest_age_ms(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  Init_FSMRequest_valid_until_ms age_ms(::planning_msgs::msg::FSMRequest::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_FSMRequest_valid_until_ms(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_reason
{
public:
  explicit Init_FSMRequest_reason(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  Init_FSMRequest_age_ms reason(::planning_msgs::msg::FSMRequest::_reason_type arg)
  {
    msg_.reason = std::move(arg);
    return Init_FSMRequest_age_ms(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_waypoint_id
{
public:
  explicit Init_FSMRequest_waypoint_id(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  Init_FSMRequest_reason waypoint_id(::planning_msgs::msg::FSMRequest::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_FSMRequest_reason(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_requested_mode
{
public:
  explicit Init_FSMRequest_requested_mode(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  Init_FSMRequest_waypoint_id requested_mode(::planning_msgs::msg::FSMRequest::_requested_mode_type arg)
  {
    msg_.requested_mode = std::move(arg);
    return Init_FSMRequest_waypoint_id(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_request_type
{
public:
  explicit Init_FSMRequest_request_type(::planning_msgs::msg::FSMRequest & msg)
  : msg_(msg)
  {}
  Init_FSMRequest_requested_mode request_type(::planning_msgs::msg::FSMRequest::_request_type_type arg)
  {
    msg_.request_type = std::move(arg);
    return Init_FSMRequest_requested_mode(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

class Init_FSMRequest_header
{
public:
  Init_FSMRequest_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FSMRequest_request_type header(::planning_msgs::msg::FSMRequest::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_FSMRequest_request_type(msg_);
  }

private:
  ::planning_msgs::msg::FSMRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::planning_msgs::msg::FSMRequest>()
{
  return planning_msgs::msg::builder::Init_FSMRequest_header();
}

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__BUILDER_HPP_
