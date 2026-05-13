// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/ObstacleTrack.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__perception_msgs__msg__ObstacleTrack __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__ObstacleTrack __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ObstacleTrack_
{
  using Type = ObstacleTrack_<ContainerAllocator>;

  explicit ObstacleTrack_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->track_id = 0ul;
      this->class_label = 0;
      this->confidence = 0.0f;
      this->position_x = 0.0f;
      this->position_y = 0.0f;
      this->distance = 0.0f;
      this->velocity_x = 0.0f;
      this->velocity_y = 0.0f;
      this->ttc = 0.0f;
      this->width = 0.0f;
      this->length = 0.0f;
      this->height = 0.0f;
      this->is_static = false;
      this->source_sensor = "";
      this->semantic_source = "";
      this->geometry_source = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit ObstacleTrack_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : source_sensor(_alloc),
    semantic_source(_alloc),
    geometry_source(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->track_id = 0ul;
      this->class_label = 0;
      this->confidence = 0.0f;
      this->position_x = 0.0f;
      this->position_y = 0.0f;
      this->distance = 0.0f;
      this->velocity_x = 0.0f;
      this->velocity_y = 0.0f;
      this->ttc = 0.0f;
      this->width = 0.0f;
      this->length = 0.0f;
      this->height = 0.0f;
      this->is_static = false;
      this->source_sensor = "";
      this->semantic_source = "";
      this->geometry_source = "";
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _track_id_type =
    uint32_t;
  _track_id_type track_id;
  using _class_label_type =
    uint8_t;
  _class_label_type class_label;
  using _confidence_type =
    float;
  _confidence_type confidence;
  using _position_x_type =
    float;
  _position_x_type position_x;
  using _position_y_type =
    float;
  _position_y_type position_y;
  using _distance_type =
    float;
  _distance_type distance;
  using _velocity_x_type =
    float;
  _velocity_x_type velocity_x;
  using _velocity_y_type =
    float;
  _velocity_y_type velocity_y;
  using _ttc_type =
    float;
  _ttc_type ttc;
  using _width_type =
    float;
  _width_type width;
  using _length_type =
    float;
  _length_type length;
  using _height_type =
    float;
  _height_type height;
  using _is_static_type =
    bool;
  _is_static_type is_static;
  using _source_sensor_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _source_sensor_type source_sensor;
  using _semantic_source_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _semantic_source_type semantic_source;
  using _geometry_source_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _geometry_source_type geometry_source;
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
  Type & set__track_id(
    const uint32_t & _arg)
  {
    this->track_id = _arg;
    return *this;
  }
  Type & set__class_label(
    const uint8_t & _arg)
  {
    this->class_label = _arg;
    return *this;
  }
  Type & set__confidence(
    const float & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__position_x(
    const float & _arg)
  {
    this->position_x = _arg;
    return *this;
  }
  Type & set__position_y(
    const float & _arg)
  {
    this->position_y = _arg;
    return *this;
  }
  Type & set__distance(
    const float & _arg)
  {
    this->distance = _arg;
    return *this;
  }
  Type & set__velocity_x(
    const float & _arg)
  {
    this->velocity_x = _arg;
    return *this;
  }
  Type & set__velocity_y(
    const float & _arg)
  {
    this->velocity_y = _arg;
    return *this;
  }
  Type & set__ttc(
    const float & _arg)
  {
    this->ttc = _arg;
    return *this;
  }
  Type & set__width(
    const float & _arg)
  {
    this->width = _arg;
    return *this;
  }
  Type & set__length(
    const float & _arg)
  {
    this->length = _arg;
    return *this;
  }
  Type & set__height(
    const float & _arg)
  {
    this->height = _arg;
    return *this;
  }
  Type & set__is_static(
    const bool & _arg)
  {
    this->is_static = _arg;
    return *this;
  }
  Type & set__source_sensor(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->source_sensor = _arg;
    return *this;
  }
  Type & set__semantic_source(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->semantic_source = _arg;
    return *this;
  }
  Type & set__geometry_source(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->geometry_source = _arg;
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
  static constexpr uint8_t UNKNOWN_OBSTACLE =
    0u;
  static constexpr uint8_t VEHICLE =
    1u;
  static constexpr uint8_t PEDESTRIAN =
    2u;
  static constexpr uint8_t CONE =
    3u;
  static constexpr uint8_t BARRIER =
    4u;
  static constexpr uint8_t SIGN_POLE =
    5u;

  // pointer types
  using RawPtr =
    perception_msgs::msg::ObstacleTrack_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::ObstacleTrack_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__ObstacleTrack
    std::shared_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__ObstacleTrack
    std::shared_ptr<perception_msgs::msg::ObstacleTrack_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ObstacleTrack_ & other) const
  {
    if (this->track_id != other.track_id) {
      return false;
    }
    if (this->class_label != other.class_label) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->position_x != other.position_x) {
      return false;
    }
    if (this->position_y != other.position_y) {
      return false;
    }
    if (this->distance != other.distance) {
      return false;
    }
    if (this->velocity_x != other.velocity_x) {
      return false;
    }
    if (this->velocity_y != other.velocity_y) {
      return false;
    }
    if (this->ttc != other.ttc) {
      return false;
    }
    if (this->width != other.width) {
      return false;
    }
    if (this->length != other.length) {
      return false;
    }
    if (this->height != other.height) {
      return false;
    }
    if (this->is_static != other.is_static) {
      return false;
    }
    if (this->source_sensor != other.source_sensor) {
      return false;
    }
    if (this->semantic_source != other.semantic_source) {
      return false;
    }
    if (this->geometry_source != other.geometry_source) {
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
  bool operator!=(const ObstacleTrack_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ObstacleTrack_

// alias to use template instance with default allocator
using ObstacleTrack =
  perception_msgs::msg::ObstacleTrack_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::UNKNOWN_OBSTACLE;
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::VEHICLE;
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::PEDESTRIAN;
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::CONE;
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::BARRIER;
template<typename ContainerAllocator>
constexpr uint8_t ObstacleTrack_<ContainerAllocator>::SIGN_POLE;

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__OBSTACLE_TRACK__STRUCT_HPP_
