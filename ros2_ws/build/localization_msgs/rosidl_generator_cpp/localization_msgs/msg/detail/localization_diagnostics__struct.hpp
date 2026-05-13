// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from localization_msgs:msg/LocalizationDiagnostics.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_HPP_

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
# define DEPRECATED__localization_msgs__msg__LocalizationDiagnostics __attribute__((deprecated))
#else
# define DEPRECATED__localization_msgs__msg__LocalizationDiagnostics __declspec(deprecated)
#endif

namespace localization_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LocalizationDiagnostics_
{
  using Type = LocalizationDiagnostics_<ContainerAllocator>;

  explicit LocalizationDiagnostics_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->ekf_output_hz = 0.0;
      this->gps_input_hz = 0.0;
      this->imu_input_hz = 0.0;
      this->ndt_output_hz = 0.0;
      this->ekf_latency_ms = 0.0;
      this->ndt_latency_ms = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->ndt_quality = 0.0;
      this->ekf_healthy = false;
      this->gps_healthy = false;
      this->imu_healthy = false;
      this->ndt_healthy = false;
      this->map_odom_stable = false;
    }
  }

  explicit LocalizationDiagnostics_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->ekf_output_hz = 0.0;
      this->gps_input_hz = 0.0;
      this->imu_input_hz = 0.0;
      this->ndt_output_hz = 0.0;
      this->ekf_latency_ms = 0.0;
      this->ndt_latency_ms = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->ndt_quality = 0.0;
      this->ekf_healthy = false;
      this->gps_healthy = false;
      this->imu_healthy = false;
      this->ndt_healthy = false;
      this->map_odom_stable = false;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _age_ms_type =
    uint32_t;
  _age_ms_type age_ms;
  using _valid_until_ms_type =
    uint32_t;
  _valid_until_ms_type valid_until_ms;
  using _ekf_output_hz_type =
    double;
  _ekf_output_hz_type ekf_output_hz;
  using _gps_input_hz_type =
    double;
  _gps_input_hz_type gps_input_hz;
  using _imu_input_hz_type =
    double;
  _imu_input_hz_type imu_input_hz;
  using _ndt_output_hz_type =
    double;
  _ndt_output_hz_type ndt_output_hz;
  using _ekf_latency_ms_type =
    double;
  _ekf_latency_ms_type ekf_latency_ms;
  using _ndt_latency_ms_type =
    double;
  _ndt_latency_ms_type ndt_latency_ms;
  using _position_covariance_type =
    double;
  _position_covariance_type position_covariance;
  using _heading_covariance_type =
    double;
  _heading_covariance_type heading_covariance;
  using _ndt_quality_type =
    double;
  _ndt_quality_type ndt_quality;
  using _ekf_healthy_type =
    bool;
  _ekf_healthy_type ekf_healthy;
  using _gps_healthy_type =
    bool;
  _gps_healthy_type gps_healthy;
  using _imu_healthy_type =
    bool;
  _imu_healthy_type imu_healthy;
  using _ndt_healthy_type =
    bool;
  _ndt_healthy_type ndt_healthy;
  using _map_odom_stable_type =
    bool;
  _map_odom_stable_type map_odom_stable;
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
  Type & set__ekf_output_hz(
    const double & _arg)
  {
    this->ekf_output_hz = _arg;
    return *this;
  }
  Type & set__gps_input_hz(
    const double & _arg)
  {
    this->gps_input_hz = _arg;
    return *this;
  }
  Type & set__imu_input_hz(
    const double & _arg)
  {
    this->imu_input_hz = _arg;
    return *this;
  }
  Type & set__ndt_output_hz(
    const double & _arg)
  {
    this->ndt_output_hz = _arg;
    return *this;
  }
  Type & set__ekf_latency_ms(
    const double & _arg)
  {
    this->ekf_latency_ms = _arg;
    return *this;
  }
  Type & set__ndt_latency_ms(
    const double & _arg)
  {
    this->ndt_latency_ms = _arg;
    return *this;
  }
  Type & set__position_covariance(
    const double & _arg)
  {
    this->position_covariance = _arg;
    return *this;
  }
  Type & set__heading_covariance(
    const double & _arg)
  {
    this->heading_covariance = _arg;
    return *this;
  }
  Type & set__ndt_quality(
    const double & _arg)
  {
    this->ndt_quality = _arg;
    return *this;
  }
  Type & set__ekf_healthy(
    const bool & _arg)
  {
    this->ekf_healthy = _arg;
    return *this;
  }
  Type & set__gps_healthy(
    const bool & _arg)
  {
    this->gps_healthy = _arg;
    return *this;
  }
  Type & set__imu_healthy(
    const bool & _arg)
  {
    this->imu_healthy = _arg;
    return *this;
  }
  Type & set__ndt_healthy(
    const bool & _arg)
  {
    this->ndt_healthy = _arg;
    return *this;
  }
  Type & set__map_odom_stable(
    const bool & _arg)
  {
    this->map_odom_stable = _arg;
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
    localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> *;
  using ConstRawPtr =
    const localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__localization_msgs__msg__LocalizationDiagnostics
    std::shared_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__localization_msgs__msg__LocalizationDiagnostics
    std::shared_ptr<localization_msgs::msg::LocalizationDiagnostics_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LocalizationDiagnostics_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->age_ms != other.age_ms) {
      return false;
    }
    if (this->valid_until_ms != other.valid_until_ms) {
      return false;
    }
    if (this->ekf_output_hz != other.ekf_output_hz) {
      return false;
    }
    if (this->gps_input_hz != other.gps_input_hz) {
      return false;
    }
    if (this->imu_input_hz != other.imu_input_hz) {
      return false;
    }
    if (this->ndt_output_hz != other.ndt_output_hz) {
      return false;
    }
    if (this->ekf_latency_ms != other.ekf_latency_ms) {
      return false;
    }
    if (this->ndt_latency_ms != other.ndt_latency_ms) {
      return false;
    }
    if (this->position_covariance != other.position_covariance) {
      return false;
    }
    if (this->heading_covariance != other.heading_covariance) {
      return false;
    }
    if (this->ndt_quality != other.ndt_quality) {
      return false;
    }
    if (this->ekf_healthy != other.ekf_healthy) {
      return false;
    }
    if (this->gps_healthy != other.gps_healthy) {
      return false;
    }
    if (this->imu_healthy != other.imu_healthy) {
      return false;
    }
    if (this->ndt_healthy != other.ndt_healthy) {
      return false;
    }
    if (this->map_odom_stable != other.map_odom_stable) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const LocalizationDiagnostics_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LocalizationDiagnostics_

// alias to use template instance with default allocator
using LocalizationDiagnostics =
  localization_msgs::msg::LocalizationDiagnostics_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_DIAGNOSTICS__STRUCT_HPP_
