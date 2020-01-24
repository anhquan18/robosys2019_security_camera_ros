#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image, CameraInfo
from darknet_ros_msgs.msg import BoundingBoxes, BoundingBox
from std_msgs.msg import String
from cv_bridge import CvBridge
import numpy as np
import cv2


class SecurityCenter(object):
    def __init__(self):
        self.pub = rospy.Publisher("human_detected_notification", String, queue_size=10)
        self.detector_sub = rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, self.human_detector_callback)
        self.raw_img_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.img_receiver_callback, queue_size=10)

        self.img = Image()
        self.bridge = CvBridge()
        self.last_detected = 0.0

    def img_receiver_callback(self, img):
        self.img = img

    def human_detector_callback(self, detection_data):
        if rospy.get_rostime().secs - self.last_detected <= 50.0:
            return

        try:
            detected_img = self.bridge.imgmsg_to_cv2(self.img, desired_encoding='bgr8')
        except:
            pass

        for obj in detection_data.bounding_boxes:
            if obj.Class == "person" and obj.probability >= 0.7:
                rospy.loginfo("HUMAN DETECTED")
                cv2.imwrite("./human_detected.png", detected_img)
                self.pub.publish("detected") 
                self.last_detected = rospy.get_rostime().secs


if __name__ == "__main__":
    rospy.init_node("SecurityCenter")
    sec = SecurityCenter()
    rospy.spin()
