// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__BUILDER_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__BUILDER_HPP_

#include "localization_msgs/msg/detail/localization_status__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace localization_msgs
{

namespace msg
{

namespace builder
{

class Init_LocalizationStatus_warning_flags
{
public:
  explicit Init_LocalizationStatus_warning_flags(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  ::localization_msgs::msg::LocalizationStatus warning_flags(::localization_msgs::msg::LocalizationStatus::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_lidar_available
{
public:
  explicit Init_LocalizationStatus_lidar_available(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_warning_flags lidar_available(::localization_msgs::msg::LocalizationStatus::_lidar_available_type arg)
  {
    msg_.lidar_available = std::move(arg);
    return Init_LocalizationStatus_warning_flags(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_imu_available
{
public:
  explicit Init_LocalizationStatus_imu_available(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_lidar_available imu_available(::localization_msgs::msg::LocalizationStatus::_imu_available_type arg)
  {
    msg_.imu_available = std::move(arg);
    return Init_LocalizationStatus_lidar_available(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_gps_available
{
public:
  explicit Init_LocalizationStatus_gps_available(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_imu_available gps_available(::localization_msgs::msg::LocalizationStatus::_gps_available_type arg)
  {
    msg_.gps_available = std::move(arg);
    return Init_LocalizationStatus_imu_available(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_map_odom_drift
{
public:
  explicit Init_LocalizationStatus_map_odom_drift(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_gps_available map_odom_drift(::localization_msgs::msg::LocalizationStatus::_map_odom_drift_type arg)
  {
    msg_.map_odom_drift = std::move(arg);
    return Init_LocalizationStatus_gps_available(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_map_odom_stable
{
public:
  explicit Init_LocalizationStatus_map_odom_stable(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_map_odom_drift map_odom_stable(::localization_msgs::msg::LocalizationStatus::_map_odom_stable_type arg)
  {
    msg_.map_odom_stable = std::move(arg);
    return Init_LocalizationStatus_map_odom_drift(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_ndt_quality
{
public:
  explicit Init_LocalizationStatus_ndt_quality(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_map_odom_stable ndt_quality(::localization_msgs::msg::LocalizationStatus::_ndt_quality_type arg)
  {
    msg_.ndt_quality = std::move(arg);
    return Init_LocalizationStatus_map_odom_stable(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_ndt_healthy
{
public:
  explicit Init_LocalizationStatus_ndt_healthy(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_ndt_quality ndt_healthy(::localization_msgs::msg::LocalizationStatus::_ndt_healthy_type arg)
  {
    msg_.ndt_healthy = std::move(arg);
    return Init_LocalizationStatus_ndt_quality(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_heading_covariance
{
public:
  explicit Init_LocalizationStatus_heading_covariance(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_ndt_healthy heading_covariance(::localization_msgs::msg::LocalizationStatus::_heading_covariance_type arg)
  {
    msg_.heading_covariance = std::move(arg);
    return Init_LocalizationStatus_ndt_healthy(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_position_covariance
{
public:
  explicit Init_LocalizationStatus_position_covariance(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_heading_covariance position_covariance(::localization_msgs::msg::LocalizationStatus::_position_covariance_type arg)
  {
    msg_.position_covariance = std::move(arg);
    return Init_LocalizationStatus_heading_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_localization_confidence
{
public:
  explicit Init_LocalizationStatus_localization_confidence(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_position_covariance localization_confidence(::localization_msgs::msg::LocalizationStatus::_localization_confidence_type arg)
  {
    msg_.localization_confidence = std::move(arg);
    return Init_LocalizationStatus_position_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_status
{
public:
  explicit Init_LocalizationStatus_status(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_localization_confidence status(::localization_msgs::msg::LocalizationStatus::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_LocalizationStatus_localization_confidence(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_valid_until_ms
{
public:
  explicit Init_LocalizationStatus_valid_until_ms(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_status valid_until_ms(::localization_msgs::msg::LocalizationStatus::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_LocalizationStatus_status(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_age_ms
{
public:
  explicit Init_LocalizationStatus_age_ms(::localization_msgs::msg::LocalizationStatus & msg)
  : msg_(msg)
  {}
  Init_LocalizationStatus_valid_until_ms age_ms(::localization_msgs::msg::LocalizationStatus::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_LocalizationStatus_valid_until_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

class Init_LocalizationStatus_header
{
public:
  Init_LocalizationStatus_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LocalizationStatus_age_ms header(::localization_msgs::msg::LocalizationStatus::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LocalizationStatus_age_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::localization_msgs::msg::LocalizationStatus>()
{
  return localization_msgs::msg::builder::Init_LocalizationStatus_header();
}

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__BUILDER_HPP_
