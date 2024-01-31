import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='fred2_navigation').find('fred2_navigation')
    # default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')


    robot_localization_node = launch_ros.actions.Node(
       package='robot_localization',
       executable='ekf_node',
       name='ekf_filter_node',
       output='screen',
       parameters=[os.path.join(pkg_share, 'config/robot_localization_ekf.yaml'), {'use_sim_time': LaunchConfiguration('use_sim_time')}]
)

    # rviz_node = launch_ros.actions.Node(
    #     package='rviz2',
    #     executable='rviz2',
    #     name='rviz2',
    #     output='screen',
    #     # arguments=['-d', LaunchConfiguration('rvizconfig')],
    # )


    return launch.LaunchDescription([

        # launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
        #                                     description='Absolute path to rviz config file'),
        launch.actions.DeclareLaunchArgument(name='use_sim_time', default_value='True',
                                            description='Flag to enable use_sim_time'),

        robot_localization_node,
        # rviz_node
    ])