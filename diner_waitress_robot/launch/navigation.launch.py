from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

import os

def generate_launch_description():
    # Konfigurasi Path
    pkg_share = FindPackageShare('diner_waitress_robot')
    
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    map_yaml_file = LaunchConfiguration('map', default=PathJoinSubstitution([pkg_share, 'maps', 'map.yaml']))
    params_file = LaunchConfiguration('params_file', default=PathJoinSubstitution([pkg_share, 'config', 'nav2_params.yaml']))

    # Include launch file robot_state_publisher
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([pkg_share, 'launch', 'rsp.launch.py'])),
        launch_arguments={'use_sim_time': use_sim_time}.items()
    )

    # Include RPLiDAR
    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([pkg_share, 'launch', 'rplidar.launch.py']))
    )

    # Node SLAM Toolbox
    slam_toolbox_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[params_file],
        remappings=[('/scan', 'scan')]
    )

    # Launch Navigasi Nav2
    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution([pkg_share, 'launch', 'online_async_launch.py'])),
        launch_arguments={
            'map': map_yaml_file,
            'use_sim_time': use_sim_time,
            'params_file': params_file
        }.items()
    )

    # Launch RViz
    rviz_config = PathJoinSubstitution([pkg_share, 'rviz', 'view_waitress.rviz'])
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    return LaunchDescription([
        robot_state_publisher,
        lidar_launch,
        slam_toolbox_node,
        nav2_launch,
        rviz_node
    ])
