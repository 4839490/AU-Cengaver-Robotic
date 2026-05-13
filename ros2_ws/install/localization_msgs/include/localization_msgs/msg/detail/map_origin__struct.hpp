// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from localization_msgs:msg/MapOrigin.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_HPP_

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
# define DEPRECATED__localization_msgs__msg__MapOrigin __attribute__((deprecated))
#else
# define DEPRECATED__localization_msgs__msg__MapOrigin __declspec(deprecated)
#endif

namespace localization_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MapOrigin_
{
  using Type = MapOrigin_<ContainerAllocator>;

  explicit MapOrigin_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lat_ref = 0.0;
      this->lon_ref = 0.0;
      this->alt_ref = 0.0;
      this->yaw_ref = 0.0;
      this->source = "";
      this->locked = false;
    }
  }

  explicit MapOrigin_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    source(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lat_ref = 0.0;
      this->lon_ref = 0.0;
      this->alt_ref = 0.0;
      this->yaw_ref = 0.0;
      this->source = "";
      this->locked = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _lat_ref_type =
    double;
  _lat_ref_type lat_ref;
  using _lon_ref_type =
    double;
  _lon_ref_type lon_ref;
  using _alt_ref_type =
    double;
  _alt_ref_type alt_ref;
  using _yaw_ref_type =
    double;
  _yaw_ref_type yaw_ref;
  using _source_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_type source;
  using _locked_type =
    bool;
  _locked_type locked;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__lat_ref(
    const double & _arg)
  {
    this->lat_ref = _arg;
    return *this;
  }
  Type & set__lon_ref(
    const double & _arg)
  {
    this->lon_ref = _arg;
    return *this;
  }
  Type & set__alt_ref(
    const double & _arg)
  {
    this->alt_ref = _arg;
    return *this;
  }
  Type & set__yaw_ref(
    const double & _arg)
  {
    this->yaw_ref = _arg;
    return *this;
  }
  Type & set__source(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->source = _arg;
    return *this;
  }
  Type & set__locked(
    const bool & _arg)
  {
    this->locked = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    localization_msgs::msg::MapOrigin_<ContainerAllocator> *;
  using ConstRawPtr =
    const localization_msgs::msg::MapOrigin_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::MapOrigin_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::MapOrigin_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__localization_msgs__msg__MapOrigin
    std::shared_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__localization_msgs__msg__MapOrigin
    std::shared_ptr<localization_msgs::msg::MapOrigin_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MapOrigin_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->lat_ref != other.lat_ref) {
      return false;
    }
    if (this->lon_ref != other.lon_ref) {
      return false;
    }
    if (this->alt_ref != other.alt_ref) {
      return false;
    }
    if (this->yaw_ref != other.yaw_ref) {
      return false;
    }
    if (this->source != other.source) {
      return false;
    }
    if (this->locked != other.locked) {
      return false;
    }
    return true;
  }
  bool operator!=(const MapOrigin_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MapOrigin_

// alias to use template instance with default allocator
using MapOrigin =
  localization_msgs::msg::MapOrigin_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__MAP_ORIGIN__STRUCT_HPP_
