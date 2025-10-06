# rosserial_nested_array
This repository provides Arduino firmware to check rosserial communication with array of array message.  
With original repository (https://github.com/ros-drivers/rosserial), deserialization of message is incorrect and wrong message is received in microcomputer.  
This problem is solved in https://github.com/sugikazu75/rosserial/tree/PR/rosserial_client/library/nested_array. [[Pull Request](https://github.com/ros-drivers/rosserial/pull/633)]

# Prerequisite
Please install Arduino IDE on Ubuntu machine.

# Test
## 1. Test with original rosserial
```
source /opt/ros/${ROS_DISTRO}/setup.bash
mkdir -p ~/ros/rosserial_test_ws/src
cd ~/ros/rosserial_test_ws/src
git clone https://github.com/sugikazu75/rosserial_nested_array.git
git clone https://github.com/sugikazu75/rosserial.git
cd ~/ros/rosserial_test_ws
catkin build
cp -rf ~/ros/rosserial_test_ws/src/rosserial_nested_array/ros_lib ~/Arduino/libraries
source ~/ros/rosserial_test_ws/devel/setup.bash
```
Write `~/ros/rosserial_test_ws/src/rosserial_nested_array/firmware/nested_array_test/nested_array_test.ino` to Arduino Uno. 
```
roscore
```
```
rosrun rosserial_python serial_node.py 
```
```
rostopic echo /publisher # This is from Arduino
```
```
rostopic echo /subscriber # This is to Arduino
```
```
rosrun rosserial_nested_array test_node.py
```
Arduino publishes received message from `/subscriber` to `/publisher`, however, they are different.

## 2. Test with patched rosserial
```
roscd rosserial
git checkout -b PR/rosserial_client/library/nested_array origin/PR/rosserial_client/library/nested_array # assume origin is set https://github.com/sugikazu75/rosserial.git
catkin build
cp -rf ~/ros/rosserial_test_ws/src/rosserial_nested_array/ros_lib ~/Arduino/libraries
```
Please repeat the same process and check whether same message is returned from Arduino.