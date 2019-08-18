#!/usr/bin/env python

import rospy
import actionlib
from ros_action_tutorial.msg import FibonacciAction, \
                                    FibonacciGoal, \
                                    FibonacciResult, \
                                    FibonacciFeedback

def main():

	# Node name initialization
	rospy.init_node('action_client')

	action_server_name = '/ros_action_tutorial'

	client = actionlib.SimpleActionClient(action_server_name, \
		                                  FibonacciAction)

	rospy.loginfo("Waiting for action server to start.")

	# Wait until action server starts
	client.wait_for_server()

	rospy.loginfo("Action server started, sending goal.")

	# Declare action goal
	goal = FibonacciGoal()

	# Set action goal (process the Fibonacci sequence 20 times)
	goal.order = 20

	# Transmit action goal
	client.send_goal(goal)

    # Set action time limit (set to 30 seconds)
	finished_before_timeout = client.wait_for_result(rospy.Duration(30))

	if(finished_before_timeout):
    	# Receive action target status value and display on screen
		state = client.get_state()
		rospy.loginfo("Action finished: " + str(state))
		rospy.loginfo("The result is: " + str(client.get_result()))
	else:
    	# If time out occurs
		rospy.loginfo("Action did not finish before the time out.")


if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass













