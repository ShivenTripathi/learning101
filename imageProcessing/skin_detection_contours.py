import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
import numpy as np
#import matplotlib.pyplot as plt

min_HSV = np.array([0, 0, 0], dtype = "uint8")
max_HSV = np.array([10, 10, 255], dtype = "uint8")
# Get pointer to video frames from primary device
image = cv2.imread("r1.png")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)

skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)
cv2.imwrite("r_b.png",skinRegionHSV)
cv2.imwrite("r_c.png",skinHSV)
#cv2.imwrite("detected_binary.jpg", np.hstack([image, skinRegionHSV]))
#contours, hierarchy = cv2.findContours(skinRegionHSV,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#img = cv2.drawContours(skinRegionHSV, contours, -1, (0,255,0), 3)
#cv2.imwrite("detected_binary_contours.jpg",img)
#print(contours)
