cmake_minimum_required(VERSION 3.8)
project(custom_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(action_msgs REQUIRED)
find_package(unique_identifier_msgs REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_cpplint_FOUND TRUE)
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

# Add custom service and action
rosidl_generate_interfaces(${PROJECT_NAME}
  "interfaces/srv/CheckStock.srv"
  "interfaces/action/DeliverItem.action"
  DEPENDENCIES action_msgs unique_identifier_msgs
)

# Install rosidl files
install(
  DIRECTORY interfaces/srv interfaces/action
  DESTINATION share/${PROJECT_NAME}/interfaces
)

ament_package()

