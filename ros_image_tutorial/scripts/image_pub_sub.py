#!/usr/bin/env python

from __future__ import print_function

import sys
import cv2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

	def __init__(self):

		self.bridge = CvBridge()
		self.image_pub = rospy.Publisher("webcam_image",Image, queue_size=10)
		self.image_sub = rospy.Subscriber("/usb_cam/image_raw", Image, self.callback)

		# Check if ROS is ready for operation
		while(rospy.is_shutdown()):
			print("ROS is shutdown!")

	def callback(self, data):

		try:
			# Convert ROS image to OpenCV image
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)

		(rows,cols,channels) = cv_image.shape

		if cols > 100 and rows > 100:
			cv2.circle(cv_image, (100,100), 30, (0,0,255))

		cv2.namedWindow("Image Window")
		cv2.imshow("Image Window", cv_image)
		cv2.waitKey(2)

		try:
			# Convert OpenCV image to ROS image and publish
			self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
		except CvBridgeError as e:
			print(e)

def main():

	ic = image_converter()
	rospy.init_node('ros_image_tutorial', anonymous=True)

	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down!")
    
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()