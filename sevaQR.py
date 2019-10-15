from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import pyqrcode, png, sys


def generate_QR(name, data):
    big_code = pyqrcode.create(str(data))
    big_code.png(name +'.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
    return "generate_QR"


def recognise_QR(im):
    decodedObjects = pyzbar.decode(im)

    # Print results
    if len(decodedObjects) == 1:
        # return decodedObjects[0].data.decode()
        return decodedObjects

    if len(decodedObjects) == 0:
        return "no QR codes"
    if len(decodedObjects) > 1:
        return "many QR codes"

#text="'lesha', '1997.10.4', 3.14, 0.1, 0.2, 0.4, 'oxygen2', 1"
#print(text[text.find("'")+1:text.find("'",2)])
#generate_QR("'lesha', '1997.10.4', 3.14, 0.1, 0.2, 0.4, 'oxygen2', 1")
'''im = cv2.imread('code.png')
print(recognise_QR(im)[0].data.decode())
'''