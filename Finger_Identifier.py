#!/usr/bin/env python
# coding: utf-8

# In[9]:


import cv2
import time
import os
import mediapipe as mp
import HandTrackingModule as htm


# In[10]:


def indexFinger(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[11]:


def middleFinger(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] < lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[12]:


def ringFinger(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] < lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[13]:


def pinkyFinger(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] < lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[14]:


def thumbFinger(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] < lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[15]:


def allFingers(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
        middle = lmList[12][2] < lmList[10][2]
        ring = lmList[16][2] < lmList[14][2]
        pinky = lmList[20][2] < lmList[18][2]
        thumb = lmList[4][1] < lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[16]:


wCam, hCam = 640, 480

camera = cv2.VideoCapture(0)

camera.set(3, wCam)
camera.set(4, hCam)

# For importing pictures
#folderPath = "FingerImages"
#myList = os.listdir(folderPath)

#overlayList = []

#for imPath in myList:
    #image = cv2.imread(f'{folderPath}/{imPath}')
    #overlayList.append(image)

pTime = 0

detector = htm.handDetector(detectionCon = 0.75)


# In[17]:


while True:
    success, frame = camera.read()
    
    frame = cv2.flip(frame, 1)
    
    frame = detector.findHands(frame)
    
    lmList = detector.findPosition(frame, draw = False)
    
    if indexFinger(lmList):
        cv2.putText(frame, f'Index Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    elif middleFinger(lmList):
        cv2.putText(frame, f'Middle Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    elif ringFinger(lmList):
        cv2.putText(frame, f'Ring Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    elif pinkyFinger(lmList):
        cv2.putText(frame, f'Pinky Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    elif thumbFinger(lmList):
        cv2.putText(frame, f'Thumb Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
    elif allFingers(lmList):
        cv2.putText(frame, f'All Fingers', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
   
    
    #Code for images
    #h, w, c = overlayList[0].shape
    #img[0:h, 0:w] = overlayList[0]
    
    
    # Calculating the Frames per Seconds (FPS)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # Displaying the FPS (ERROR PRINTING HIGH NUMBERS)
    cv2.putText(frame, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)
    
    cv2.imshow("Camera", frame)
    
    key = cv2.waitKey(1)
    if key in [27, ord('Q'), ord('q')]:
        break
        
camera.release()
cv2.destroyAllWindows()


# In[ ]:




