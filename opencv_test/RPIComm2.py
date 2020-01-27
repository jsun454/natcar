import serial
import time
import sys
from lineFollow2 import lineFollow
sys.path.insert(1, '../pi_cam')
from timelapse2 import takePicture

def comm(firstAngle):
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1.65)
    try:
        s.write(str.encode(firstAngle))
        i = 1
        while True:
            response = s.readline()
            print(response)
            if response == b'DONE\r\n':
                takePicture(i)
                angle, shift = lineFollow(i)
                s.write(str.encode(chr(angle)))
                i+=1
    except KeyboardInterrupt:
        s.close()
    
# if __name__ == '__main__':
#     angle = '1'
#     comm(angle)             