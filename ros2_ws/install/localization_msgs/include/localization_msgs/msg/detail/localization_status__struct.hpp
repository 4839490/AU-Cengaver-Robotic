// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from localization_msgs:msg/LocalizationStatus.idl
// generated code does not contain a copyright notice

#ifndef LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_HPP_
#define LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_HPP_

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
# define DEPRECATED__localization_msgs__msg__LocalizationStatus __attribute__((deprecated))
#else
# define DEPRECATED__localization_msgs__msg__LocalizationStatus __declspec(deprecated)
#endif

namespace localization_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LocalizationStatus_
{
  using Type = LocalizationStatus_<ContainerAllocator>;

  explicit LocalizationStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->status = 0;
      this->localization_confidence = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->ndt_healthy = false;
      this->ndt_quality = 0.0;
      this->map_odom_stable = false;
      this->map_odom_drift = 0.0;
      this->gps_available = false;
      this->imu_available = false;
      this->lidar_available = false;
    }
  }

  explicit LocalizationStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->age_ms = 0ul;
      this->valid_until_ms = 0ul;
      this->status = 0;
      this->localization_confidence = 0.0;
      this->position_covariance = 0.0;
      this->heading_covariance = 0.0;
      this->ndt_healthy = false;
      this->ndt_quality = 0.0;
      this->map_odom_stable = false;
      this->map_odom_drift = 0.0;
      this->gps_available = false;
      this->imu_available = false;
      this->lidar_available = false;
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
  using _status_type =
    uint8_t;
  _status_type status;
  using _localization_confidence_type =
    double;
  _localization_confidence_type localization_confidence;
  using _position_covariance_type =
    double;
  _position_covariance_type position_covariance;
  using _heading_covariance_type =
    double;
  _heading_covariance_type heading_covariance;
  using _ndt_healthy_type =
    bool;
  _ndt_healthy_type ndt_healthy;
  using _ndt_quality_type =
    double;
  _ndt_quality_type ndt_quality;
  using _map_odom_stable_type =
    bool;
  _map_odom_stable_type map_odom_stable;
  using _map_odom_drift_type =
    double;
  _map_odom_drift_type map_odom_drift;
  using _gps_available_type =
    bool;
  _gps_available_type gps_available;
  using _imu_available_type =
    bool;
  _imu_available_type imu_available;
  using _lidar_available_type =
    bool;
  _lidar_available_type lidar_available;
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
  Type & set__status(
    const uint8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__localization_confidence(
    const double & _arg)
  {
    this->localization_confidence = _arg;
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
  Type & set__ndt_healthy(
    const bool & _arg)
  {
    this->ndt_healthy = _arg;
    return *this;
  }
  Type & set__ndt_quality(
    const double & _arg)
  {
    this->ndt_quality = _arg;
    return *this;
  }
  Type & set__map_odom_stable(
    const bool & _arg)
  {
    this->map_odom_stable = _arg;
    return *this;
  }
  Type & set__map_odom_drift(
    const double & _arg)
  {
    this->map_odom_drift = _arg;
    return *this;
  }
  Type & set__gps_available(
    const bool & _arg)
  {
    this->gps_available = _arg;
    return *this;
  }
  Type & set__imu_available(
    const bool & _arg)
  {
    this->imu_available = _arg;
    return *this;
  }
  Type & set__lidar_available(
    const bool & _arg)
  {
    this->lidar_available = _arg;
    return *this;
  }
  Type & set__warning_flags(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>, typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other>>::other> & _arg)
  {
    this->warning_flags = _arg;
    return *this;
  }

  // constant declarations
  static constexpr uint8_t OK =
    0u;
  static constexpr uint8_t GNSS_LOST =
    1u;
  static constexpr uint8_t IMU_ONLY =
    2u;
  static constexpr uint8_t LIDAR_ONLY =
    3u;
  static constexpr uint8_t DEGRADED =
    4u;
  static constexpr uint8_t RELOCALIZING =
    5u;
  static constexpr uint8_t LOST =
    6u;

  // pointer types
  using RawPtr =
    localization_msgs::msg::LocalizationStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const localization_msgs::msg::LocalizationStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      localization_msgs::msg::LocalizationStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__localization_msgs__msg__LocalizationStatus
    std::shared_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__localization_msgs__msg__LocalizationStatus
    std::shared_ptr<localization_msgs::msg::LocalizationStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LocalizationStatus_ & other) const
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
    if (this->status != other.status) {
      return false;
    }
    if (this->localization_confidence != other.localization_confidence) {
      return false;
    }
    if (this->position_covariance != other.position_covariance) {
      return false;
    }
    if (this->heading_covariance != other.heading_covariance) {
      return false;
    }
    if (this->ndt_healthy != other.ndt_healthy) {
      return false;
    }
    if (this->ndt_quality != other.ndt_quality) {
      return false;
    }
    if (this->map_odom_stable != other.map_odom_stable) {
      return false;
    }
    if (this->map_odom_drift != other.map_odom_drift) {
      return false;
    }
    if (this->gps_available != other.gps_available) {
      return false;
    }
    if (this->imu_available != other.imu_available) {
      return false;
    }
    if (this->lidar_available != other.lidar_available) {
      return false;
    }
    if (this->warning_flags != other.warning_flags) {
      return false;
    }
    return true;
  }
  bool operator!=(const LocalizationStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LocalizationStatus_

// alias to use template instance with default allocator
using LocalizationStatus =
  localization_msgs::msg::LocalizationStatus_<std::allocator<void>>;

// constant definitions
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::OK;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::GNSS_LOST;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::IMU_ONLY;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::LIDAR_ONLY;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::DEGRADED;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::RELOCALIZING;
template<typename ContainerAllocator>
constexpr uint8_t LocalizationStatus_<ContainerAllocator>::LOST;

}  // namespace msg

}  // namespace localization_msgs

#endif  // LOCALIZATION_MSGS__MSG__DETAIL__LOCALIZATION_STATUS__STRUCT_HPP_
