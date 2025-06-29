# test_display.py
import cv2
from pixel import imshow

img_path = "cat.jpg"
img = cv2.imread(img_path)
img = cv2.resize(img, (500, 500))

imshow('My Image Viewer', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
