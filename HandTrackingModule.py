import cv2
import mediapipe as mp
import time

class handDetector():
    def __init__(self, mode = False, maxHands = 2, modelComplex = 1, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
    
    
    def findHands(self, img, draw = True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
    
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                
        return img
    
    
    def findPosition(self, img, handNo = 0, draw = True):
        lmList = []
        
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
        
            for iD, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                lmList.append([iD, cx, cy])
                
                if draw:
                    cv2.circle(img, (cx, cy), 55, (255, 0, 255), cv2.FILLED)
        return lmList

    def fingerCombination(self, lmList):
        
        #the fingers are represented in binary manner. If a finger is shown it is 
        #represented as 1 and if it is not it is represented as 0 starting from pinky.
        #e.g. if only pinky is raised it will give the value 1(00001)
        #if middle and index is raised, the value is 00110
        #if thumb is raised, the value is 10000

        fingerNum = 0
        if len(lmList) != 0:
            index = lmList[8][2] < lmList[6][2]
            middle = lmList[12][2] < lmList[10][2]
            ring = lmList[16][2] < lmList[14][2]
            pinky = lmList[20][2] < lmList[18][2]
            thumb = lmList[4][1] < lmList[3][1]

            if pinky:
                fingerNum += 10**0
            if ring: 
                fingerNum += 10**1
            if middle: 
                fingerNum += 10**2
            if index:
                fingerNum += 10**3
            if thumb:
                fingerNum += 10**4
        return fingerNum

    
def main():
    # Initialize webcam
    cam = cv2.VideoCapture(0)
    
    # Initialize time variables: Previous Time = pTime, Current Time = cTime
    pTime = 0
    cTime = 0
    
    # Creating a handDetector object
    detector = handDetector()
    
    while True:
        # Read frames from webcam
        success, frame = cam.read()
        
        # Send frames to detector object
        frame = detector.findHands(frame)
            
        # Creating list of hand landmark data
        lmList = detector.findPosition(frame)
            
        # Checking if the list is empty or not
        if len(lmList) != 0:
            print(lmList[4])
        
        # Track Frames per Seconds (FPS)
        cTime = time.time()
        FPS = 1 / (cTime - pTime)
        pTime = cTime
        
        # Displays the FPS value onto the frame
        cv2.putText(frame, str(int(FPS)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        # Display frames in a new window called Camera
        cv2.imshow('Camera', frame)
        
        # Exits or breaks when user presses the Q key, q key, or the Esc key
        key = cv2.waitKey(1)
        if key in [27, ord('Q'), ord('q')]:
            break
            
    # Close window
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()