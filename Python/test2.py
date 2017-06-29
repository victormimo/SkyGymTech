#This code is run with Hall_Speed_June_26_Directional
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

arduino = serial.Serial('COM5', 9600, timeout=.1)
# vel_old = 1
# rep = 0
# set = 0
# vel_list = []

prev_A = 0
prev_val_B = 0
# long t_A, t_B, cur_t  #time variables
t_A = -0.0001
t_B = -0.0001
radius = 0.04 # m
way = -1;
reps = 0;
oldway = 0;
reptime = 0
reptime2 = 0
set = 0
A = 0
B = 0

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        if "A" in data:
            A = filter(lambda x: x.isdigit(), data)
            A = float(A)
            print "A is: ", A
        if "B" in data:
            B = filter(lambda x: x.isdigit(), data)
            B = float(B)
            print "B is: ", B
    if prev_A == 0 and A == 1:
        cur_t = time.clock()
        vel = way*2*3.14*0.04 / (cur_t - t_A)
        t_A = cur_t
        prev_A = A

    if prev_B == 0 and B == 1:
        t_B = time.clock()

        # print vel
        # if (vel > -7 and vel < 7):
        #     if (vel_old<=0 and vel>0):
        #         if (rep!=0):
        #             if (time.time()-reptime > 10):
        #                 rep = 0
        #                 set = set +1
        #         rep = rep +1
        #         reptime = time.time()
        #     vel_old = vel
        #     vel_list.append(vel)
        #     print rep
        #     print vel_list
        #     print len(vel_list)
