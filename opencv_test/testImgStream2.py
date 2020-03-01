import io
import os
import time
import picamera
import threading
import cv2
import PIL
from PIL import Image
from time import sleep
import numpy as np

stream = io.BytesIO()
os.chdir('/home/pi/Desktop/temp')
i = 0
bufEmpty = True
camera = picamera.PiCamera()
camera.resolution = (640, 480)
time.sleep(2)
lock = threading.RLock()


def startStream():
    s = threading.Thread(target=imgStream)
    s.start()

def imgStream():
    global stream
    global camera
    global bufEmpty
    while True:
        camera.capture(stream,format='jpeg')
        bufEmpty = False

def show(img):
    with lock:
        try:
            cv2.imshow('hello', img)
            cv2.waitKey(0)
        except KeyboardInterrupt:
            cv2.destroyAllWindows()

def getImage():
    global stream
    global i
    global lock
    stream.seek(0)
    
    data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
    img = cv2.imdecode(data,1)
    try:
        showImg = threading.Thread(target=show, args=(img,))
        showImg.start()
    except RuntimeError:
        pass
    return img
    #cv2.imwrite('test' + str(i) + '.jpg', img)
    #cv2.imshow('img', cv2.imread('test' + str(i) + '.jpg'))
    #cv2.imshow('img', img)
    #cv2.waitKey(0)

def main():
    global bufEmpty
    s = threading.Thread(target=imgStream)
    
    s.start()
    
    while bufEmpty:
        continue

    for i in range(10):
        g = threading.Thread(target=getImage)
        g.start()
        g.join()
        
if __name__ == '__main__':
    main()
