#!/usr/bin/env python

import rospy
import roslaunch

"""
Call and run another ROS node from scripts

"""

def start_node_task():

	package = 'ros_launch_tutorial'
	executable = 'task.py'
	node = roslaunch.core.Node(package, executable)
	launch = roslaunch.scriptapi.ROSLaunch()

	rospy.loginfo("Staring ROS task node ...")
	launch.start()

	node_task = launch.launch(node)
	rospy.loginfo("ROS task node running status: %s" % node_task.is_alive())

def main():
	rospy.init_node('main_node')
	start_node_task()
	rospy.spin()


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass