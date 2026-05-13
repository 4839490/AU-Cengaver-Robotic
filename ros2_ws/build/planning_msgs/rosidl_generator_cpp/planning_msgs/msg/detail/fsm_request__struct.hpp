// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/FSMRequest.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__FSMRequest __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__FSMRequest __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FSMRequest_
{
  using Type = FSMRequest_<ContainerAllocator>;

  explicit FSMRequest_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->request_type = 0;
      this->requested_mode = 0;
      this->waypoint_id = 0ul;
      this->reason = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit FSMRequest_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    reason(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->request_type = 0;
      this->requested_mode = 0;
      this->waypoint_id = 0ul;
      this->reason = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _request_type_type =
    uint8_t;
  _request_type_type request_type;
  using _requested_mode_type =
    uint8_t;
  _requested_mode_type requested_mode;
  using _waypoint_id_type =
    uint32_t;
  _waypoint_id_type waypoint_id;
  using _reason_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _reason_type reason;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__request_type(
    const uint8_t & _arg)
  {
    this->request_type = _arg;
    return *this;
  }
  Type & set__requested_mode(
    const uint8_t & _arg)
  {
    this->requested_mode = _arg;
    return *this;
  }
  Type & set__waypoint_id(
    const uint32_t & _arg)
  {
    this->waypoint_id = _arg;
    return *this;
  }
  Type & set__reason(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->reason = _arg;
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

  // constant declarations
  static constexpr uint8_t MODE_CHANGE =
    0u;
  static constexpr uint8_t REPLANNING_NEEDED =
    1u;
  static constexpr uint8_t GOAL_CONFIRMED =
    2u;
  static constexpr uint8_t OBSTACLE_BLOCKED =
    3u;
  static constexpr uint8_t LOCALIZATION_DEGRADED =
    4u;
  static constexpr uint8_t PARK_READY =
    5u;

  // pointer types
  using RawPtr =
    planning_msgs::msg::FSMRequest_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::FSMRequest_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::FSMRequest_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::FSMRequest_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__FSMRequest
    std::shared_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__FSMRequest
    std::shared_ptr<planning_msgs::msg::FSMRequest_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FSMRequest_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->request_type != other.request_type) {
      return false;
    }
    if (this->requested_mode != other.requested_mode) {
      return false;
    }
    if (this->waypoint_id != other.waypoint_id) {
      return false;
    }
    if (this->reason != other.reason) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    return true;
  }
  bool operator!=(const FSMRequest_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FSMRequest_

// alias to use template instance with default allocator
using FSMRequest =
  planning_msgs::msg::FSMRequest_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::MODE_CHANGE;
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::REPLANNING_NEEDED;
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::GOAL_CONFIRMED;
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::OBSTACLE_BLOCKED;
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::LOCALIZATION_DEGRADED;
template<typename ContainerAllocator>
constexpr uint8_t FSMRequest_<ContainerAllocator>::PARK_READY;

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__FSM_REQUEST__STRUCT_HPP_
