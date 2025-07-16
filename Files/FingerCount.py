# import cv2
# import time
# import os

# weightCam, heightCam = 640, 480

# #Initialize WebCam Capture
# cap  = cv2.VideoCapture(0)
# cap.set(3, weightCam)
# cap.set(4, heightCam)

# folderPath = "FingerImage"
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for impath in myList:
#     image = cv2.imread(f'{folderPath}/{impath}')
#     # print(f'{folderPath}/{impath}') verifying
#     overlayList.append(image)

# print(len(overlayList))

# while True:
#     success, img = cap.read()
#     h,w,c = overlayList[0].shape
#     # img[0:283, 0:200] = overlayList[0]
#     img[0:h, 0:w] = overlayList[0]

#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

import cv2
import time
import os
import HandTrackingModule as htm

# Initialize camera dimensions
widthCam, heightCam = 640, 480

# Initialize WebCam Capture
cap = cv2.VideoCapture(0)
cap.set(3, widthCam)  # 3 is for width
cap.set(4, heightCam)  # 4 is for height

# Load overlay images
folderPath = "FingerImage"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    if image is not None:
        overlayList.append(image)
    else:
        print(f"Failed to load image: {impath}")

if not overlayList:
    print("No images loaded successfully")
    exit()

print(f"Loaded {len(overlayList)} overlay images")

pTime = 0
detector = htm.HandDetector(detectionCon=0.75)

tipIds = [4,8,12,15,20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    #print(lmList)

    if len(lmList) != 0:
        for id in range(0,5):
        if lmList[8][2] < lmList[6][2]:
            print("Index Finger Opened")

    if not success:
        print("Failed to capture frame")
        break

    
    # Apply overlay if images exist
    if overlayList:
        h, w, c = overlayList[0].shape
        img[0:h, 0:w] = overlayList[0]
    
    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), 
               cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
