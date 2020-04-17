import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([255,173,127],np.uint8)

def findMove(frame1,frame2):

    frame1=cv2.GaussianBlur(frame1,(5,5),10)
    frame2=cv2.GaussianBlur(frame2,(5,5),10)

    frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2YCR_CB)
    frame2=cv2.cvtColor(frame2,cv2.COLOR_BGR2YCR_CB)

    region1=cv2.inRange(frame1,min_YCrCb,max_YCrCb)
    region2=cv2.inRange(frame2,min_YCrCb,max_YCrCb)

    # frame1=cv2.bitwise_and(frame1,frame1,mask=region1)
    # frame2=cv2.bitwise_and(frame2,frame2,mask=region2)

    _,cnts1,_=cv2.findContours(region1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    _,cnts2,_=cv2.findContours(region2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

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
                    print("Left")#Camera is inverted
                else:
                    print("Right")
            else:
                if(y2>y1):#(0,0) is at top left, so inverted
                    print("Down")
                else:
                    print("Up")
            # cv2.circle(frame1,(x1,y1),7,(255,0,0),-1)
            # cv2.circle(frame2,(x2,y2),7,(255,0,0),-1)
            # cv2.imshow('frame1',frame1)
            # cv2.imshow('frame2',frame2)
            # cv2.waitKey(0)
    print("Finished")

cap=cv2.VideoCapture(0)
print("Start Motion")
count =0
ret,frame1=cap.read()
while count<11: 
    ret,frame=cap.read()
    count+=1
    #print(count)
    if(count==10):
        frame2=frame
        print("Captured, now processing")
        # print(np.shape(frame1))
        # print(np.shape(frame2))
        findMove(frame1,frame2)
#findMove(frame1,frame2)
cap.release()
#cv2.destroyAllWindows()