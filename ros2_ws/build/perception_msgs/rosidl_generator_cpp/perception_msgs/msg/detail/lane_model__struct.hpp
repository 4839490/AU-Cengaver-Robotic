// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/LaneModel.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_HPP_

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
// Member 'centerline'
// Member 'left_boundary'
// Member 'right_boundary'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__perception_msgs__msg__LaneModel __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__LaneModel __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LaneModel_
{
  using Type = LaneModel_<ContainerAllocator>;

  explicit LaneModel_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lane_confidence = 0.0f;
      this->lane_lost = false;
      this->curvature = 0.0f;
      this->lane_width_estimate = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  explicit LaneModel_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    source_sensor(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->lane_confidence = 0.0f;
      this->lane_lost = false;
      this->curvature = 0.0f;
      this->lane_width_estimate = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _centerline_type =
    std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other>;
  _centerline_type centerline;
  using _left_boundary_type =
    std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other>;
  _left_boundary_type left_boundary;
  using _right_boundary_type =
    std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other>;
  _right_boundary_type right_boundary;
  using _lane_confidence_type =
    float;
  _lane_confidence_type lane_confidence;
  using _lane_lost_type =
    bool;
  _lane_lost_type lane_lost;
  using _curvature_type =
    float;
  _curvature_type curvature;
  using _lane_width_estimate_type =
    float;
  _lane_width_estimate_type lane_width_estimate;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
  using _source_sensor_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_sensor_type source_sensor;
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
  Type & set__centerline(
    const std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other> & _arg)
  {
    this->centerline = _arg;
    return *this;
  }
  Type & set__left_boundary(
    const std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other> & _arg)
  {
    this->left_boundary = _arg;
    return *this;
  }
  Type & set__right_boundary(
    const std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other> & _arg)
  {
    this->right_boundary = _arg;
    return *this;
  }
  Type & set__lane_confidence(
    const float & _arg)
  {
    this->lane_confidence = _arg;
    return *this;
  }
  Type & set__lane_lost(
    const bool & _arg)
  {
    this->lane_lost = _arg;
    return *this;
  }
  Type & set__curvature(
    const float & _arg)
  {
    this->curvature = _arg;
    return *this;
  }
  Type & set__lane_width_estimate(
    const float & _arg)
  {
    this->lane_width_estimate = _arg;
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
  Type & set__source_sensor(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->source_sensor = _arg;
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
    perception_msgs::msg::LaneModel_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::LaneModel_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::LaneModel_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::LaneModel_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__LaneModel
    std::shared_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__LaneModel
    std::shared_ptr<perception_msgs::msg::LaneModel_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LaneModel_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->centerline != other.centerline) {
      return false;
    }
    if (this->left_boundary != other.left_boundary) {
      return false;
    }
    if (this->right_boundary != other.right_boundary) {
      return false;
    }
    if (this->lane_confidence != other.lane_confidence) {
      return false;
    }
    if (this->lane_lost != other.lane_lost) {
      return false;
    }
    if (this->curvature != other.curvature) {
      return false;
    }
    if (this->lane_width_estimate != other.lane_width_estimate) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->source_sensor != other.source_sensor) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const LaneModel_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LaneModel_

// alias to use template instance with default allocator
using LaneModel =
  perception_msgs::msg::LaneModel_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__LANE_MODEL__STRUCT_HPP_
