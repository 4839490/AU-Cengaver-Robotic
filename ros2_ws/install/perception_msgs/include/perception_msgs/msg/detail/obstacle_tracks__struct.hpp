// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/ObstacleTracks.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_HPP_

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
// Member 'tracks'
#include "perception_msgs/msg/detail/obstacle_track__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__perception_msgs__msg__ObstacleTracks __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__ObstacleTracks __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObstacleTracks_
{
  using Type = ObstacleTracks_<ContainerAllocator>;

  explicit ObstacleTracks_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit ObstacleTracks_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _tracks_type =
    std::vector<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>, typename ContainerAllocator::template rebind<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>::other>;
  _tracks_type tracks;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__tracks(
    const std::vector<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>, typename ContainerAllocator::template rebind<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>::other> & _arg)
  {
    this->tracks = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    perception_msgs::msg::ObstacleTracks_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::ObstacleTracks_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::ObstacleTracks_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::ObstacleTracks_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__ObstacleTracks
    std::shared_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__ObstacleTracks
    std::shared_ptr<perception_msgs::msg::ObstacleTracks_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObstacleTracks_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->tracks != other.tracks) {
      return false;
    }
    return true;
  }
  bool operator!=(const ObstacleTracks_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObstacleTracks_

// alias to use template instance with default allocator
using ObstacleTracks =
  perception_msgs::msg::ObstacleTracks_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACKS__STRUCT_HPP_
