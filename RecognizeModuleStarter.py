import cv2
import HandTrackingModule as htm

# width and heigh of the camera
W_CAM, H_CAM = 640, 480

# the default detection confidence
DEFAULT_DETECTION_CON = 0.75

def start(recognizeCommand):
    r'''
     Starts looping until ^[, Q, or q is pressed while evaluating a
     recognition module command on the frame. This is a convenience
     function for a single recognition module.
     @param recognizeCommand : (list, numpy.ndarray) -> NoneType
         = a command for recognizing and reacting to hand gestures
     '''
    recognitions = RecognitionList(aggregateUntilTrue)
    recognitions.add(recognizeCommand)
    recognitions.start()

class RecognitionList:
    r'''
     A list of recognition modules that can be added to, started and
     called.
     '''

    def __init__(self, aggregate):
        r'''
         Creates a new empty recognition list.
         @param aggregate : (list, list, numpy.ndarray) -> NoneType =
             a command for aggregating the listeners; a strategy on how
             to notify each listener
         '''
        self.listeners = []         # 
        self.aggregate = aggregate  # the aggregation strategy

    def add(self, recognizeCommand):
        r'''
         Adds the given recognition module command to listen to gestures.
         @param recognizeCommand : (list, numpy.ndarray) -> NoneType
             = a command for recognizing and reacting to hand gestures
         '''
        self.listeners.append(recognizeCommand)

    def call(self, lmList, frame):
        r'''
         Calls each recognition module command with the given landmark
         list and frame, according to the aggregator command.
         @param lmList : list = landmark list representing the hand
         @param frame : numpy.ndarray = represents the camera frame
         '''
        self.aggregate(self.listeners, lmList, frame)

    def start(self):
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

def aggregateUntilTrue(listeners, lmList, frame):
    r'''
     Aggregates listeners by calling them in order until one returns
     true.
     @param listeners : list<(list, numpy.ndarray) -> NoneType> = list
         of recognition listeners
     @param lmList : list = landmark list representing the hand
     @param frame : numpy.ndarray = represents the camera frame
     '''
    for command in listeners:
        # if a listener returns true, then stop
        if (command(lmList, frame)):
            return

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
