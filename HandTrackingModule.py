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
    
    # Creating a handDetector object
    detector = handDetector()
    
    # start the recognition loop
    recognizeGestures(cam, detector, recognizeThumbEnd, frameNoop)


def recognizeGestures(cam, detector, recognizeCommand, frameTransform,
        drawPosition = True,
        fpsFormat = r'{}', org = (10, 70), color = (255, 0, 255)):
    r'''
     Loops until ^[, Q, or q is pressed while evaluating a recognition
     module command on the frame.
     @param cam : cv2.VideoCapture = video capture from a camera
     @param detector : htm.handDetector = parses a camera frame for
         hand data
     @param recognizeCommand : (list, numpy.ndarray) -> NoneType
         = a command that recognizes and reacts to hand gestures
     @param frameTransform : numpy.ndarray -> numpy.ndarray = a command
         that transforms a camera frame for further processing and
         display
     @param drawPosition : bool = whether to draw positions of key
         landmarks on the frame
     @param fpsFormat : str = formatting for frames per second
     @param org : (int,)*2 = coordinates of point of origin (bottom
         left corner)
     @param color : (int,)*3 = RGB triplet for text color on camera
     '''
    # Initialize time variables: Previous Time = pTime, Current Time = cTime
    pTime = 0
    cTime = 0
    
    while True:
        # Read frames from webcam
        success, frame = cam.read()

        # perform any necessary camera transformations
        frame = frameTransform(frame)
        
        # Send frames to detector object
        frame = detector.findHands(frame)
            
        # Creating list of hand landmark data
        lmList = detector.findPosition(frame, draw = drawPosition)
        
        # call the recognition command
        recognizeCommand(lmList, frame)
        
        #Code for images
        #h, w, c = overlayList[0].shape
        #img[0:h, 0:w] = overlayList[0]
        
        
        # Track Frames per Seconds (FPS)
        cTime = time.time()
        FPS = int(1 / (cTime - pTime))
        pTime = cTime
        
        # Displays the FPS value onto the frame
        cv2.putText(frame, fpsFormat.format(FPS), org, cv2.FONT_HERSHEY_PLAIN, 3, color, 3)
        
        # Display frames in a new window called Camera
        cv2.imshow('Camera', frame)
        
        # Exits or breaks when user presses the Q key, q key, or the Esc key
        key = cv2.waitKey(1)
        if key in [27, ord('Q'), ord('q')]:
            break
            
    # Close window
    cam.release()
    cv2.destroyAllWindows()


def frameNoop(frame):
    r'''
     Does nothing to the frame.
     @return the unaltered frame
     '''
    return frame


def recognizeThumbEnd(lmList, frame):
    r'''
     Prints the location of the end of the thumb.
     @param lmList : list = landmark list representing the hand
     @param frame : numpy.ndarray = unused for this implementation, but
         represents the camera frame
     '''
    # Checking if the list is empty or not
    if len(lmList) != 0:
        print(lmList[4])


if __name__ == "__main__":
    main()
