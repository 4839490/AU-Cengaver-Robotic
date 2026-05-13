// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__BUILDER_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__BUILDER_HPP_

#include "localization_msgs/msg/detail/map_origin__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace localization_msgs
{

namespace msg
{

namespace builder
{

class Init_MapOrigin_locked
{
public:
  explicit Init_MapOrigin_locked(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  ::localization_msgs::msg::MapOrigin locked(::localization_msgs::msg::MapOrigin::_locked_type arg)
  {
    msg_.locked = std::move(arg);
    return std::move(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_source
{
public:
  explicit Init_MapOrigin_source(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  Init_MapOrigin_locked source(::localization_msgs::msg::MapOrigin::_source_type arg)
  {
    msg_.source = std::move(arg);
    return Init_MapOrigin_locked(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_yaw_ref
{
public:
  explicit Init_MapOrigin_yaw_ref(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  Init_MapOrigin_source yaw_ref(::localization_msgs::msg::MapOrigin::_yaw_ref_type arg)
  {
    msg_.yaw_ref = std::move(arg);
    return Init_MapOrigin_source(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_alt_ref
{
public:
  explicit Init_MapOrigin_alt_ref(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  Init_MapOrigin_yaw_ref alt_ref(::localization_msgs::msg::MapOrigin::_alt_ref_type arg)
  {
    msg_.alt_ref = std::move(arg);
    return Init_MapOrigin_yaw_ref(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_lon_ref
{
public:
  explicit Init_MapOrigin_lon_ref(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  Init_MapOrigin_alt_ref lon_ref(::localization_msgs::msg::MapOrigin::_lon_ref_type arg)
  {
    msg_.lon_ref = std::move(arg);
    return Init_MapOrigin_alt_ref(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_lat_ref
{
public:
  explicit Init_MapOrigin_lat_ref(::localization_msgs::msg::MapOrigin & msg)
  : msg_(msg)
  {}
  Init_MapOrigin_lon_ref lat_ref(::localization_msgs::msg::MapOrigin::_lat_ref_type arg)
  {
    msg_.lat_ref = std::move(arg);
    return Init_MapOrigin_lon_ref(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

class Init_MapOrigin_header
{
public:
  Init_MapOrigin_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MapOrigin_lat_ref header(::localization_msgs::msg::MapOrigin::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_MapOrigin_lat_ref(msg_);
  }

private:
  ::localization_msgs::msg::MapOrigin msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::localization_msgs::msg::MapOrigin>()
{
  return localization_msgs::msg::builder::Init_MapOrigin_header();
}

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__BUILDER_HPP_
