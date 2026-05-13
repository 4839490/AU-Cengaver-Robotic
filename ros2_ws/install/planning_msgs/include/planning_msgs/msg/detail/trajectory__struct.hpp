// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/Trajectory.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_HPP_

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
// Member 'points'
#include "planning_msgs/msg/detail/trajectory_point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__planning_msgs__msg__Trajectory __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__Trajectory __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Trajectory_
{
  using Type = Trajectory_<ContainerAllocator>;

  explicit Trajectory_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->planner_mode = 0;
      this->valid_until_ms = 0ul;
      this->age_ms = 0ul;
    }
  }

  explicit Trajectory_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->planner_mode = 0;
      this->valid_until_ms = 0ul;
      this->age_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _points_type =
    std::vector<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>, typename ContainerAllocator::template rebind<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>::other>;
  _points_type points;
  using _planner_mode_type =
    uint8_t;
  _planner_mode_type planner_mode;
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
  Type & set__points(
    const std::vector<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>, typename ContainerAllocator::template rebind<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>::other> & _arg)
  {
    this->points = _arg;
    return *this;
  }
  Type & set__planner_mode(
    const uint8_t & _arg)
  {
    this->planner_mode = _arg;
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

  // pointer types
  using RawPtr =
    planning_msgs::msg::Trajectory_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::Trajectory_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::Trajectory_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::Trajectory_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__Trajectory
    std::shared_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__Trajectory
    std::shared_ptr<planning_msgs::msg::Trajectory_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Trajectory_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->points != other.points) {
      return false;
    }
    if (this->planner_mode != other.planner_mode) {
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
  bool operator!=(const Trajectory_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Trajectory_

// alias to use template instance with default allocator
using Trajectory =
  planning_msgs::msg::Trajectory_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY__STRUCT_HPP_
