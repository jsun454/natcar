import serial
import time
import sys
# from lineFollow2 import lineFollow
from lineFollowLOCALTEST import handle_pic
sys.path.insert(1, '../pi_cam')
from timelapse2 import takePicture
from imgStream import initStream, closeStream

def comm(firstAngle):
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1.65)
    try:
        firstAngle = ord(firstAngle)
        if not isinstance(firstAngle, int):
            print("d")
            firstAngle = 150
#         firstAngle = 90 - firstAngle
#         firstAngle
        firstAngle = firstAngle/3.6
        firstAngle = firstAngle + 65
        firstAngle = int(firstAngle)
        s.write(str.encode(chr(firstAngle)))
        i = 1
        initStream()
        while True:
            response = s.readline()
            print(response)
            if response == b'DONE\r\n':
                takePicture(i)
                angle, shift = lineFollow(i)
                if angle is None:
                    angle = 120
                #time.sleep(0.2)
                angle = angle/3.6
                angle = angle + 65
                angle = int(angle)
                print(angle)
                s.write(str.encode(chr(angle)))
                i+=1
    except KeyboardInterrupt:
        s.close()

# if __name__ == '__main__':
#     angle = '1'
#     comm(angle)
