#!/usr/bin/env python


import rospy 
from ros_service_tutorial.srv import ServiceMessage, ServiceMessageResponse


def add_two_ints(request):

    print ("Request from %s" % request._connection_header['callerid'])

    if ('cookies' in request._connection_header):
        print ("Request gave me %s cookies" % request._connection_header['cookies'])

    print ("Returning [%s + %s = %s]" % (request.num_1, request.num_2, (request.num_1 + request.num_2)))

    return ServiceMessageResponse(request.num_1 + request.num_2)


def add_two_ints_server():

    rospy.init_node("add_two_ints_server")

    s = rospy.Service('add_two_ints', ServiceMessage, add_two_ints)

    rospy.spin()


if __name__ == "__main__":
    add_two_ints_server()
