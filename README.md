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

$ rosservice list  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 2  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 3  
$ rosservice call /ros_service_param 10 5  

$ rosparam set /calculation_method 4  
$ rosservice call /ros_service_param 10 5  















