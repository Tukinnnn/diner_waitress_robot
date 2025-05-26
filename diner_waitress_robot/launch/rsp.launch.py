from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    urdf_file = LaunchConfiguration('urdf_file')

    declare_use_sim_time = DeclareLaunchArgument(
        'use_sim_time', default_value='false', description='Use simulation clock if true'
    )

    declare_urdf_file = DeclareLaunchArgument(
        'urdf_file',
        default_value='urdf/waitress.urdf',
        description='Full path to robot URDF file to load'
    )

    return LaunchDescription([
        declare_use_sim_time,
        declare_urdf_file,

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}],
            arguments=[urdf_file]
        )
    ])
