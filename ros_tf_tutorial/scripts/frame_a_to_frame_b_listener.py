#!/usr/bin/env python  

import rospy
import tf
import geometry_msgs.msg
import turtlesim.srv

if __name__ == '__main__':

    rospy.init_node('frame_a_frame_b_listener_node')

    listener = tf.TransformListener()

    rate = rospy.Rate(1) # 1Hz

    # Wait 5 seconds as maximum to listen this transformation
    listener.waitForTransform('/frame_a', '/frame_b', rospy.Time(), rospy.Duration(5.0))
    
    while (not rospy.is_shutdown()):

        try:
            (trans, quat) = listener.lookupTransform('/frame_a', '/frame_b', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        rpy = tf.transformations.euler_from_quaternion(quat)

        print('Transformation between frame_a and frame_b detected:')
        print('Translation vector: x={0}, y={1}, z={2}'.format(trans[0], trans[1], trans[2]))   
        print('Rotation angles: roll={0}, pitch={1}, yaw={2}\n'.format(rpy[0], rpy[1], rpy[2]))

        rate.sleep()