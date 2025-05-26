from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Directories
    pkg_dir = get_package_share_directory('diner_waitress_robot')

    # Launch Configs
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        # --- Arguments ---
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation clock'
        ),

        # --- Launch RSP (robot_state_publisher + URDF) ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_dir, 'launch', 'rsp.launch.py')
            ),
            launch_arguments={'use_sim_time': use_sim_time}.items()
        ),

        # --- Launch LiDAR (rplidar_ros) ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_dir, 'launch', 'rplidar.launch.py')
            ),
            launch_arguments={'use_sim_time': use_sim_time}.items()
        ),

        # --- Launch SLAM Toolbox ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_dir, 'launch', 'slam_toolbox.launch.py')
            ),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'slam_params_file': os.path.join(pkg_dir, 'config', 'mapper_params_online_async.yaml')
            }.items()
        ),

        # --- Launch Navigation2 (Nav2 stack) ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_dir, 'launch', 'navigation.launch.py')
            ),
            launch_arguments={
                'use_sim_time': use_sim_time,
                'params_file': os.path.join(pkg_dir, 'config', 'nav2_params.yaml')
            }.items()
        ),

        # --- Launch RViz (optional) ---
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_dir, 'launch', 'view_waitress.launch.py')
            ),
            launch_arguments={'use_sim_time': use_sim_time}.items()
        ),
    ])
