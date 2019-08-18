#!/usr/bin/env python

import rospy
from ros_topic_tutorial.msg import TopicMessage
# this is an example of using ROS built-in message
from std_msgs.msg import String
from std_msgs.msg import Int32 

def talker():

    """
    This node uses 'topic_publisher' as its name and communicates
    with other nodes. If two nodes are running with the same node
    name, one will shutdown. If we want to run both nodes, use the
    anonymous=True flag
    """

    # package name: ros_topic_tutorial
    # node name: topic_publisher
    # publisher: ros_pub_topic
    # topic name: ros_msg_topic
    # published message type: TopicMessage (TopicMessage.msg)
    # queue size: 100

    rospy.init_node('topic_publisher', anonymous=True)

    ros_pub_topic = rospy.Publisher('ros_msg_topic', TopicMessage, queue_size=100)

    loop_rate = rospy.Rate(10)  # 10Hz

    # Use self-defined message
    msg = TopicMessage()
    msg.stamp = 0
    msg.count = 0 

    # This is an example of using ROS built-in message
    # Create a Int32() integer and initialize it
    any_num = Int32()    
    any_num.data = 0   

    count = 0

    while not rospy.is_shutdown():

        # rospy.get_time(): get the current time in float seconds
        # rospy.Time.now(): get the current time in integer seconds
        msg.stamp = rospy.Time.now()
        msg.count = count;

        send_secs = "send msg = %i" % msg.stamp.secs
        rospy.loginfo(send_secs)

        send_nsecs = "send msg = %i" % msg.stamp.nsecs
        rospy.loginfo(send_nsecs)

        send_count = "send msg = %i" % msg.count
        rospy.loginfo(send_count)

        # Publish info to the system
        ros_pub_topic.publish(msg)

        # Use sleep() method in the Rate object, 0.1s
        loop_rate.sleep()

        # Increase count variable by 1
        count += 1


# Program run from here
if __name__== '__main__':
    try:
        talker()
    # When Ctrl+C is executed, it catches the exception
    except rospy.ROSInterruptException:
        pass
















