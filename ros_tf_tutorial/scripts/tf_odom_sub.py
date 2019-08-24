#!/usr/bin/env python

import tf
import rospy
from std_srvs.srv import Empty
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

import numpy as np

"""
Subscribe odom topic and gets the position and orientation of the robot

"""

def odomPoseCallback(odom_msg):

	print("Odom pose infomation:\n")

	# Get the position of the robot
	print('x = %s' % odom_msg.pose.pose.position.x)
	print('y = %s\n' % odom_msg.pose.pose.position.y) 

	# Get the velocity of the robot
	print('linear_x = %s' % odom_msg.twist.twist.linear.x)
	print('angular_z = %s\n' % odom_msg.twist.twist.angular.z)

    # Get orientation in quaternion
	quat = [odom_msg.pose.pose.orientation.x,\
            odom_msg.pose.pose.orientation.y,\
            odom_msg.pose.pose.orientation.z,\
            odom_msg.pose.pose.orientation.w]

	print("Quaternion: qx=%s, qy=%s, qz=%s, qw=%s\n" % (quat[0], quat[1], quat[2], quat[3]))
    
	# Convert the quaternion to roll-pitch-yaw
	rpy = tf.transformations.euler_from_quaternion(quat)

	# Extract the values of roll, pitch and yaw from the array
	roll = rpy[0]   # 0 for ground robot
	pitch = rpy[1]  # 0 for ground robot
	yaw = rpy[2]

	print("Robot yaw angle: %s\n" % np.degrees(yaw))


if __name__ == '__main__':
    try:
        rospy.init_node('odom_sub_node', anonymous=True)
        position_topic = "/odom"
        pose_subscriber = rospy.Subscriber(position_topic, Odometry, odomPoseCallback) 
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node terminated.")