import serial
import time
import numpy
import math
import matplotlib
import matplotlib.pyplot as plt
from drawnow import *

accelX = []
accelY = []
accelZ = []
accelAvg = []

xAxis = 0
yAxis = 0
zAxis = 0

#ser = serial.Serial('COM3', 9600, timeout=0) #port on Windows
ser = serial.Serial('/dev/ttyACM0',9600,timeout=0) #port on Linux
plt.ion()

def makeChart():
    plt.title("Axis Avg")
    plt.grid(True)
    plt.ylabel("Axis acceleration")
    plt.plot(accelAvg)
    #plt.show(block=True)    

def main():
    cnt = 0
    plt.show(block=True)
    while True:
        #ser.write(".")
        line = ser.readline()
        axis = line.split(",")
	print axis
	if len(axis) == 3:
            yAxis = float(axis[1])
            accel_avg = math.sqrt((xAxis*xAxis)+(yAxis*yAxis)+(zAxis*zAxis))
            print accel_avg
	    accelX.append(xAxis)
            accelY.append(yAxis)
            accelZ.append(zAxis)
            accelAvg.append(accel_avg)
            plt.pause(.0000001)
            drawnow(makeChart)
            cnt = cnt+1
            if(cnt>50):
                accelX.pop(0)
                accelY.pop(0)
                accelZ.pop(0)
                accelAvg.pop(0)

if __name__ == '__main__': main()
