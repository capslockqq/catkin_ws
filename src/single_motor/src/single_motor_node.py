#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

class myNode():
    def __init__(self):
        self.my_publisher = rospy.Publisher("/joint1/command",Float64)
        self.timer = rospy.Timer(rospy.Duration(5), self.on_timer)
        self.toggle = False
    
    def on_timer(self, eventArg):
	rospy.loginfo("timer tick")
	if self.toggle:
		self.my_publisher.publish(1.5)
	else:
		self.my_publisher.publish(-1.5)
	
	self.toggle = not self.toggle
               
            
if __name__ == "__main__":
    rospy.init_node("lol")
    node = myNode()
    rospy.spin()
