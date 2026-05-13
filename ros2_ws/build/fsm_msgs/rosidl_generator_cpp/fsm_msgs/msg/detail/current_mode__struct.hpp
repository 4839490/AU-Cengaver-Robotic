// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fsm_msgs:msg/CurrentMode.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_HPP_
#define FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_HPP_

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
# define DEPRECATED__fsm_msgs__msg__CurrentMode __attribute__((deprecated))
#else
# define DEPRECATED__fsm_msgs__msg__CurrentMode __declspec(deprecated)
#endif

namespace fsm_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CurrentMode_
{
  using Type = CurrentMode_<ContainerAllocator>;

  explicit CurrentMode_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0;
      this->previous_mode = 0;
      this->reason = "";
      this->stop_reason = 0;
      this->waypoint_id = 0ul;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit CurrentMode_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    reason(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mode = 0;
      this->previous_mode = 0;
      this->reason = "";
      this->stop_reason = 0;
      this->waypoint_id = 0ul;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _mode_type =
    uint8_t;
  _mode_type mode;
  using _previous_mode_type =
    uint8_t;
  _previous_mode_type previous_mode;
  using _reason_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _reason_type reason;
  using _stop_reason_type =
    uint8_t;
  _stop_reason_type stop_reason;
  using _waypoint_id_type =
    uint32_t;
  _waypoint_id_type waypoint_id;
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
  Type & set__mode(
    const uint8_t & _arg)
  {
    this->mode = _arg;
    return *this;
  }
  Type & set__previous_mode(
    const uint8_t & _arg)
  {
    this->previous_mode = _arg;
    return *this;
  }
  Type & set__reason(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->reason = _arg;
    return *this;
  }
  Type & set__stop_reason(
    const uint8_t & _arg)
  {
    this->stop_reason = _arg;
    return *this;
  }
  Type & set__waypoint_id(
    const uint32_t & _arg)
  {
    this->waypoint_id = _arg;
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
    fsm_msgs::msg::CurrentMode_<ContainerAllocator> *;
  using ConstRawPtr =
    const fsm_msgs::msg::CurrentMode_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::CurrentMode_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::CurrentMode_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fsm_msgs__msg__CurrentMode
    std::shared_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fsm_msgs__msg__CurrentMode
    std::shared_ptr<fsm_msgs::msg::CurrentMode_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CurrentMode_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->mode != other.mode) {
      return false;
    }
    if (this->previous_mode != other.previous_mode) {
      return false;
    }
    if (this->reason != other.reason) {
      return false;
    }
    if (this->stop_reason != other.stop_reason) {
      return false;
    }
    if (this->waypoint_id != other.waypoint_id) {
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
  bool operator!=(const CurrentMode_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CurrentMode_

// alias to use template instance with default allocator
using CurrentMode =
  fsm_msgs::msg::CurrentMode_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::LANE_FOLLOW;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::PICKUP_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::DROPOFF_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::OBSTACLE_AVOID;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::PARK_APPROACH;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::PARK_MANEUVER;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::MISSION_COMPLETE;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_NONE;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_RED_LIGHT;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_STOP_SIGN;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_OBSTACLE_TTC;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_LOCALIZATION_LOST;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_STALE_SENSOR;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_MISSION_ABORT;
template<typename ContainerAllocator>
constexpr uint8_t CurrentMode_<ContainerAllocator>::STOP_PEDESTRIAN;

}  // namespace msg

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__CURRENT_MODE__STRUCT_HPP_
