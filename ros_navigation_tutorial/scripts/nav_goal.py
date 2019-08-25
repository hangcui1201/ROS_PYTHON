#!/usr/bin/env python 

import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

import numpy as np


# Move robot to the goal point
def move_to_goal(xGoal, yGoal):

	# Define a client for to send goal requests to the move_base server through a SimpleActionClient
	ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

	# Wait for the action server to come up
	while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
		rospy.loginfo("Waiting for the move_base action server to come up ...")

	goal = MoveBaseGoal()

	# Set up the frame parameters
	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()

	# Moving towards the goal
	goal.target_pose.pose.position =  Point(xGoal, yGoal, 0)
	goal.target_pose.pose.orientation.x = 0.0
	goal.target_pose.pose.orientation.y = 0.0
	goal.target_pose.pose.orientation.z = 0.0
	goal.target_pose.pose.orientation.w = 1.0

	rospy.loginfo("Sending goal location ...")
	ac.send_goal(goal)

	ac.wait_for_result(rospy.Duration(60))

	if(ac.get_state() ==  GoalStatus.SUCCEEDED):
		rospy.loginfo("The robot have reached the goal point")
		return True
	else:
		rospy.loginfo("The robot failed to reach the goal point")
		return False


if __name__ == '__main__':

	rospy.init_node('map_nav_node', anonymous=False)

	(x_goal, y_goal) = (-3, 4)

	print('Moving to goal point ...') 

	move_to_goal(x_goal, y_goal)

	rospy.spin()
