cmake_minimum_required(VERSION 3.8)
project(localization_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/LocalizationPose.msg"
  "msg/LocalizationOdometry.msg"
  "msg/LocalizationStatus.msg"
  "msg/LocalizationDiagnostics.msg"
  "msg/MapOrigin.msg"
  "msg/RawGps.msg"
  DEPENDENCIES std_msgs
)

ament_export_dependencies(rosidl_default_runtime)
ament_package()