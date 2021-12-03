#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import RecognizeModuleStarter as rms


# In[2]:


def rock(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] < lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[3]:


def gnarly(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] < lmList[18][2]
        thumb = lmList[4][1] < lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[4]:


def peace(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
        middle = lmList[12][2] < lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[5]:


def fist(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[6]:


def loser(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
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


# In[8]:


def signA(lmList):
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


# In[9]:


def signB(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] < lmList[6][2]
        middle = lmList[12][2] < lmList[10][2]
        ring = lmList[16][2] < lmList[14][2]
        pinky = lmList[20][2] < lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[10]:


def signC(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        index = lmList[8][2] > lmList[6][2]
        middle = lmList[12][2] > lmList[10][2]
        ring = lmList[16][2] > lmList[14][2]
        pinky = lmList[20][2] > lmList[18][2]
        thumb = lmList[4][1] > lmList[3][1]
        
        if index and middle and ring and pinky and thumb:
            return 1
        else:
            return 0


# In[11]:


def signD(lmList):
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


# In[12]:


def startRecognizingStaticGestures():
    rms.start(recognizeStaticGestures)


# In[13]:


def recognizeStaticGestures(lmList, frame):
    if recognizeStaticSymbolGestures(lmList, frame):
        return True
    if recognizeStaticSignLanguageGestures(lmList, frame):
        return True
    return False


# In[14]:


def recognizeStaticSymbolGestures(lmList, frame):
    if rock(lmList):
        cv2.putText(frame, f'Rock', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif gnarly(lmList):
        cv2.putText(frame, f'Gnarly', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif peace(lmList):
        cv2.putText(frame, f'Peace', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif fist(lmList):
        cv2.putText(frame, f'Fist', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif loser(lmList):
        cv2.putText(frame, f'Loser', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif allFingers(lmList):
        cv2.putText(frame, f'All Fingers', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    return False


# In[15]:


def recognizeStaticSignLanguageGestures(lmList, frame):
    if signA(lmList):
        cv2.putText(frame, f'Sign Language A', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif signA(lmList):
        cv2.putText(frame, f'Sign Language B', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif signC(lmList):
        cv2.putText(frame, f'Sign Language C', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif signD(lmList):
        cv2.putText(frame, f'Sign Language D', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    return False


# In[16]:


if __name__ == "__main__":
    startRecognizingStaticGestures()

