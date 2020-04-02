import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
#import matplotlib.pyplot as plt

# min_HSV = np.array([0, 230, 230], dtype = "uint8")
# max_HSV = np.array([20, 255, 255], dtype = "uint8")
# # Get pointer to video frames from primary device
# 
# imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)

# skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)
# image = cv2.imread("r1.png")
#cv2.imwrite("r_c.png", skinHSV)
im = cv2.imread("robot.jpg")
h,w=np.shape(im)[0],np.shape(im)[1]
print(h,w)
for i in range(h):
    j=w-1
    while(j>0):
        j-=1
        if(im[i][j][0]==0 and im[i][j][1]==0 and im[i][j][2]==255):
            x2,y2=i,j
            break

j=0
for j in range(w):
    i=0
    while(i<h-1):
        i+=1
        if(im[i][j][0]==0 and im[i][j][1]==0 and im[i][j][2]==255):
            x1,y1=i,j
            break

i=h-1
while(i>0):
    i-=1
    j=0
    while(j<w-1):
        j+=1
        if(im[i][j][0]==0 and im[i][j][1]==0 and im[i][j][2]==255):
            x3,y3=i,j
            break
j=w-1
while(j>0):
    j-=1
    i=h-1
    while(i>0):
        i-=1
        if(im[i][j][0]==0 and im[i][j][1]==0 and im[i][j][2]==255):
            x4,y4=i,j
            break
print(x1,y1)
print(x2,y2)
print(x3,y3)
print(x4,y4)


# h,w=np.shape(im)[0],np.shape(im)[1]
# print("og_image")
# print(h,w)
# for i in range(h):
#     j=w-1
#     while(j>0):
#         j-=1
#         if(im[i][j][1]==255):
#             x2,y2=i,j
#             cv2.circle(im,(x2,y2),10,(255,0,0),2)
#             break

# j=0
# for j in range(w):
#     i=0
#     while(i<h-1):
#         i+=1
#         if(im[i][j][1]==255):
#             x1,y1=i,j
#             cv2.circle(im,(x1,y1),10,(255,0,0),2)
#             break

# i=h-1
# while(i>0):
#     i-=1
#     j=0
#     while(j<w-1):
#         j+=1
#         if(im[i][j][1]==255):
#             x3,y3=i,j
#             cv2.circle(im,(x3,y3),10,(255,0,0),2)
#             break
# j=w-1
# while(j>0):
#     j-=1
#     i=h-1
#     while(i>0):
#         i-=1
#         if(im[i][j][1]==255):
#             x4,y4=i,j
#             cv2.circle(im,(x4,y4),10,(255,0,0),2)
#             break
# print(x1,y1)
# print(x2,y2)
# print(x3,y3)
# print(x4,y4)
# cv2.circle(im,(0,0),10,(255,0,0),2)
# #skinHSV=cv2.rectangle(skinHSV,(x1,y1),(x4,y4),(255,0,0),5)
# im=cv2.line(im,(x1,y1),(x2,y2),(0,255,0),5)
cv2.circle(im,(y1,x1),10,(255,0,0),2)
cv2.circle(im,(y2,x2),10,(255,0,0),2)
cv2.circle(im,(y3,x3),10,(255,0,0),2)
cv2.circle(im,(y4,x4),10,(255,0,0),2)
cv2.line(im,(y1,x1),(y2,x2),(255,0,0),5)
cv2.line(im,(y1,x1),(y3,x3),(255,0,0),5)
cv2.line(im,(y3,x3),(y4,x4),(255,0,0),5)
cv2.line(im,(y4,x4),(y2,x2),(255,0,0),5)
cv2.imwrite("rf1.jpg", im)
