cmake_minimum_required(VERSION 3.8)
project(diner_waitress_robot)

# Gunakan ament_cmake sebagai build system
find_package(ament_cmake REQUIRED)

# Dependencies untuk runtime
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(robot_state_publisher REQUIRED)
find_package(joint_state_publisher REQUIRED)
find_package(joint_state_publisher_gui REQUIRED)
find_package(xacro REQUIRED)
find_package(slam_toolbox REQUIRED)
find_package(nav2_bringup REQUIRED)
find_package(rviz2 REQUIRED)
find_package(launch REQUIRED)
find_package(launch_ros REQUIRED)

# Install direktori penting
install(
  DIRECTORY
    launch
    config
    description
  DESTINATION share/${PROJECT_NAME}
)

# Export ke sistem ROS 2
ament_package()
