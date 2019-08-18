#!/usr/bin/env python

import rospy
import actionlib
from ros_action_tutorial.msg import FibonacciFeedback, \
                                    FibonacciResult, \
                                    FibonacciAction

class FibonacciClass(object):

	feedback_ = FibonacciFeedback()
	result_ = FibonacciResult()

	def __init__(self, as_name = "fibonacci_as"):

		self.as_name = as_name

		# create an action server
		self.as_ = actionlib.SimpleActionServer(self.as_name, \
			                                    FibonacciAction, \
			                                    self.goal_callback, \
			                                    False)
		self.as_.start()

	# A function that receives an action goal message and performs a specified
    # action (in this example, a Fibonacci calculation)
	def goal_callback(self, goal):

		# Loop Rate: 1Hz
		r = rospy.Rate(1)

		# Used as a variable to store the success or failure of an action
		success = True

		# Setting Fibonacci sequence initialization,
		# add first (0) and second message (1) of feedback.
		self.feedback_.sequence = []
		self.feedback_.sequence.append(0)
		self.feedback_.sequence.append(1)

		# Notify the user of action name, goal, initial two values of Fibonacci sequence
		rospy.loginfo(self.as_name + \
			  ": Executing, creating fibonacci sequence of order %i with seeds %i, %i" % \
			  (goal.order, self.feedback_.sequence[0], self.feedback_.sequence[1]))

		# Action content
		for i in xrange(1, goal.order):

			# Confirm action cancellation from action client
			if(self.as_.is_preempt_requested()):

				# Notify action cancellation
				rospy.loginfo(self.as_name + ": Preempted")

				# Action cancellation
				self.as_.set_preempted()

				# Consider action as failure and save to variable
				success = False

				break

			# Store the sum of current Fibonacci number and the previous number in the feedback
		    # while there is no action cancellation or the action target value is reached.
			self.feedback_.sequence.append(self.feedback_.sequence[i] + self.feedback_.sequence[i-1])

		    # Publish feedback
			self.as_.publish_feedback(self.feedback_)

		    # Sleep according to the defined loop rate
			r.sleep()


		if(success):
			self.result_.sequence = self.feedback_.sequence
			rospy.loginfo(self.as_name + ": Succeeded")
			self.as_.set_succeeded(self.result_)


if __name__ == '__main__':

	rospy.init_node('action_server')
	FibonacciClass('ros_action_tutorial')
	rospy.spin()










