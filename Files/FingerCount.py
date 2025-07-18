# import cv2
# import time
# import os

# widthCam, heightCam = 640, 480

# cap = cv2.VideoCapture(0)
# cap.set(3, widthCam)
# cap.set(4, heightCam)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Image", img)
#     cv2.waitKey(1)

import cv2
import time
import os
import HandTrackingModule as htm

weightCam, heightCam = 640, 480

#Initialize WebCam Capture
cap  = cv2.VideoCapture(0)
cap.set(3, weightCam)
cap.set(4, heightCam)

folderPath = "FingerImage"
myList = os.listdir(folderPath)
print(myList)

overlayList = []
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    # print(f'{folderPath}/{impath}') verifying
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.HandDetector(detectionCon=0.75)
tipsIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []
        for id in range(0,5):
            if lmList[tipsIds[id]][2] < lmList[tipsIds[id]-2][2]:
                # print("Index Finger Opened")
                fingers.append(1)
            else:
                fingers.append(0)
                
        print(fingers)

    h,w,c = overlayList[0].shape
    #img[0:283, 0:200] = overlayList[0]
    img[0:h, 0:w] = overlayList[0]

    cTime = time.time()
    fps =  1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


