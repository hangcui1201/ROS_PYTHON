#!/usr/bin/env python

import rospy

# this is an example of using ROS built-in message
from std_msgs.msg import Header 
from std_msgs.msg import String
from std_msgs.msg import Int32 
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped


class PoseChange:

	def __init__(self):
		
		rospy.init_node("topic_pose_message", anonymous=True)

		rospy.Subscriber("/pose", Pose, self.pose_callback)

		self.pose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=3)

		self.msg = PoseWithCovarianceStamped()

		
	def pose_callback(self, pose_msg):

		self.msg.header = Header()
		self.msg.header.stamp = rospy.Time.now()
		self.msg.header.frame_id = "map"
		self.msg.pose.pose = pose_msg
		self.msg.pose.covariance = [ [0.09, 0, 0, 0, 0, 0],
			                         [0, 0.09, 0, 0, 0, 0],
			                         [0, 0, 0.09, 0, 0, 0],
			                         [0, 0, 0, 0.25, 0, 0],
			                         [0, 0, 0, 0, 0.25, 0],
			                         [0, 0, 0, 0, 0, 0.25] ]
			                         

	def run(self):
		self.pose_pub.publish(self.msg)


if __name__ == '__main__':

	try:
		pc = PoseChange()
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			connections = pc.pose_pub.get_num_connections()
			rospy.loginfo("Connection: %d", connections)
			if (connections > 0):
				pc.run()
				rospy.loginfo("Published once")
				break
			rate.sleep()
	except rospy.ROSInterruptException:
		raise e



