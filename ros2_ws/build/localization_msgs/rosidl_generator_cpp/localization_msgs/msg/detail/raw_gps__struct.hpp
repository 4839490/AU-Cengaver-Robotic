// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from localization_msgs:msg/RawGps.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__localization_msgs__msg__RawGps __attribute__((deprecated))
#else
# define DEPRECATED__localization_msgs__msg__RawGps __declspec(deprecated)
#endif

namespace localization_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RawGps_
{
  using Type = RawGps_<ContainerAllocator>;

  explicit RawGps_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0;
      this->speed = 0.0;
      this->heading_deg = 0.0;
      this->hdop = 0.0;
      this->vdop = 0.0;
      this->fix_type = 0;
    }
  }

  explicit RawGps_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->latitude = 0.0;
      this->longitude = 0.0;
      this->altitude = 0.0;
      this->speed = 0.0;
      this->heading_deg = 0.0;
      this->hdop = 0.0;
      this->vdop = 0.0;
      this->fix_type = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
  using _latitude_type =
    double;
  _latitude_type latitude;
  using _longitude_type =
    double;
  _longitude_type longitude;
  using _altitude_type =
    double;
  _altitude_type altitude;
  using _speed_type =
    double;
  _speed_type speed;
  using _heading_deg_type =
    double;
  _heading_deg_type heading_deg;
  using _hdop_type =
    double;
  _hdop_type hdop;
  using _vdop_type =
    double;
  _vdop_type vdop;
  using _fix_type_type =
    uint8_t;
  _fix_type_type fix_type;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__age_ms(
    const uint32_t & _arg)
  {
    this->age_ms = _arg;
    return *this;
  }
  Type & set__valid_until_ms(
    const uint32_t & _arg)
  {
    this->valid_until_ms = _arg;
    return *this;
  }
  Type & set__latitude(
    const double & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const double & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__altitude(
    const double & _arg)
  {
    this->altitude = _arg;
    return *this;
  }
  Type & set__speed(
    const double & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__heading_deg(
    const double & _arg)
  {
    this->heading_deg = _arg;
    return *this;
  }
  Type & set__hdop(
    const double & _arg)
  {
    this->hdop = _arg;
    return *this;
  }
  Type & set__vdop(
    const double & _arg)
  {
    this->vdop = _arg;
    return *this;
  }
  Type & set__fix_type(
    const uint8_t & _arg)
  {
    this->fix_type = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t FIX_NONE =
    0u;
  static constexpr uint8_t FIX_GPS =
    1u;
  static constexpr uint8_t FIX_DGPS =
    2u;
  static constexpr uint8_t FIX_RTK_FLOAT =
    4u;
  static constexpr uint8_t FIX_RTK_FIXED =
    5u;

  // pointer types
  using RawPtr =
    localization_msgs::msg::RawGps_<ContainerAllocator> *;
  using ConstRawPtr =
    const localization_msgs::msg::RawGps_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<localization_msgs::msg::RawGps_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<localization_msgs::msg::RawGps_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::RawGps_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::RawGps_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::RawGps_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::RawGps_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<localization_msgs::msg::RawGps_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<localization_msgs::msg::RawGps_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__localization_msgs__msg__RawGps
    std::shared_ptr<localization_msgs::msg::RawGps_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__localization_msgs__msg__RawGps
    std::shared_ptr<localization_msgs::msg::RawGps_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RawGps_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->altitude != other.altitude) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->heading_deg != other.heading_deg) {
      return false;
    }
    if (this->hdop != other.hdop) {
      return false;
    }
    if (this->vdop != other.vdop) {
      return false;
    }
    if (this->fix_type != other.fix_type) {
      return false;
    }
    return true;
  }
  bool operator!=(const RawGps_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RawGps_

// alias to use template instance with default allocator
using RawGps =
  localization_msgs::msg::RawGps_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t RawGps_<ContainerAllocator>::FIX_NONE;
template<typename ContainerAllocator>
constexpr uint8_t RawGps_<ContainerAllocator>::FIX_GPS;
template<typename ContainerAllocator>
constexpr uint8_t RawGps_<ContainerAllocator>::FIX_DGPS;
template<typename ContainerAllocator>
constexpr uint8_t RawGps_<ContainerAllocator>::FIX_RTK_FLOAT;
template<typename ContainerAllocator>
constexpr uint8_t RawGps_<ContainerAllocator>::FIX_RTK_FIXED;

}  // namespace msg

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__RAW_GPS__STRUCT_HPP_
