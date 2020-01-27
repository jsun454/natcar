from time import sleep
import picamera
import os

takePhoto = True

def main():

    os.chdir('/home/pi/Desktop/NATCAR/opencv_test/img')

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    #sleep(2)
    i = 0
    
    #while takePhoto:
    for x in range(3):
        camera.capture('image{0:04d}.jpg'.format(i))
        i += 1
    camera.close()
#main()