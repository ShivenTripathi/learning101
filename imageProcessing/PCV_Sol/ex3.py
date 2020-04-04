import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
im=cv2.imread("noise.jpg")
blur=cv2.GaussianBlur(im,(5,5),1)
cv2.imwrite("quo.jpg", np.hstack((im,blur,im/blur)))
