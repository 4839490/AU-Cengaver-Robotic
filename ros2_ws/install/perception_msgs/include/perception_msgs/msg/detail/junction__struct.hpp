// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/Junction.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_HPP_

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
# define DEPRECATED__perception_msgs__msg__Junction __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__Junction __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Junction_
{
  using Type = Junction_<ContainerAllocator>;

  explicit Junction_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->detected = false;
      this->junction_type = 0;
      this->arm_count = 0;
      this->distance_to_entry = 0.0f;
      this->confidence = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  explicit Junction_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    source_sensor(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->detected = false;
      this->junction_type = 0;
      this->arm_count = 0;
      this->distance_to_entry = 0.0f;
      this->confidence = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _detected_type =
    bool;
  _detected_type detected;
  using _junction_type_type =
    uint8_t;
  _junction_type_type junction_type;
  using _arm_count_type =
    uint8_t;
  _arm_count_type arm_count;
  using _distance_to_entry_type =
    float;
  _distance_to_entry_type distance_to_entry;
  using _confidence_type =
    float;
  _confidence_type confidence;
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
  Type & set__detected(
    const bool & _arg)
  {
    this->detected = _arg;
    return *this;
  }
  Type & set__junction_type(
    const uint8_t & _arg)
  {
    this->junction_type = _arg;
    return *this;
  }
  Type & set__arm_count(
    const uint8_t & _arg)
  {
    this->arm_count = _arg;
    return *this;
  }
  Type & set__distance_to_entry(
    const float & _arg)
  {
    this->distance_to_entry = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
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
  static constexpr uint8_t NORMAL =
    0u;
  static constexpr uint8_t ROUNDABOUT =
    1u;

  // pointer types
  using RawPtr =
    perception_msgs::msg::Junction_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::Junction_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::Junction_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::Junction_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::Junction_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::Junction_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::Junction_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::Junction_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::Junction_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::Junction_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__Junction
    std::shared_ptr<perception_msgs::msg::Junction_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__Junction
    std::shared_ptr<perception_msgs::msg::Junction_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Junction_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->detected != other.detected) {
      return false;
    }
    if (this->junction_type != other.junction_type) {
      return false;
    }
    if (this->arm_count != other.arm_count) {
      return false;
    }
    if (this->distance_to_entry != other.distance_to_entry) {
      return false;
    }
    if (this->confidence != other.confidence) {
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
  bool operator!=(const Junction_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Junction_

// alias to use template instance with default allocator
using Junction =
  perception_msgs::msg::Junction_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t Junction_<ContainerAllocator>::NORMAL;
template<typename ContainerAllocator>
constexpr uint8_t Junction_<ContainerAllocator>::ROUNDABOUT;

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__JUNCTION__STRUCT_HPP_
