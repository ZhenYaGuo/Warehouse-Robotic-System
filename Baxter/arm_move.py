#!/usr/bin/env python
import rospy
from moveit_msgs.srv import GetPositionIK, GetPositionIKRequest, GetPositionIKResponse
from geometry_msgs.msg import PoseStamped
from moveit_commander import MoveGroupCommander
import numpy as np
from numpy import linalg

import tf
import tf2_ros

from GetARtagDistance import *
from baxter_interface import gripper as robot_gripper

def PID(error,camera_base_position,error_accu):
	#position is the translation vector of camera in the camera frame
	#error_accu is the accumulation translation error vector of ar tag in the camera frame
	Kp = 0.3
	Ki = 0.1
	target_position = [-Kp*error[1]+Ki*error_accu[1]+camera_base_position[0] , -Kp*error[0]-Ki*error_accu[0]+camera_base_position[1] , Kp*error[2]+Ki*error_accu[2]+camera_base_position[2]]
	return target_position

def Z_Move(target_translation,compute_ik,z):
    request = GetPositionIKRequest()
    request.ik_request.group_name = "left_arm"
    request.ik_request.ik_link_name = "left_gripper"
    request.ik_request.attempts = 20
    #request.ik_request.pose_stamped.header.frame_id = "base"
    request.ik_request.pose_stamped.header.frame_id = "base"
    #Set the desired orientation for the end effector HERE
    euler_angle = [-np.pi, 0, 0]
    quaternion = tf.transformations.quaternion_from_euler(euler_angle[0], euler_angle[1], euler_angle[2])
    request.ik_request.pose_stamped.pose.position.x = 0.6743145909230185
    request.ik_request.pose_stamped.pose.position.y = 0.2560765138916417
    request.ik_request.pose_stamped.pose.position.z = 0.45896199498824425
    request.ik_request.pose_stamped.pose.orientation.x = quaternion[0]
    request.ik_request.pose_stamped.pose.orientation.y = quaternion[1]
    request.ik_request.pose_stamped.pose.orientation.z = quaternion[2]
    request.ik_request.pose_stamped.pose.orientation.w = quaternion[3]
    
    try:
        #Send the request to the service
        response = compute_ik(request)
        
        #Print the response HERE
        #print(response)
        group = MoveGroupCommander("left_arm")

        # Setting position and orientation target
        group.set_pose_target(request.ik_request.pose_stamped)

        # TRY THIS
        # Setting just the position without specifying the orientation
        ###group.set_position_target([0.5, 0.5, 0.0])

        # Plan IK and execute
        group.go()
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def Baxter_Go(target_translation, reference_frame ,compute_ik):
    #Construct the request
    request = GetPositionIKRequest()
    request.ik_request.group_name = "left_arm"
    request.ik_request.ik_link_name = "left_gripper"
    request.ik_request.attempts = 20
    #request.ik_request.pose_stamped.header.frame_id = "base"
    request.ik_request.pose_stamped.header.frame_id = reference_frame
    
    #Set the desired orientation for the end effector HERE
    euler_angle = [-np.pi, 0, 0]
    quaternion = tf.transformations.quaternion_from_euler(euler_angle[0], euler_angle[1], euler_angle[2])
    request.ik_request.pose_stamped.pose.position.x = target_translation[0]
    request.ik_request.pose_stamped.pose.position.y = target_translation[1]
    request.ik_request.pose_stamped.pose.position.z = target_translation[2]      
    request.ik_request.pose_stamped.pose.orientation.x = quaternion[0]
    request.ik_request.pose_stamped.pose.orientation.y = quaternion[1]
    request.ik_request.pose_stamped.pose.orientation.z = quaternion[2]
    request.ik_request.pose_stamped.pose.orientation.w = quaternion[3]
    
    try:
        #Send the request to the service
        response = compute_ik(request)
        
        #Print the response HERE
        #print(response)
        group = MoveGroupCommander("left_arm")

        # Setting position and orientation target
        group.set_pose_target(request.ik_request.pose_stamped)

        # TRY THIS
        # Setting just the position without specifying the orientation
        ###group.set_position_target([0.5, 0.5, 0.0])

        # Plan IK and execute
        group.go()
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e


def Firstmove(target_translation,compute_ik):
    request = GetPositionIKRequest()
    request.ik_request.group_name = "left_arm"
    request.ik_request.ik_link_name = "left_gripper"
    request.ik_request.attempts = 20
    #request.ik_request.pose_stamped.header.frame_id = "base"
    request.ik_request.pose_stamped.header.frame_id = "base"
    #Set the desired orientation for the end effector HERE
    euler_angle = [-np.pi, 0, 0]
    quaternion = tf.transformations.quaternion_from_euler(euler_angle[0], euler_angle[1], euler_angle[2])
    request.ik_request.pose_stamped.pose.position.x = target_translation[0]
    request.ik_request.pose_stamped.pose.position.y = target_translation[1]
    request.ik_request.pose_stamped.pose.position.z = target_translation[2]      
    request.ik_request.pose_stamped.pose.orientation.x = quaternion[0]
    request.ik_request.pose_stamped.pose.orientation.y = quaternion[1]
    request.ik_request.pose_stamped.pose.orientation.z = quaternion[2]
    request.ik_request.pose_stamped.pose.orientation.w = quaternion[3]
    
    try:
        #Send the request to the service
        response = compute_ik(request)
        
        #Print the response HERE
        #print(response)
        group = MoveGroupCommander("left_arm")

        # Setting position and orientation target
        group.set_pose_target(request.ik_request.pose_stamped)

        # TRY THIS
        # Setting just the position without specifying the orientation
        ###group.set_position_target([0.5, 0.5, 0.0])

        # Plan IK and execute
        group.go()
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def GripperSetup():
    global left_gripper
    left_gripper = robot_gripper.Gripper('left')

    #Calibrate the gripper (other commands won't work unless you do this first)
    print('Calibrating Gripper...')
    left_gripper.calibrate()
    rospy.sleep(2.0)

def PositionDataError(target,tfBuffer):
    i = 0;
    while(GetARtagDistance(tfBuffer,'base',target) == [int(404),int(404),int(404)]):
        rospy.sleep(0.1)
        i+=1
        if(i == 20):
            return 1
    return 0

def GraspObject(rough_target,precise_target,tfBuffer,compute_ik):
    # Rough localization
    rospy.sleep(1)
    Base_artag_translation = [0,0,0]
    target = rough_target
    if(PositionDataError(target,tfBuffer)):
        print("Position Data Error","target ->",target)
        return 0
    else:
        for i in range(10):
            temp = GetARtagDistance(tfBuffer,'base',target)
            Base_artag_translation[0] = Base_artag_translation[0] + temp[0]
            Base_artag_translation[1] = Base_artag_translation[1] + temp[1]
            Base_artag_translation[2] = Base_artag_translation[2] + temp[2]
            rospy.sleep(0.1)
        Base_artag_translation[0] = Base_artag_translation[0]/10
        Base_artag_translation[1] = Base_artag_translation[1]/10
        Base_artag_translation[2] = Base_artag_translation[2]/10
        Base_artag_translation2 = [Base_artag_translation[0],Base_artag_translation[1],Base_artag_translation[2]-0*abs(Base_artag_translation[2])]
        print(Base_artag_translation2)
        Baxter_Go(Base_artag_translation2,'base',compute_ik)

    # Precise localization
    rospy.sleep(1)
    Base_artag_translation = [0,0,0]
    target = precise_target
    if(PositionDataError(target,tfBuffer)):
        print("Position Data Error","target ->",target)
        return 0
    else:
        for i in range(10):
            temp = GetARtagDistance(tfBuffer,'base',target)
            Base_artag_translation[0] = Base_artag_translation[0] + temp[0]
            Base_artag_translation[1] = Base_artag_translation[1] + temp[1]
            Base_artag_translation[2] = Base_artag_translation[2] + temp[2]
            rospy.sleep(0.1)
        Base_artag_translation[0] = Base_artag_translation[0]/10
        Base_artag_translation[1] = Base_artag_translation[1]/10
        Base_artag_translation[2] = Base_artag_translation[2]/10
        Base_artag_translation2 = [Base_artag_translation[0],Base_artag_translation[1],Base_artag_translation[2]]
        print(Base_artag_translation2)
        Baxter_Go(Base_artag_translation2,'base',compute_ik)

    # Grasp object
    left_gripper.close()
    return 1

def main():
    #Wait for the IK service to become available
    rospy.wait_for_service('compute_ik')
    rospy.init_node('service_query')
    
    #Create the function used to call the service
    compute_ik = rospy.ServiceProxy('compute_ik', GetPositionIK)

    # create a tf2_ros type buffer
    tfBuffer = tf2_ros.Buffer()
    # create a TF2 transform listener object. Save data into tfBuffer
    listener = tf2_ros.TransformListener(tfBuffer)

    translation_error_accu = [0.0,0.0,0.0]
    #desired_position_camera_artag = [0.016,-0.023,0.213]
    desired_position_base_camera = [0.689, 0.071, 0.244]
    desired_position_base_camera2 = [0.621, -0.161, 0.017-0.1]
    desired_position_base_camera3 = [0.742, -0.060, 0.090]
    desired_position_base_camera4 = [0.647, -0.145, 0.209]
    GripperSetup()
    left_gripper.open()
    #reach = 0

    while not rospy.is_shutdown():

        Firstmove(desired_position_base_camera,compute_ik)

        if(not GraspObject('ar_marker_1','ar_marker_9',tfBuffer,compute_ik)):
            print("Grasping failed")
            break

        # Move to storage position and leave object
        rospy.sleep(0.5)
        Baxter_Go([0.775, 0.198, 0.172],'base',compute_ik)
        Baxter_Go(desired_position_base_camera2,'base',compute_ik)
        rospy.sleep(0.5)
        left_gripper.open()

        # Observe the location of turtlebot
        rospy.sleep(3)
        Baxter_Go(desired_position_base_camera3,'base',compute_ik)
        Base_artag_translation = [0,0,0]
        target = 'ar_marker_7'
        if(PositionDataError(target,tfBuffer)):
            print("Position Data Error","target ->",target)
            break
        else:
            for i in range(10):
                temp = GetARtagDistance(tfBuffer,'base',target)
                Base_artag_translation[0] = Base_artag_translation[0] + temp[0]
                Base_artag_translation[1] = Base_artag_translation[1] + temp[1]
                Base_artag_translation[2] = Base_artag_translation[2] + temp[2]
                rospy.sleep(0.1)
            Base_artag_translation[0] = Base_artag_translation[0]/10
            Base_artag_translation[1] = Base_artag_translation[1]/10
            Base_artag_translation[2] = Base_artag_translation[2]/10
            TurtleBot_Position = [Base_artag_translation[0],Base_artag_translation[1],Base_artag_translation[2]]
            print(TurtleBot_Position)
            #Baxter_Go(Base_artag_translation2,'base',compute_ik)

        # Grasp the object from storage place
        Baxter_Go(desired_position_base_camera4,'base',compute_ik)
        if(not GraspObject('ar_marker_1','ar_marker_9',tfBuffer,compute_ik)):
            print("Grasping failed")
            break

        rospy.sleep(1)
        Baxter_Go(TurtleBot_Position,'base',compute_ik)

        left_gripper.open()

        Firstmove(desired_position_base_camera,compute_ik)

        break
        #raw_input("Successfully done!")


#Python's syntax for a main() method
if __name__ == '__main__':
    main()
