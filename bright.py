import cv2
import matplotlib.pyplot as plt

import numpy as np

image= cv2.imread('star.jpg')
image1=cv2.resize(image,(600,800))
#image_rgb=np.copy(image)
#image_rgb=cv2.cvtColor(image_rgb,cv2.COLOR_BGR2RGB)
plt.imshow(image)
cv2.imshow('image_rgb',image1)
cv2.waitKey(0)

gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
cv2.minMaxLoc(gray)
cv2.imshow('gray image', gray)
cv2.waitKey(0)
max_loc_x=cv2.minMaxLoc(gray)[3][0]
max_loc_y=cv2.minMaxLoc(gray)[3][1]
print(max_loc_x)
print(max_loc_y)

s=20
coord1=(max_loc_x+s,max_loc_y+s)
coord2=(max_loc_x-s,max_loc_y-s)
color=(255,0,0)
print(coord1,coord2)
t=5

brightest=np.copy(image1)
brightest=cv2.rectangle(brightest,coord1,coord2,color,t)
plt.imshow(brightest)
cv2.imshow('Bright Star',brightest)
cv2.waitKey(0)
