// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/ParkComplete.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__ParkComplete __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__ParkComplete __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ParkComplete_
{
  using Type = ParkComplete_<ContainerAllocator>;

  explicit ParkComplete_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_cross_track_error = 0.0f;
      this->final_heading_error = 0.0f;
      this->iterations_used = 0;
      this->waypoint_id = 0ul;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit ParkComplete_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_cross_track_error = 0.0f;
      this->final_heading_error = 0.0f;
      this->iterations_used = 0;
      this->waypoint_id = 0ul;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _success_type =
    bool;
  _success_type success;
  using _final_cross_track_error_type =
    float;
  _final_cross_track_error_type final_cross_track_error;
  using _final_heading_error_type =
    float;
  _final_heading_error_type final_heading_error;
  using _iterations_used_type =
    uint8_t;
  _iterations_used_type iterations_used;
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
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__final_cross_track_error(
    const float & _arg)
  {
    this->final_cross_track_error = _arg;
    return *this;
  }
  Type & set__final_heading_error(
    const float & _arg)
  {
    this->final_heading_error = _arg;
    return *this;
  }
  Type & set__iterations_used(
    const uint8_t & _arg)
  {
    this->iterations_used = _arg;
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

  // pointer types
  using RawPtr =
    planning_msgs::msg::ParkComplete_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::ParkComplete_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ParkComplete_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ParkComplete_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__ParkComplete
    std::shared_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__ParkComplete
    std::shared_ptr<planning_msgs::msg::ParkComplete_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ParkComplete_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    if (this->final_cross_track_error != other.final_cross_track_error) {
      return false;
    }
    if (this->final_heading_error != other.final_heading_error) {
      return false;
    }
    if (this->iterations_used != other.iterations_used) {
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
  bool operator!=(const ParkComplete_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ParkComplete_

// alias to use template instance with default allocator
using ParkComplete =
  planning_msgs::msg::ParkComplete_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__PARK_COMPLETE__STRUCT_HPP_
