import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import numpy as np
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
im=cv2.imread("shapes.jpg")
#blur=cv2.GaussianBlur(im,(5,5),1)
fil=np.array([[-1, -1, -1,], [-1, 8, -1],[-1,-1,-1]], np.int32)
outline=cv2.filter2D(im,-1,fil)
cv2.imwrite("outline_shapes.jpg", np.hstack((im,outline)))
