import cv2
import HandTrackingModule as htm

# width and heigh of the camera
W_CAM, H_CAM = 640, 480

# the default detection confidence
DEFAULT_DETECTION_CON = 0.75

class RecognitionList:
    r'''
     A list of recognition modules that can be added to, started and
     called.
     '''

    def __init__(self):
        r'''
         Creates a new empty recognition list.
         '''
        self.listeners = []

    def add(recognizeCommand):
        r'''
         Adds the given recognition module command to listen to gestures.
         @param recognizeCommand : (list, numpy.ndarray) -> NoneType
             = a command for recognizing and reacting to hand gestures
         '''
        self.listeners.append(recognizeCommand)

    def call(lmList, frame):
        r'''
         Calls each recognition module command with the given landmark
         list and frame.
         @param lmList : list = landmark list representing the hand
         @param frame : numpy.ndarray = represents the camera frame
         '''
        for command in self.listeners:
            # if a listener returns false, then stop
            if (not(self.listeners(lmList, frame))):
                break

    def start():
        r'''
         Starts looping until ^[, Q, or q is pressed while evaluating
         each recognition module command on the frame.
         '''
        # Initialize webcam
        camera = cv2.VideoCapture(0)
        camera.set(3, W_CAM)
        camera.set(4, H_CAM)
        
        # For importing pictures
        #folderPath = "FingerImages"
        #myList = os.listdir(folderPath)

        #overlayList = []

        #for imPath in myList:
            #image = cv2.imread(f'{folderPath}/{imPath}')
            #overlayList.append(image)

        # calibrate the confidence
        detectionCon = calibrate(camera)

        # Creating a handDetector object
        detector = htm.handDetector(detectionCon = detectionCon)
        
        # start the recognition loop
        htm.recognizeGestures(camera, detector, self.call,
            frameFlip,
            drawPosition = False,
            fpsFormat = r'FPS: {}', org = (400, 70), color = (0,0,0))
# class RecognitionList

def start(recognizeCommand):
    r'''
     Starts looping until ^[, Q, or q is pressed while evaluating a
     recognition module command on the frame. This is a convenience
     function for a single recognition module.
     @param recognizeCommand : (list, numpy.ndarray) -> NoneType
         = a command for recognizing and reacting to hand gestures
     '''
    recognitions = RecognitionList()
    recognitions.add(recognizeCommand)
    recognitions.start()

def calibrate(camera):
    r'''
     Calibrates the detection confidence given a camera. Currently
     just returns the default value.
     @return the default detection confidence
     '''
    return DEFAULT_DETECTION_CON

def frameFlip(frame):
    r'''
     Flips the camera frame to mirror the user actor.
     @return the flipped frame
     '''
    return cv2.flip(frame, 1)
