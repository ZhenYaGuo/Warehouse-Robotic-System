#!/usr/bin/env python
import rospy
import tf2_ros
import tf

rospy.init_node('my_tf_listener')

# create a tf2_ros type buffer
tfBuffer = tf2_ros.Buffer()
# create a TF2 transform listener object. Save data into tfBuffer
listener = tf2_ros.TransformListener(tfBuffer)

rate = rospy.Rate(1) # rate at 1 hz

while not rospy.is_shutdown():

    try:
        # Get last ( Time(0) )transform from the base frame to frame l7
        frame_info = tfBuffer.lookup_transform('right_hand_camera', 'ar_marker_10', rospy.Time(0))
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
        print (translation_vector)
        print (quaternion)
        euler_rotate = tf.transformations.euler_from_quaternion(quaternion)
        print ("euler:",euler_rotate)

    except (tf2_ros.TransformException):
        rate.sleep()
        continue

    rate.sleep()
