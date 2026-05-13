// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from planning_msgs:msg/PlanningStatus.idl
// generated code does not contain a copyright notice

#ifndef PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_H_
#define PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'STATUS_ACTIVE'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_ACTIVE = 0
};

/// Constant 'STATUS_WAITING_FSM'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_WAITING_FSM = 1
};

/// Constant 'STATUS_OBSTACLE_BLOCKED'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_OBSTACLE_BLOCKED = 2
};

/// Constant 'STATUS_LANE_LOST'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_LANE_LOST = 3
};

/// Constant 'STATUS_LOCALIZATION_DEGRADED'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_LOCALIZATION_DEGRADED = 4
};

/// Constant 'STATUS_EMERGENCY'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_EMERGENCY = 5
};

/// Constant 'STATUS_MISSION_COMPLETE'.
enum
{
  planning_msgs__msg__PlanningStatus__STATUS_MISSION_COMPLETE = 6
};

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"
// Member 'warning_flags'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/PlanningStatus in the package planning_msgs.
typedef struct planning_msgs__msg__PlanningStatus
{
  std_msgs__msg__Header header;
  uint8_t status;
  bool trajectory_valid;
  bool goal_reached;
  bool parking_entry_reached;
  bool obstacle_blocking;
  bool lane_lost;
  bool localization_degraded;
  uint32_t active_waypoint_id;
  float distance_to_goal;
  uint8_t planner_mode;
  uint32_t age_ms;
  uint32_t valid_until_ms;
  rosidl_runtime_c__String__Sequence warning_flags;
} planning_msgs__msg__PlanningStatus;

// Struct for a sequence of planning_msgs__msg__PlanningStatus.
typedef struct planning_msgs__msg__PlanningStatus__Sequence
{
  planning_msgs__msg__PlanningStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} planning_msgs__msg__PlanningStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PLANNING_MSGS__MSG__DETAIL__PLANNING_STATUS__STRUCT_H_
