import PIL
from PIL import Image, ImageTk
import pytesseract
import cv2
import numpy as np
from tkinter import *
from sevaQR import *
from sevaSQL import *
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import *

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    decodedObjects = recognise_QR(frame)
    if (decodedObjects != "no QR codes") and (decodedObjects != "many QR codes"):
        points = decodedObjects[0].polygon

        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        for j in range(0, len(hull)):
            cv2.line(frame, hull[j], hull[(j + 1) % len(hull)], (255, 0, 0), 3)

    press_button = False
    
    if (GPIO.input(36) == GPIO.HIGH) and (decodedObjects != "no QR codes") and (decodedObjects != "many QR codes"):
        print(decodedObjects[0].data.decode())
        print(insert_into_sql(decodedObjects[0].data.decode()))
        frame = cv2.imread("working.png")
    

    cv2.namedWindow("test", cv2.WND_PROP_FULLSCREEN)          
    cv2.setWindowProperty("test", cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    cv2.imshow("test",frame)
    
    if cv2.waitKey(1) == 27: 
        break  # esc to quit

cv2.destroyAllWindows()