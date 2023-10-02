# OpenCV(cv2) library - computer vision using webcam
# setting default web cam as inbuilt webam (0)
# frame for comparison
#continuous looping(capturing)
    #reading the frame read()
    #collect true or false in ret based on the detected frame
    # converting frame to grayscale for easy detection
    # bgr is converted to gray color
    # Applying Gaussianblur() - reduce noise
    # 21x21 -pixel kernel
#updating the previous frame
#difference calculation
# apply threshold to motion to detect motion
    #30 - pixel comparison if value<30 - set to 0 , value>=30 - 255
    #THRESH_BINARY - either 0 or 255, [1]- retive 2nd ele of tuple
# dialation - expanding white area in thresh obtained
    # None uses default 3x3 kernel, dialation is done twice
# findContours()- ftn in Opencv fro extracting contours of binary image
    #thresh.copy() keeping a copy of the threshhold image before findcontour modifies it
    #cv2.RETR_EXTERNAL - retive external contour by ingnoring the internal contour
    #cv2.CHAIN_APPROX_SIMPLE - removing redundant points, focus on shape of contour not the pixel location
    #contours - stores thresh.copy()
    #_ - indicating secont value returned by cv2.findContours()
#Line 57- indicating the moving areas using green rectangular boxes, 2- thickness of box
# show motion detection frame
# Update pframe
# press q to quit the loop
# relese the webcam and close all the windows of opencv

import cv2

ob = cv2.VideoCapture(0)
pframe = None

while True:
    ret, frame = ob.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if pframe is None:
        pframe = gray
        continue

    motion = cv2.absdiff(pframe, gray)
    thresh = cv2.threshold(motion, 30, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 500:  # checks area pixel less than 500
            continue

        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Motion Recognition", frame)
    pframe = gray

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

ob.release()
cv2.destroyAllWindows()
