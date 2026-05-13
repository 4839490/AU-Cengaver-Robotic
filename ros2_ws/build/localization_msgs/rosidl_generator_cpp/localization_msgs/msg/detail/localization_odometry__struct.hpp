// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from localization_msgs:msg/LocalizationOdometry.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_HPP_

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
# define DEPRECATED__localization_msgs__msg__LocalizationOdometry __attribute__((deprecated))
#else
# define DEPRECATED__localization_msgs__msg__LocalizationOdometry __declspec(deprecated)
#endif

namespace localization_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LocalizationOdometry_
{
  using Type = LocalizationOdometry_<ContainerAllocator>;

  explicit LocalizationOdometry_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->x = 0.0;
      this->y = 0.0;
      this->yaw = 0.0;
      this->linear_velocity = 0.0;
      this->angular_velocity = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->velocity_covariance = 0.0;
    }
  }

  explicit LocalizationOdometry_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->x = 0.0;
      this->y = 0.0;
      this->yaw = 0.0;
      this->linear_velocity = 0.0;
      this->angular_velocity = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->velocity_covariance = 0.0;
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
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _yaw_type =
    double;
  _yaw_type yaw;
  using _linear_velocity_type =
    double;
  _linear_velocity_type linear_velocity;
  using _angular_velocity_type =
    double;
  _angular_velocity_type angular_velocity;
  using _position_covariance_type =
    double;
  _position_covariance_type position_covariance;
  using _heading_covariance_type =
    double;
  _heading_covariance_type heading_covariance;
  using _velocity_covariance_type =
    double;
  _velocity_covariance_type velocity_covariance;
  using _warning_flags_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other>;
  _warning_flags_type warning_flags;

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
  Type & set__x(
    const double & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const double & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__yaw(
    const double & _arg)
  {
    this->yaw = _arg;
    return *this;
  }
  Type & set__linear_velocity(
    const double & _arg)
  {
    this->linear_velocity = _arg;
    return *this;
  }
  Type & set__angular_velocity(
    const double & _arg)
  {
    this->angular_velocity = _arg;
    return *this;
  }
  Type & set__position_covariance(
    const double & _arg)
  {
    this->position_covariance = _arg;
    return *this;
  }
  Type & set__heading_covariance(
    const double & _arg)
  {
    this->heading_covariance = _arg;
    return *this;
  }
  Type & set__velocity_covariance(
    const double & _arg)
  {
    this->velocity_covariance = _arg;
    return *this;
  }
  Type & set__warning_flags(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other> & _arg)
  {
    this->warning_flags = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> *;
  using ConstRawPtr =
    const localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__localization_msgs__msg__LocalizationOdometry
    std::shared_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__localization_msgs__msg__LocalizationOdometry
    std::shared_ptr<localization_msgs::msg::LocalizationOdometry_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LocalizationOdometry_ & other) const
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
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->linear_velocity != other.linear_velocity) {
      return false;
    }
    if (this->angular_velocity != other.angular_velocity) {
      return false;
    }
    if (this->position_covariance != other.position_covariance) {
      return false;
    }
    if (this->heading_covariance != other.heading_covariance) {
      return false;
    }
    if (this->velocity_covariance != other.velocity_covariance) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const LocalizationOdometry_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LocalizationOdometry_

// alias to use template instance with default allocator
using LocalizationOdometry =
  localization_msgs::msg::LocalizationOdometry_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_ODOMETRY__STRUCT_HPP_
