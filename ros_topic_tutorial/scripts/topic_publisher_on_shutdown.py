#!/usr/bin/env python

import rospy
from std_msgs.msg import String

topic_pub = None

# Publish a message to subscribers when it die
def talker_shutdown():

    print("Publisher dead!")
    topic_pub.publish("I'm dead!")
    
    
def talker():

    global topic_pub

    rospy.init_node('topic_publisher_on_shutdown', anonymous=True)

    topic_pub = rospy.Publisher('ros_on_shutdown_topic', String, queue_size=10)

    # Register talker_shutdown() to be called when rospy exits
    rospy.on_shutdown(talker_shutdown)

    print("Hit Ctrl-C to see on_shutdown!")

    rospy.spin()
        

# Program run from here
if __name__== '__main__':
    try:
        talker()
    # When Ctrl+C is executed, it catches the exception
    except rospy.ROSInterruptException:
        pass

