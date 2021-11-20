#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import mediapipe as mp
import pyautogui as pg
import HandTrackingModule as htm
import numpy as np
import time
from math import *

pg.FAILSAFE = False


# In[2]:


def trackingBox(frame, horizontal, vertical, draw = True):
    # Probably should estimate values regarding the shape of the box and take in those values as arguments to this function
    x1, x2 = horizontal
    y1, y2 = vertical
    new_frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (192, 192, 192), 2)
    return new_frame


# In[3]:


def scale(cur, screenRange, horizontal, vertical):
    w, h = screenRange
    hCur, vCur = cur
    hMin, hMax = horizontal
    vMin, vMax = vertical
    hrange = hMax - hMin
    vrange = vMax - vMin
    x = (hCur - hMin) * w / hrange + 0
    y = (vCur - vMin) * h / vrange + 0
    
    return (x, y)
    
    


# In[4]:


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


# In[5]:


def valid(list):
    if len(list) != 0:
        return True
    else:
        return False


# In[6]:


def smoothing(x, y, prev_x, prev_y, smooth = 8):
    curr_x = prev_x + (x - prev_x)/smooth
    curr_y = prev_y + (y - prev_y)/smooth
    #prev_x, prev_y = curr_x, curr_y
    return (curr_x, curr_y)


# In[7]:


def lineTrack(frame, lmList, p1, p2, draw = True):
    if valid(lmList):
        startPoint = (lmList[p1][1], lmList[p1][2])
        endPoint = (lmList[p2][1], lmList[p2][2])
        
        if draw:
            frame = cv2.line(frame, startPoint, endPoint, (255, 255, 255), 9)
    return (frame, startPoint, endPoint)


# In[8]:


def length(start, end):
    x1, y1 = start
    x2, y2 = end
    x = (x2 - x1)**2
    y = (y2 - y1)**2
    return sqrt(x+y)


# In[9]:


def click(frame, lmList, draw = True):
    p1, p2 = 4, 13
    frame, start, end = lineTrack(frame, lmList, p1, p2, draw)
    lineLength = length(start, end)
    
    if lineLength < 70:
        return True
    else:
        return False
        


# In[10]:


def screenShot(frame, lmList, draw = True):
    p1, p2 = 8, 12
    frame, start, end = lineTrack(frame, lmList, p1, p2, draw)
    lineLength = length(start, end)
    
    ring = lmList[16][2] > lmList[14][2]
    pinky = lmList[20][2] > lmList[18][2]
    
    if lineLength < 50 and ring and pinky:
        return True
    else:
        return False


# In[11]:


def vKey(frame, lmList, draw = True):
    p1, p2 = 8, 4
    frame, start, end = lineTrack(frame, lmList, p1, p2, draw)
    lineLength = length(start, end)
    
    if lineLength < 60:
        return True
    else:
        return False


# In[12]:


width, height = pg.size()
print(width)
print(height)


# In[19]:


# Camera setup
wCam, hCam = 1280, 720
camera = cv2.VideoCapture(0)
if camera:
    camera.set(3, wCam)
    camera.set(4, hCam)

#smoothing = 8
prev_x, prev_y = 0, 0
clck = 0x5D
#dk.PressKey(clck)

# Hand object setup
detector = htm.handDetector(detectionCon = 0.75)


# In[20]:


while True:
    # Reading in every frame
    success, frame = camera.read()
    
    # Make the camera mirror
    frame = cv2.flip(frame, 1)
    
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw = False)
    
    #frame = trackingBox(frame)
    
    horizontal = (200, 840)
    vertical = (50, 330)
    
    frame = trackingBox(frame, horizontal, vertical)
    
    if len(lmList) != 0:
        
        # Cursor to index finger tracking
        cur = (lmList[8][1], lmList[8][2])
        cur1, cur2 = cur
        
        x, y = scale(cur, pg.size(), horizontal, vertical)
        curr_x, curr_y = smoothing(x, y, prev_x, prev_y)
        pg.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y
        
        #################################################
        # THUMB CLICKING (A clicked is performed when the thumb is closed)
        # This clicking seems to not work with certain things so please use direct keys.
        if pinkyFinger(lmList):
            break
        elif click(frame, lmList, draw = False):
            pg.click()
        elif vKey(frame, lmList, draw = False):
            pg.hotkey('ctrl', 'win', 'o')
        elif screenShot(frame, lmList, draw = False):
            pg.hotkey('win', 'printscreen')
        
       
        #if bothFingers(lmList) and lineLength < 65:
            #pg.mouseDown(button = 'left')
            #pg.click()
        #if allVKey(lmList):
            #pg.hotkey('ctrl','win','o')
            
        #if thumbClick(lmList):
            #cv2.putText(frame, f'click', (0, 150), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
            #pg.click()
        #if lineLength < 70:
            #pg.click()
        
        #if pinkyFinger(lmList):
            #break
    cv2.imshow("Screen Controller", frame)
        #if pinkyFinger(lmList):
            #break
    key = cv2.waitKey(1)
    if key in [27, ord('Q'), ord('q')]:
        break

# Close camera and window
camera.release()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




