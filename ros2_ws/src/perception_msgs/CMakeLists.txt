cmake_minimum_required(VERSION 3.5)
project(perception_msgs)

if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

set(msg_files
  "msg/LaneModel.msg"
  "msg/TrafficLightState.msg"
  "msg/TrafficSign.msg"
  "msg/TrafficSigns.msg"
  "msg/ObstacleTrack.msg"
  "msg/ObstacleTracks.msg"
  "msg/StopTarget.msg"
  "msg/Junction.msg"
  "msg/PerceptionDiagnostics.msg"
)

rosidl_generate_interfaces(${PROJECT_NAME}
  ${msg_files}
  DEPENDENCIES std_msgs geometry_msgs
)

ament_export_dependencies(rosidl_default_runtime std_msgs geometry_msgs)

ament_package()
