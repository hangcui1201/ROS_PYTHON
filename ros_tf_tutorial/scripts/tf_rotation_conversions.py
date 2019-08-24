#!/usr/bin/env python

#this script converts between Roll-Pitch-Yaw angles and Quaternions

import tf
import rospy
import numpy as np
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

print('----------------------------------------')
print('Roll-Pitch-Yaw Conversion to Quaternions')
print('----------------------------------------')

# Roll, pitch and yaw in radians
roll = np.radians(30)
pitch = np.radians(42)
yaw = np.radians(58)
print("roll = {0}, pitch = {1}, yaw = {2}\n".format(np.degrees(roll), np.degrees(pitch), np.degrees(yaw)))

# Convert the roll-pitch-yaw angles to a quaternion using ROS TF Library
quat = tf.transformations.quaternion_from_euler(roll, pitch, yaw)

print('The resulting quaternion using "quaternion_from_euler" function: ')
print("x = {0}, y = {1}, z = {2}, w = {3}\n".format(quat[0], quat[1], quat[2], quat[3]))

# Convert quaternion to the roll-pitch-yaw angles
rpy = tf.transformations.euler_from_quaternion(quat)
roll_from_quat = rpy[0]
pitch_from_quat = rpy[1]
yaw_from_quat = rpy[2]

print('Convert roll-pitch-yaw using "euler_from_quaternion" function: ')
print("roll = {0}, pitch = {1}, yaw = {2}\n".format(np.degrees(roll_from_quat), np.degrees(pitch_from_quat), np.degrees(yaw_from_quat)))


