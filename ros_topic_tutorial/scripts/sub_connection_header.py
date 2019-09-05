#!/usr/bin/env python

"""
sub_connection_header looks at the connection header
from the received message to determine who it is talking to
"""

import sys 
import rospy
from std_msgs.msg import String

# /pub_connection_header just offered me oreo cookies

def callback(msg):

    chatter = msg.data

    if 'callerid' in msg._connection_header:
        who = msg._connection_header['callerid']
    else:
        who = 'unknown'

    if 'cookies' in msg._connection_header:
        print ("%s just offered me %s cookies"%(who, msg._connection_header['cookies']))
    else:
        print ("I just heard %s from %s" % (chatter, who))
    

def listener_header():

    rospy.Subscriber("chatter", String, callback)
    rospy.init_node('sub_connection_header', anonymous=True)
    rospy.spin()
        

if __name__ == '__main__':
    try:
        listener_header()
    except KeyboardInterrupt, e:
        pass
