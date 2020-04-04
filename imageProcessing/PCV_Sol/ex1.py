import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
im=cv2.imread("noise.jpg")
#drawing=im
blur=cv2.GaussianBlur(im,(5,5),1)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 30, 200) 
#ret, thresh = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(edged, contours, -1, (0,255,0), 3)
cv2.imwrite("gblur.jpg", np.hstack((im,blur)))
cv2.imwrite("ctrs.jpg",edged)
