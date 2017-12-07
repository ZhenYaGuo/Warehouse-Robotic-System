#!/usr/bin/env python

import rospy

from std_msgs.msg import String,Empty

from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose
from std_msgs.msg import Header


import tf
import tf2_ros
from geometry_msgs.msg import PoseWithCovariance
from geometry_msgs.msg import PoseWithCovarianceStamped
import numpy as np
import scipy as sp
from scipy import linalg


def ar2turtle():

    rospy.init_node('endpoint_tf_listener', anonymous=True)
    ar_tag_lib=['ar_marker_9','ar_marker_15']
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        for i in range(0, 2):
            try:
                tf_listener=tf.TransformListener()
                tf_listener.waitForTransform(ar_tag_lib[i],'base_link', rospy.Time(0),rospy.Duration(1))
                return i
            except (tf2_ros.TransformException):
                print("No ar_tag detected")
                continue
            rate.sleep()

	


if __name__ == '__main__':
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10,latch = True)
    flag_list=[1,1]
    while (not rospy.is_shutdown()):
        k= ar2turtle()

        if (flag_list[k] == 0):
            continue;
        flag=0
        r = rospy.Rate(10)
        while (k==0) :
            px = 0.0
            py = 0.0
            pz = 0.18
            qx=float(0.0)
            qy=float(0.0)
            qz=float(0.999855339248)
            qw=float(0.0170088381907)
            seq = 1
            stamp = rospy.get_rostime()     
            frame_id = "ar_marker_9"
            point = Point(px,py,pz)
            quat = Quaternion(qx,qy,qz,qw)
            pose = Pose(point, quat)
            header = Header(seq,stamp,frame_id)
            msg = PoseStamped(header, pose)
            pub.publish(msg)
            flag = flag + 1
            r.sleep()
            if flag>2 :
                break

        # if (flag_list[k] == 0):
        #     continue;
        # flag=0

        # r = rospy.Rate(10)
        # while (k==1) :
        #     px = 0.0
        #     py = 0.0
        #     pz = 2.3
        #     qx=float(0.0)
        #     qy=float(0.0)
        #     qz=float(2.274)
        #     qw=float(-0.024)
        #     seq = 1
        #     stamp = rospy.get_rostime()     
        #     frame_id = "ar_marker_15"
        #     point = Point(px,py,pz)
        #     quat = Quaternion(qx,qy,qz,qw)
        #     pose = Pose(point, quat)
        #     header = Header(seq,stamp,frame_id)
        #     msg = PoseStamped(header, pose)
        #     pub.publish(msg)
        #     flag = flag + 1
        #     r.sleep()
        #     if flag>2 :
        #         break

        flag_list = [1,1]
        flag_list[k] = 0;
        print('yes')


