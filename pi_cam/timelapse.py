from picamera import PiCamera
import os

takePhoto = True

def main():

    os.chdir('/home/pi/img')

    camera = PiCamera()
    camera.resolution = (640, 480)
    i = 0

    while takePhoto: 
        camera.capture('image{0:04d}.jpg'.format(i))
        i += 1
    
    camera.close()

main()