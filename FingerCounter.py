import cv2
import os                     #This is for Listing the Paths of the Images.
import time
import HTMFinalModule as htm    #Holds all the necessary functions for basic Gesture Control Ops.

detector = htm.detection()        #Object Creation.

########################################################

#Basic Variables needed.
cTime = 0
pTime = 0
wCam = 640
hCam = 480
lmList = []
overLayList = []    #This will be used to overlay the images one on top of another.

########################################################

#Camera Capture settings.
cap = cv2.VideoCapture(0)  #In-built default camera.
#Camera resolution is set as 640 X 480
cap.set(3, wCam)
cap.set(4, hCam)

########################################################

#Now the path listing and overlay structure.
folderPath = "FingerImages"             #As we are in the same directory with FolderImages as Sub-Directory.
myList = os.listdir(folderPath)         #Returns the list of files present in the FolderImages Directory.

for i in myList:
    image = cv2.imread(folderPath + "/" + i)    #This reads each picture in the directory and stores it in image.
    overLayList.append(image)                   #We append information of each picture read in the OverLayList.

########################################################

#Note : This Program here is for the Right Hand with Palm Facing Forward for Left Hand change the Code as per Logic.
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)    #To get the images as mirror image.
    img = detector.find_my_hands(img)   #To Draw the LandMarks for the Hand(refer to HTMFinalModule).

    handTipIds = [4,8,12,16,20]         #These are the Landmarks of tips of each finger of the Hand.
    fingers = []                        #A list needed to find the open and close fingers.

    lmList = detector.hand_position(img)        #These provide the co-ordinates of the landmarks.
    if len(lmList) != 0:

        #So we check the tip of each finger is above the 2nd landmark below it if yes then open and append 1.
        # If Finger is open we add 1 to the list [1,1,1,1,1] else [0].

        #This code is for thumb as it behaves differently we work here with left and right of the below landmark.
        if lmList[handTipIds[0]][1] < lmList[handTipIds[0]-2][1]:       #Left or right of the x-oridinate of 2.
            fingers.append(1)                                           #Thumb open.
        else:
            fingers.append(0)                                           #Thumb close.

        for i in range(1,5):                                            #Index,Middle,Ring,Little fingers.
            if lmList[handTipIds[i]][2] < lmList[handTipIds[i]-2][2]:   #Same logic but with y-ordinate.
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)                                                 #To check if it's working properly.
        total = sum(fingers)                                            #Sum of number of fingers.


        h,w,c = overLayList[total-1].shape                              #We take the dimensions of the image.
        img[0:h,0:w] = overLayList[total-1]                             #We overlay it with what we need.
        #For 0 we do -1 as thr last image to keep it as thr last image.
        cv2.rectangle(img,(5,370),(150,410),(255,255,255),2)
        cv2.putText(img, f'COUNT:{int(total)}', (10, 400), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

    #FPS Calculation.
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}',(10,450),cv2.FONT_HERSHEY_PLAIN,2,(255,255,255),2)
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)




