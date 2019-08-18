#!/usr/bin/env python

import rospy
from ros_parameter_tutorial.srv import ServiceParamMessage, ServiceParamMessageResponse


# PLUS             =  1 # Addition
# MINUS            =  2 # Subtraction
# MULTIPLICATION   =  3 # Multiplication
# DIVISION         =  4 # Division

g_operator = 1


def switch_color(g_operator, req_value1, req_value2):

	divide_result = 0

	if(req_value2 != 0):
		divide_result = req_value1/(req_value2*1.0)

	switcher = {
   		
        1: req_value1+req_value2,
        2: req_value1-req_value2,
        3: req_value1*req_value2,
        4: divide_result,
    }

	return switcher.get(g_operator, req_value1+req_value2)


# The below process is performed when there is a service request
def calculationCallback(request):

	global g_operator

	response = ServiceParamMessageResponse()

	response.result = switch_color(g_operator, request.num_1, request.num_2)

	rospy.loginfo("Request: x=%ld, y=%ld" % (request.num_1, request.num_2))
	rospy.loginfo("Sending back response: %ld" % response.result)

	return True



def main():

	global g_operator

	rospy.init_node('service_param_server')

	rospy.set_param("calculation_method", 1)

	ros_service_param_server = rospy.Service("ros_service_param",\
												ServiceParamMessage, \
												calculationCallback)

	rospy.loginfo("Ready ROS Service Param Server!")

	rate = rospy.Rate(10)

	while True:

		rospy.set_param("calculation_method", g_operator)

		rate.sleep(); 


if __name__ == '__main__':
	main()