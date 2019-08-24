#!/usr/bin/env python  

import rospy
import tf
import time  

"""
Broadcast a transformation between 
frame_a (parent) and frame_b (child)
"""

if __name__ == '__main__':

    rospy.init_node('frame_a_frame_b_broadcaster_node')
    
    time.sleep(2)

    # Create a transformation broadcaster (publisher)
    transform_broadcaster = tf.TransformBroadcaster()

    while(not rospy.is_shutdown()):

        # Create a quaternion, roll=0.2, pitch=0.3, yaw=0.1
        rotation_quat = tf.transformations.quaternion_from_euler(0.2, 0.3, 0.1)

        # Translation vector, x=1.0, y=2.0, z=3.0
        translation_vector = (1.0, 2.0, 3.0)

        # Time
        current_time = rospy.Time.now()

        transform_broadcaster.sendTransform(
            translation_vector, 
            rotation_quat,
            current_time, 
            "frame_b", "frame_a") # Child frame, Parent frame

        time.sleep(0.5)

    rospy.spin()

    