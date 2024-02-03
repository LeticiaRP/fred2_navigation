# Fred Navigation
**note: Package for ROS 2 - C++/Python (CMake) based package**
The fred2_navigation package in ROS 2 is designed to provide essential tools for robot navigation. It includes the robot_localization node, which utilizes an Extended Kalman Filter (EKF) to fuse odometry data and sensor measurements for accurate localization.

## Installation

**Clone the repository into your ROS2 workspace:**

```
cd ros2_ws/src
git clone https://github.com/AMRFrederico/fred2_navigation.git
```

**Install Robot Localization package:**

```
sudo apt install ros-humble-robot-localization 
```


**Build the package:**

```
cd ros2_ws
colcon build
```

### Launch
To launch the robot_localization node, use the following command:

```
ros2 launch fred2_navigation localization.launch.py
```
## Robot Localization
The fred2_navigation package includes the robot_localization node, which is responsible for sensor fusion and localization using an Extended Kalman Filter (EKF).

### Parameters
The ekf_filter_node node is configured using the `ekf_odom.yaml` file found in the config directory of the fred2_navigation package.

