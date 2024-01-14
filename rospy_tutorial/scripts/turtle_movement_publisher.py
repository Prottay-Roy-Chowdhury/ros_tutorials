#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('turtle_movement_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    while not rospy.is_shutdown():
        # Create a Twist message with linear and angular velocities
        twist_msg = Twist()
        twist_msg.linear.x = 1.0  # linear velocity (m/s)
        twist_msg.angular.z = 0.5  # angular velocity (rad/s)

        # Publish the Twist message
        pub.publish(twist_msg)

        rate.sleep()

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass
