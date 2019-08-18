#!/usr/bin/python

import rospy
from ros_service_tutorial.srv import ServiceMessage, ServiceMessageResponse

# The below process is performed when there is a service request
def calculationCallback(request):

	# Create a response object
	my_response_object = ServiceMessageResponse()

	# The service name is 'ros_service' and 
    # it will call 'calculationCallback' function upon the service request
	my_response_object.result = request.num_1 + request.num_2

	# Displays 'num_1' and 'num_2' values used in the service request and
	# the 'result' value corresponding to the service response
	rospy.loginfo("Request: x=%ld, y=%ld" % (request.num_1, request.num_2))
	rospy.loginfo("Sending back response: %ld" % my_response_object.result)

	return my_response_object.result


# Initializes Node Name
rospy.init_node('service_server')

# Declare service server's name as 'ros_service_server'
# Use the 'ServiceMessage' service file in the 'ros_service_tutorial' package
# The service name is 'ros_service' and it will call 'calculationCallback' function
# upon the service request.
ros_service_server = rospy.Service('ros_service', \
	                                ServiceMessage,   \
	                                calculationCallback)

# Print if the service server is ready
rospy.loginfo("Ready ROS Service Server!")

# Wait for the service request
rospy.spin()
