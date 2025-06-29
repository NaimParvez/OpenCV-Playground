import os
import cv2
from pixel import imshow

img_path = "cat.jpg"
img = cv2.imread(img_path)
img = cv2.resize(img,(500,500))

img_rbg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # color changed to b->r, r->b
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) 

# cv2.imshow('image',img)
# cv2.imshow('img_rgb',img_rbg)
# cv2.imshow('img_gray',img_gray)
imshow("img_gray",img_gray)
# imshow("img_gray",img_hsv,'hsv') 

cv2.waitKey(0)