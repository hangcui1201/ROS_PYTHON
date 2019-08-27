#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
from laser_geometry import LaserProjection
import sensor_msgs.point_cloud2 as pc2

import numpy as np

class Laser2PC():

	def __init__(self):

		self.laserProj = LaserProjection()
		self.pcPub = rospy.Publisher("/laserPointCloud", PointCloud2, queue_size=1)
		self.laserSub = rospy.Subscriber("/scan", LaserScan, self.laserCallback, queue_size=1)


	def laserCallback(self, msg):

		pc2_msg = self.laserProj.projectLaser(msg)
		self.pcPub.publish(pc2_msg)

		# Convert it to a generator of the individual points
		point_generator = pc2.read_points(pc2_msg)

		# Access a generator in a loop
		sum_points = 0.0
		num = 0
		for point in point_generator:
			if not np.isnan(point[2]):
				sum_points += point[2]
				num += 1

		# Calculate the average z value for example
		print("Average height: " + str(sum_points/num))


if __name__ == '__main__':
	
	rospy.init_node("laserscan_to_pointcloud")
	laser2PC = Laser2PC()
	rospy.spin()