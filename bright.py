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
plt.imshow(image)
cv2.imshow('image_rgb',image1)
cv2.waitKey(0)

# converting the rgb image into grayscale as minMaxLoc function only takes single channel input
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
# Locating the maximum brightest point
cv2.minMaxLoc(gray)
cv2.imshow('gray image', gray)
cv2.waitKey(0)
max_loc_x=cv2.minMaxLoc(gray)[3][0]
max_loc_y=cv2.minMaxLoc(gray)[3][1]
print("The Coordinates of the brightest point are :" ,max_loc_x,max_loc_y)

# To plot the rectangle around the brightest point
s=20
coord1=(max_loc_x+s,max_loc_y+s)
coord2=(max_loc_x-s,max_loc_y-s)
color=(255,0,0)
t=5

# To show the location of the brightest point on the image
brightest=np.copy(image1)
brightest=cv2.rectangle(brightest,coord1,coord2,color,t)
plt.imshow(brightest)
cv2.imshow('Bright Star',brightest)
cv2.waitKey(0)
