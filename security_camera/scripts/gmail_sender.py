#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.utils import formatdate

from_addr = 'sender@gmail.com'
addr_password = 'sender password'
to_addr = 'receiver@gmail.com'
bcc = ''
subject = 'Human detected'
content = 'A person has been detected in front of the camera'


def create_msg_with_image(from_addr, to_addr, bcc_addrs, subject, content):
    # Read file as binary
    with open("human_detected.png",'rb') as img_file: # can also do with file(filename, 'rb')
        img_data = img_file.read()

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    text = MIMEText(content)
    msg.attach(text)
    #image = MIMEImage(img_data, _subtype="jpeg")#, name=os.path.basename('./ononoki.jpeg'))
    image = MIMEImage(img_data)#, _subtype="jpeg")
    msg.attach(image)

    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(from_addr, addr_password)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


def callback(msg):
    msg = create_msg_with_image(from_addr, to_addr, bcc, subject, content)
    send(from_addr, to_addr, msg)
    rospy.loginfo("Email sended")


if __name__ == '__main__':
    rospy.init_node("EmailSender")
    sub = rospy.Subscriber("human_detected_notification", String, callback, queue_size=10)
    rospy.spin()
