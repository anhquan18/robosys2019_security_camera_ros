# robosys2019_security_cameara_ros  

## Description  
Software for security camera with human detection using darknet/yolo and gmail notification.  
A small project from Robot System Lecture.  

## Demo  
[Security camera with gmail notification](https://www.youtube.com/watch?v=pFAk4SXtzgE)

## Requirements  
- [ROS](http://wiki.ros.org/ROS/Installation)  
- [Darknet/Yolo ROS](https://github.com/leggedrobotics/darknet_ros)  
- Python 2.7  
- USB camera  

## Installation  
- Install this repository with `git`
```bash
$ cd ~/catkin_ws/src  
$ git clone https://github.com/anhquan18/robosys2019_security_camera_ros.git
```
- Build package using `catkin_make`
```bash
$ cd ~/catkin_ws && catkin_make
$ source ~/catkin_ws/devel/set_up.bash
```

 
 ## Usage
 Run the following command
 ```
 $ ./marble_machine_cover.py
 ```
 
 ## License
 This repository is licensed under the GPLv3 license, see [LICENSE](./COPYING)
