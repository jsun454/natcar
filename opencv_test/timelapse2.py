from picamera import PiCamera
import os

# takePhoto = True

def takePicture(i):

    os.chdir('/home/pi/Desktop/images')

    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.capture('image{0:04d}.jpg'.format(i))
    
    camera.close()

# main()
