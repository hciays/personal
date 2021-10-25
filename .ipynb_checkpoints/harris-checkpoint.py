"""
This program demonstrates line finding of Corners with rhe Harris Corner Detector
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv



# Read in the image
image = cv.imread('h.jpg')

# Change the color of the image to grayscale
grays = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
gray = np.float32(grays)
# Detect corners 
dst = cv.cornerHarris(gray, 2, 3, 0.04)
    
# Dilate corner image to enhance corner points
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
image[dst>0.01*dst.max()]=[0,0,255] 

cv.imshow("Source", image)
cv.imshow("Grayscale Image", grays)
print(gray)
cv.imshow("Harris",dst)

#plt.imshow(image_copy)
cv.waitKey()