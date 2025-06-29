from pixel import imshow
import cv2


img_path='cat2.jpg'

img=cv2.imread(img_path)
img = cv2.resize(img,(500,500))

edge=cv2.Canny(img,100,200) # 100 is min threshold and 200 is max threshold 

imshow('frame',img)
imshow('edge',edge)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Canny edge detection is a popular edge detection algorithm that uses a multi-stage process to detect edges in an image.