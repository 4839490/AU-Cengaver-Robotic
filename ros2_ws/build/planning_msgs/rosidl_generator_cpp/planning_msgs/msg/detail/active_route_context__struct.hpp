// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/ActiveRouteContext.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_HPP_

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
// Member 'planned_trajectory'
#include "geometry_msgs/msg/detail/point__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__planning_msgs__msg__ActiveRouteContext __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__ActiveRouteContext __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ActiveRouteContext_
{
  using Type = ActiveRouteContext_<ContainerAllocator>;

  explicit ActiveRouteContext_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->active_waypoint_id = 0ul;
      this->target_x = 0.0f;
      this->target_y = 0.0f;
      this->target_heading = 0.0f;
      this->planner_mode = 0;
      this->route_direction = "";
      this->lookahead_distance = 0.0f;
      this->in_stop_zone = false;
      this->distance_to_stop_zone = 0.0f;
      this->localization_confidence = 0.0f;
      this->ego_speed_mps = 0.0f;
      this->route_context_valid = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit ActiveRouteContext_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    route_direction(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->active_waypoint_id = 0ul;
      this->target_x = 0.0f;
      this->target_y = 0.0f;
      this->target_heading = 0.0f;
      this->planner_mode = 0;
      this->route_direction = "";
      this->lookahead_distance = 0.0f;
      this->in_stop_zone = false;
      this->distance_to_stop_zone = 0.0f;
      this->localization_confidence = 0.0f;
      this->ego_speed_mps = 0.0f;
      this->route_context_valid = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _active_waypoint_id_type =
    uint32_t;
  _active_waypoint_id_type active_waypoint_id;
  using _target_x_type =
    float;
  _target_x_type target_x;
  using _target_y_type =
    float;
  _target_y_type target_y;
  using _target_heading_type =
    float;
  _target_heading_type target_heading;
  using _planner_mode_type =
    uint8_t;
  _planner_mode_type planner_mode;
  using _route_direction_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _route_direction_type route_direction;
  using _planned_trajectory_type =
    std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other>;
  _planned_trajectory_type planned_trajectory;
  using _lookahead_distance_type =
    float;
  _lookahead_distance_type lookahead_distance;
  using _in_stop_zone_type =
    bool;
  _in_stop_zone_type in_stop_zone;
  using _distance_to_stop_zone_type =
    float;
  _distance_to_stop_zone_type distance_to_stop_zone;
  using _localization_confidence_type =
    float;
  _localization_confidence_type localization_confidence;
  using _ego_speed_mps_type =
    float;
  _ego_speed_mps_type ego_speed_mps;
  using _route_context_valid_type =
    bool;
  _route_context_valid_type route_context_valid;
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
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__active_waypoint_id(
    const uint32_t & _arg)
  {
    this->active_waypoint_id = _arg;
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
  Type & set__target_heading(
    const float & _arg)
  {
    this->target_heading = _arg;
    return *this;
  }
  Type & set__planner_mode(
    const uint8_t & _arg)
  {
    this->planner_mode = _arg;
    return *this;
  }
  Type & set__route_direction(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->route_direction = _arg;
    return *this;
  }
  Type & set__planned_trajectory(
    const std::vector<geometry_msgs::msg::Point_<ContainerAllocator>, typename ContainerAllocator::template rebind<geometry_msgs::msg::Point_<ContainerAllocator>>::other> & _arg)
  {
    this->planned_trajectory = _arg;
    return *this;
  }
  Type & set__lookahead_distance(
    const float & _arg)
  {
    this->lookahead_distance = _arg;
    return *this;
  }
  Type & set__in_stop_zone(
    const bool & _arg)
  {
    this->in_stop_zone = _arg;
    return *this;
  }
  Type & set__distance_to_stop_zone(
    const float & _arg)
  {
    this->distance_to_stop_zone = _arg;
    return *this;
  }
  Type & set__localization_confidence(
    const float & _arg)
  {
    this->localization_confidence = _arg;
    return *this;
  }
  Type & set__ego_speed_mps(
    const float & _arg)
  {
    this->ego_speed_mps = _arg;
    return *this;
  }
  Type & set__route_context_valid(
    const bool & _arg)
  {
    this->route_context_valid = _arg;
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

  // pointer types
  using RawPtr =
    planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__ActiveRouteContext
    std::shared_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__ActiveRouteContext
    std::shared_ptr<planning_msgs::msg::ActiveRouteContext_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ActiveRouteContext_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->active_waypoint_id != other.active_waypoint_id) {
      return false;
    }
    if (this->target_x != other.target_x) {
      return false;
    }
    if (this->target_y != other.target_y) {
      return false;
    }
    if (this->target_heading != other.target_heading) {
      return false;
    }
    if (this->planner_mode != other.planner_mode) {
      return false;
    }
    if (this->route_direction != other.route_direction) {
      return false;
    }
    if (this->planned_trajectory != other.planned_trajectory) {
      return false;
    }
    if (this->lookahead_distance != other.lookahead_distance) {
      return false;
    }
    if (this->in_stop_zone != other.in_stop_zone) {
      return false;
    }
    if (this->distance_to_stop_zone != other.distance_to_stop_zone) {
      return false;
    }
    if (this->localization_confidence != other.localization_confidence) {
      return false;
    }
    if (this->ego_speed_mps != other.ego_speed_mps) {
      return false;
    }
    if (this->route_context_valid != other.route_context_valid) {
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
  bool operator!=(const ActiveRouteContext_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ActiveRouteContext_

// alias to use template instance with default allocator
using ActiveRouteContext =
  planning_msgs::msg::ActiveRouteContext_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__ACTIVE_ROUTE_CONTEXT__STRUCT_HPP_
