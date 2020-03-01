# from picamera import PiCamera
# import io
# import time
# import cv2
# import numpy as np

# stream = None

# def initStream():
#     global stream

#     # stream = io.BytesIO()
#     # with PiCamera() as camera:
#     #     camera.resolution = (640, 480)
#     #     camera.capture_continuous(stream, 'jpeg', use_video_port=True)

#     # while True:
#     #     try:
#     #         stream.seek(0)
#     #         data = np.fromstring(stream.getvalue(), dtype=np.uint8)
#     #         image = cv2.imdecode(data, 1)[:, :, ::-1]
#     #         cv2.imshow('Image', image)
#     #         stream.truncate()
#     #     except:
#     #         continue

#     stream = io.BytesIO()
#     with PiCamera() as camera:
#         camera.start_preview()
#         time.sleep(2)
#         camera.capture(stream, format='jpeg')
#     data = np.fromstring(stream.getvalue(), dtype=np.uint8)
#     image = cv2.imdecode(data, 1)
#     image = image[:, :, ::-1]
#     cv2.imshow('Image', image)

#     # with PiCamera() as camera:
#     #     camera.resolution = (640, 480)
#     #     camera.start_preview()
#     #     time.sleep(2)
#     #     while True:
#     #         camera.capture(stream, format='jpeg')
#     #         # camera.capture_continuous(stream, 'jpeg', use_video_port=True)
#     #     try:
#     #         data = np.fromstring(stream.getvalue(), dtype=np.uint8)
#     #         image = cv2.imdecode(data, 1)[:, :, ::-1]
#     #         cv2.imshow('Image', image)
#     #     except:
#     #         continue

# def closeStream():
#     global stream

#     if stream is not None:
#         stream.close()
#         stream = None

# def main():
#     initStream()

# main()

##############################################################

# import os
import io
import time
import picamera
import threading
from PIL import Image
from time import sleep

stream = io.BytesIO()
camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_preview()
time.sleep(2)
# takePhoto = True
# lock = Lock()

def thread_function():
    global stream
    global camera
    while True:
        # lock.acquire()
        camera.capture(stream, format='jpeg')
        # lock.release()
        # stream.seek(0)
        # stream.truncate()

def thread_function2():
    global stream
    global camera
    # lock.acquire()
    while True:
        try:
            stream.seek(0)
            image = Image.open(stream)
            image.show()
        except:
            continue
    # lock.release()

def main():

    # os.chdir('/home/pi/Desktop/images')

    # Create the in-memory stream
    x = threading.Thread(target=thread_function)
    y = threading.Thread(target=thread_function2)
    x.start()
    y.start()
    x.join()
    y.join()

    # "Rewind" the stream to the beginning so we can read its content

main()
