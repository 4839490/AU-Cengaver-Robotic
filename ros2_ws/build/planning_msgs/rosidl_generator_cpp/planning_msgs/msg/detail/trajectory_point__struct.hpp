// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/TrajectoryPoint.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__planning_msgs__msg__TrajectoryPoint __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__TrajectoryPoint __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TrajectoryPoint_
{
  using Type = TrajectoryPoint_<ContainerAllocator>;

  explicit TrajectoryPoint_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->yaw = 0.0;
      this->speed = 0.0f;
      this->curvature = 0.0f;
      this->distance_from_start = 0.0f;
    }
  }

  explicit TrajectoryPoint_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0;
      this->y = 0.0;
      this->yaw = 0.0;
      this->speed = 0.0f;
      this->curvature = 0.0f;
      this->distance_from_start = 0.0f;
    }
  }

  // field types and members
  using _x_type =
    double;
  _x_type x;
  using _y_type =
    double;
  _y_type y;
  using _yaw_type =
    double;
  _yaw_type yaw;
  using _speed_type =
    float;
  _speed_type speed;
  using _curvature_type =
    float;
  _curvature_type curvature;
  using _distance_from_start_type =
    float;
  _distance_from_start_type distance_from_start;

  // setters for named parameter idiom
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
  Type & set__speed(
    const float & _arg)
  {
    this->speed = _arg;
    return *this;
  }
  Type & set__curvature(
    const float & _arg)
  {
    this->curvature = _arg;
    return *this;
  }
  Type & set__distance_from_start(
    const float & _arg)
  {
    this->distance_from_start = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__TrajectoryPoint
    std::shared_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__TrajectoryPoint
    std::shared_ptr<planning_msgs::msg::TrajectoryPoint_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrajectoryPoint_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->yaw != other.yaw) {
      return false;
    }
    if (this->speed != other.speed) {
      return false;
    }
    if (this->curvature != other.curvature) {
      return false;
    }
    if (this->distance_from_start != other.distance_from_start) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrajectoryPoint_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrajectoryPoint_

// alias to use template instance with default allocator
using TrajectoryPoint =
  planning_msgs::msg::TrajectoryPoint_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__TRAJECTORY_POINT__STRUCT_HPP_
