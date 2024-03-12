from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource


import os

def generate_launch_description():
    # Define paths to files
    pkg_dir = get_package_share_directory('fred2_navigation')
    config_dir = os.path.join(pkg_dir, 'config')
    map_dir = os.path.join(pkg_dir, 'maps')
    amcl_config = os.path.join(config_dir, 'amcl.yaml')
    map_file = os.path.join(map_dir, 'iron-day2.yaml')

    rplidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('rplidar_ros'), 'launch'), 
                                       '/rplidar.launch.py'])
    )

    return LaunchDescription([
        TimerAction(period= 5.0, actions= [rplidar]),
        # Map Server Node
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'yaml_filename': map_file}],
        ),

        # AMCL Node
        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[amcl_config],
        ),

        # Add other navigation nodes here as needed

        # Lifecycle Manager Node
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[
                {'autostart': True},
                {'node_names': ['map_server', 'amcl']}
                # Add other node names as needed
            ],
        )
        # TimerAction(period= 5.0, actions= [rplidar]),


        
    ])
