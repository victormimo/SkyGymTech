#This code is run with Hall_Speed_June_26_Directional
import serial
import time
import numpy as np
import matplotlib.pyplot as plt

arduino = serial.Serial('COM5', 9600, timeout=.1)

prev_A = 0
prev_B = 0

t_A = -0.0001
t_B = -0.0001
t_B_old = -0.0001
radius = 0.04 # m
way = 0;
reps = 0;
oldway = 0;
reptime = 0
sets = 0
A = 0
B = 0

def arduino_pin(letter, data_in):
    if letter in data_in:
        data_out = filter(lambda x: x.isdigit(), data)
        data_out = float(data_out)
        return data_out

def rising_edge(prev, pres):
    cur_t = time.clock()
    return cur_t

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:

        A_input = arduino_pin("A", data)
        B_input = arduino_pin("B", data)
        if A_input == 0 or A_input == 1:
            # print time.time()
            A = A_input
            # print "A:"
            # print A
            # print prev_A
        if B_input == 0 or B_input == 1:
            B = B_input
            # print "B:"
            # print B
            # print prev_B
        if prev_A == 0 and A == 1:
            t_A = time.clock()
        prev_A = A
        if prev_B == 0 and B == 1:
            t_B = time.clock()
            if (t_A - t_B_old) < (t_B - t_A):
                way = 1
            else:
                way = -1
            vel = way * 2 * 3.14 * 0.04 / (t_B - t_B_old)
            print vel
            # print time.time()
            t_B_old = t_B
        prev_B = B

        if way == -1 and oldway == 1:
            reptime = time.time()
            reps = reps + 1
            print "sets:"
            print sets
            print "reps:"
            print reps
        oldway = way

        if (time.time() - reptime) >= 20 and reps > 0:
            reps = 0
            sets = sets + 1