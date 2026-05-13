// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/PerceptionDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__BUILDER_HPP_

#include "perception_msgs/msg/detail/perception_diagnostics__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_PerceptionDiagnostics_warning_flags
{
public:
  explicit Init_PerceptionDiagnostics_warning_flags(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::PerceptionDiagnostics warning_flags(::perception_msgs::msg::PerceptionDiagnostics::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_gpu_utilization
{
public:
  explicit Init_PerceptionDiagnostics_gpu_utilization(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_warning_flags gpu_utilization(::perception_msgs::msg::PerceptionDiagnostics::_gpu_utilization_type arg)
  {
    msg_.gpu_utilization = std::move(arg);
    return Init_PerceptionDiagnostics_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_num_outputs
{
public:
  explicit Init_PerceptionDiagnostics_num_outputs(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_gpu_utilization num_outputs(::perception_msgs::msg::PerceptionDiagnostics::_num_outputs_type arg)
  {
    msg_.num_outputs = std::move(arg);
    return Init_PerceptionDiagnostics_gpu_utilization(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_mean_confidence
{
public:
  explicit Init_PerceptionDiagnostics_mean_confidence(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_num_outputs mean_confidence(::perception_msgs::msg::PerceptionDiagnostics::_mean_confidence_type arg)
  {
    msg_.mean_confidence = std::move(arg);
    return Init_PerceptionDiagnostics_num_outputs(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_last_msg_age_ms
{
public:
  explicit Init_PerceptionDiagnostics_last_msg_age_ms(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_mean_confidence last_msg_age_ms(::perception_msgs::msg::PerceptionDiagnostics::_last_msg_age_ms_type arg)
  {
    msg_.last_msg_age_ms = std::move(arg);
    return Init_PerceptionDiagnostics_mean_confidence(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_latency_ms
{
public:
  explicit Init_PerceptionDiagnostics_latency_ms(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_last_msg_age_ms latency_ms(::perception_msgs::msg::PerceptionDiagnostics::_latency_ms_type arg)
  {
    msg_.latency_ms = std::move(arg);
    return Init_PerceptionDiagnostics_last_msg_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_output_hz
{
public:
  explicit Init_PerceptionDiagnostics_output_hz(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_latency_ms output_hz(::perception_msgs::msg::PerceptionDiagnostics::_output_hz_type arg)
  {
    msg_.output_hz = std::move(arg);
    return Init_PerceptionDiagnostics_latency_ms(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_input_hz
{
public:
  explicit Init_PerceptionDiagnostics_input_hz(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_output_hz input_hz(::perception_msgs::msg::PerceptionDiagnostics::_input_hz_type arg)
  {
    msg_.input_hz = std::move(arg);
    return Init_PerceptionDiagnostics_output_hz(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_node_name
{
public:
  explicit Init_PerceptionDiagnostics_node_name(::perception_msgs::msg::PerceptionDiagnostics & msg)
  : msg_(msg)
  {}
  Init_PerceptionDiagnostics_input_hz node_name(::perception_msgs::msg::PerceptionDiagnostics::_node_name_type arg)
  {
    msg_.node_name = std::move(arg);
    return Init_PerceptionDiagnostics_input_hz(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

class Init_PerceptionDiagnostics_header
{
public:
  Init_PerceptionDiagnostics_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PerceptionDiagnostics_node_name header(::perception_msgs::msg::PerceptionDiagnostics::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_PerceptionDiagnostics_node_name(msg_);
  }

private:
  ::perception_msgs::msg::PerceptionDiagnostics msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::PerceptionDiagnostics>()
{
  return perception_msgs::msg::builder::Init_PerceptionDiagnostics_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__BUILDER_HPP_
