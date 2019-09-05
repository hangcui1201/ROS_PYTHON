#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():

    pub = rospy.Publisher('chatter', String, headers={'cookies': 'oreo'}, queue_size=10)

    rospy.init_node('pub_connection_header', anonymous=True)

    r = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        pub_str = "Hello World %s" % rospy.get_time()
        rospy.loginfo(pub_str)
        pub.publish(pub_str)
        r.sleep()
        
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
    	pass
