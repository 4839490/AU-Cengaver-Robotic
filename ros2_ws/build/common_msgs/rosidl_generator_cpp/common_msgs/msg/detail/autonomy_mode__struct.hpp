// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from common_msgs:msg/AutonomyMode.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_HPP_
#define COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__common_msgs__msg__AutonomyMode __attribute__((deprecated))
#else
# define DEPRECATED__common_msgs__msg__AutonomyMode __declspec(deprecated)
#endif

namespace common_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AutonomyMode_
{
  using Type = AutonomyMode_<ContainerAllocator>;

  explicit AutonomyMode_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0;
    }
  }

  explicit AutonomyMode_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0;
    }
  }

  // field types and members
  using _mode_type =
    uint8_t;
  _mode_type mode;

  // setters for named parameter idiom
  Type & set__mode(
    const uint8_t & _arg)
  {
    this->mode = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t LANE_FOLLOW =
    0u;
  static constexpr uint8_t STOP_APPROACH =
    1u;
  static constexpr uint8_t PICKUP_APPROACH =
    2u;
  static constexpr uint8_t DROPOFF_APPROACH =
    3u;
  static constexpr uint8_t OBSTACLE_AVOID =
    4u;
  static constexpr uint8_t PARK_APPROACH =
    5u;
  static constexpr uint8_t PARK_MANEUVER =
    6u;
  static constexpr uint8_t MISSION_COMPLETE =
    7u;

  // pointer types
  using RawPtr =
    common_msgs::msg::AutonomyMode_<ContainerAllocator> *;
  using ConstRawPtr =
    const common_msgs::msg::AutonomyMode_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      common_msgs::msg::AutonomyMode_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      common_msgs::msg::AutonomyMode_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__common_msgs__msg__AutonomyMode
    std::shared_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__common_msgs__msg__AutonomyMode
    std::shared_ptr<common_msgs::msg::AutonomyMode_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AutonomyMode_ & other) const
  {
    if (this->mode != other.mode) {
      return false;
    }
    return true;
  }
  bool operator!=(const AutonomyMode_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AutonomyMode_

// alias to use template instance with default allocator
using AutonomyMode =
  common_msgs::msg::AutonomyMode_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::LANE_FOLLOW;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::STOP_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::PICKUP_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::DROPOFF_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::OBSTACLE_AVOID;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::PARK_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::PARK_MANEUVER;
template<typename ContainerAllocator>
constexpr uint8_t AutonomyMode_<ContainerAllocator>::MISSION_COMPLETE;

}  // namespace msg

}  // namespace common_msgs

#endif  // COMMON_MSGS__MSG__DETAIL__AUTONOMY_MODE__STRUCT_HPP_
