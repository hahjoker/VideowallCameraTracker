#usage
#sudo python locationRetriever.py

import logging
import sys
import time
import os

from Adafruit_BNO055 import BNO055

bno = BNO055.BNO055(serial_port='/dev/ttyAMA0', rst=18)


#check mode of the sensor
count=0
if len(sys.argv) == 2 and sys.argv[1].lower() == '-v':
    logging.basicConfig(level=logging.DEBUG)

if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055')

while True:
    x, y, z, w = bno.read_quaternion()
    print 'x'
    print round(x,2)
    print 'y'
    print round(y,2)
    print 'z'
    print round(z,2)
    print 'w'
    print round(w,2)
    if(count==1):
        f=open('savedlocation.txt', 'w').close()
        f=open('savedlocation.txt', 'w')
        f.write(str(round(x,2)))
        f.write('\n')
        f.write(str(round(y,2)))
        f.write('\n')
        f.write(str(round(z,2)))
        #f.write('\n')
        #f.write(str(round(w,2)))
        f.flush()
        count+=1
    count+=1
    f=open('location.txt', 'w').close() #creating file, ensuring file exists
    f=open('location.txt', 'w')
    f.write(str(round(x,2)))
    f.write('\n')
    f.write(str(round(y,2)))
    f.write('\n')
    f.write(str(round(z,2)))
    #f.write('\n')
    #f.write(str(round(w,2)))
    f.flush()
    sys, gyro, accel, mag = bno.get_calibration_status()
    status, self_test, error = bno.get_system_status(run_self_test=False)
    if error != 0:
       print 'Error! Value: {0}'.format(error)
    time.sleep(1.0)
