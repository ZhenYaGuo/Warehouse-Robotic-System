#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ar_track_alvar_msgs.msg import AlvarMarkers
from ar_track_alvar_msgs.msg import AlvarMarker


def callback(AlvarMarkers):
    warehouse_info={}
    try:
        message_inlines=str(AlvarMarkers.markers[0]).splitlines()
        id_instringlist=message_inlines[6].split()
        id_number=id_instringlist[1]
  

    except:
        print('Please Scan Your Object')

    else:
        print('The object: '+id_number+' has been successully scan')
        object_name=raw_input('please enter your object_name: ')
        warehouse_info[object_name]=id_number
        del id_number
        exit()


    #print(AlvarMarkers.markers)
    #print('-----------------')
def AR_id_listener():
    rospy.init_node('AR_id_listener', anonymous=True)

    rospy.Subscriber("/ar_pose_marker", AlvarMarkers, callback)

    rospy.spin()

if __name__ == '__main__':
    AR_id_listener()

