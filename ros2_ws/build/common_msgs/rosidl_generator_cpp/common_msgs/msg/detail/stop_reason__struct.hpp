// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from common_msgs:msg/StopReason.idl
// generated code does not contain a copyright notice

#ifndef COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_
#define COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__common_msgs__msg__StopReason __attribute__((deprecated))
#else
# define DEPRECATED__common_msgs__msg__StopReason __declspec(deprecated)
#endif

namespace common_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StopReason_
{
  using Type = StopReason_<ContainerAllocator>;

  explicit StopReason_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reason = 0;
    }
  }

  explicit StopReason_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->reason = 0;
    }
  }

  // field types and members
  using _reason_type =
    uint8_t;
  _reason_type reason;

  // setters for named parameter idiom
  Type & set__reason(
    const uint8_t & _arg)
  {
    this->reason = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t STOP_NONE =
    0u;
  static constexpr uint8_t STOP_RED_LIGHT =
    1u;
  static constexpr uint8_t STOP_STOP_SIGN =
    2u;
  static constexpr uint8_t STOP_OBSTACLE_TTC =
    3u;
  static constexpr uint8_t STOP_LOCALIZATION_LOST =
    4u;
  static constexpr uint8_t STOP_STALE_SENSOR =
    5u;
  static constexpr uint8_t STOP_MISSION_ABORT =
    6u;
  static constexpr uint8_t STOP_PEDESTRIAN =
    7u;

  // pointer types
  using RawPtr =
    common_msgs::msg::StopReason_<ContainerAllocator> *;
  using ConstRawPtr =
    const common_msgs::msg::StopReason_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<common_msgs::msg::StopReason_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<common_msgs::msg::StopReason_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      common_msgs::msg::StopReason_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<common_msgs::msg::StopReason_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      common_msgs::msg::StopReason_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<common_msgs::msg::StopReason_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<common_msgs::msg::StopReason_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<common_msgs::msg::StopReason_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__common_msgs__msg__StopReason
    std::shared_ptr<common_msgs::msg::StopReason_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__common_msgs__msg__StopReason
    std::shared_ptr<common_msgs::msg::StopReason_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StopReason_ & other) const
  {
    if (this->reason != other.reason) {
      return false;
    }
    return true;
  }
  bool operator!=(const StopReason_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StopReason_

// alias to use template instance with default allocator
using StopReason =
  common_msgs::msg::StopReason_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_NONE;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_RED_LIGHT;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_STOP_SIGN;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_OBSTACLE_TTC;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_LOCALIZATION_LOST;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_STALE_SENSOR;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_MISSION_ABORT;
template<typename ContainerAllocator>
constexpr uint8_t StopReason_<ContainerAllocator>::STOP_PEDESTRIAN;

}  // namespace msg

}  // namespace common_msgs

#endif  // COMMON_MSGS__MSG__DETAIL__STOP_REASON__STRUCT_HPP_
