cmake_minimum_required(VERSION 3.8)
project(planning_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TrajectoryPoint.msg"
  "msg/Trajectory.msg"
  "msg/TargetSpeed.msg"
  "msg/PlanningStatus.msg"
  "msg/ActiveRouteContext.msg"
  "msg/GoalReached.msg"
  "msg/ParkComplete.msg"
  "msg/ControllerFeedback.msg"
  "msg/FSMRequest.msg"
  DEPENDENCIES
    std_msgs
    geometry_msgs
)

ament_export_dependencies(
  rosidl_default_runtime
  std_msgs
  geometry_msgs
)

ament_package()
