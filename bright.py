import cv2
# import cv2 for image reading, changing colors & finding the brightest point
import matplotlib.pyplot as plt
# import matplotlib.pyplot for creating rectangle around the brightest point
import numpy as np
# import numpy for doing mathematical operations on array

# cv2.imread is a cv2 function used to read the image
image = cv2.imread('star.jpg')
# cv2.imread is a cv2 function to resize the image
image1 =cv2.resize(image,(600,800))
# Displaying the rgb image
cv2.imshow('image_rgb',image1)
cv2.waitKey(0)

# converting the rgb image into grayscale as minMaxLoc function only takes single channel input
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# Locating the maximum brightest point
cv2.minMaxLoc(gray)
cv2.imshow('gray image', gray)
cv2.waitKey(0)
# (6.0, 248.0, (599, 13), (315, 461))
x_coordinate=cv2.minMaxLoc(gray)[3][0]
y_coordinate=cv2.minMaxLoc(gray)[3][1]
print("The Coordinates of the brightest point are :" ,x_coordinate,y_coordinate)

# To plot the rectangle around the brightest point
s=20
coordinate1=(x_coordinate+s,y_coordinate+s)
coordinate2=(x_coordinate-s,y_coordinate-s)
color=(255,0,0)
t=5

# To show the location of the brightest point on the image
brightest=np.copy(image1)
brightest=cv2.rectangle(brightest,coordinate1,coordinate2,color,t)
cv2.imshow('Bright Star',brightest)
cv2.waitKey(0)

# Output
# The Coordinates of the brightest point are : (315,461)
