import cv2
from sevaCV2 import *
while True:
    cv2.imshow('frame', frame_openCV())
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()