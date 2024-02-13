import os
import launch
import launch_ros

from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import TimerAction, LogInfo

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='fred2_navigation').find('fred2_navigation')
    # default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')


    robot_path = launch_ros.actions.Node(
       package='fred2_navigation',
       executable='robot_path_node.py',
       name='robot_path_monitor',
       output='screen',
)

    return LaunchDescription([

        TimerAction(period= 3.0, actions= [
            
            LogInfo(msg=' ######################### LAUNCHING PATH MONITOR #################################### '), 
            robot_path
        ])
    ])