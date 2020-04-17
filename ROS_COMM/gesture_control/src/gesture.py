#!/usr/bin/env python
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
import rospy
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([255,173,127],np.uint8)

def findMove(frame1,frame2):

    frame1=cv2.GaussianBlur(frame1,(5,5),10)
    frame2=cv2.GaussianBlur(frame2,(5,5),10)

    frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2YCR_CB)
    frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2YCR_CB)

    region1=cv2.inRange(frame1,min_YCrCb,max_YCrCb)
    region2=cv2.inRange(frame2,min_YCrCb,max_YCrCb)

    cnts1,_=cv2.findContours(region1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts2,_=cv2.findContours(region2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    if len(cnts1) !=0 and len(cnts2) !=0:
        cnt1=max(cnts1,key=cv2.contourArea)
        cnt2=max(cnts2,key=cv2.contourArea)
        M1=cv2.moments(cnt1)
        M2=cv2.moments(cnt2)
        
        if(M1["m00"]!=0 and M2["m00"]!=0):
            x1=int(M1["m10"]/M1["m00"]) 
            #print(x1)
            x2=int(M2["m10"]/M2["m00"])
            #print(x2)
            y1=int(M1["m01"]/M1["m00"])
            #print(y1)
            y2=int(M2["m01"]/M2["m00"])
            #print(y2)

            if(np.abs(x2-x1)>np.abs(y2-y1)):
                if(x2>x1):
                    print("Left")
                    return 'l'#Camera is inverted
                else:
                    print("Right")
                    return 'r'
            else:
                if(y2>y1):#(0,0) is at top left, so inverted
                    print("Down")
                    return 'd'
                else:
                    print("Up")
                    return 'u'
def tracker():
    cap=cv2.VideoCapture(0)
    print("Start Motion")
    count =0
    _,frame1=cap.read()
    while count<11: 
        ret,frame=cap.read()
        count+=1
        if(count==10):
            frame2=frame
            print("Captured, now processing")
            direction=findMove(frame1,frame2)
    cap.release()
    return direction

from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_gesture', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    #Receiveing the user's input
    print("Let's move your robot")
    speed = 5#input("Input your speed:")
    distance = 2#input("Type your distance:")
    direction=tracker()
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    if direction=='r':
        vel_msg.linear.x = speed
    if direction=='l':
        vel_msg.linear.x = -speed
    if direction=='u':
        vel_msg.linear.y = speed
    if direction=='d':
        vel_msg.linear.y = -speed
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #Setting the current time for distance calculus
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            #Publish the velocity
            velocity_publisher.publish(vel_msg)
            #Takes actual time to velocity calculus
            t1=rospy.Time.now().to_sec()
            #Calculates distancePoseStamped
            current_distance= speed*(t1-t0)
        #After the loop, stops the robot
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        #Force the robot to stop
        velocity_publisher.publish(vel_msg)

move()
