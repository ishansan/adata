import serial
import thread
import time
import math
from plotcat import *

data = [0 for i in range(0, 1000)]
xAxis = 0
yAxis = 0
zAxis = 0
p = plotter(number_of_samples=1000)
ser = serial.Serial('/dev/ttyACM0',115200,timeout=0)

def get_vals():
	while True:
		line = ser.readline()
		axis = line.split(",")
		if len(axis) == 3:
			try:
				xAxis = float(axis[0])
				yAxis = float(axis[1])
				zAxis = float(axis[2])
				accel_avg = math.sqrt((xAxis*xAxis)+(yAxis*yAxis)+(zAxis*zAxis))*100
				print accel_avg
				data.append(accel_avg)
				data.pop(0)
			except:
				print "Exception"
				pass

@p.plot_self
def update_plot():
	try:
		p.lines[0][0].set_data(p.currentAxis[0],data)
	except:
		pass

if __name__ == '__main__':
	thread.start_new_thread(get_vals,())
	p.set_call_back(update_plot)
	plotter.show()