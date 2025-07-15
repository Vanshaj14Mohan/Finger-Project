import cv2
import time
import os

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

while True:
    success, img = cap.read()
    h,w,c = overlayList[0].shape
    # img[0:283, 0:200] = overlayList[0]
    img[0:h, 0:w] = overlayList[0]

    cv2.imshow("Image", img)
    cv2.waitKey(1)
