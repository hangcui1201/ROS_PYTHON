#!/usr/bin/env python

import sys
import rospy
from ros_service_tutorial.srv import ServiceMessage, ServiceMessageRequest


def add_two_ints_client(x, y):

    rospy.wait_for_service('add_two_ints')
    
    try:
        # Initialize ServiceProxy with extra header information.
        # Header is only exchanged on initial connection
        metadata = {'cookies' : 'peanut butter'} 

        add_two_ints = rospy.ServiceProxy('add_two_ints', ServiceMessage, headers=metadata)
        
        print ("Requesting %s + %s with cookies = %s" % (x, y, metadata['cookies']))
        
        response = add_two_ints(x, y)

        print ("Server's connection headers were", response._connection_header)

        return response.result

    except rospy.ServiceException, e:

        print ("Service call failed: %s" % e)


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        import random
        x = random.randint(-50000, 50000)
        y = random.randint(-50000, 50000)
    elif len(sys.argv) == 3:
        try:
            import string
            x = string.atoi(sys.argv[1])
            y = string.atoi(sys.argv[2])
        except:
            print ("%s [x y]" % sys.argv[0])
            sys.exit(1)
    else:
        print ("%s [x y]" % sys.argv[0])
        sys.exit(1)

    print ("%s + %s = %s" % (x, y, add_two_ints_client(x, y)))
