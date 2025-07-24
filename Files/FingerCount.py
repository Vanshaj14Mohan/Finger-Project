import cv2
import time
import os
import HandTrackingModule as htm  # Importing custom hand tracking module

# Set camera resolution
weightCam, heightCam = 640, 480

# Initialize webcam capture
cap = cv2.VideoCapture(0)
cap.set(3, weightCam)  # Set width
cap.set(4, heightCam)  # Set height

# Load finger images from folder
folderPath = "FingerImage"
myList = os.listdir(folderPath)  # List all image filenames in the folder
print(myList)

overlayList = []  # List to store loaded images
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')  # Read each image
    overlayList.append(image)  # Add to the overlay list

print(len(overlayList))  # Print how many images were loaded

pTime = 0  # For FPS calculation

# Initialize the hand detector with 0.75 detection confidence
detector = htm.HandDetector(detectionCon=0.75)

# IDs for the tips of each finger according to MediaPipe
tipsIds = [4, 8, 12, 16, 20]

# Main loop
while True:
    success, img = cap.read()  # Read frame from webcam
    img = detector.findHands(img)  # Detect hands and draw landmarks
    lmList = detector.findPosition(img, draw=False)  # Get landmark list without drawing

    if len(lmList) != 0:
        fingers = []

        # ----- Thumb -----
        # For right hand: if tip (id 4) is to the right of joint (id 3), it's open
        if lmList[tipsIds[0]][1] > lmList[tipsIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # ----- Other 4 Fingers -----
        # If tip is above the middle joint, the finger is open
        for id in range(1, 5):
            if lmList[tipsIds[id]][2] < lmList[tipsIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Count the number of fingers open
        totalFingers = fingers.count(1)
        print(totalFingers)

        # Display corresponding finger image overlay
        h, w, c = overlayList[totalFingers-1].shape
        img[0:h, 0:w] = overlayList[totalFingers-1]

        # Draw a filled green rectangle on the screen
        cv2.rectangle(img, (20, 275), (170, 475), (0, 255, 0), cv2.FILLED)

        # Put the total finger count as text inside the rectangle
        cv2.putText(img, str(totalFingers), (45, 425),
                    cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Show the final output frame
    cv2.imshow("Image", img)

    # Break loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

