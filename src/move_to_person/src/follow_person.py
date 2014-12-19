#!/usr/bin/env python
# license removed for brevity
# Need to figure out how to read data from human/pose as it provides the position
# of the human using geometry_msgs/PoseStamped
# Possibly missing dependecies
# Just moving the robot requires simply inputting coordinates for messagr.pose...
# position.xyz to move towards the person it requires the coordinates from the
# human/pose topic.
# Possibly use Rosbag, will reasearch over xmas
import rospy
from geometry_msgs.msg import PoseStamped

def move_1mf():
    pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.init_node('move_1mf', anonymous=True)
    r = rospy.Rate(5) # 5hz
    #hold value of x,y,z and orientaion or w - will be used when reading in from file
    x,y,z,w = 2.0,0.0,0.0,1.0
    while not rospy.is_shutdown():
        message = PoseStamped()
        message.header.frame_id = '/map'
        message.pose.position.x = human/pose.x
        message.pose.position.y = human/pose.y
        message.pose.position.z = human/pose.z
        message.pose.orientation.x = 0.0
        message.pose.orientation.y = 0.0
        message.pose.orientation.z = 0.0
        message.pose.orientation.w = w
       # rospy.loginfo('moving to X: ',x, ' Y :',y,' Z:',z,' and oriention of: ',w)
        pub.publish(message)
        r.sleep()

if __name__ == '__main__':
    try:
        move_1mf()
    except rospy.ROSInterruptException: pass
