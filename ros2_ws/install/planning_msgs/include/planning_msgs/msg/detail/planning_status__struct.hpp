// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_HPP_
#define PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_HPP_

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
# define DEPRECATED__planning_msgs__msg__PlanningStatus __attribute__((deprecated))
#else
# define DEPRECATED__planning_msgs__msg__PlanningStatus __declspec(deprecated)
#endif

namespace planning_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PlanningStatus_
{
  using Type = PlanningStatus_<ContainerAllocator>;

  explicit PlanningStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
      this->trajectory_valid = false;
      this->goal_reached = false;
      this->parking_entry_reached = false;
      this->obstacle_blocking = false;
      this->lane_lost = false;
      this->localization_degraded = false;
      this->active_waypoint_id = 0ul;
      this->distance_to_goal = 0.0f;
      this->planner_mode = 0;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit PlanningStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
      this->trajectory_valid = false;
      this->goal_reached = false;
      this->parking_entry_reached = false;
      this->obstacle_blocking = false;
      this->lane_lost = false;
      this->localization_degraded = false;
      this->active_waypoint_id = 0ul;
      this->distance_to_goal = 0.0f;
      this->planner_mode = 0;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _status_type =
    uint8_t;
  _status_type status;
  using _trajectory_valid_type =
    bool;
  _trajectory_valid_type trajectory_valid;
  using _goal_reached_type =
    bool;
  _goal_reached_type goal_reached;
  using _parking_entry_reached_type =
    bool;
  _parking_entry_reached_type parking_entry_reached;
  using _obstacle_blocking_type =
    bool;
  _obstacle_blocking_type obstacle_blocking;
  using _lane_lost_type =
    bool;
  _lane_lost_type lane_lost;
  using _localization_degraded_type =
    bool;
  _localization_degraded_type localization_degraded;
  using _active_waypoint_id_type =
    uint32_t;
  _active_waypoint_id_type active_waypoint_id;
  using _distance_to_goal_type =
    float;
  _distance_to_goal_type distance_to_goal;
  using _planner_mode_type =
    uint8_t;
  _planner_mode_type planner_mode;
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
  Type & set__status(
    const uint8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__trajectory_valid(
    const bool & _arg)
  {
    this->trajectory_valid = _arg;
    return *this;
  }
  Type & set__goal_reached(
    const bool & _arg)
  {
    this->goal_reached = _arg;
    return *this;
  }
  Type & set__parking_entry_reached(
    const bool & _arg)
  {
    this->parking_entry_reached = _arg;
    return *this;
  }
  Type & set__obstacle_blocking(
    const bool & _arg)
  {
    this->obstacle_blocking = _arg;
    return *this;
  }
  Type & set__lane_lost(
    const bool & _arg)
  {
    this->lane_lost = _arg;
    return *this;
  }
  Type & set__localization_degraded(
    const bool & _arg)
  {
    this->localization_degraded = _arg;
    return *this;
  }
  Type & set__active_waypoint_id(
    const uint32_t & _arg)
  {
    this->active_waypoint_id = _arg;
    return *this;
  }
  Type & set__distance_to_goal(
    const float & _arg)
  {
    this->distance_to_goal = _arg;
    return *this;
  }
  Type & set__planner_mode(
    const uint8_t & _arg)
  {
    this->planner_mode = _arg;
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
  static constexpr uint8_t STATUS_ACTIVE =
    0u;
  static constexpr uint8_t STATUS_WAITING_FSM =
    1u;
  static constexpr uint8_t STATUS_OBSTACLE_BLOCKED =
    2u;
  static constexpr uint8_t STATUS_LANE_LOST =
    3u;
  static constexpr uint8_t STATUS_LOCALIZATION_DEGRADED =
    4u;
  static constexpr uint8_t STATUS_EMERGENCY =
    5u;
  static constexpr uint8_t STATUS_MISSION_COMPLETE =
    6u;

  // pointer types
  using RawPtr =
    planning_msgs::msg::PlanningStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const planning_msgs::msg::PlanningStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::PlanningStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      planning_msgs::msg::PlanningStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__planning_msgs__msg__PlanningStatus
    std::shared_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__planning_msgs__msg__PlanningStatus
    std::shared_ptr<planning_msgs::msg::PlanningStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PlanningStatus_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    if (this->trajectory_valid != other.trajectory_valid) {
      return false;
    }
    if (this->goal_reached != other.goal_reached) {
      return false;
    }
    if (this->parking_entry_reached != other.parking_entry_reached) {
      return false;
    }
    if (this->obstacle_blocking != other.obstacle_blocking) {
      return false;
    }
    if (this->lane_lost != other.lane_lost) {
      return false;
    }
    if (this->localization_degraded != other.localization_degraded) {
      return false;
    }
    if (this->active_waypoint_id != other.active_waypoint_id) {
      return false;
    }
    if (this->distance_to_goal != other.distance_to_goal) {
      return false;
    }
    if (this->planner_mode != other.planner_mode) {
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
  bool operator!=(const PlanningStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PlanningStatus_

// alias to use template instance with default allocator
using PlanningStatus =
  planning_msgs::msg::PlanningStatus_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_ACTIVE;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_WAITING_FSM;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_OBSTACLE_BLOCKED;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_LANE_LOST;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_LOCALIZATION_DEGRADED;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_EMERGENCY;
template<typename ContainerAllocator>
constexpr uint8_t PlanningStatus_<ContainerAllocator>::STATUS_MISSION_COMPLETE;

}  // namespace msg

}  // namespace planning_msgs

#endif  // PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_HPP_
