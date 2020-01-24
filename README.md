# robosys2019_security_cameara_ros  

## Description  
Software for security camera with gmail notification human detection using darknet/yolo.  
A small project from Robot System Lecture.  

## Demo  
[Security camera with gmail notification](https://www.youtube.com/watch?v=pFAk4SXtzgE)  

## System Environment  
|||
|:--:|:--:|
|OS|Ubuntu 18.04|
|ROS|Melodic|
|GPU|GTX 1060|
|Camera|Logitech C270|

## Requirements  
- [ROS](http://wiki.ros.org/ROS/Installation)  
- [usb_cam ROS](http://wiki.ros.org/usb_cam)
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
- Enable [less secure apps to access Gmail](https://hotter.io/docs/email-accounts/secure-app-gmail/) in Sender Google account  
- Next, access and edit Sender and Receiver gmail accounts
```bash
$ cd ~/catkin_ws/src/robosys2019_security_camera_ros/security_camera/scripts
$ gedit gmail_sender.py
```
- Replace `sender@gmail.com`, `sender password`, `receiver@gmail.com` with your Sender and Receiver gmail accounts  
 
 ## Usage
 Run the following command
 ```bash
 $ roslaunch security_camera security_camera.launch
 ```
 
 ## License
 This repository is licensed under the BSD3 license, see [LICENSE](./COPYING)  
 
 ## Reference
 - [Send email with python](https://qiita.com/nakasuke_/items/607cf74d8841f76e59c6)
