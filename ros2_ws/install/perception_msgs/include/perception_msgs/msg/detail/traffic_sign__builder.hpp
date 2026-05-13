// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__BUILDER_HPP_

#include "perception_msgs/msg/detail/traffic_sign__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficSign_warning_flags
{
public:
  explicit Init_TrafficSign_warning_flags(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::TrafficSign warning_flags(::perception_msgs::msg::TrafficSign::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_source_sensor
{
public:
  explicit Init_TrafficSign_source_sensor(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_warning_flags source_sensor(::perception_msgs::msg::TrafficSign::_source_sensor_type arg)
  {
    msg_.source_sensor = std::move(arg);
    return Init_TrafficSign_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_event_memory_ttl_ms
{
public:
  explicit Init_TrafficSign_event_memory_ttl_ms(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_source_sensor event_memory_ttl_ms(::perception_msgs::msg::TrafficSign::_event_memory_ttl_ms_type arg)
  {
    msg_.event_memory_ttl_ms = std::move(arg);
    return Init_TrafficSign_source_sensor(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_valid_until_ms
{
public:
  explicit Init_TrafficSign_valid_until_ms(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_event_memory_ttl_ms valid_until_ms(::perception_msgs::msg::TrafficSign::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_TrafficSign_event_memory_ttl_ms(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_age_ms
{
public:
  explicit Init_TrafficSign_age_ms(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_valid_until_ms age_ms(::perception_msgs::msg::TrafficSign::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_TrafficSign_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_bbox_h
{
public:
  explicit Init_TrafficSign_bbox_h(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_age_ms bbox_h(::perception_msgs::msg::TrafficSign::_bbox_h_type arg)
  {
    msg_.bbox_h = std::move(arg);
    return Init_TrafficSign_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_bbox_w
{
public:
  explicit Init_TrafficSign_bbox_w(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_bbox_h bbox_w(::perception_msgs::msg::TrafficSign::_bbox_w_type arg)
  {
    msg_.bbox_w = std::move(arg);
    return Init_TrafficSign_bbox_h(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_bbox_y
{
public:
  explicit Init_TrafficSign_bbox_y(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_bbox_w bbox_y(::perception_msgs::msg::TrafficSign::_bbox_y_type arg)
  {
    msg_.bbox_y = std::move(arg);
    return Init_TrafficSign_bbox_w(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_bbox_x
{
public:
  explicit Init_TrafficSign_bbox_x(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_bbox_y bbox_x(::perception_msgs::msg::TrafficSign::_bbox_x_type arg)
  {
    msg_.bbox_x = std::move(arg);
    return Init_TrafficSign_bbox_y(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_confirmed
{
public:
  explicit Init_TrafficSign_confirmed(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_bbox_x confirmed(::perception_msgs::msg::TrafficSign::_confirmed_type arg)
  {
    msg_.confirmed = std::move(arg);
    return Init_TrafficSign_bbox_x(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_event_status
{
public:
  explicit Init_TrafficSign_event_status(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_confirmed event_status(::perception_msgs::msg::TrafficSign::_event_status_type arg)
  {
    msg_.event_status = std::move(arg);
    return Init_TrafficSign_confirmed(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_distance
{
public:
  explicit Init_TrafficSign_distance(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_event_status distance(::perception_msgs::msg::TrafficSign::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_TrafficSign_event_status(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_relevant_to_route
{
public:
  explicit Init_TrafficSign_relevant_to_route(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_distance relevant_to_route(::perception_msgs::msg::TrafficSign::_relevant_to_route_type arg)
  {
    msg_.relevant_to_route = std::move(arg);
    return Init_TrafficSign_distance(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_confidence
{
public:
  explicit Init_TrafficSign_confidence(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_relevant_to_route confidence(::perception_msgs::msg::TrafficSign::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_TrafficSign_relevant_to_route(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_type
{
public:
  explicit Init_TrafficSign_type(::perception_msgs::msg::TrafficSign & msg)
  : msg_(msg)
  {}
  Init_TrafficSign_confidence type(::perception_msgs::msg::TrafficSign::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_TrafficSign_confidence(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

class Init_TrafficSign_sign_id
{
public:
  Init_TrafficSign_sign_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficSign_type sign_id(::perception_msgs::msg::TrafficSign::_sign_id_type arg)
  {
    msg_.sign_id = std::move(arg);
    return Init_TrafficSign_type(msg_);
  }

private:
  ::perception_msgs::msg::TrafficSign msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::TrafficSign>()
{
  return perception_msgs::msg::builder::Init_TrafficSign_sign_id();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__BUILDER_HPP_
