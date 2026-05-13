// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_

#include "perception_msgs/msg/detail/traffic_light_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_TrafficLightState_warning_flags
{
public:
  explicit Init_TrafficLightState_warning_flags(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::TrafficLightState warning_flags(::perception_msgs::msg::TrafficLightState::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_source_sensor
{
public:
  explicit Init_TrafficLightState_source_sensor(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_warning_flags source_sensor(::perception_msgs::msg::TrafficLightState::_source_sensor_type arg)
  {
    msg_.source_sensor = std::move(arg);
    return Init_TrafficLightState_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_valid_until_ms
{
public:
  explicit Init_TrafficLightState_valid_until_ms(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_source_sensor valid_until_ms(::perception_msgs::msg::TrafficLightState::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_TrafficLightState_source_sensor(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_age_ms
{
public:
  explicit Init_TrafficLightState_age_ms(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_valid_until_ms age_ms(::perception_msgs::msg::TrafficLightState::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_TrafficLightState_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_bbox_h
{
public:
  explicit Init_TrafficLightState_bbox_h(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_age_ms bbox_h(::perception_msgs::msg::TrafficLightState::_bbox_h_type arg)
  {
    msg_.bbox_h = std::move(arg);
    return Init_TrafficLightState_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_bbox_w
{
public:
  explicit Init_TrafficLightState_bbox_w(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_bbox_h bbox_w(::perception_msgs::msg::TrafficLightState::_bbox_w_type arg)
  {
    msg_.bbox_w = std::move(arg);
    return Init_TrafficLightState_bbox_h(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_bbox_y
{
public:
  explicit Init_TrafficLightState_bbox_y(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_bbox_w bbox_y(::perception_msgs::msg::TrafficLightState::_bbox_y_type arg)
  {
    msg_.bbox_y = std::move(arg);
    return Init_TrafficLightState_bbox_w(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_bbox_x
{
public:
  explicit Init_TrafficLightState_bbox_x(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_bbox_y bbox_x(::perception_msgs::msg::TrafficLightState::_bbox_x_type arg)
  {
    msg_.bbox_x = std::move(arg);
    return Init_TrafficLightState_bbox_y(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_in_stop_zone
{
public:
  explicit Init_TrafficLightState_in_stop_zone(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_bbox_x in_stop_zone(::perception_msgs::msg::TrafficLightState::_in_stop_zone_type arg)
  {
    msg_.in_stop_zone = std::move(arg);
    return Init_TrafficLightState_bbox_x(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_confirmed
{
public:
  explicit Init_TrafficLightState_confirmed(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_in_stop_zone confirmed(::perception_msgs::msg::TrafficLightState::_confirmed_type arg)
  {
    msg_.confirmed = std::move(arg);
    return Init_TrafficLightState_in_stop_zone(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_distance_to_stop
{
public:
  explicit Init_TrafficLightState_distance_to_stop(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_confirmed distance_to_stop(::perception_msgs::msg::TrafficLightState::_distance_to_stop_type arg)
  {
    msg_.distance_to_stop = std::move(arg);
    return Init_TrafficLightState_confirmed(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_relevant_to_route
{
public:
  explicit Init_TrafficLightState_relevant_to_route(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_distance_to_stop relevant_to_route(::perception_msgs::msg::TrafficLightState::_relevant_to_route_type arg)
  {
    msg_.relevant_to_route = std::move(arg);
    return Init_TrafficLightState_distance_to_stop(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_confidence
{
public:
  explicit Init_TrafficLightState_confidence(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_relevant_to_route confidence(::perception_msgs::msg::TrafficLightState::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_TrafficLightState_relevant_to_route(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_state
{
public:
  explicit Init_TrafficLightState_state(::perception_msgs::msg::TrafficLightState & msg)
  : msg_(msg)
  {}
  Init_TrafficLightState_confidence state(::perception_msgs::msg::TrafficLightState::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_TrafficLightState_confidence(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

class Init_TrafficLightState_header
{
public:
  Init_TrafficLightState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_TrafficLightState_state header(::perception_msgs::msg::TrafficLightState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_TrafficLightState_state(msg_);
  }

private:
  ::perception_msgs::msg::TrafficLightState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::TrafficLightState>()
{
  return perception_msgs::msg::builder::Init_TrafficLightState_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__BUILDER_HPP_
