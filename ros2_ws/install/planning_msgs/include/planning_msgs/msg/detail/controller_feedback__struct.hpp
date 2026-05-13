// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/ControllerFeedback.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__ControllerFeedback __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__ControllerFeedback __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControllerFeedback_
{
  using Type = ControllerFeedback_<ContainerAllocator>;

  explicit ControllerFeedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->actual_speed = 0.0f;
      this->actual_steering_deg = 0.0f;
      this->cross_track_error = 0.0f;
      this->heading_error = 0.0f;
      this->brake_active = false;
      this->full_brake_active = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit ControllerFeedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->actual_speed = 0.0f;
      this->actual_steering_deg = 0.0f;
      this->cross_track_error = 0.0f;
      this->heading_error = 0.0f;
      this->brake_active = false;
      this->full_brake_active = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _actual_speed_type =
    float;
  _actual_speed_type actual_speed;
  using _actual_steering_deg_type =
    float;
  _actual_steering_deg_type actual_steering_deg;
  using _cross_track_error_type =
    float;
  _cross_track_error_type cross_track_error;
  using _heading_error_type =
    float;
  _heading_error_type heading_error;
  using _brake_active_type =
    bool;
  _brake_active_type brake_active;
  using _full_brake_active_type =
    bool;
  _full_brake_active_type full_brake_active;
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
  Type & set__actual_speed(
    const float & _arg)
  {
    this->actual_speed = _arg;
    return *this;
  }
  Type & set__actual_steering_deg(
    const float & _arg)
  {
    this->actual_steering_deg = _arg;
    return *this;
  }
  Type & set__cross_track_error(
    const float & _arg)
  {
    this->cross_track_error = _arg;
    return *this;
  }
  Type & set__heading_error(
    const float & _arg)
  {
    this->heading_error = _arg;
    return *this;
  }
  Type & set__brake_active(
    const bool & _arg)
  {
    this->brake_active = _arg;
    return *this;
  }
  Type & set__full_brake_active(
    const bool & _arg)
  {
    this->full_brake_active = _arg;
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

  // pointer types
  using RawPtr =
    planning_msgs::msg::ControllerFeedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::ControllerFeedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ControllerFeedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ControllerFeedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__ControllerFeedback
    std::shared_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__ControllerFeedback
    std::shared_ptr<planning_msgs::msg::ControllerFeedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControllerFeedback_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->actual_speed != other.actual_speed) {
      return false;
    }
    if (this->actual_steering_deg != other.actual_steering_deg) {
      return false;
    }
    if (this->cross_track_error != other.cross_track_error) {
      return false;
    }
    if (this->heading_error != other.heading_error) {
      return false;
    }
    if (this->brake_active != other.brake_active) {
      return false;
    }
    if (this->full_brake_active != other.full_brake_active) {
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
  bool operator!=(const ControllerFeedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControllerFeedback_

// alias to use template instance with default allocator
using ControllerFeedback =
  planning_msgs::msg::ControllerFeedback_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__CONTROLLER_FEEDBACK__STRUCT_HPP_
