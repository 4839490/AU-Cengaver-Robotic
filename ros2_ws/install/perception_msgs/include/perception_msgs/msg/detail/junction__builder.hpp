// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/Junction.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__BUILDER_HPP_

#include "perception_msgs/msg/detail/junction__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_Junction_warning_flags
{
public:
  explicit Init_Junction_warning_flags(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::Junction warning_flags(::perception_msgs::msg::Junction::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_source_sensor
{
public:
  explicit Init_Junction_source_sensor(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_warning_flags source_sensor(::perception_msgs::msg::Junction::_source_sensor_type arg)
  {
    msg_.source_sensor = std::move(arg);
    return Init_Junction_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_valid_until_ms
{
public:
  explicit Init_Junction_valid_until_ms(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_source_sensor valid_until_ms(::perception_msgs::msg::Junction::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_Junction_source_sensor(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_age_ms
{
public:
  explicit Init_Junction_age_ms(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_valid_until_ms age_ms(::perception_msgs::msg::Junction::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_Junction_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_confidence
{
public:
  explicit Init_Junction_confidence(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_age_ms confidence(::perception_msgs::msg::Junction::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_Junction_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_distance_to_entry
{
public:
  explicit Init_Junction_distance_to_entry(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_confidence distance_to_entry(::perception_msgs::msg::Junction::_distance_to_entry_type arg)
  {
    msg_.distance_to_entry = std::move(arg);
    return Init_Junction_confidence(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_arm_count
{
public:
  explicit Init_Junction_arm_count(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_distance_to_entry arm_count(::perception_msgs::msg::Junction::_arm_count_type arg)
  {
    msg_.arm_count = std::move(arg);
    return Init_Junction_distance_to_entry(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_junction_type
{
public:
  explicit Init_Junction_junction_type(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_arm_count junction_type(::perception_msgs::msg::Junction::_junction_type_type arg)
  {
    msg_.junction_type = std::move(arg);
    return Init_Junction_arm_count(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_detected
{
public:
  explicit Init_Junction_detected(::perception_msgs::msg::Junction & msg)
  : msg_(msg)
  {}
  Init_Junction_junction_type detected(::perception_msgs::msg::Junction::_detected_type arg)
  {
    msg_.detected = std::move(arg);
    return Init_Junction_junction_type(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

class Init_Junction_header
{
public:
  Init_Junction_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Junction_detected header(::perception_msgs::msg::Junction::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Junction_detected(msg_);
  }

private:
  ::perception_msgs::msg::Junction msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::Junction>()
{
  return perception_msgs::msg::builder::Init_Junction_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__BUILDER_HPP_
