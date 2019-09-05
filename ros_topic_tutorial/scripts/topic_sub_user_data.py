#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import *
from ros_topic_tutorial.msg import TopicMessage

"""
Simple listener demo that demonstrates how to register additional
arguments to be passed to a subscription callback
"""

def msgCallback(msg, args):

    if args == 1:
        print ("#1: I heard [%s] with userdata from [%s]" % (msg.count, "ros_msg_topic_1"))
    elif args == "ros_msg_topic_2":
        print ("#2: I heard [%s] with userdata from [%s]" % (msg.count, str(args)))
    else:
        print ("#3 I heard [%s] with userdata from [%s]" % (msg.count, str(args))) 
    
def listener_with_user_data():

	"""
    Callback arguments (aka user data) allow you to reuse the same
    callback for different topics, or they can even allow you to use
    the same callback for the same topic, but have it do something
    different based on the arguments.
    """
	rospy.Subscriber('ros_msg_topic_1', TopicMessage, msgCallback, 1)
	rospy.Subscriber('ros_msg_topic_2', TopicMessage, msgCallback, "ros_msg_topic_2")
	rospy.Subscriber("ros_msg_topic_3", TopicMessage, msgCallback, "ros_msg_topic_3")

	rospy.init_node('topic_sub_user_data', anonymous=True)

	rospy.spin()
        

if __name__ == '__main__':

    try:
        listener_with_user_data()
    except KeyboardInterrupt, e:
        pass
