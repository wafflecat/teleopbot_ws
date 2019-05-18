#!/usr/bin/env python

# References
# ----------
# https://andrewdai.co/xbox-controller-ros.html#rosjoy


# BEGIN ALL
import rospy
# from std_msgs.msg import String
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

# BEGIN KEYMAP
# key_mapping = { 'w': [ 0, 1], 'x': [0, -1], 
#                 'a': [1, 0], 'd': [-1,  0], 
#                 's': [ 0, 0] }
# END KEYMAP

# "joy" callback function
def joy_cb(msg, twist_pub):
    # BEGIN CB
    # if len(msg.data) == 0 or not key_mapping.has_key(msg.data[0]):
    #     return # unknown key.
    # vels = key_mapping[msg.data[0]]
    # END CB

    print(str(msg.axes[0]) + " " + str(msg.axes[1]))

    t = Twist()
    t.angular.z = msg.axes[0]
    t.linear.x  = msg.axes[1]
    twist_pub.publish(t)

    # MY DEBUG
    # print(t)


if __name__ == '__main__':
    rospy.init_node('keys_to_twist')
    twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    rospy.Subscriber('joy', Joy, joy_cb, twist_pub)
    rospy.spin()
# END ALL