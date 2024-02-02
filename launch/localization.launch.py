import os
import launch
import launch_ros

from launch import LaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from launch.actions import TimerAction, LogInfo

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='fred2_navigation').find('fred2_navigation')
    # default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')


    robot_localization_node = launch_ros.actions.Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node',
       output='screen',
       parameters=[os.path.join(pkg_share, 'config/ekf_odom.yaml')]
)

    return LaunchDescription([

        TimerAction(period= 3.0, actions= [
            
            LogInfo(msg=' ######################### LAUNCHING ROBOT LOCALIZATION #################################### '), 
            robot_localization_node
        ])
    ])