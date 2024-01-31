instalar robot localization package: 

sudo apt install ros-humble-robot-localization




instalar slam toolbox
sudo apt install ros-humble-slam-toolbox



The thing is, as you may know, ROS2 is based on DDS for the middleware. There are different DDS implementations, the default one (as for now) being Fast DDS.

Due to some issues with Fast DDS and Navigation in ROS2, it has been recommended to use Cyclone DDS instead. So, we need to tell ROS2 to use a different DDS.

