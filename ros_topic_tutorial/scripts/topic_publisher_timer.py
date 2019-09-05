#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32 

def publish_callback(event):

    hello_str = "Hello World %s" % event.current_real.to_sec()
    rospy.loginfo(hello_str)
    pub_topic.publish(hello_str)


# Program run from here
if __name__== '__main__':
    try:
    	rospy.init_node('topic_publisher_timer', anonymous=True)
    	pub_topic = rospy.Publisher('ros_timer_topic', String, queue_size=10)
        timer = rospy.Timer(rospy.Duration(1. / 10), publish_callback)  # 10Hz
        rospy.spin()
    # When Ctrl+C is executed, it catches the exception
    except rospy.ROSInterruptException:
        pass
















