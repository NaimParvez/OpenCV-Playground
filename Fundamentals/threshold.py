from pixel import imshow
import cv2
img_path='cat.jpg'

img=cv2.imread(img_path)
img = cv2.resize(img,(500,500))

img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#simple threshold
# ret,thresh=cv2.threshold(img_gray,80,250,cv2.THRESH_BINARY)
# thresh=cv2.blur(thresh,(10,10))
# ret,thresh=cv2.threshold(thresh,80,250,cv2.THRESH_BINARY)

#adaptive
thresh=cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,30)

imshow('frame',img)
imshow('thresh',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()


## threshold is used in OCR to detect text from a image