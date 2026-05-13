// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__MISSION_STATE__BUILDER_HPP_
#define FSM_MSGS__MSG__DETAIL__MISSION_STATE__BUILDER_HPP_

#include "fsm_msgs/msg/detail/mission_state__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace fsm_msgs
{

namespace msg
{

namespace builder
{

class Init_MissionState_valid_until_ms
{
public:
  explicit Init_MissionState_valid_until_ms(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  ::fsm_msgs::msg::MissionState valid_until_ms(::fsm_msgs::msg::MissionState::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_age_ms
{
public:
  explicit Init_MissionState_age_ms(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_valid_until_ms age_ms(::fsm_msgs::msg::MissionState::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_MissionState_valid_until_ms(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_dropoff_complete
{
public:
  explicit Init_MissionState_dropoff_complete(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_age_ms dropoff_complete(::fsm_msgs::msg::MissionState::_dropoff_complete_type arg)
  {
    msg_.dropoff_complete = std::move(arg);
    return Init_MissionState_age_ms(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_pickup_complete
{
public:
  explicit Init_MissionState_pickup_complete(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_dropoff_complete pickup_complete(::fsm_msgs::msg::MissionState::_pickup_complete_type arg)
  {
    msg_.pickup_complete = std::move(arg);
    return Init_MissionState_dropoff_complete(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_next_waypoint_type
{
public:
  explicit Init_MissionState_next_waypoint_type(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_pickup_complete next_waypoint_type(::fsm_msgs::msg::MissionState::_next_waypoint_type_type arg)
  {
    msg_.next_waypoint_type = std::move(arg);
    return Init_MissionState_pickup_complete(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_next_waypoint_id
{
public:
  explicit Init_MissionState_next_waypoint_id(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_next_waypoint_type next_waypoint_id(::fsm_msgs::msg::MissionState::_next_waypoint_id_type arg)
  {
    msg_.next_waypoint_id = std::move(arg);
    return Init_MissionState_next_waypoint_type(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_current_waypoint_type
{
public:
  explicit Init_MissionState_current_waypoint_type(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_next_waypoint_id current_waypoint_type(::fsm_msgs::msg::MissionState::_current_waypoint_type_type arg)
  {
    msg_.current_waypoint_type = std::move(arg);
    return Init_MissionState_next_waypoint_id(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_current_waypoint_id
{
public:
  explicit Init_MissionState_current_waypoint_id(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_current_waypoint_type current_waypoint_id(::fsm_msgs::msg::MissionState::_current_waypoint_id_type arg)
  {
    msg_.current_waypoint_id = std::move(arg);
    return Init_MissionState_current_waypoint_type(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_completed_waypoints
{
public:
  explicit Init_MissionState_completed_waypoints(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_current_waypoint_id completed_waypoints(::fsm_msgs::msg::MissionState::_completed_waypoints_type arg)
  {
    msg_.completed_waypoints = std::move(arg);
    return Init_MissionState_current_waypoint_id(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_total_waypoints
{
public:
  explicit Init_MissionState_total_waypoints(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_completed_waypoints total_waypoints(::fsm_msgs::msg::MissionState::_total_waypoints_type arg)
  {
    msg_.total_waypoints = std::move(arg);
    return Init_MissionState_completed_waypoints(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_mission_active
{
public:
  explicit Init_MissionState_mission_active(::fsm_msgs::msg::MissionState & msg)
  : msg_(msg)
  {}
  Init_MissionState_total_waypoints mission_active(::fsm_msgs::msg::MissionState::_mission_active_type arg)
  {
    msg_.mission_active = std::move(arg);
    return Init_MissionState_total_waypoints(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

class Init_MissionState_header
{
public:
  Init_MissionState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MissionState_mission_active header(::fsm_msgs::msg::MissionState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_MissionState_mission_active(msg_);
  }

private:
  ::fsm_msgs::msg::MissionState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::fsm_msgs::msg::MissionState>()
{
  return fsm_msgs::msg::builder::Init_MissionState_header();
}

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__MISSION_STATE__BUILDER_HPP_
