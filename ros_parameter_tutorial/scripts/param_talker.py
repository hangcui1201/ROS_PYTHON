#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def param_talker():

    rospy.init_node('param_talker')

    # Fetch values from the Parameter Server. 
    # Fetch parameters from three different namespaces:
    #
    # 1) global (/global_example)
    # 2) parent (/foo/utterance)
    # 3) private (/foo/param_talker/topic_name)

    # Fetch a global parameter
    global_example = rospy.get_param("/global_example")
    rospy.loginfo("Parameter %s is %s", rospy.resolve_name('/global_example'), global_example)
    
    # Fetch the utterance parameter from our parent namespace
    utterance = rospy.get_param('utterance')
    rospy.loginfo("Parameter %s is %s", rospy.resolve_name('utterance'), utterance)
    
    # Fetch topic_name from the ~private namespace
    topic_name = rospy.get_param('~topic_name')
    rospy.loginfo("Parameter %s is %s", rospy.resolve_name('~topic_name'), topic_name)

    # Fetch a parameter, using 'default_value' if it doesn't exist
    default_param = rospy.get_param('default_param', 'default_value')
    rospy.loginfo('Parameter %s is %s', rospy.resolve_name('default_param'), default_param)
    
    # Fetch a group (dictionary) of parameters
    gains = rospy.get_param('gains')
    p, i, d = gains['P'], gains['I'], gains['D']
    rospy.loginfo("Gains are %s, %s, %s", p, i, d)    

    # Set some parameters
    rospy.loginfo('Setting parameters ...')
    rospy.set_param('list_of_floats', [1., 2., 3., 4.])
    rospy.set_param('bool_True', True)
    rospy.set_param('~private_bar', 1+2)
    rospy.set_param('to_delete', 'baz')
    rospy.loginfo('Parameters have been set')

    # Delete a parameter
    if rospy.has_param('to_delete'):
        rospy.delete_param('to_delete')
        rospy.loginfo("Deleted %s parameter" % rospy.resolve_name('to_delete'))
    else:
        rospy.loginfo('Parameter %s was already deleted' % rospy.resolve_name('to_delete'))

    # Search for a parameter
    param_name = rospy.search_param('global_example')
    rospy.loginfo('Found global_example parameter under key: %s' % param_name)
    
    # Publish the value of utterance repeatedly
    pub = rospy.Publisher(topic_name, String, queue_size=10)
    
    while not rospy.is_shutdown():
        pub.publish(utterance)
        rospy.loginfo(utterance)
        rospy.sleep(1)
        

if __name__ == '__main__':

    try:
        param_talker()
    except rospy.ROSInterruptException: 
    	pass
    
