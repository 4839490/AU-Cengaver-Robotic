// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from localization_msgs:msg/LocalizationDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__BUILDER_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__BUILDER_HPP_

#include "localization_msgs/msg/detail/localization_diagnostics__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace localization_msgs
{

namespace msg
{

namespace builder
{

class Init_LocalizationDiagnostics_warning_flags
{
public:
  explicit Init_LocalizationDiagnostics_warning_flags(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  ::localization_msgs::msg::LocalizationDiagnostics warning_flags(::localization_msgs::msg::LocalizationDiagnostics::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_map_odom_stable
{
public:
  explicit Init_LocalizationDiagnostics_map_odom_stable(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_warning_flags map_odom_stable(::localization_msgs::msg::LocalizationDiagnostics::_map_odom_stable_type arg)
  {
    msg_.map_odom_stable = std::move(arg);
    return Init_LocalizationDiagnostics_warning_flags(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ndt_healthy
{
public:
  explicit Init_LocalizationDiagnostics_ndt_healthy(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_map_odom_stable ndt_healthy(::localization_msgs::msg::LocalizationDiagnostics::_ndt_healthy_type arg)
  {
    msg_.ndt_healthy = std::move(arg);
    return Init_LocalizationDiagnostics_map_odom_stable(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_imu_healthy
{
public:
  explicit Init_LocalizationDiagnostics_imu_healthy(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ndt_healthy imu_healthy(::localization_msgs::msg::LocalizationDiagnostics::_imu_healthy_type arg)
  {
    msg_.imu_healthy = std::move(arg);
    return Init_LocalizationDiagnostics_ndt_healthy(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_gps_healthy
{
public:
  explicit Init_LocalizationDiagnostics_gps_healthy(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_imu_healthy gps_healthy(::localization_msgs::msg::LocalizationDiagnostics::_gps_healthy_type arg)
  {
    msg_.gps_healthy = std::move(arg);
    return Init_LocalizationDiagnostics_imu_healthy(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ekf_healthy
{
public:
  explicit Init_LocalizationDiagnostics_ekf_healthy(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_gps_healthy ekf_healthy(::localization_msgs::msg::LocalizationDiagnostics::_ekf_healthy_type arg)
  {
    msg_.ekf_healthy = std::move(arg);
    return Init_LocalizationDiagnostics_gps_healthy(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ndt_quality
{
public:
  explicit Init_LocalizationDiagnostics_ndt_quality(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ekf_healthy ndt_quality(::localization_msgs::msg::LocalizationDiagnostics::_ndt_quality_type arg)
  {
    msg_.ndt_quality = std::move(arg);
    return Init_LocalizationDiagnostics_ekf_healthy(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_heading_covariance
{
public:
  explicit Init_LocalizationDiagnostics_heading_covariance(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ndt_quality heading_covariance(::localization_msgs::msg::LocalizationDiagnostics::_heading_covariance_type arg)
  {
    msg_.heading_covariance = std::move(arg);
    return Init_LocalizationDiagnostics_ndt_quality(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_position_covariance
{
public:
  explicit Init_LocalizationDiagnostics_position_covariance(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_heading_covariance position_covariance(::localization_msgs::msg::LocalizationDiagnostics::_position_covariance_type arg)
  {
    msg_.position_covariance = std::move(arg);
    return Init_LocalizationDiagnostics_heading_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ndt_latency_ms
{
public:
  explicit Init_LocalizationDiagnostics_ndt_latency_ms(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_position_covariance ndt_latency_ms(::localization_msgs::msg::LocalizationDiagnostics::_ndt_latency_ms_type arg)
  {
    msg_.ndt_latency_ms = std::move(arg);
    return Init_LocalizationDiagnostics_position_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ekf_latency_ms
{
public:
  explicit Init_LocalizationDiagnostics_ekf_latency_ms(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ndt_latency_ms ekf_latency_ms(::localization_msgs::msg::LocalizationDiagnostics::_ekf_latency_ms_type arg)
  {
    msg_.ekf_latency_ms = std::move(arg);
    return Init_LocalizationDiagnostics_ndt_latency_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ndt_output_hz
{
public:
  explicit Init_LocalizationDiagnostics_ndt_output_hz(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ekf_latency_ms ndt_output_hz(::localization_msgs::msg::LocalizationDiagnostics::_ndt_output_hz_type arg)
  {
    msg_.ndt_output_hz = std::move(arg);
    return Init_LocalizationDiagnostics_ekf_latency_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_imu_input_hz
{
public:
  explicit Init_LocalizationDiagnostics_imu_input_hz(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ndt_output_hz imu_input_hz(::localization_msgs::msg::LocalizationDiagnostics::_imu_input_hz_type arg)
  {
    msg_.imu_input_hz = std::move(arg);
    return Init_LocalizationDiagnostics_ndt_output_hz(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_gps_input_hz
{
public:
  explicit Init_LocalizationDiagnostics_gps_input_hz(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_imu_input_hz gps_input_hz(::localization_msgs::msg::LocalizationDiagnostics::_gps_input_hz_type arg)
  {
    msg_.gps_input_hz = std::move(arg);
    return Init_LocalizationDiagnostics_imu_input_hz(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_ekf_output_hz
{
public:
  explicit Init_LocalizationDiagnostics_ekf_output_hz(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_gps_input_hz ekf_output_hz(::localization_msgs::msg::LocalizationDiagnostics::_ekf_output_hz_type arg)
  {
    msg_.ekf_output_hz = std::move(arg);
    return Init_LocalizationDiagnostics_gps_input_hz(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_valid_until_ms
{
public:
  explicit Init_LocalizationDiagnostics_valid_until_ms(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_ekf_output_hz valid_until_ms(::localization_msgs::msg::LocalizationDiagnostics::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_LocalizationDiagnostics_ekf_output_hz(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_age_ms
{
public:
  explicit Init_LocalizationDiagnostics_age_ms(::localization_msgs::msg::LocalizationDiagnostics & msg)
  : msg_(msg)
  {}
  Init_LocalizationDiagnostics_valid_until_ms age_ms(::localization_msgs::msg::LocalizationDiagnostics::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_LocalizationDiagnostics_valid_until_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

class Init_LocalizationDiagnostics_header
{
public:
  Init_LocalizationDiagnostics_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LocalizationDiagnostics_age_ms header(::localization_msgs::msg::LocalizationDiagnostics::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LocalizationDiagnostics_age_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationDiagnostics msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::localization_msgs::msg::LocalizationDiagnostics>()
{
  return localization_msgs::msg::builder::Init_LocalizationDiagnostics_header();
}

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__BUILDER_HPP_
