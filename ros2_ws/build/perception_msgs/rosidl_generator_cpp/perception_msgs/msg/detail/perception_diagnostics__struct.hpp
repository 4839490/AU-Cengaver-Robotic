// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from perception_msgs:msg/PerceptionDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_HPP_
#define PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_HPP_

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
# define DEPRECATED__perception_msgs__msg__PerceptionDiagnostics __attribute__((deprecated))
#else
# define DEPRECATED__perception_msgs__msg__PerceptionDiagnostics __declspec(deprecated)
#endif

namespace perception_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PerceptionDiagnostics_
{
  using Type = PerceptionDiagnostics_<ContainerAllocator>;

  explicit PerceptionDiagnostics_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_name = "";
      this->input_hz = 0.0f;
      this->output_hz = 0.0f;
      this->latency_ms = 0.0f;
      this->last_msg_age_ms = 0ul;
      this->mean_confidence = 0.0f;
      this->num_outputs = 0ul;
      this->gpu_utilization = 0.0f;
    }
  }

  explicit PerceptionDiagnostics_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    node_name(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->node_name = "";
      this->input_hz = 0.0f;
      this->output_hz = 0.0f;
      this->latency_ms = 0.0f;
      this->last_msg_age_ms = 0ul;
      this->mean_confidence = 0.0f;
      this->num_outputs = 0ul;
      this->gpu_utilization = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _node_name_type =
    std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>;
  _node_name_type node_name;
  using _input_hz_type =
    float;
  _input_hz_type input_hz;
  using _output_hz_type =
    float;
  _output_hz_type output_hz;
  using _latency_ms_type =
    float;
  _latency_ms_type latency_ms;
  using _last_msg_age_ms_type =
    uint32_t;
  _last_msg_age_ms_type last_msg_age_ms;
  using _mean_confidence_type =
    float;
  _mean_confidence_type mean_confidence;
  using _num_outputs_type =
    uint32_t;
  _num_outputs_type num_outputs;
  using _gpu_utilization_type =
    float;
  _gpu_utilization_type gpu_utilization;
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
  Type & set__node_name(
    const std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other> & _arg)
  {
    this->node_name = _arg;
    return *this;
  }
  Type & set__input_hz(
    const float & _arg)
  {
    this->input_hz = _arg;
    return *this;
  }
  Type & set__output_hz(
    const float & _arg)
  {
    this->output_hz = _arg;
    return *this;
  }
  Type & set__latency_ms(
    const float & _arg)
  {
    this->latency_ms = _arg;
    return *this;
  }
  Type & set__last_msg_age_ms(
    const uint32_t & _arg)
  {
    this->last_msg_age_ms = _arg;
    return *this;
  }
  Type & set__mean_confidence(
    const float & _arg)
  {
    this->mean_confidence = _arg;
    return *this;
  }
  Type & set__num_outputs(
    const uint32_t & _arg)
  {
    this->num_outputs = _arg;
    return *this;
  }
  Type & set__gpu_utilization(
    const float & _arg)
  {
    this->gpu_utilization = _arg;
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
    perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> *;
  using ConstRawPtr =
    const perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__perception_msgs__msg__PerceptionDiagnostics
    std::shared_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__perception_msgs__msg__PerceptionDiagnostics
    std::shared_ptr<perception_msgs::msg::PerceptionDiagnostics_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PerceptionDiagnostics_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->node_name != other.node_name) {
      return false;
    }
    if (this->input_hz != other.input_hz) {
      return false;
    }
    if (this->output_hz != other.output_hz) {
      return false;
    }
    if (this->latency_ms != other.latency_ms) {
      return false;
    }
    if (this->last_msg_age_ms != other.last_msg_age_ms) {
      return false;
    }
    if (this->mean_confidence != other.mean_confidence) {
      return false;
    }
    if (this->num_outputs != other.num_outputs) {
      return false;
    }
    if (this->gpu_utilization != other.gpu_utilization) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const PerceptionDiagnostics_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PerceptionDiagnostics_

// alias to use template instance with default allocator
using PerceptionDiagnostics =
  perception_msgs::msg::PerceptionDiagnostics_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace perception_msgs

#endif  // PERCEPTION_MSGS__MSG__DETAIL__PERCEPTION_DIAGNOSTICS__STRUCT_HPP_
