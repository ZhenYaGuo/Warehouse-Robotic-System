#!/usr/bin/env python

import rospy

from std_msgs.msg import String,Empty

from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Point

from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Pose
from std_msgs.msg import Header

def goal_pub():

	rospy.init_node('goal_pub', anonymous=True)

	pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10,latch = True)

	r = rospy.Rate(10)
	
	flag=0
	while (not rospy.is_shutdown()):
		flag=0
		user = input("pleas input the number 1 or 2 or 3 or 4 (1:begin 2:destination 3:calibartion_A 4:calibration_B) :  ")
		while (user== 1) :
			px = float(0.333835750818) 
			py = float(1.71722459793)
			pz = float(0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.979302940617)
			qw=float(0.202399976528)
			seq = 1

			stamp = rospy.get_rostime()		
			frame_id = "map"
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

		while (user == 2) :
			px=float(-6.23748922348)
			py=float(2.80582213402)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.492913058167)
			qw=float(0.870078569492)
			seq = 2

			stamp = rospy.get_rostime()		
			frame_id = "map"
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
		
		while (user == 3) :
			px=float(-2.38125944138)
			py=float(1.79362559319)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.966729731306)
			qw=float(0.255799973826)
			seq = 1

			stamp = rospy.get_rostime()		
			frame_id = "map"
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

		while (user== 4) :
			px=float(-3.77560639381)
			py=float(2.03946948051)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.690671720558)
			qw=float(0.723168427423)
			seq = 1

			stamp = rospy.get_rostime()		
			frame_id = "map"
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
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
  try:
    goal_pub()
    #rospy.spin()
  except rospy.ROSInterruptException: pass

