// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from fsm_msgs:msg/FSMEvent.idl
// generated code does not contain a copyright notice

#ifndef FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_HPP_
#define FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_HPP_

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
# define DEPRECATED__fsm_msgs__msg__FSMEvent __attribute__((deprecated))
#else
# define DEPRECATED__fsm_msgs__msg__FSMEvent __declspec(deprecated)
#endif

namespace fsm_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FSMEvent_
{
  using Type = FSMEvent_<ContainerAllocator>;

  explicit FSMEvent_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->event_type = 0;
      this->waypoint_id = 0ul;
      this->data = "";
      this->age_ms = 0ul;
    }
  }

  explicit FSMEvent_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    data(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->event_type = 0;
      this->waypoint_id = 0ul;
      this->data = "";
      this->age_ms = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _event_type_type =
    uint8_t;
  _event_type_type event_type;
  using _waypoint_id_type =
    uint32_t;
  _waypoint_id_type waypoint_id;
  using _data_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _data_type data;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__event_type(
    const uint8_t & _arg)
  {
    this->event_type = _arg;
    return *this;
  }
  Type & set__waypoint_id(
    const uint32_t & _arg)
  {
    this->waypoint_id = _arg;
    return *this;
  }
  Type & set__data(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->data = _arg;
    return *this;
  }
  Type & set__age_ms(
    const uint32_t & _arg)
  {
    this->age_ms = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t PICKUP_COMPLETE =
    0u;
  static constexpr uint8_t DROPOFF_COMPLETE =
    1u;
  static constexpr uint8_t OBSTACLE_CLEARED =
    2u;
  static constexpr uint8_t REPLANNING_REQUEST =
    3u;
  static constexpr uint8_t MISSION_ABORT =
    4u;
  static constexpr uint8_t RESUME =
    5u;
  static constexpr uint8_t PARK_SLOT_CHANGE =
    6u;
  static constexpr uint8_t EMERGENCY_STOP_REQUEST =
    7u;

  // pointer types
  using RawPtr =
    fsm_msgs::msg::FSMEvent_<ContainerAllocator> *;
  using ConstRawPtr =
    const fsm_msgs::msg::FSMEvent_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::FSMEvent_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      fsm_msgs::msg::FSMEvent_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__fsm_msgs__msg__FSMEvent
    std::shared_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__fsm_msgs__msg__FSMEvent
    std::shared_ptr<fsm_msgs::msg::FSMEvent_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FSMEvent_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->event_type != other.event_type) {
      return false;
    }
    if (this->waypoint_id != other.waypoint_id) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    return true;
  }
  bool operator!=(const FSMEvent_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FSMEvent_

// alias to use template instance with default allocator
using FSMEvent =
  fsm_msgs::msg::FSMEvent_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::PICKUP_COMPLETE;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::DROPOFF_COMPLETE;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::OBSTACLE_CLEARED;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::REPLANNING_REQUEST;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::MISSION_ABORT;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::RESUME;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::PARK_SLOT_CHANGE;
template<typename ContainerAllocator>
constexpr uint8_t FSMEvent_<ContainerAllocator>::EMERGENCY_STOP_REQUEST;

}  // namespace msg

}  // namespace fsm_msgs

#endif  // FSM_MSGS__MSG__DETAIL__FSM_EVENT__STRUCT_HPP_
