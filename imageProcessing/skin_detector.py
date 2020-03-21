import cv2
import numpy as np
#import matplotlib.pyplot as plt

min_HSV = np.array([0, 48, 80], dtype = "uint8")
max_HSV = np.array([20, 255, 255], dtype = "uint8")
# Get pointer to video frames from primary device
image = cv2.imread("multiple_tone.jpg")
imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
skinRegionHSV = cv2.inRange(imageHSV, min_HSV, max_HSV)

skinHSV = cv2.bitwise_and(image, image, mask = skinRegionHSV)

cv2.imwrite("detected_tones.jpg", skinHSV)