## ROS Basic Tutorials (Python)

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

### Lesson 5: ROS Image Tutorial

#### Terminal 1
$ source devel/setup.bash  
$ roslaunch usb_cam usb_cam.launch  

#### Terminal 2
$ source devel/setup.bash  
$ rosrun ros_image_tutorial image_pub_sub.py  

### Lesson 6: ROS 2D Laser Scanner Tutorial

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












