// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__BUILDER_HPP_

#include "perception_msgs/msg/detail/obstacle_track__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_ObstacleTrack_warning_flags
{
public:
  explicit Init_ObstacleTrack_warning_flags(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::ObstacleTrack warning_flags(::perception_msgs::msg::ObstacleTrack::_warning_flags_type arg)
  {
    msg_.warning_flags = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_valid_until_ms
{
public:
  explicit Init_ObstacleTrack_valid_until_ms(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_warning_flags valid_until_ms(::perception_msgs::msg::ObstacleTrack::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_ObstacleTrack_warning_flags(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_age_ms
{
public:
  explicit Init_ObstacleTrack_age_ms(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_valid_until_ms age_ms(::perception_msgs::msg::ObstacleTrack::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_ObstacleTrack_valid_until_ms(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_geometry_source
{
public:
  explicit Init_ObstacleTrack_geometry_source(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_age_ms geometry_source(::perception_msgs::msg::ObstacleTrack::_geometry_source_type arg)
  {
    msg_.geometry_source = std::move(arg);
    return Init_ObstacleTrack_age_ms(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_semantic_source
{
public:
  explicit Init_ObstacleTrack_semantic_source(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_geometry_source semantic_source(::perception_msgs::msg::ObstacleTrack::_semantic_source_type arg)
  {
    msg_.semantic_source = std::move(arg);
    return Init_ObstacleTrack_geometry_source(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_source_sensor
{
public:
  explicit Init_ObstacleTrack_source_sensor(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_semantic_source source_sensor(::perception_msgs::msg::ObstacleTrack::_source_sensor_type arg)
  {
    msg_.source_sensor = std::move(arg);
    return Init_ObstacleTrack_semantic_source(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_is_static
{
public:
  explicit Init_ObstacleTrack_is_static(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_source_sensor is_static(::perception_msgs::msg::ObstacleTrack::_is_static_type arg)
  {
    msg_.is_static = std::move(arg);
    return Init_ObstacleTrack_source_sensor(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_height
{
public:
  explicit Init_ObstacleTrack_height(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_is_static height(::perception_msgs::msg::ObstacleTrack::_height_type arg)
  {
    msg_.height = std::move(arg);
    return Init_ObstacleTrack_is_static(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_length
{
public:
  explicit Init_ObstacleTrack_length(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_height length(::perception_msgs::msg::ObstacleTrack::_length_type arg)
  {
    msg_.length = std::move(arg);
    return Init_ObstacleTrack_height(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_width
{
public:
  explicit Init_ObstacleTrack_width(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_length width(::perception_msgs::msg::ObstacleTrack::_width_type arg)
  {
    msg_.width = std::move(arg);
    return Init_ObstacleTrack_length(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_ttc
{
public:
  explicit Init_ObstacleTrack_ttc(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_width ttc(::perception_msgs::msg::ObstacleTrack::_ttc_type arg)
  {
    msg_.ttc = std::move(arg);
    return Init_ObstacleTrack_width(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_velocity_y
{
public:
  explicit Init_ObstacleTrack_velocity_y(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_ttc velocity_y(::perception_msgs::msg::ObstacleTrack::_velocity_y_type arg)
  {
    msg_.velocity_y = std::move(arg);
    return Init_ObstacleTrack_ttc(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_velocity_x
{
public:
  explicit Init_ObstacleTrack_velocity_x(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_velocity_y velocity_x(::perception_msgs::msg::ObstacleTrack::_velocity_x_type arg)
  {
    msg_.velocity_x = std::move(arg);
    return Init_ObstacleTrack_velocity_y(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_distance
{
public:
  explicit Init_ObstacleTrack_distance(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_velocity_x distance(::perception_msgs::msg::ObstacleTrack::_distance_type arg)
  {
    msg_.distance = std::move(arg);
    return Init_ObstacleTrack_velocity_x(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_position_y
{
public:
  explicit Init_ObstacleTrack_position_y(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_distance position_y(::perception_msgs::msg::ObstacleTrack::_position_y_type arg)
  {
    msg_.position_y = std::move(arg);
    return Init_ObstacleTrack_distance(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_position_x
{
public:
  explicit Init_ObstacleTrack_position_x(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_position_y position_x(::perception_msgs::msg::ObstacleTrack::_position_x_type arg)
  {
    msg_.position_x = std::move(arg);
    return Init_ObstacleTrack_position_y(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_confidence
{
public:
  explicit Init_ObstacleTrack_confidence(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_position_x confidence(::perception_msgs::msg::ObstacleTrack::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_ObstacleTrack_position_x(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_class_label
{
public:
  explicit Init_ObstacleTrack_class_label(::perception_msgs::msg::ObstacleTrack & msg)
  : msg_(msg)
  {}
  Init_ObstacleTrack_confidence class_label(::perception_msgs::msg::ObstacleTrack::_class_label_type arg)
  {
    msg_.class_label = std::move(arg);
    return Init_ObstacleTrack_confidence(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

class Init_ObstacleTrack_track_id
{
public:
  Init_ObstacleTrack_track_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObstacleTrack_class_label track_id(::perception_msgs::msg::ObstacleTrack::_track_id_type arg)
  {
    msg_.track_id = std::move(arg);
    return Init_ObstacleTrack_class_label(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTrack msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::ObstacleTrack>()
{
  return perception_msgs::msg::builder::Init_ObstacleTrack_track_id();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__BUILDER_HPP_
