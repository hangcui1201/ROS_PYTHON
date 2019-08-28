#!/usr/bin/env python

import rospy
from ros_topic_tutorial.msg import TopicMessage
# this is an example of using ROS built-in message
from std_msgs.msg import String
from std_msgs.msg import Int32 


class MessageChange:

	def __init__(self):
		
		rospy.init_node("topic_message", anonymous=True)

		self.msg_pub = rospy.Publisher('/ros_msg_change', TopicMessage, queue_size=100)
		self.msg = TopicMessage()

		rospy.Subscriber("/ros_msg_topic", TopicMessage, self.msg_callback)

	def msg_callback(self, msg):

		self.msg.stamp.secs = 1
		self.msg.stamp.nsecs = 2
		self.msg.count = 3


	def run(self):
		self.msg_pub.publish(self.msg)


if __name__ == '__main__':

	try:
		pc = MessageChange()
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			connections = pc.msg_pub.get_num_connections()
			rospy.loginfo("Connection: %d", connections)
			if (connections > 0):
				pc.run()
				rospy.loginfo("Published once")
				break
			rate.sleep()
	except rospy.ROSInterruptException:
		raise e



