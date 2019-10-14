import PIL
from PIL import Image, ImageTk
import pytesseract
import cv2
import numpy as np
from tkinter import *
from sevaQR import *
from sevaSQL import *
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
width, height = 320, 240
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()
a=0
def show_frame():

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

    global a
    if (GPIO.input(36) == GPIO.HIGH) and (decodedObjects != "no QR codes") and (decodedObjects != "many QR codes"):
        print(decodedObjects[0].data.decode())
        print(insert_into_sql(decodedObjects[0].data.decode()))
        
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()
print("sss")