// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from localization_msgs:msg/RawGps.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__BUILDER_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__BUILDER_HPP_

#include "localization_msgs/msg/detail/raw_gps__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace localization_msgs
{

namespace msg
{

namespace builder
{

class Init_RawGps_fix_type
{
public:
  explicit Init_RawGps_fix_type(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  ::localization_msgs::msg::RawGps fix_type(::localization_msgs::msg::RawGps::_fix_type_type arg)
  {
    msg_.fix_type = std::move(arg);
    return std::move(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_vdop
{
public:
  explicit Init_RawGps_vdop(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_fix_type vdop(::localization_msgs::msg::RawGps::_vdop_type arg)
  {
    msg_.vdop = std::move(arg);
    return Init_RawGps_fix_type(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_hdop
{
public:
  explicit Init_RawGps_hdop(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_vdop hdop(::localization_msgs::msg::RawGps::_hdop_type arg)
  {
    msg_.hdop = std::move(arg);
    return Init_RawGps_vdop(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_heading_deg
{
public:
  explicit Init_RawGps_heading_deg(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_hdop heading_deg(::localization_msgs::msg::RawGps::_heading_deg_type arg)
  {
    msg_.heading_deg = std::move(arg);
    return Init_RawGps_hdop(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_speed
{
public:
  explicit Init_RawGps_speed(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_heading_deg speed(::localization_msgs::msg::RawGps::_speed_type arg)
  {
    msg_.speed = std::move(arg);
    return Init_RawGps_heading_deg(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_altitude
{
public:
  explicit Init_RawGps_altitude(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_speed altitude(::localization_msgs::msg::RawGps::_altitude_type arg)
  {
    msg_.altitude = std::move(arg);
    return Init_RawGps_speed(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_longitude
{
public:
  explicit Init_RawGps_longitude(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_altitude longitude(::localization_msgs::msg::RawGps::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_RawGps_altitude(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_latitude
{
public:
  explicit Init_RawGps_latitude(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_longitude latitude(::localization_msgs::msg::RawGps::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_RawGps_longitude(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_valid_until_ms
{
public:
  explicit Init_RawGps_valid_until_ms(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_latitude valid_until_ms(::localization_msgs::msg::RawGps::_valid_until_ms_type arg)
  {
    msg_.valid_until_ms = std::move(arg);
    return Init_RawGps_latitude(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_age_ms
{
public:
  explicit Init_RawGps_age_ms(::localization_msgs::msg::RawGps & msg)
  : msg_(msg)
  {}
  Init_RawGps_valid_until_ms age_ms(::localization_msgs::msg::RawGps::_age_ms_type arg)
  {
    msg_.age_ms = std::move(arg);
    return Init_RawGps_valid_until_ms(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

class Init_RawGps_header
{
public:
  Init_RawGps_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_RawGps_age_ms header(::localization_msgs::msg::RawGps::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_RawGps_age_ms(msg_);
  }

private:
  ::localization_msgs::msg::RawGps msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::localization_msgs::msg::RawGps>()
{
  return localization_msgs::msg::builder::Init_RawGps_header();
}

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__BUILDER_HPP_
