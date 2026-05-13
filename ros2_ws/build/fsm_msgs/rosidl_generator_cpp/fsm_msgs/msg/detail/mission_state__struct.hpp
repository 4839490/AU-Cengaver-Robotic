// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fsm_msgs:msg/MissionState.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_HPP_
#define FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_HPP_

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
# define DEPRECATED__fsm_msgs__msg__MissionState __attribute__((deprecated))
#else
# define DEPRECATED__fsm_msgs__msg__MissionState __declspec(deprecated)
#endif

namespace fsm_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MissionState_
{
  using Type = MissionState_<ContainerAllocator>;

  explicit MissionState_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mission_active = false;
      this->total_waypoints = 0;
      this->completed_waypoints = 0;
      this->current_waypoint_id = 0ul;
      this->current_waypoint_type = 0;
      this->next_waypoint_id = 0ul;
      this->next_waypoint_type = 0;
      this->pickup_complete = false;
      this->dropoff_complete = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  explicit MissionState_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->mission_active = false;
      this->total_waypoints = 0;
      this->completed_waypoints = 0;
      this->current_waypoint_id = 0ul;
      this->current_waypoint_type = 0;
      this->next_waypoint_id = 0ul;
      this->next_waypoint_type = 0;
      this->pickup_complete = false;
      this->dropoff_complete = false;
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _mission_active_type =
    bool;
  _mission_active_type mission_active;
  using _total_waypoints_type =
    uint8_t;
  _total_waypoints_type total_waypoints;
  using _completed_waypoints_type =
    uint8_t;
  _completed_waypoints_type completed_waypoints;
  using _current_waypoint_id_type =
    uint32_t;
  _current_waypoint_id_type current_waypoint_id;
  using _current_waypoint_type_type =
    uint8_t;
  _current_waypoint_type_type current_waypoint_type;
  using _next_waypoint_id_type =
    uint32_t;
  _next_waypoint_id_type next_waypoint_id;
  using _next_waypoint_type_type =
    uint8_t;
  _next_waypoint_type_type next_waypoint_type;
  using _pickup_complete_type =
    bool;
  _pickup_complete_type pickup_complete;
  using _dropoff_complete_type =
    bool;
  _dropoff_complete_type dropoff_complete;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__mission_active(
    const bool & _arg)
  {
    this->mission_active = _arg;
    return *this;
  }
  Type & set__total_waypoints(
    const uint8_t & _arg)
  {
    this->total_waypoints = _arg;
    return *this;
  }
  Type & set__completed_waypoints(
    const uint8_t & _arg)
  {
    this->completed_waypoints = _arg;
    return *this;
  }
  Type & set__current_waypoint_id(
    const uint32_t & _arg)
  {
    this->current_waypoint_id = _arg;
    return *this;
  }
  Type & set__current_waypoint_type(
    const uint8_t & _arg)
  {
    this->current_waypoint_type = _arg;
    return *this;
  }
  Type & set__next_waypoint_id(
    const uint32_t & _arg)
  {
    this->next_waypoint_id = _arg;
    return *this;
  }
  Type & set__next_waypoint_type(
    const uint8_t & _arg)
  {
    this->next_waypoint_type = _arg;
    return *this;
  }
  Type & set__pickup_complete(
    const bool & _arg)
  {
    this->pickup_complete = _arg;
    return *this;
  }
  Type & set__dropoff_complete(
    const bool & _arg)
  {
    this->dropoff_complete = _arg;
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

  // constant declarations
  static constexpr uint8_t PICKUP =
    0u;
  static constexpr uint8_t DROPOFF =
    1u;
  static constexpr uint8_t WAYPOINT =
    2u;
  static constexpr uint8_t PARK_ENTRY =
    3u;

  // pointer types
  using RawPtr =
    fsm_msgs::msg::MissionState_<ContainerAllocator> *;
  using ConstRawPtr =
    const fsm_msgs::msg::MissionState_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::MissionState_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::MissionState_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fsm_msgs__msg__MissionState
    std::shared_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fsm_msgs__msg__MissionState
    std::shared_ptr<fsm_msgs::msg::MissionState_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MissionState_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->mission_active != other.mission_active) {
      return false;
    }
    if (this->total_waypoints != other.total_waypoints) {
      return false;
    }
    if (this->completed_waypoints != other.completed_waypoints) {
      return false;
    }
    if (this->current_waypoint_id != other.current_waypoint_id) {
      return false;
    }
    if (this->current_waypoint_type != other.current_waypoint_type) {
      return false;
    }
    if (this->next_waypoint_id != other.next_waypoint_id) {
      return false;
    }
    if (this->next_waypoint_type != other.next_waypoint_type) {
      return false;
    }
    if (this->pickup_complete != other.pickup_complete) {
      return false;
    }
    if (this->dropoff_complete != other.dropoff_complete) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    return true;
  }
  bool operator!=(const MissionState_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MissionState_

// alias to use template instance with default allocator
using MissionState =
  fsm_msgs::msg::MissionState_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t MissionState_<ContainerAllocator>::PICKUP;
template<typename ContainerAllocator>
constexpr uint8_t MissionState_<ContainerAllocator>::DROPOFF;
template<typename ContainerAllocator>
constexpr uint8_t MissionState_<ContainerAllocator>::WAYPOINT;
template<typename ContainerAllocator>
constexpr uint8_t MissionState_<ContainerAllocator>::PARK_ENTRY;

}  // namespace msg

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__MISSION_STATE__STRUCT_HPP_
