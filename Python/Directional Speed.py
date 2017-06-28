#This code is run with Hall_Speed_June_26_Directional
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

arduino = serial.Serial('COM5', 9600, timeout=.1)
vel_old = 1
rep = 0
set = 0
vel_list = []

#while True:
while rep < 5:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        vel = float(data)
        print vel
        if (vel > -7 and vel < 7):
            if (vel_old<=0 and vel>0):
                if (rep!=0):
                    if (time.time()-reptime > 10):
                        rep = 0
                        set = set +1
                rep = rep +1
                reptime = time.time()
            vel_old = vel
            vel_list.append(vel)
            print rep
            print vel_list
            print len(vel_list)
x = np.arange(0, len(vel_list), 1);
y = vel_list
plt.plot(x, y)
plt.title("Our First Velocity Graph")
plt.ylabel("Velocity (m/s)")
plt.show()
