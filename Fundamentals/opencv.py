import cv2

# img_path= "image.jpg"
# img = cv2.imread(img_path)


# cv2.imshow("Image", img)
# cv2.waitKey(0)

#--------------video----------------


# video_path = "video.mp4"
# video = cv2.VideoCapture(video_path)
# ret = True
# while ret:
#     ret,frame = video.read()
#     if ret:
#         cv2.imshow('Video', frame)
#         cv2.waitKey(15)
        
# video.release()
# cv2.destroyAllWindows()


#--------------webcam----------------

# webcam=cv2.VideoCapture(0)

# while True:
#     ret, frame = webcam.read()
#     if not ret:
#         break
#     cv2.imshow("Webcam", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# webcam.release()
# cv2.destroyAllWindows()


#--------------img resize and crop----------------

img_path= "image.jpg"
img =cv2.imread(img_path)
print(img.shape)
img_resize=cv2.resize(img,(300,300))
print(img_resize.shape)
#crop
img_crop=img[200:400, 200:400] # y1:y2, x1:x2 axis

cv2.imshow("Image", img)
cv2.imshow("Resized Image", img_resize)
cv2.imshow("Cropped Image", img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()


