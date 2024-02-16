import os 
import launch_ros

from ament_index_python import get_package_share_directory

from launch import LaunchDescription 
from launch.actions import IncludeLaunchDescription, TimerAction, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node


def generate_launch_description(): 

    rplidar = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('rplidar_ros'), 'launch'), 
                                       '/rplidar.launch.py'])
    )

    slam_toolbox = launch_ros.actions.Node(
        
        package='slam_toolbox',
        executable='localization_slam_toolbox_node',
        name='slam_toolbox_node',
        output='screen',
        parameters=[
            {'mode:' 'localization'},
            {'map_file_name': '/home/ubuntu/ros2_ws/src/fred2_navigation/maps/meiu'},
            {'map_update_interval': 1.5}, 
            {'map_start_pose': [5.0, 1.0, 0.0]},
            {'resolution': 0.05}, # 10 cm 
            {'max_laser_range': 12.0}, 
            {'stack_size_to_use': 40000000}, # value in bytes -> 40MB
            {'minimum_travel_distance': 0.10}, 
            {'minimum_travel_heading': 0.17},  # 10°  
              # Add your SLAM parameters here
        ],
    )


    return LaunchDescription([
        
        # TimerAction(period= 5.0, actions= [rplidar]),

        TimerAction(period= 5.0, actions= [slam_toolbox]),
        
    ])  
