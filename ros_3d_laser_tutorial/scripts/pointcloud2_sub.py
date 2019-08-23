#!/usr/bin/env python

import rospy
from roslib import message
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.msg import PointCloud2, PointField

import csv

stamp = None
stamp_str = None
stamp_count = 0   # in seconds

data_len = 0

record_secs = 5
record_laser = []

head_str = "time x y z intensity ring"
record_laser.append(head_str)

def pointcloud2_callback(pc_msg) :

	"""
	std_msgs/Header header
	  uint32 seq
	  time stamp
	  string frame_id
	uint32 height  
	uint32 width   
	sensor_msgs/PointField[] fields
	  uint8 INT8=1
	  uint8 UINT8=2
	  uint8 INT16=3
	  uint8 UINT16=4
	  uint8 INT32=5
	  uint8 UINT32=6
	  uint8 FLOAT32=7
	  uint8 FLOAT64=8
	  string name
	  uint32 offset
	  uint8 datatype
	  uint32 count
	bool is_bigendian
	uint32 point_step
	uint32 row_step
	uint8[] data
	bool is_dense
	"""
	global stamp
	global stamp_str
	global stamp_count
	global record_laser
	global record_secs
	global data_len

	stamp_curr = pc_msg.header.stamp.secs

	if(stamp != stamp_curr):
		stamp = stamp_curr
		stamp_str = str(stamp)
		stamp_count += 1
		print("time:{0}, data points:{1}".format(stamp, len(record_laser)-data_len))
		data_len = len(record_laser)
		record_laser.append("\n")

	# record record_secs seconds data points
	if(stamp_count <= record_secs):
		for p in pc2.read_points(pc_msg, field_names = ("x", "y", "z", "intensity", "ring"), skip_nans=True):
			# print("time:%s x:%s y:%s z:%s intensity:%s ring:%s" % (stamp_str, p[0], p[1], p[2], p[3], p[4]))
			txyz_str = "%s %s %s %s %s %s" % (stamp_str, p[0], p[1], p[2], p[3], p[4])
			record_laser.append(txyz_str)
	else:
		with open("record_laser.csv", "w") as outfile:
			for entries in record_laser:
				outfile.write(entries)
				outfile.write("\n")
		print("End Record")

def main():
    rospy.init_node('point_cloud_node', anonymous=True)
    rospy.Subscriber("/velodyne_points", PointCloud2, pointcloud2_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
