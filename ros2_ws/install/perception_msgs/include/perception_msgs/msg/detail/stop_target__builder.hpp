// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/StopTarget.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__BUILDER_HPP_

#include "perception_msgs/msg/detail/stop_target__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_StopTarget_source_topic
{
public:
  explicit Init_StopTarget_source_topic(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::StopTarget source_topic(::perception_msgs::msg::StopTarget::_source_topic_type arg)
  {
    msg_.source_topic = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_stop_reason_id
{
public:
  explicit Init_StopTarget_stop_reason_id(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_source_topic stop_reason_id(::perception_msgs::msg::StopTarget::_stop_reason_id_type arg)
  {
    msg_.stop_reason_id = std::move(arg);
    return Init_StopTarget_source_topic(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_required_stop_duration_ms
{
public:
  explicit Init_StopTarget_required_stop_duration_ms(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_stop_reason_id required_stop_duration_ms(::perception_msgs::msg::StopTarget::_required_stop_duration_ms_type arg)
  {
    msg_.required_stop_duration_ms = std::move(arg);
    return Init_StopTarget_stop_reason_id(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_priority
{
public:
  explicit Init_StopTarget_priority(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_required_stop_duration_ms priority(::perception_msgs::msg::StopTarget::_priority_type arg)
  {
    msg_.priority = std::move(arg);
    return Init_StopTarget_required_stop_duration_ms(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_heading_at_stop
{
public:
  explicit Init_StopTarget_heading_at_stop(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_priority heading_at_stop(::perception_msgs::msg::StopTarget::_heading_at_stop_type arg)
  {
    msg_.heading_at_stop = std::move(arg);
    return Init_StopTarget_priority(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_waypoint_id
{
public:
  explicit Init_StopTarget_waypoint_id(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_heading_at_stop waypoint_id(::perception_msgs::msg::StopTarget::_waypoint_id_type arg)
  {
    msg_.waypoint_id = std::move(arg);
    return Init_StopTarget_heading_at_stop(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_valid_until_ms
{
public:
  explicit Init_StopTarget_valid_until_ms(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_waypoint_id valid_until_ms(::perception_msgs::msg::StopTarget::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_StopTarget_waypoint_id(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_age_ms
{
public:
  explicit Init_StopTarget_age_ms(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_valid_until_ms age_ms(::perception_msgs::msg::StopTarget::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_StopTarget_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_source
{
public:
  explicit Init_StopTarget_source(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_age_ms source(::perception_msgs::msg::StopTarget::_source_type arg)
  {
    msg_.source = std::move(arg);
    return Init_StopTarget_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_confidence
{
public:
  explicit Init_StopTarget_confidence(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_source confidence(::perception_msgs::msg::StopTarget::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_StopTarget_source(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_target_y
{
public:
  explicit Init_StopTarget_target_y(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_confidence target_y(::perception_msgs::msg::StopTarget::_target_y_type arg)
  {
    msg_.target_y = std::move(arg);
    return Init_StopTarget_confidence(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_target_x
{
public:
  explicit Init_StopTarget_target_x(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_target_y target_x(::perception_msgs::msg::StopTarget::_target_x_type arg)
  {
    msg_.target_x = std::move(arg);
    return Init_StopTarget_target_y(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_distance_from_front_bumper
{
public:
  explicit Init_StopTarget_distance_from_front_bumper(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_target_x distance_from_front_bumper(::perception_msgs::msg::StopTarget::_distance_from_front_bumper_type arg)
  {
    msg_.distance_from_front_bumper = std::move(arg);
    return Init_StopTarget_target_x(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_target_type
{
public:
  explicit Init_StopTarget_target_type(::perception_msgs::msg::StopTarget & msg)
  : msg_(msg)
  {}
  Init_StopTarget_distance_from_front_bumper target_type(::perception_msgs::msg::StopTarget::_target_type_type arg)
  {
    msg_.target_type = std::move(arg);
    return Init_StopTarget_distance_from_front_bumper(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

class Init_StopTarget_header
{
public:
  Init_StopTarget_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_StopTarget_target_type header(::perception_msgs::msg::StopTarget::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_StopTarget_target_type(msg_);
  }

private:
  ::perception_msgs::msg::StopTarget msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::StopTarget>()
{
  return perception_msgs::msg::builder::Init_StopTarget_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__BUILDER_HPP_
