#!/usr/bin/env python

import sys
import rospy
from ros_parameter_tutorial.srv import ServiceParamMessage, ServiceParamMessageRequest

def main():

	rospy.init_node('service_param_client')

	if len(sys.argv) != 3:
		rospy.loginfo("Command: rosrun ros_parameter_tutorial service_param_client arg0 arg1")
		rospy.loginfo("arg0: double number, arg1: double number")
		sys.exit()
		
	rospy.wait_for_service('ros_service_param')

	ros_service_client = rospy.ServiceProxy('ros_service_param', ServiceParamMessage)

	request = ServiceParamMessageRequest()
	request.num_1 = int(sys.argv[1])
	request.num_2 = int(sys.argv[2])

	response_result = ros_service_client(request)

	# result: value
	response_result = str(response_result).split(":")[1].strip()

	rospy.loginfo("Send service, request.num_1 and request.num_2: %ld, %ld" % \
	              (request.num_1, request.num_2))		

	rospy.loginfo("Receive service, response.result: %ld" % int(response_result))

if __name__ == '__main__':
	main()
