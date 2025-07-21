import cv2
import time
import os
import HandTrackingModule as htm

weightCam, heightCam = 640, 480

#Initialize WebCam Capture
cap  = cv2.VideoCapture(0)
cap.set(3, weightCam) # set width
cap.set(4, heightCam) # set height

folderPath = "FingerImage"
myList = os.listdir(folderPath)
print(myList)

overlayList = []
for impath in myList:
    image = cv2.imread(f'{folderPath}/{impath}')
    # print(f'{folderPath}/{impath}') verifying
    overlayList.append(image)

print(len(overlayList))# Printing length
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
        #For Thumb
        if lmList[tipsIds[0]][1] > lmList[tipsIds[0]-1][1]:
            # print("Index Finger Opened")
            fingers.append(1)
        else:
            fingers.append(0)

        #For 4 Fingers
        for id in range(1,5):
            if lmList[tipsIds[id]][2] < lmList[tipsIds[id]-2][2]:
                # print("Index Finger Opened")
                fingers.append(1)
            else:
                fingers.append(0)
        #print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers) # Printing total fingers

        h,w,c = overlayList[totalFingers-1].shape
        #img[0:283, 0:200] = overlayList[0]
        img[0:h, 0:w] = overlayList[totalFingers-1]

        cv2.rectangle(img, (20, 225), (170, 425), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 375), cv2.FONT_HERSHEY_PLAIN, 10, (255, 0, 0), 25)

    cTime = time.time()
    fps =  1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
