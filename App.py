import numpy as np
import cv2
import pafy

# live youtube video link
url = "https://www.youtube.com/watch?v=X_EWYemclKA"
vPafy = pafy.new(url)
play = vPafy.getbest(preftype="mp4")

cap = cv2.VideoCapture(play.url)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Error opening video stream or file")

fps = 60
# if you want to have the FPS according to the video then uncomment this code

# calculate the interval between frame.
interval = int(1000 / fps)
# print("FPS: ", fps, ", interval: ", interval)
# Read the video
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.namedWindow("Frames", cv2.WINDOW_NORMAL)

        both = np.concatenate((frame, gray), axis=1)

        cv2.imshow('Frames', both)
        if cv2.waitKey(interval) & 0xFF == ord('q'):
            break
    # Break the loop
    else:
        break

cap.release()
cv2.destroyAllWindows()
