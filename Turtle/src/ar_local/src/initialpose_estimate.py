#!/usr/bin/env python
import rospy
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
                tf_listener.waitForTransform('base_link',ar_tag_lib[i], rospy.Time(0),rospy.Duration(1))
                frame_info = tf_listener.lookupTransform('base_link',ar_tag_lib[i], rospy.Time(0))
                translation = frame_info[0]
                quaternion_rotate = frame_info[1]
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

def map2turtle(ar2turtle_tm,i):
    map2ar_translation_list=[[-0.025, 1.009, 0.045],[-1.231, 2.376, 0.012]]
    map2ar_euler_rotate_list=[[-1.410, -0.010, -0.245],[0.223, 1.347, -0.206]]
    #map2ar_translation=np.array([-0.69078, 1.7842, 0.0102])
    #map2ar_euler_rotate=np.array([0.1,0.1,0.1])
    map2ar_translation = map2ar_translation_list[i]
    map2ar_euler_rotate = map2ar_euler_rotate_list[i]
    map2ar_tm=transformation(map2ar_euler_rotate,map2ar_translation)
    map2turtle_tm=np.dot(map2ar_tm,ar2turtle_tm)
    map2turtle_translation=np.array([map2turtle_tm[0][3],map2turtle_tm[1][3],map2turtle_tm[2][3]])
    map2turtle_rotation=np.delete(map2turtle_tm,(3),axis=0)
    map2turtle_rotation=np.delete(map2turtle_rotation,(3),axis=1)
    map2turtle_euler_rotate=tf.transformations.euler_from_matrix(map2turtle_rotation, 'rxyz')
    map2turtle_quaternion = tf.transformations.quaternion_from_euler(map2turtle_euler_rotate[0], map2turtle_euler_rotate[1], map2turtle_euler_rotate[2])
    map2turtle=np.append([map2turtle_translation],[map2turtle_quaternion],axis=1)    

    return map2turtle


def initial_pub(map2turtle):

    pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10,latch = True)
    r = rospy.Rate(10)
    flag=0
    while (not rospy.is_shutdown()):
        px = float(map2turtle[0][0])
        py = float(map2turtle[0][1])
        pz = float(map2turtle[0][2])
        qx = float(map2turtle[0][3])
        qy = float(map2turtle[0][4])
        qz = float(map2turtle[0][5])
        qw = float(map2turtle[0][6])
        # px= 0.333835750818 `
        # py=1.71722459793 
        # pz=0.0
        # qx=0.0
        # qy=0.0
        # qz=0.979302940617
        # qw=0.202399976528	
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
        # print(msg)
        pub.publish(msg)
#        pub.publish(header,pose)
        flag = flag + 1
        r.sleep()
        if flag>5 :           
            break

if __name__ == '__main__':
     flag_list=[1,1]
     while (not rospy.is_shutdown()):
        [ar2turtle_tm,i]= ar2turtle()
        if (flag_list[i] == 0):
            continue;
        map2turtle_xyzq=map2turtle(ar2turtle_tm,i)
        print(ar2turtle_tm)
        print(map2turtle_xyzq)
    # rospy.set_param('/amcl/max_particles',100)
    # rospy.set_param('/amcl/min_particles',10)
        initial_pub(map2turtle_xyzq)
        flag_list = [1,1]
        flag_list[i] = 0;
        print('yes')
        # d = rospy.Duration(10, 0)
        # rospy.sleep(d)