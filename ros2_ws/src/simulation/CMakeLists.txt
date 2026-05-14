cmake_minimum_required(VERSION 3.5)
project(simulation)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  urdf
  worlds
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
