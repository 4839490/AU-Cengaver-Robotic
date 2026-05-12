cmake_minimum_required(VERSION 3.8)
project(perception_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/LaneModel.msg"
  "msg/TrafficLightState.msg"
  "msg/TrafficSign.msg"
  "msg/TrafficSigns.msg"
  "msg/ObstacleTrack.msg"
  "msg/ObstacleTracks.msg"
  "msg/StopTarget.msg"
  "msg/PerceptionDiagnostics.msg"
  DEPENDENCIES std_msgs
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()
