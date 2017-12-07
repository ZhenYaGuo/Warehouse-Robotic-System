#!/usr/bin/env python
import rospy
import tf2_ros
import tf

"""
----------------------------------------------------------------
| This function returns a translation vector of a certain      |
| target in a specific frame, or [404,404,404] if fails.       |
|                                                              |
| Parameters:                                                  |
| 1. tfBuffer->  A system parameter, in which stores the info. |
| 2. start->     a specific frame                              |
| 3. end->       target                                        |
----------------------------------------------------------------
"""

def GetARtagDistance(tfBuffer,start,end):
    # Try to read the translation of the "end" in the frame of the "start"
    # tfBuffer is the place tf package uses to store real time messages
    try:
        # Get last ( Time(0) )transform from the base frame to frame l7
        frame_info = tfBuffer.lookup_transform(start, end, rospy.Time(0))
        translation = frame_info.transform.translation
        quaternion_rotate = frame_info.transform.rotation
        translation_x = translation.x
        translation_y = translation.y
        translation_z = translation.z
        quaternion_x = quaternion_rotate.x
        quaternion_y = quaternion_rotate.y
        quaternion_z = quaternion_rotate.z
        quaternion_w = quaternion_rotate.w
        translation_vector = [translation_x,translation_y,translation_z]
        quaternion = [quaternion_x,quaternion_y,quaternion_z,quaternion_w]
        euler_rotate = tf.transformations.euler_from_quaternion(quaternion)

        return translation_vector
    # If reading the translation fails, the function will return [404,404,404] with all elements integer.
    except (tf2_ros.TransformException):
    	#print("Fail to get AR tag distance!")
    	return [int(404),int(404),int(404)]