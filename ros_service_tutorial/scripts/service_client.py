#!/usr/bin/python 

import sys
import rospy
import rospkg
from ros_service_tutorial.srv import ServiceMessage, ServiceMessageRequest

rospy.init_node('service_client')

# Note in python argc = len(argv)
# Input value error handling
if len(sys.argv) != 3:
	rospy.loginfo("Command: rosrun ros_service_tutorial service_client.py arg0 arg1")
	rospy.loginfo("arg0: double number, arg1: double number")
	sys.exit()
	
rospy.wait_for_service('ros_service')

# Declares service client 'ros_service_client'
# Use the 'ServiceMessage' service file in the 'ros_service_tutorial' package
# The service name is 'ros_service'
ros_service_client = rospy.ServiceProxy('ros_service', ServiceMessage)

my_request_object = ServiceMessageRequest()
my_request_object.num_1 = int(sys.argv[1])
my_request_object.num_2 = int(sys.argv[2])

response_result = ros_service_client(my_request_object)

# result: value
response_result_value = str(response_result).split(":")[1].strip()

rospy.loginfo("Send service, srv.Request.num_1 and srv.Request.num_2: %ld, %ld" % \
              (my_request_object.num_1, my_request_object.num_2))		

rospy.loginfo("Receive service, srv.Response.result: %ld" % int(response_result_value))

