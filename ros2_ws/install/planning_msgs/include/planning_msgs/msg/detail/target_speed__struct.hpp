// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/TargetSpeed.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__TargetSpeed __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__TargetSpeed __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TargetSpeed_
{
  using Type = TargetSpeed_<ContainerAllocator>;

  explicit TargetSpeed_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->speed = 0.0f;
      this->jerk_limit = 0.0f;
      this->reason = 0;
      this->valid_until_ms = 0ul;
      this->age_ms = 0ul;
    }
  }

  explicit TargetSpeed_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->speed = 0.0f;
      this->jerk_limit = 0.0f;
      this->reason = 0;
      this->valid_until_ms = 0ul;
      this->age_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _speed_type =
    float;
  _speed_type speed;
  using _jerk_limit_type =
    float;
  _jerk_limit_type jerk_limit;
  using _reason_type =
    uint8_t;
  _reason_type reason;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
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
  Type & set__speed(
    const float & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__jerk_limit(
    const float & _arg)
  {
    this->jerk_limit = _arg;
    return *this;
  }
  Type & set__reason(
    const uint8_t & _arg)
  {
    this->reason = _arg;
    return *this;
  }
  Type & set__valid_until_ms(
    const uint32_t & _arg)
  {
    this->valid_until_ms = _arg;
    return *this;
  }
  Type & set__age_ms(
    const uint32_t & _arg)
  {
    this->age_ms = _arg;
    return *this;
  }
  Type & set__warning_flags(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other> & _arg)
  {
    this->warning_flags = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t REASON_LANE_FOLLOW =
    0u;
  static constexpr uint8_t REASON_APPROACH_STOP =
    1u;
  static constexpr uint8_t REASON_PICKUP_DROPOFF =
    2u;
  static constexpr uint8_t REASON_OBSTACLE_SLOW =
    3u;
  static constexpr uint8_t REASON_JUNCTION =
    4u;
  static constexpr uint8_t REASON_TUNNEL =
    5u;
  static constexpr uint8_t REASON_PARK_APPROACH =
    6u;
  static constexpr uint8_t REASON_PARK_MANEUVER =
    7u;
  static constexpr uint8_t REASON_EMERGENCY_STOP =
    8u;
  static constexpr uint8_t REASON_LOCALIZATION_DEGRADED =
    9u;
  static constexpr uint8_t REASON_LANE_LOST =
    10u;

  // pointer types
  using RawPtr =
    planning_msgs::msg::TargetSpeed_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::TargetSpeed_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::TargetSpeed_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::TargetSpeed_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__TargetSpeed
    std::shared_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__TargetSpeed
    std::shared_ptr<planning_msgs::msg::TargetSpeed_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TargetSpeed_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->jerk_limit != other.jerk_limit) {
      return false;
    }
    if (this->reason != other.reason) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const TargetSpeed_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TargetSpeed_

// alias to use template instance with default allocator
using TargetSpeed =
  planning_msgs::msg::TargetSpeed_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_LANE_FOLLOW;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_APPROACH_STOP;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_PICKUP_DROPOFF;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_OBSTACLE_SLOW;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_JUNCTION;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_TUNNEL;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_PARK_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_PARK_MANEUVER;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_EMERGENCY_STOP;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_LOCALIZATION_DEGRADED;
template<typename ContainerAllocator>
constexpr uint8_t TargetSpeed_<ContainerAllocator>::REASON_LANE_LOST;

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TARGET_SPEED__STRUCT_HPP_
