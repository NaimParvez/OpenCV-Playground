import cv2
import mediapipe as mp

img= cv2.imread("testImg.png")

mp_face_detection = mp.solutions.face_detection # Import the face detection module from MediaPipe

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
	# model_selection=0 uses the short range model, while model_selection=1 uses the full range model
	# min_detection_confidence=0.5 sets the minimum confidence threshold for face detection

	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert the image from BGR to RGB format
	out = face_detection.process(img_rgb)  # Process the image to detect faces
	if out.detections is not None:  # Check if any faces were detected
		for detection in out.detections:  # Iterate through the detected faces
			location = detection.location_data
			bbox = location.relative_bounding_box  # Get the bounding box of the detected face
			x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height  # Extract the coordinates and dimensions of the bounding box
			# frame = cv2.rectangle(img, (int(x1 * img.shape[1]), int(y1 * img.shape[0])), (int((x1 + w) * img.shape[1]), int((y1 + h) * img.shape[0])), (0, 255, 0), 2)  # Draw a rectangle around the detected face
			x1 = int(x1 * img.shape[1]) # Convert relative coordinates to absolute pixel values
			y1 = int(y1 * img.shape[0])
			w = int(w * img.shape[1])
			h = int(h * img.shape[0])
			img[y1:y1+h,x1:x1+w,:]=cv2.blur(img[y1:y1+h,x1:x1+w,:],(30,30))


cv2.imshow("Image",  img)  # Display the image with the detected face
cv2.waitKey(0)
cv2.destroyAllWindows()