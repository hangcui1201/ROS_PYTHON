#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def main():

	rospy.init_node('task_node')
	rate = rospy.Rate(2)
	pub = rospy.Publisher('chatter', String, queue_size=10)
	while not rospy.is_shutdown():
		hello_str = "Hello World: %s" % rospy.get_time()
		pub.publish(hello_str)
		rate.sleep()

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass