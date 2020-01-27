import RPIComm2
import sys
import serial
from lineFollow2 import lineFollow
sys.path.insert(1, '../pi_cam')
from timelapse2 import takePicture

s = serial.Serial('/dev/ttyACM0', 9600)
takePicture(0)
a, shift = lineFollow(0)
s.write(str.encode(chr(a)))
RPIComm2.comm(chr(a))