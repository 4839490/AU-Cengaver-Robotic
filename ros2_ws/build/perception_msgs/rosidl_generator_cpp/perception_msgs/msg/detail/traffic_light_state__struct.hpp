// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/TrafficLightState.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_

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
# define DEPRECATED__perception_msgs__msg__TrafficLightState __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__TrafficLightState __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TrafficLightState_
{
  using Type = TrafficLightState_<ContainerAllocator>;

  explicit TrafficLightState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = 0;
      this->confidence = 0.0f;
      this->relevant_to_route = false;
      this->distance_to_stop = 0.0f;
      this->confirmed = false;
      this->in_stop_zone = false;
      this->bbox_x = 0.0f;
      this->bbox_y = 0.0f;
      this->bbox_w = 0.0f;
      this->bbox_h = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  explicit TrafficLightState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    source_sensor(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = 0;
      this->confidence = 0.0f;
      this->relevant_to_route = false;
      this->distance_to_stop = 0.0f;
      this->confirmed = false;
      this->in_stop_zone = false;
      this->bbox_x = 0.0f;
      this->bbox_y = 0.0f;
      this->bbox_w = 0.0f;
      this->bbox_h = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->source_sensor = "";
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _state_type =
    uint8_t;
  _state_type state;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _relevant_to_route_type =
    bool;
  _relevant_to_route_type relevant_to_route;
  using _distance_to_stop_type =
    float;
  _distance_to_stop_type distance_to_stop;
  using _confirmed_type =
    bool;
  _confirmed_type confirmed;
  using _in_stop_zone_type =
    bool;
  _in_stop_zone_type in_stop_zone;
  using _bbox_x_type =
    float;
  _bbox_x_type bbox_x;
  using _bbox_y_type =
    float;
  _bbox_y_type bbox_y;
  using _bbox_w_type =
    float;
  _bbox_w_type bbox_w;
  using _bbox_h_type =
    float;
  _bbox_h_type bbox_h;
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
  Type & set__state(
    const uint8_t & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__relevant_to_route(
    const bool & _arg)
  {
    this->relevant_to_route = _arg;
    return *this;
  }
  Type & set__distance_to_stop(
    const float & _arg)
  {
    this->distance_to_stop = _arg;
    return *this;
  }
  Type & set__confirmed(
    const bool & _arg)
  {
    this->confirmed = _arg;
    return *this;
  }
  Type & set__in_stop_zone(
    const bool & _arg)
  {
    this->in_stop_zone = _arg;
    return *this;
  }
  Type & set__bbox_x(
    const float & _arg)
  {
    this->bbox_x = _arg;
    return *this;
  }
  Type & set__bbox_y(
    const float & _arg)
  {
    this->bbox_y = _arg;
    return *this;
  }
  Type & set__bbox_w(
    const float & _arg)
  {
    this->bbox_w = _arg;
    return *this;
  }
  Type & set__bbox_h(
    const float & _arg)
  {
    this->bbox_h = _arg;
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
  static constexpr uint8_t UNKNOWN =
    0u;
  static constexpr uint8_t RED =
    1u;
  static constexpr uint8_t YELLOW =
    2u;
  static constexpr uint8_t GREEN =
    3u;
  static constexpr uint8_t STALE =
    4u;
  static constexpr uint8_t CONFLICT =
    5u;

  // pointer types
  using RawPtr =
    perception_msgs::msg::TrafficLightState_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::TrafficLightState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficLightState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficLightState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__TrafficLightState
    std::shared_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__TrafficLightState
    std::shared_ptr<perception_msgs::msg::TrafficLightState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrafficLightState_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->state != other.state) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->relevant_to_route != other.relevant_to_route) {
      return false;
    }
    if (this->distance_to_stop != other.distance_to_stop) {
      return false;
    }
    if (this->confirmed != other.confirmed) {
      return false;
    }
    if (this->in_stop_zone != other.in_stop_zone) {
      return false;
    }
    if (this->bbox_x != other.bbox_x) {
      return false;
    }
    if (this->bbox_y != other.bbox_y) {
      return false;
    }
    if (this->bbox_w != other.bbox_w) {
      return false;
    }
    if (this->bbox_h != other.bbox_h) {
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
  bool operator!=(const TrafficLightState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrafficLightState_

// alias to use template instance with default allocator
using TrafficLightState =
  perception_msgs::msg::TrafficLightState_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::UNKNOWN;
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::RED;
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::YELLOW;
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::GREEN;
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::STALE;
template<typename ContainerAllocator>
constexpr uint8_t TrafficLightState_<ContainerAllocator>::CONFLICT;

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_LIGHT_STATE__STRUCT_HPP_
