#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import RecognizeModuleStarter as rms


# In[2]:


def northHand(lmList):
    # The points closest to the left of the window have lower values.
    if len(lmList) != 0:
        # distances between 1st index and middle knuckles
        horizontalDistance = (lmList[9][1] - lmList[5][1])
        # vertical direction is unimportant
        verticalDistance = abs(lmList[9][2] - lmList[5][2])

        north = (horizontalDistance > verticalDistance)

        if north:
            return 1
        else:
            return 0


# In[3]:


def eastHand(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        # distances between 1st index and middle knuckles
        verticalDistance = (lmList[9][2] - lmList[5][2])
        # horizontal direction is unimportant
        horizontalDistance = abs(lmList[9][1] - lmList[5][1])
 
        east = (verticalDistance > horizontalDistance)
        
        if east:
            return 1
        else:
            return 0


# In[4]:


def westHand(lmList):
    # The points closest to the top of the window have lower values.
    if len(lmList) != 0:
        # distances between 1st index and middle knuckles
        verticalDistance = (lmList[5][2] - lmList[9][2])
        # horizontal direction is unimportant
        horizontalDistance = abs(lmList[9][1] - lmList[5][1])
 
        west = (verticalDistance > horizontalDistance)

        if west:
            return 1
        else:
            return 0


# In[5]:


def southHand(lmList):
    # The points closest to the left of the window have lower values.
    if len(lmList) != 0:
        # distances between 1st index and middle knuckles
        horizontalDistance = (lmList[5][1] - lmList[9][1])
        # vertical direction is unimportant
        verticalDistance = abs(lmList[9][2] - lmList[5][2])

        south = (horizontalDistance > verticalDistance)
        
        if south:
            return 1
        else:
            return 0


# In[6]:


def startRecognizingHandDirection():
    rms.start(recognizeHandDirection)


# In[7]:


def recognizeHandDirection(lmList, frame):
    if northHand(lmList):
        cv2.putText(frame, f'Pointing north', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif eastHand(lmList):
        cv2.putText(frame, f'Pointing east', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif westHand(lmList):
        cv2.putText(frame, f'Pointing west', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    elif southHand(lmList):
        cv2.putText(frame, f'Pointing south', (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        return True
    return False


# In[8]:


if __name__ == "__main__":
    startRecognizingHandDirection()

