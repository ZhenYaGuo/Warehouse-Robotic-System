#!/usr/bin/env python
import rospy
import os
import tf
import tf2_ros
import numpy as np
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose
from std_msgs.msg import Header
from geometry_msgs.msg import PoseWithCovariance
from geometry_msgs.msg import PoseWithCovarianceStamped
import numpy as np
import scipy as sp
from scipy import linalg


def ar2turtle():

    rospy.init_node('Initialpose_listener', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
            try:
                tf_listener=tf.TransformListener()
                tf_listener.waitForTransform('base_link','ar_marker_15', rospy.Time(0),rospy.Duration(1))

                return True
            except (tf2_ros.TransformException):
                print("No ar_tag detected")
                continue
            rate.sleep()

def initial_pub():

    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10,latch = True)
    r = rospy.Rate(10)
    flag=0
    while (not rospy.is_shutdown()):
        px= 0.333835750818 
        py=1.71722459793 
        pz=0.0
        qx=0.0
        qy=0.0
        qz=0.979302940617
        qw=0.202399976528	
        point = Point(px,py,pz)
        quat = Quaternion(qx,qy,qz,qw)
        pose = Pose(point, quat)
        covaraince=[0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.01*0.06853891945200942]
        pose =PoseWithCovariance(pose,covaraince)
        seq=1
        stamp=rospy.get_rostime()
        frame_id='map'
        header = Header(seq,stamp,frame_id)
        msg = PoseWithCovarianceStamped(header, pose)
        pub.publish(msg)
        flag = flag + 1
        r.sleep()
        if flag>5 :           
            break

if __name__ == '__main__':
     os.system("rosrun dynamic_reconfigure dynparam set /move_base/global_costmap/inflation_layer inflation_radius 0.1")
     os.system("rosrun dynamic_reconfigure dynparam set /move_base/local_costmap/inflation_layer inflation_radius 0.35")
     # os.system("rosrun dynamic_reconfigure dynparam set /move_base/DWAPlannerROS path_distance_bias 32")
     flag_list=True
     while (not rospy.is_shutdown()):
        if (flag_list and ar2turtle()):
            initial_pub()
            flag_list = False
            print('Initialpose Estimation is Done')