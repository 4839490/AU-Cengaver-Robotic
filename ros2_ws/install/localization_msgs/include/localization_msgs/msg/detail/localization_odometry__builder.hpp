// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from localization_msgs:msg/LocalizationOdometry.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__BUILDER_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__BUILDER_HPP_

#include "localization_msgs/msg/detail/localization_odometry__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace localization_msgs
{

namespace msg
{

namespace builder
{

class Init_LocalizationOdometry_warning_flags
{
public:
  explicit Init_LocalizationOdometry_warning_flags(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  ::localization_msgs::msg::LocalizationOdometry warning_flags(::localization_msgs::msg::LocalizationOdometry::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_velocity_covariance
{
public:
  explicit Init_LocalizationOdometry_velocity_covariance(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_warning_flags velocity_covariance(::localization_msgs::msg::LocalizationOdometry::_velocity_covariance_type arg)
  {
    msg_.velocity_covariance = std::move(arg);
    return Init_LocalizationOdometry_warning_flags(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_heading_covariance
{
public:
  explicit Init_LocalizationOdometry_heading_covariance(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_velocity_covariance heading_covariance(::localization_msgs::msg::LocalizationOdometry::_heading_covariance_type arg)
  {
    msg_.heading_covariance = std::move(arg);
    return Init_LocalizationOdometry_velocity_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_position_covariance
{
public:
  explicit Init_LocalizationOdometry_position_covariance(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_heading_covariance position_covariance(::localization_msgs::msg::LocalizationOdometry::_position_covariance_type arg)
  {
    msg_.position_covariance = std::move(arg);
    return Init_LocalizationOdometry_heading_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_angular_velocity
{
public:
  explicit Init_LocalizationOdometry_angular_velocity(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_position_covariance angular_velocity(::localization_msgs::msg::LocalizationOdometry::_angular_velocity_type arg)
  {
    msg_.angular_velocity = std::move(arg);
    return Init_LocalizationOdometry_position_covariance(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_linear_velocity
{
public:
  explicit Init_LocalizationOdometry_linear_velocity(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_angular_velocity linear_velocity(::localization_msgs::msg::LocalizationOdometry::_linear_velocity_type arg)
  {
    msg_.linear_velocity = std::move(arg);
    return Init_LocalizationOdometry_angular_velocity(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_yaw
{
public:
  explicit Init_LocalizationOdometry_yaw(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_linear_velocity yaw(::localization_msgs::msg::LocalizationOdometry::_yaw_type arg)
  {
    msg_.yaw = std::move(arg);
    return Init_LocalizationOdometry_linear_velocity(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_y
{
public:
  explicit Init_LocalizationOdometry_y(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_yaw y(::localization_msgs::msg::LocalizationOdometry::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_LocalizationOdometry_yaw(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_x
{
public:
  explicit Init_LocalizationOdometry_x(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_y x(::localization_msgs::msg::LocalizationOdometry::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_LocalizationOdometry_y(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_valid_until_ms
{
public:
  explicit Init_LocalizationOdometry_valid_until_ms(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_x valid_until_ms(::localization_msgs::msg::LocalizationOdometry::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_LocalizationOdometry_x(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_age_ms
{
public:
  explicit Init_LocalizationOdometry_age_ms(::localization_msgs::msg::LocalizationOdometry & msg)
  : msg_(msg)
  {}
  Init_LocalizationOdometry_valid_until_ms age_ms(::localization_msgs::msg::LocalizationOdometry::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_LocalizationOdometry_valid_until_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

class Init_LocalizationOdometry_header
{
public:
  Init_LocalizationOdometry_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LocalizationOdometry_age_ms header(::localization_msgs::msg::LocalizationOdometry::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LocalizationOdometry_age_ms(msg_);
  }

private:
  ::localization_msgs::msg::LocalizationOdometry msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::localization_msgs::msg::LocalizationOdometry>()
{
  return localization_msgs::msg::builder::Init_LocalizationOdometry_header();
}

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__BUILDER_HPP_
