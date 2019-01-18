#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String  #use String as a publisher
import RPi.GPIO as GPIO          #import GPIO fun
from time import sleep
GPIO.setmode(GPIO.BCM)       #use BCM pin Modes
GPIO.setup(23, GPIO.IN)      #IR1
GPIO.setup(24, GPIO.IN)      #IR2

def sensor():

    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('sensor', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        sensorValue_L = GPIO.input(23) #left IR
        sensorValue_R = GPIO.input(24) #right IR
        if (sensorValue_R==1 and sensorValue_L==0):
            #print for RIGHT turn
            right='R'
            rospy.loginfo(right)
            pub.publish(right)
            rate.sleep

        elif (sensorValue_R ==0 and sensorValue_L ==1):
            #print for LEFT turn
            left='L'
            rospy.loginfo(left)
            pub.publish(left)
            rate.sleep

        else:
            #print to go forward
            forward='F'    
            rospy.loginfo(forward)
            pub.publish(forward)
            rate.sleep()

if __name__ == '__main__':
    try:
        sensor()
    except rospy.ROSInterruptException:
        pass
