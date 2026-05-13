// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/TrafficSign.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__perception_msgs__msg__TrafficSign __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__TrafficSign __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct TrafficSign_
{
  using Type = TrafficSign_<ContainerAllocator>;

  explicit TrafficSign_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sign_id = 0ul;
      this->type = 0;
      this->confidence = 0.0f;
      this->relevant_to_route = false;
      this->distance = 0.0f;
      this->event_status = 0;
      this->confirmed = false;
      this->bbox_x = 0.0f;
      this->bbox_y = 0.0f;
      this->bbox_w = 0.0f;
      this->bbox_h = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->event_memory_ttl_ms = 0ul;
      this->source_sensor = "";
    }
  }

  explicit TrafficSign_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : source_sensor(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->sign_id = 0ul;
      this->type = 0;
      this->confidence = 0.0f;
      this->relevant_to_route = false;
      this->distance = 0.0f;
      this->event_status = 0;
      this->confirmed = false;
      this->bbox_x = 0.0f;
      this->bbox_y = 0.0f;
      this->bbox_w = 0.0f;
      this->bbox_h = 0.0f;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->event_memory_ttl_ms = 0ul;
      this->source_sensor = "";
    }
  }

  // field types and members
  using _sign_id_type =
    uint32_t;
  _sign_id_type sign_id;
  using _type_type =
    uint8_t;
  _type_type type;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _relevant_to_route_type =
    bool;
  _relevant_to_route_type relevant_to_route;
  using _distance_type =
    float;
  _distance_type distance;
  using _event_status_type =
    uint8_t;
  _event_status_type event_status;
  using _confirmed_type =
    bool;
  _confirmed_type confirmed;
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
  using _event_memory_ttl_ms_type =
    uint32_t;
  _event_memory_ttl_ms_type event_memory_ttl_ms;
  using _source_sensor_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_sensor_type source_sensor;
  using _warning_flags_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other>;
  _warning_flags_type warning_flags;

  // setters for named parameter idiom
  Type & set__sign_id(
    const uint32_t & _arg)
  {
    this->sign_id = _arg;
    return *this;
  }
  Type & set__type(
    const uint8_t & _arg)
  {
    this->type = _arg;
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
  Type & set__distance(
    const float & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__event_status(
    const uint8_t & _arg)
  {
    this->event_status = _arg;
    return *this;
  }
  Type & set__confirmed(
    const bool & _arg)
  {
    this->confirmed = _arg;
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
  Type & set__event_memory_ttl_ms(
    const uint32_t & _arg)
  {
    this->event_memory_ttl_ms = _arg;
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
  static constexpr uint8_t UNKNOWN_SIGN =
    0u;
  static constexpr uint8_t STOP =
    1u;
  static constexpr uint8_t SPEED_LIMIT =
    2u;
  static constexpr uint8_t NO_ENTRY =
    3u;
  static constexpr uint8_t MANDATORY_LEFT =
    4u;
  static constexpr uint8_t MANDATORY_RIGHT =
    5u;
  static constexpr uint8_t MANDATORY_STRAIGHT =
    6u;
  static constexpr uint8_t MANDATORY_LEFT_STRAIGHT =
    7u;
  static constexpr uint8_t MANDATORY_RIGHT_STRAIGHT =
    8u;
  static constexpr uint8_t ROUNDABOUT =
    9u;
  static constexpr uint8_t PARKING =
    10u;
  static constexpr uint8_t NO_PARKING =
    11u;
  static constexpr uint8_t TUNNEL =
    12u;
  static constexpr uint8_t PEDESTRIAN_CROSSING =
    13u;
  static constexpr uint8_t NEW =
    0u;
  static constexpr uint8_t TRACKED =
    1u;
  static constexpr uint8_t ALREADY_HANDLED =
    2u;
  static constexpr uint8_t STALE =
    3u;

  // pointer types
  using RawPtr =
    perception_msgs::msg::TrafficSign_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::TrafficSign_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficSign_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::TrafficSign_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__TrafficSign
    std::shared_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__TrafficSign
    std::shared_ptr<perception_msgs::msg::TrafficSign_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TrafficSign_ & other) const
  {
    if (this->sign_id != other.sign_id) {
      return false;
    }
    if (this->type != other.type) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->relevant_to_route != other.relevant_to_route) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    if (this->event_status != other.event_status) {
      return false;
    }
    if (this->confirmed != other.confirmed) {
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
    if (this->event_memory_ttl_ms != other.event_memory_ttl_ms) {
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
  bool operator!=(const TrafficSign_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TrafficSign_

// alias to use template instance with default allocator
using TrafficSign =
  perception_msgs::msg::TrafficSign_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::UNKNOWN_SIGN;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::STOP;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::SPEED_LIMIT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::NO_ENTRY;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::MANDATORY_LEFT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::MANDATORY_RIGHT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::MANDATORY_STRAIGHT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::MANDATORY_LEFT_STRAIGHT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::MANDATORY_RIGHT_STRAIGHT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::ROUNDABOUT;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::PARKING;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::NO_PARKING;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::TUNNEL;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::PEDESTRIAN_CROSSING;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::NEW;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::TRACKED;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::ALREADY_HANDLED;
template<typename ContainerAllocator>
constexpr uint8_t TrafficSign_<ContainerAllocator>::STALE;

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__TRAFFIC_SIGN__STRUCT_HPP_
