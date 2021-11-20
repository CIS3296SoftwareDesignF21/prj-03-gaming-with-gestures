import cv2
import HandTrackingModule as htm

# width and heigh of the camera
W_CAM, H_CAM = 640, 480

# the default detection confidence
DEFAULT_DETECTION_CON = 0.75

def start(recognizeCommand):
    r'''
     Starts looping until ^[, Q, or q is pressed while evaluating a
     recognition module command on the frame.
     @param recognizeCommand : (list, numpy.ndarray) -> NoneType
         = a command for recognizing and reacting to hand gestures
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
    htm.recognizeGestures(camera, detector, recognizeCommand, frameFlip,
        drawPosition = False,
        fpsFormat = r'FPS: {}', org = (400, 70), color = (0,0,0))

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
