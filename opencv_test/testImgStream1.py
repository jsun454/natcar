import io
import os
import time
import picamera
#import threading
import cv2
import PIL
from PIL import Image
from time import sleep
import numpy as np

def main():
    stream = io.BytesIO()
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    time.sleep(2)

    camera.capture(stream,format='jpeg')
    
    stream.seek(0)
    
    
    data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(data,1)
    cv2.imwrite('test.jpg', img)
    # cv2.imshow('img', img)
    cv2.imshow('img', cv2.imread('test.jpg'))
    cv2.waitKey(0)

    
main()