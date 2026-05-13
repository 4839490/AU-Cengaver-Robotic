// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/GoalReached.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__GoalReached __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__GoalReached __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct GoalReached_
{
  using Type = GoalReached_<ContainerAllocator>;

  explicit GoalReached_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_id = 0ul;
      this->waypoint_type = 0;
      this->success = false;
      this->distance_error = 0.0f;
      this->heading_error = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit GoalReached_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->waypoint_id = 0ul;
      this->waypoint_type = 0;
      this->success = false;
      this->distance_error = 0.0f;
      this->heading_error = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _waypoint_id_type =
    uint32_t;
  _waypoint_id_type waypoint_id;
  using _waypoint_type_type =
    uint8_t;
  _waypoint_type_type waypoint_type;
  using _success_type =
    bool;
  _success_type success;
  using _distance_error_type =
    float;
  _distance_error_type distance_error;
  using _heading_error_type =
    float;
  _heading_error_type heading_error;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
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
  Type & set__waypoint_id(
    const uint32_t & _arg)
  {
    this->waypoint_id = _arg;
    return *this;
  }
  Type & set__waypoint_type(
    const uint8_t & _arg)
  {
    this->waypoint_type = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__distance_error(
    const float & _arg)
  {
    this->distance_error = _arg;
    return *this;
  }
  Type & set__heading_error(
    const float & _arg)
  {
    this->heading_error = _arg;
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
  Type & set__warning_flags(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other> & _arg)
  {
    this->warning_flags = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t PICKUP =
    0u;
  static constexpr uint8_t DROPOFF =
    1u;
  static constexpr uint8_t WAYPOINT =
    2u;
  static constexpr uint8_t PARK_ENTRY =
    3u;

  // pointer types
  using RawPtr =
    planning_msgs::msg::GoalReached_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::GoalReached_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::GoalReached_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::GoalReached_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__GoalReached
    std::shared_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__GoalReached
    std::shared_ptr<planning_msgs::msg::GoalReached_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GoalReached_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->waypoint_id != other.waypoint_id) {
      return false;
    }
    if (this->waypoint_type != other.waypoint_type) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    if (this->distance_error != other.distance_error) {
      return false;
    }
    if (this->heading_error != other.heading_error) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const GoalReached_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GoalReached_

// alias to use template instance with default allocator
using GoalReached =
  planning_msgs::msg::GoalReached_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t GoalReached_<ContainerAllocator>::PICKUP;
template<typename ContainerAllocator>
constexpr uint8_t GoalReached_<ContainerAllocator>::DROPOFF;
template<typename ContainerAllocator>
constexpr uint8_t GoalReached_<ContainerAllocator>::WAYPOINT;
template<typename ContainerAllocator>
constexpr uint8_t GoalReached_<ContainerAllocator>::PARK_ENTRY;

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__GOAL_REACHED__STRUCT_HPP_
