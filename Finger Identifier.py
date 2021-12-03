#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import RecognizeModuleStarter as rms


# In[2]:


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


# In[3]:


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


# In[4]:


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


# In[5]:


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


# In[6]:


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


# In[7]:


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


# In[ ]:


def startIdentifyingFingers():
    rms.start(identifyFingers)


# In[8]:


def identifyFingers(lmList, frame):
    if indexFinger(lmList):
        cv2.putText(frame, f'Index Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif middleFinger(lmList):
        cv2.putText(frame, f'Middle Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif ringFinger(lmList):
        cv2.putText(frame, f'Ring Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif pinkyFinger(lmList):
        cv2.putText(frame, f'Pinky Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif thumbFinger(lmList):
        cv2.putText(frame, f'Thumb Finger', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif allFingers(lmList):
        cv2.putText(frame, f'All Fingers', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    return False

