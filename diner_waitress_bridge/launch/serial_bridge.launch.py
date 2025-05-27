# launch/serial_bridge.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import ThisLaunchFileDir
from os.path import join, dirname

def generate_launch_description():
    config = join(dirname(__file__), '..', 'config', 'serial_params.yaml')

    return LaunchDescription([
        Node(
            package='diner_waitress_bridge',
            executable='serial_bridge_node',
            name='serial_bridge',
            output='screen',
            parameters=[config]
        )
    ])
