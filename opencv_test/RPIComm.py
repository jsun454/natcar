import serial
import time

def comm(angle):
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1.65)
    try:
        angleInt = ord(angle);
        s.write(str.encode(angle))
        while True:
            response = s.readline()
            print(response)
            time.sleep(0.1)
            s.write(str.encode(chr(angleInt)))
            angleInt-=1
            if angleInt == 60:
                angleInt = 115
    except KeyboardInterrupt:
        s.close()

def commReal(angle):
    s = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(1.65)
    s.write(str.encode(angle))
    try:
        while True:
            response = s.readline()
            if response == b'DONE\r\n':
                #take picture
                #send to processing
                #output angle
                s.write(str.encode(angle))    
    except KeyboardInterrupt:
        s.close()

#if __name__ == '__main__':
#    comm(angle)               