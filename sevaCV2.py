import PIL
from PIL import Image, ImageTk
import pytesseract
import cv2
import numpy as np
from tkinter import *
from sevaQR import *
width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()

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

    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)

show_frame()
root.mainloop()