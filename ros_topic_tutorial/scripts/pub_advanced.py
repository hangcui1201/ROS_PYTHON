#!/usr/bin/env python

import rospy
from std_msgs.msg import ColorRGBA


def talker():

	topic_name = 'color_talker'

	rospy.init_node('color', anonymous=True)

	pub = rospy.Publisher(topic_name, ColorRGBA, queue_size=10)

	print ("\nNode running. To see messages, rostopic echo %s\n"%(rospy.resolve_name(topic_name)))

	while not rospy.is_shutdown():

		# Publish with in-order initialization of arguments (r, g, b, a)
		pub.publish(1, 2, 3, 4)

		rospy.sleep(.5)

		# Publish with a=1, use default values for rest
		pub.publish(a = 1.0)

		rospy.sleep(.5)

		# Print the number of subscribers
		rospy.loginfo("I have %s subscribers" % pub.get_num_connections())
        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: 
    	pass
