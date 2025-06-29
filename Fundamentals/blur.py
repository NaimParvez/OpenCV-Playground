from pixel import imshow
import cv2
img_path='cat.jpg'

img=cv2.imread(img_path)
img = cv2.resize(img,(500,500))


k_size=3
img_blur=cv2.blur(img,(k_size,k_size))
img_gblur=cv2.GaussianBlur(img,(k_size,k_size))
img_mblur=cv2.medianBlur(img,(k_size,k_size))


imshow('frame',img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

## we can use blur to remove noise from the image ..
## medium blur works the best but depends on the blur..