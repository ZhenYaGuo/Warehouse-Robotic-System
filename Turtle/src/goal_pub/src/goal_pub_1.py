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
		while (user == 1) :
			px = 0.333835750818 
			py = 1.71722459793
			pz = 0;
			# px=float(-1.08893692493)
			# py=float(1.49224531651)
			# pz=float(0.0)
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

		while (user == 2) :
			px=float(-4.73719739914)
			py=float(2.64434456825)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.543395753737)
			qw=float(0.839476655316)
			seq = 2

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
		while (user == 3) :
			px=float(-1.62814486027)
			py=float(0.419653236866)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.910160292304)
			qw=float(0.414256251991)
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
			px=float(-1.08893692493)
			py=float(1.49224531651)
			pz=float(0.0)
			qx=float(0.0)
			qy=float(0.0)
			qz=float(0.999855339248)
			qw=float(0.0170088381907)
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
	#rospy.sleep(10.)
	#r.sleep()

	



# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
  try:
    goal_pub()
    #rospy.spin()
  except rospy.ROSInterruptException: pass

