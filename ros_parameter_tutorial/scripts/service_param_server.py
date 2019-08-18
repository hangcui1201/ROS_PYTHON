#!/usr/bin/env python

import rospy
from ros_parameter_tutorial.srv import ServiceParamMessage, ServiceParamMessageResponse


# PLUS             =  1 # Addition
# MINUS            =  2 # Subtraction
# MULTIPLICATION   =  3 # Multiplication
# DIVISION         =  4 # Division

g_operator = 1


# The below process is performed when there is a service request
def calculationCallback(request):

	global g_operator

	response = ServiceParamMessageResponse()

	if(g_operator == 1):
		response.result = request.num_1 + request.num_2
	elif(g_operator == 2):
		response.result = request.num_1 - request.num_2
	elif(g_operator == 3):
		response.result = request.num_1 * request.num_2
	elif(g_operator == 4):
		if(request.num_2 == 0):
			response.result = 0
		else:
			response.result = request.num_1 // request.num_2
	else:
		rospy.loginfo("Default calculation_method: PLUS")
		response.result = request.num_1 + request.num_2

	rospy.loginfo("Request: x=%ld, y=%ld" % (request.num_1, request.num_2))
	rospy.loginfo("Sending back response: %ld" % response.result)

	return response.result



def main():

	global g_operator

	rospy.init_node('service_param_server')

	rospy.set_param("calculation_method", g_operator)

	ros_service_param_server = rospy.Service("ros_service_param",\
												ServiceParamMessage, \
												calculationCallback)

	rospy.loginfo("Ready ROS Service Param Server!")

	rate = rospy.Rate(10)

	while not rospy.is_shutdown():

		g_operator = rospy.get_param("calculation_method")

		rospy.set_param("calculation_method", g_operator)

		rate.sleep(); 


if __name__ == '__main__':
	main()