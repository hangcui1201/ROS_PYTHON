#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
import numpy as np

"""
360 Laser Distance Sensor HLS-LFCD-LDS is a 2D laser scanner 
capable of sensing 360 degrees that collects a set of data 
around the robot to use for SLAM and Navigation. 

/scan   --  sensor_msgs/LaserScan

std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id

float32 angle_min
float32 angle_max
float32 angle_increment
float32 time_increment
float32 scan_time
float32 range_min
float32 range_max
float32[] ranges
float32[] intensities

"""

def min_range_index(ranges):
	min_dist = np.nanmin(ranges)
	min_dist_index = ranges.index(min_dist)
	return (min_dist, min_dist_index)

def max_range_index(ranges):
	max_dist = np.nanmax(ranges)
	max_dist_index = ranges.index(max_dist)
	return (max_dist, max_dist_index)

def average_range(ranges):
    ranges = [x for x in ranges if not np.isnan(x)]
    return (sum(ranges)/float(len(ranges)))

def average_between_indices(ranges, i, j):
	slice_of_array = ranges[i: j+1]
	slice_of_array = [x for x in slice_of_array if not np.isnan(x)]
	return (sum(slice_of_array)/float(len(slice_of_array)))

def field_of_view(scan_data):
    return (scan_data.angle_max-scan_data.angle_min)*180.0/np.pi


def laserscan_callback(scan_data):

	# print("The minimum distance value is %s mm" % (scan_data.range_min*1000.0))
	# print("The maximum distance value is %s mm" % (scan_data.range_max*1000.0))
	# print("The angle increment is %s degrees" % (scan_data.angle_increment*180.0/np.pi))

	min_value, min_index = min_range_index(scan_data.ranges)
	print("The minimum measured distance: {0} m and index: {1}".format(min_value, min_index))

	max_value, max_index = max_range_index(scan_data.ranges)
	print("The maximum measured distance: {0} m and index: {1}".format(max_value, max_index))

	average_value = average_range (scan_data.ranges)
	print("The average distance of all measured values: {0} m".format(average_value))

	index_start = 20
	index_end = 100
	average_btw_index = average_between_indices(scan_data.ranges, index_start, index_end)
	print("The average distance between index {0} and {1}: {2} m".format(index_start, index_end, average_btw_index))

	print("The field of view of laser sensor: {0} degrees\n".format(field_of_view(scan_data)))


if __name__ == '__main__':
    
    rospy.init_node('laser_scan_node', anonymous=True)

    rospy.Subscriber("scan", LaserScan, laserscan_callback)

    rospy.spin()