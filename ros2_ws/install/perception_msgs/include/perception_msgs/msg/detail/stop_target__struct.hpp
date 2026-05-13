// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/StopTarget.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_HPP_

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
# define DEPRECATED__perception_msgs__msg__StopTarget __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__StopTarget __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct StopTarget_
{
  using Type = StopTarget_<ContainerAllocator>;

  explicit StopTarget_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_type = 0;
      this->distance_from_front_bumper = 0.0f;
      this->target_x = 0.0f;
      this->target_y = 0.0f;
      this->confidence = 0.0f;
      this->source = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->waypoint_id = 0l;
      this->heading_at_stop = 0.0f;
      this->priority = 0;
      this->required_stop_duration_ms = 0ul;
      this->stop_reason_id = 0ul;
      this->source_topic = "";
    }
  }

  explicit StopTarget_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    source(_alloc),
    source_topic(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_type = 0;
      this->distance_from_front_bumper = 0.0f;
      this->target_x = 0.0f;
      this->target_y = 0.0f;
      this->confidence = 0.0f;
      this->source = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->waypoint_id = 0l;
      this->heading_at_stop = 0.0f;
      this->priority = 0;
      this->required_stop_duration_ms = 0ul;
      this->stop_reason_id = 0ul;
      this->source_topic = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _target_type_type =
    uint8_t;
  _target_type_type target_type;
  using _distance_from_front_bumper_type =
    float;
  _distance_from_front_bumper_type distance_from_front_bumper;
  using _target_x_type =
    float;
  _target_x_type target_x;
  using _target_y_type =
    float;
  _target_y_type target_y;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _source_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_type source;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
  using _waypoint_id_type =
    int32_t;
  _waypoint_id_type waypoint_id;
  using _heading_at_stop_type =
    float;
  _heading_at_stop_type heading_at_stop;
  using _priority_type =
    uint8_t;
  _priority_type priority;
  using _required_stop_duration_ms_type =
    uint32_t;
  _required_stop_duration_ms_type required_stop_duration_ms;
  using _stop_reason_id_type =
    uint32_t;
  _stop_reason_id_type stop_reason_id;
  using _source_topic_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_topic_type source_topic;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__target_type(
    const uint8_t & _arg)
  {
    this->target_type = _arg;
    return *this;
  }
  Type & set__distance_from_front_bumper(
    const float & _arg)
  {
    this->distance_from_front_bumper = _arg;
    return *this;
  }
  Type & set__target_x(
    const float & _arg)
  {
    this->target_x = _arg;
    return *this;
  }
  Type & set__target_y(
    const float & _arg)
  {
    this->target_y = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__source(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->source = _arg;
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
  Type & set__waypoint_id(
    const int32_t & _arg)
  {
    this->waypoint_id = _arg;
    return *this;
  }
  Type & set__heading_at_stop(
    const float & _arg)
  {
    this->heading_at_stop = _arg;
    return *this;
  }
  Type & set__priority(
    const uint8_t & _arg)
  {
    this->priority = _arg;
    return *this;
  }
  Type & set__required_stop_duration_ms(
    const uint32_t & _arg)
  {
    this->required_stop_duration_ms = _arg;
    return *this;
  }
  Type & set__stop_reason_id(
    const uint32_t & _arg)
  {
    this->stop_reason_id = _arg;
    return *this;
  }
  Type & set__source_topic(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->source_topic = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t TRAFFIC_LIGHT_STOP =
    0u;
  static constexpr uint8_t STOP_SIGN =
    1u;
  static constexpr uint8_t PICKUP =
    2u;
  static constexpr uint8_t DROPOFF =
    3u;
  static constexpr uint8_t LOW =
    0u;
  static constexpr uint8_t NORMAL =
    1u;
  static constexpr uint8_t HIGH =
    2u;
  static constexpr uint8_t CRITICAL =
    3u;

  // pointer types
  using RawPtr =
    perception_msgs::msg::StopTarget_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::StopTarget_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::StopTarget_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::StopTarget_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__StopTarget
    std::shared_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__StopTarget
    std::shared_ptr<perception_msgs::msg::StopTarget_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StopTarget_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->target_type != other.target_type) {
      return false;
    }
    if (this->distance_from_front_bumper != other.distance_from_front_bumper) {
      return false;
    }
    if (this->target_x != other.target_x) {
      return false;
    }
    if (this->target_y != other.target_y) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->source != other.source) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->waypoint_id != other.waypoint_id) {
      return false;
    }
    if (this->heading_at_stop != other.heading_at_stop) {
      return false;
    }
    if (this->priority != other.priority) {
      return false;
    }
    if (this->required_stop_duration_ms != other.required_stop_duration_ms) {
      return false;
    }
    if (this->stop_reason_id != other.stop_reason_id) {
      return false;
    }
    if (this->source_topic != other.source_topic) {
      return false;
    }
    return true;
  }
  bool operator!=(const StopTarget_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StopTarget_

// alias to use template instance with default allocator
using StopTarget =
  perception_msgs::msg::StopTarget_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::TRAFFIC_LIGHT_STOP;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::STOP_SIGN;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::PICKUP;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::DROPOFF;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::LOW;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::NORMAL;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::HIGH;
template<typename ContainerAllocator>
constexpr uint8_t StopTarget_<ContainerAllocator>::CRITICAL;

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__STOP_TARGET__STRUCT_HPP_
