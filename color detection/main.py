import cv2
from PIL import Image
from util import get_limits


yellow = [0, 255, 255]  # BGR color for yellow
webcam=cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    if not ret:
        break
    
    lower,upper=get_limits(yellow)
    mask = cv2.inRange(frame, lower, upper) # Create a mask for the color
    
    mask_=Image.fromarray(mask) # Convert the mask to a PIL Image for further processing
    
    bbox = mask_.getbbox()  # Get the bounding box of the non-zero regions
    if bbox:
        # Draw a rectangle around the detected color
        frame=cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
    
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()