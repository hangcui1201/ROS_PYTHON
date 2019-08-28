#!/usr/bin/env python

import rospy
import rosnode
from std_msgs.msg import String
from std_msgs.msg import Int32 
from ros_topic_tutorial.msg import TopicMessage

def msgCallback(msg):

	ros_node_name = "ROS node: %s" % rosnode.get_node_names()
	rospy.loginfo(ros_node_name)

	# rospy.get_caller_id()

	receive_secs = "recieve msg = %i" % msg.stamp.secs
	rospy.loginfo(receive_secs)

	receive_nsecs = "recieve msg = %i" % msg.stamp.nsecs
	rospy.loginfo(receive_nsecs)

	receive_count = "recieve msg = %i" % msg.count
	rospy.loginfo(receive_count)


def listener():

	# node name: topic_subscriber
	# topic name: ros_msg_topic
	# data type: String
	rospy.init_node('topic_subscriber', anonymous=True)
	rospy.Subscriber('ros_msg_topic', TopicMessage, msgCallback)

	# Keep the node from exiting until it is shutdown
	rospy.spin()

if __name__ == '__main__':
	listener()