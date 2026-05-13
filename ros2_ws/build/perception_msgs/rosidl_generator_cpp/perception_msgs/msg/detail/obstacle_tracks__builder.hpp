// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from perception_msgs:msg/ObstacleTracks.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__BUILDER_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__BUILDER_HPP_

#include "perception_msgs/msg/detail/obstacle_tracks__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace perception_msgs
{

namespace msg
{

namespace builder
{

class Init_ObstacleTracks_tracks
{
public:
  explicit Init_ObstacleTracks_tracks(::perception_msgs::msg::ObstacleTracks & msg)
  : msg_(msg)
  {}
  ::perception_msgs::msg::ObstacleTracks tracks(::perception_msgs::msg::ObstacleTracks::_tracks_type arg)
  {
    msg_.tracks = std::move(arg);
    return std::move(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTracks msg_;
};

class Init_ObstacleTracks_header
{
public:
  Init_ObstacleTracks_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ObstacleTracks_tracks header(::perception_msgs::msg::ObstacleTracks::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ObstacleTracks_tracks(msg_);
  }

private:
  ::perception_msgs::msg::ObstacleTracks msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::perception_msgs::msg::ObstacleTracks>()
{
  return perception_msgs::msg::builder::Init_ObstacleTracks_header();
}

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__BUILDER_HPP_
