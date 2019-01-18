#!/usr/bin/env python
#license removed for brevity
import rospy
from std_msgs.msg import String #use Int as a publisher
import RPi.GPIO as GPIO       #import GPIO fun
from time import sleep
                              #set the pinModes for SENSOR
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
#movement of robot for LINE follwer
def callback(data):
    rospy.loginfo("I heard %s", data.data)

    #enter the MOVEMENT conditions
    #left turn
    if (data.data=='R'):
        #motor RIGHT
        print ("RIGHT")
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        GPIO.output(22,GPIO.LOW)

        #sleep (0.5)
    elif(data.data=='L'):
        #motor_b
        print ("LEFT")
        GPIO.output(18, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)

    else:
        print ("FORWARD")
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(22,GPIO.LOW)        



        #sleep (0.5)



def motor():
    rospy.init_node('motor', anonymous=True)

    rospy.Subscriber("chatter", String , callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    motor()
