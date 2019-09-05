#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from ros_topic_tutorial.msg import TopicMessage

"""
Publisher that receives notification of new subscriptions
"""

class ChatterListener(rospy.SubscribeListener):

    def peer_subscribe(self, topic_name, topic_publish, peer_publish):

        print("\nA peer subscribed to topic [%s]" % topic_name)
        
        print("Hey everyone, we have a new friend!")

        # Publish message data to all subscribers
        topic_publish(TopicMessage(rospy.Time.now(), 1000))

        print("Greetings, welcome to subscribe topic" + topic_name + "\n")

        # Publish message data to new subscriber
        peer_publish(TopicMessage(rospy.Time.now(), 1111))
        

    def peer_unsubscribe(self, topic_name, numPeers):

        print("A peer unsubscribed from topic [%s]" % topic_name)
        if numPeers == 0:
            print("I have no friends")
    

def talker_callback():

	rospy.init_node("topic_publisher_notify", anonymous=True)

	ros_pub_topic = rospy.Publisher("ros_msg_topic", TopicMessage, subscriber_listener = ChatterListener(), queue_size=10)

	msg = TopicMessage()
	msg.stamp = 0
	msg.count = 0 

	count = 0

	while not rospy.is_shutdown():

		msg.stamp = rospy.Time.now()
		msg.count = count;

		# send_secs = "send msg = %i" % msg.stamp.secs
		# rospy.loginfo(send_secs)

		# send_nsecs = "send msg = %i" % msg.stamp.nsecs
		# rospy.loginfo(send_nsecs)

		# send_count = "send msg = %i" % msg.count
		# rospy.loginfo(send_count)

		# Publish info to the system
		ros_pub_topic.publish(msg)

		count += 1

		rospy.sleep(0.1)


if __name__ == '__main__':
    try:
        talker_callback()
    except rospy.ROSInterruptException: 
    	pass
