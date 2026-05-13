// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/TrafficSigns.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__STRUCT_HPP_

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
// Member 'signs'
#include "perception_msgs/msg/detail/traffic_sign__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__perception_msgs__msg__TrafficSigns __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__TrafficSigns __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TrafficSigns_
{
  using Type = TrafficSigns_<ContainerAllocator>;

  explicit TrafficSigns_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit TrafficSigns_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _signs_type =
    std::vector<perception_msgs::msg::TrafficSign_<ContainerAllocator>, typename ContainerAllocator::template rebind<perception_msgs::msg::TrafficSign_<ContainerAllocator>>::other>;
  _signs_type signs;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__signs(
    const std::vector<perception_msgs::msg::TrafficSign_<ContainerAllocator>, typename ContainerAllocator::template rebind<perception_msgs::msg::TrafficSign_<ContainerAllocator>>::other> & _arg)
  {
    this->signs = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    perception_msgs::msg::TrafficSigns_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::TrafficSigns_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficSigns_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficSigns_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__TrafficSigns
    std::shared_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__TrafficSigns
    std::shared_ptr<perception_msgs::msg::TrafficSigns_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrafficSigns_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->signs != other.signs) {
      return false;
    }
    return true;
  }
  bool operator!=(const TrafficSigns_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrafficSigns_

// alias to use template instance with default allocator
using TrafficSigns =
  perception_msgs::msg::TrafficSigns_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGNS__STRUCT_HPP_
