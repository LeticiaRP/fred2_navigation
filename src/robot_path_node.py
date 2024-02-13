#!/usr/bin/env python3

import rclpy
import threading

from typing import List, Optional

from rclpy.node import Node
from rclpy.context import Context 
from rclpy.parameter import Parameter

from rclpy.qos import QoSPresetProfiles, QoSProfile, QoSHistoryPolicy, QoSLivelinessPolicy, QoSReliabilityPolicy, QoSDurabilityPolicy

from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool

class RobotPathNode(Node):
    
    def __init__(self, 
                 node_name: str, 
                 *, # keyword-only argument
                 context: Context = None, 
                 cli_args: List[str] = None, 
                 namespace: str = None, 
                 use_global_arguments: bool = True, 
                 enable_rosout: bool = True, 
                 start_parameter_services: bool = True, 
                 parameter_overrides: List[Parameter] | None = None) -> None:
        
        
        super().__init__(node_name, 
                         context=context, 
                         cli_args=cli_args, 
                         namespace=namespace, 
                         use_global_arguments=use_global_arguments, 
                         enable_rosout=enable_rosout, 
                         start_parameter_services=start_parameter_services, 
                         parameter_overrides=parameter_overrides)
    
        # quality protocol -> the node must not lose any message 
        qos_profile = QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE, 
            durability= QoSDurabilityPolicy.VOLATILE,
            history=QoSHistoryPolicy.KEEP_LAST, 
            depth=10, 
            liveliness=QoSLivelinessPolicy.AUTOMATIC
            
        )

        self.get_logger().info('Odometry to Path Node is running')

        self.seq = 0
        self.path = Path()

        self.path_publisher = self.create_publisher(Path, 'robot/path', 10)

        self.odom_subscription = self.create_subscription(Odometry, '/odom', self.odometry_callback, qos_profile)
        self.reset_goals_subscription = self.create_subscription(Bool, '/odom/reset', self.reset_goals_callback, 10)



    def reset_goals_callback(self, msg):
        reset = msg.data
        if reset:
            self.path.poses.clear()
            self.seq = 0



    def odometry_callback(self, msg):
        pose_stamped = PoseStamped()
        pose_stamped.pose = msg.pose.pose

        pose_stamped.header.stamp = self.get_clock().now().to_msg()
        # pose_stamped.header.seq = self.seq
        # self.seq += 1

        self.path.poses.append(pose_stamped)

        # Publish the 'path' message
        self.path.header.stamp = self.get_clock().now().to_msg()
        self.path.header.frame_id = "odom"

        self.path_publisher.publish(self.path)




if __name__ == '__main__': 
        
    rclpy.init()

    node = RobotPathNode(
        node_name='robot_path_monitor',
        cli_args=['--debug'],
        namespace='navigation',
        enable_rosout=False)


    try: 
        while rclpy.ok(): 
            rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    rclpy.shutdown()
