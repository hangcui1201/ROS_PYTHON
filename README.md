## ROS Tutorials (Python)


### Lesson 1: ROS Topic Tutorial

#### Terminal 1  
$ source devel/setup.bash  
$ roscore  

#### Terminal 2  
$ source devel/setup.bash  
$ rosrun ros_topic_tutorial topic_publisher.py  

#### Terminal 3  
$ source devel/setup.bash  
$ rosrun ros_topic_tutorial topic_subscriber.py  

#### Terminal 4  
$ source devel/setup.bash  
$ rostopic echo /ros_msg_change  

#### Terminal 5  
$ source devel/setup.bash  
$ rosrun ros_topic_tutorial topic_pub_once.py  


### Lesson 2: ROS Service Tutorial

#### Terminal 1  
$ source devel/setup.bash  
$ roscore  

#### Terminal 2  
$ source devel/setup.bash  
$ rosrun ros_service_tutorial service_server.py  

#### Terminal 3  
$ source devel/setup.bash  
$ rosrun ros_service_tutorial service_client.py 11 12  



### Lesson 3: ROS Action Tutorial

#### Terminal 1  
$ source devel/setup.bash  
$ roscore  

#### Terminal 2  
$ source devel/setup.bash  
$ rosrun ros_action_tutorial action_server.py  

#### Terminal 3  
$ source devel/setup.bash  
$ rosrun ros_action_tutorial action_client.py  



### Lesson 4: ROS Parameters Tutorial

#### Terminal 1
$ source devel/setup.bash  
$ roscore  

#### Terminal 2
$ source devel/setup.bash  
$ rosrun ros_parameter_tutorial service_param_server.py  

#### Terminal 3
$ source devel/setup.bash  
$ rosrun ros_parameter_tutorial service_param_client.py 10 5  

#### Terminal 4

$ rosservice list  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 2  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 3  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 4  
$ rosservice call /ros_service_param 10 5  



### Lesson 5: ROS TF Tutorial

#### Terminal 1
$ source devel/setup.bash  
$ rosrun ros_tf_tutorial tf_rotation_conversions.py  

#### Terminal 2
$ source devel/setup.bash  
$ rosrun ros_tf_tutorial tf_odom_sub.py  

#### Terminal 3
$ source devel/setup.bash  
$ roslaunch ros_tf_tutorial static_transform_publisher.launch  

#### Terminal 4
$ source devel/setup.bash  
$ rosrun tf view_frames  
$ rosrun tf tf_echo frame_a frame_b  

#### Terminal 5
$ source devel/setup.bash  
$ rosrun ros_tf_tutorial frame_a_to_frame_b_broadcaster.py  

#### Terminal 6
$ source devel/setup.bash  
$ rosrun ros_tf_tutorial frame_a_to_frame_b_listener.py  



### Lesson 6: ROS Navigation Tutorial

#### Terminal 1
$ source devel/setup.bash  
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch  

#### Terminal 2
$ source devel/setup.bash  
$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=/home/hang/ros/tb3_house_map.yaml  

#### Terminal 3
$ source devel/setup.bash  
$ rosrun ros_navigation_tutorial nav_goal.py  



### Lesson 7: ROS Image Tutorial

#### Terminal 1
$ source devel/setup.bash  
$ roslaunch usb_cam usb_cam.launch  

#### Terminal 2
$ source devel/setup.bash  
$ rosrun ros_image_tutorial image_pub_sub.py  



### Lesson 8: ROS Image RGBD Tutorial

#### Terminal 1
$ source devel/setup.bash  



### Lesson 9: ROS 2D Laser Tutorial

[HLS LFCD LDS 2D LASER DRIVER](https://github.com/ROBOTIS-GIT/hls_lfcd_lds_driver/tree/kinetic-devel)  

#### Terminal 1

$ source devel/setup.bash  
$ roslaunch hls_lfcd_lds_driver hlds_laser.launch  

#### Terminal 2

$ source devel/setup.bash  
$ roslaunch ros_2d_laser_tutorial tf_scan.launch  

#### Terminal 3
$ source devel/setup.bash  
$ rosrun rviz rviz  

#### Terminal 4
$ source devel/setup.bash  
$ rosrun ros_2d_laser_tutorial laserscan_sub.py  

#### Terminal 5
$ source devel/setup.bash  
$ rosrun ros_2d_laser_tutorial laserscan_pointcloud.py     

### Lesson 10: ROS 3D Laser Tutorial

#### Terminal 1
$ source devel/setup.bash  










