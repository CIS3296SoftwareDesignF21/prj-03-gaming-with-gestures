import cv2
import time
#import os
import mediapipe as mp
import HandTrackingModule as htm

def gameMovement(cameraVal):
  
    movementDict = {
                    'Forward': 11111, # all fingers
                    'Stop'   :     0, # no finger
                    'Left'   : 10000, # thumb
                    'Right'  :     1, # pinky
                    'Jump'   :  1100, # index and middle
                    'Fire'   : 11000  # thumb and index
                   }
    
    for movement, value in movementDict.items():
        if (cameraVal == value):
            return movement

def main():
    
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

    while True:
        success, frame = camera.read()
        
        frame = cv2.flip(frame, 1)
        
        frame = detector.findHands(frame)
        
        lmList = detector.findPosition(frame, draw = False)
        
        fingerComb = detector.fingerCombination(lmList)

        
        cv2.putText(frame, str(gameMovement(fingerComb)), (0, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 3)
        
        
        #Code for images
        #h, w, c = overlayList[0].shape
        #img[0:h, 0:w] = overlayList[0]
        
        cv2.putText(frame, 'Press Q to quit', (800, 700), cv2.FONT_HERSHEY_PLAIN, 3, (0,0,0), 3)

        
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

if __name__ == "__main__":
    main()