// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/LaneModel.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__BUILDER_HPP_

#include "perception_msgs/msg/detail/lane_model__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_LaneModel_warning_flags
{
public:
  explicit Init_LaneModel_warning_flags(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::LaneModel warning_flags(::perception_msgs::msg::LaneModel::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_source_sensor
{
public:
  explicit Init_LaneModel_source_sensor(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_warning_flags source_sensor(::perception_msgs::msg::LaneModel::_source_sensor_type arg)
  {
    msg_.source_sensor = std::move(arg);
    return Init_LaneModel_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_valid_until_ms
{
public:
  explicit Init_LaneModel_valid_until_ms(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_source_sensor valid_until_ms(::perception_msgs::msg::LaneModel::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_LaneModel_source_sensor(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_age_ms
{
public:
  explicit Init_LaneModel_age_ms(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_valid_until_ms age_ms(::perception_msgs::msg::LaneModel::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_LaneModel_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_lane_width_estimate
{
public:
  explicit Init_LaneModel_lane_width_estimate(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_age_ms lane_width_estimate(::perception_msgs::msg::LaneModel::_lane_width_estimate_type arg)
  {
    msg_.lane_width_estimate = std::move(arg);
    return Init_LaneModel_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_curvature
{
public:
  explicit Init_LaneModel_curvature(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_lane_width_estimate curvature(::perception_msgs::msg::LaneModel::_curvature_type arg)
  {
    msg_.curvature = std::move(arg);
    return Init_LaneModel_lane_width_estimate(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_lane_lost
{
public:
  explicit Init_LaneModel_lane_lost(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_curvature lane_lost(::perception_msgs::msg::LaneModel::_lane_lost_type arg)
  {
    msg_.lane_lost = std::move(arg);
    return Init_LaneModel_curvature(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_lane_confidence
{
public:
  explicit Init_LaneModel_lane_confidence(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_lane_lost lane_confidence(::perception_msgs::msg::LaneModel::_lane_confidence_type arg)
  {
    msg_.lane_confidence = std::move(arg);
    return Init_LaneModel_lane_lost(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_right_boundary
{
public:
  explicit Init_LaneModel_right_boundary(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_lane_confidence right_boundary(::perception_msgs::msg::LaneModel::_right_boundary_type arg)
  {
    msg_.right_boundary = std::move(arg);
    return Init_LaneModel_lane_confidence(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_left_boundary
{
public:
  explicit Init_LaneModel_left_boundary(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_right_boundary left_boundary(::perception_msgs::msg::LaneModel::_left_boundary_type arg)
  {
    msg_.left_boundary = std::move(arg);
    return Init_LaneModel_right_boundary(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_centerline
{
public:
  explicit Init_LaneModel_centerline(::perception_msgs::msg::LaneModel & msg)
  : msg_(msg)
  {}
  Init_LaneModel_left_boundary centerline(::perception_msgs::msg::LaneModel::_centerline_type arg)
  {
    msg_.centerline = std::move(arg);
    return Init_LaneModel_left_boundary(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

class Init_LaneModel_header
{
public:
  Init_LaneModel_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LaneModel_centerline header(::perception_msgs::msg::LaneModel::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LaneModel_centerline(msg_);
  }

private:
  ::perception_msgs::msg::LaneModel msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::LaneModel>()
{
  return perception_msgs::msg::builder::Init_LaneModel_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__BUILDER_HPP_
