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

def transformation(euler_rotate,translation_vector):

    rot_yaw = np.array([[np.cos(euler_rotate[2]), -np.sin(euler_rotate[2]), 0],
                    [np.sin(euler_rotate[2]), np.cos(euler_rotate[2]), 0] ,
                    [0, 0, 1]
                    ])

    rot_pitch = np.array([[np.cos(euler_rotate[1]), 0, np.sin(euler_rotate[1])],
                    [0, 1, 0] ,
                    [-np.sin(euler_rotate[1]), 0, np.cos(euler_rotate[1])]
                    ])    

    rot_roll = np.array([[1, 0, 0],
                    [0, np.cos(euler_rotate[0]), -np.sin(euler_rotate[0])] ,
                    [0, np.sin(euler_rotate[0]),  np.cos(euler_rotate[0])]
                    ])

    rot = np.dot(rot_yaw,rot_pitch)
    rot = np.dot(rot,rot_roll)
    tm =np.append(rot,[[translation_vector[0]],[translation_vector[1]],[translation_vector[2]]],1)
    tm =np.vstack((tm,[0,0,0,1]))
    return tm

def ar2turtle():

    rospy.init_node('ar2turtle_tf_listener', anonymous=True)
    ar_tag_lib=['ar_marker_15','ar_marker_9']
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():

        for i in range(0, 2):
            try:
                tf_listener=tf.TransformListener()
                tf_listener.waitForTransform(ar_tag_lib[i],'base_link', rospy.Time(0),rospy.Duration(1))
                frame_info = tf_listener.lookupTransform(ar_tag_lib[i],'base_link', rospy.Time(0))
                translation = frame_info[0]
                quaternion_rotate = frame_info[1]
                # translation_x = 0.528
                # translation_y = 1.817
                # translation_z = 0
                # quaternion_x = 0.098
                # quaternion_y = -0.676
                # quaternion_z = 0.720
                # quaternion_w = -0.124
                translation_x = translation[0]
                translation_y = translation[1]
                translation_z = translation[2]
                quaternion_x = quaternion_rotate[0]
                quaternion_y = quaternion_rotate[1]
                quaternion_z = quaternion_rotate[2]
                quaternion_w = quaternion_rotate[3]
                translation_vector = np.array([translation_x,translation_y,translation_z])
                quaternion = np.array([quaternion_x,quaternion_y,quaternion_z,quaternion_w])
                euler_rotate = tf.transformations.euler_from_quaternion(quaternion)
                ar2turtle_tm=transformation(euler_rotate,translation_vector)
                return ar2turtle_tm,i
            except (tf2_ros.TransformException):
                print("No ar_tag detected")
                continue
        rate.sleep()

	


# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10,latch = True)
	flag_list=[1,1]
	while (not rospy.is_shutdown()):
		[ar2turtle_tm,i]= ar2turtle()
		if (flag_list[i] == 0):
			continue;
		flag=0
		r = rospy.Rate(10)
		while (True) :
			px = 0.0
			py = 0.0
			pz = 0.0
			# px = ar2turtle_tm[0][3]
			# py = ar2turtle_tm[1][3]
			# pz = ar2turtle_tm[2][3]
			# px=float(-1.08893692493)
			# py=float(1.49224531651)
			# pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.999855339248)
			qw=float(0.0170088381907)
			seq = 1

			stamp = rospy.get_rostime()		
			frame_id = "ar_marker_15"
			point = Point(px,py,pz)
			quat = Quaternion(qx,qy,qz,qw)
			pose = Pose(point, quat)

			header = Header(seq,stamp,frame_id)
			msg = PoseStamped(header, pose)
			#connections = pub.get_num_connections()
			#rospy.loginfo('connections: %d', connections)
			#if connections > 0:
			pub.publish(msg)
			#rospy.loginfo('Published')
			#break
			flag = flag + 1
			r.sleep()
			if flag>2 :
				break
    # rospy.set_param('/amcl/max_particles',100)
    # rospy.set_param('/amcl/min_particles',10)
        flag_list = [1,1]
        flag_list[i] = 0;
        print('yes')
        # d = rospy.Duration(10, 0)
        # rospy.sleep(d)

