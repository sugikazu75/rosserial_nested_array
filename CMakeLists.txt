cmake_minimum_required(VERSION 3.0.2)
project(rosserial_nested_array)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rosserial_arduino
  rosserial_client
  rosserial_python
  trajectory_msgs
  )

add_message_files(FILES
  Point.msg
  Points.msg
)

generate_messages()

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

execute_process(
  COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh rospack find rosserial_arduino
  OUTPUT_VARIABLE ROSSERIAL_CLIENT_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
  )
if(NOT ROSSERIAL_CLIENT_DIR)
  message(FATAL_ERROR "rosserial_client not found")
endif()

set(ROSSERIAL_MAKE_LIB ${ROSSERIAL_CLIENT_DIR}/src/rosserial_arduino/make_libraries.py)
set(ROS_LIB_DIR ${PROJECT_SOURCE_DIR})

add_custom_target(generate_ros_lib ALL
  COMMAND ${CMAKE_COMMAND} -E make_directory ${ROS_LIB_DIR}
  COMMAND ${CATKIN_DEVEL_PREFIX}/env.sh
          ${PYTHON_EXECUTABLE} ${ROSSERIAL_MAKE_LIB} ${ROS_LIB_DIR}
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
  COMMENT "Generating ros_lib via ${ROSSERIAL_MAKE_LIB}"
  VERBATIM
  )
add_dependencies(generate_ros_lib ${catkin_EXPORTED_TARGETS} ${PROJECT_NAME}_generate_messages_cpp)
