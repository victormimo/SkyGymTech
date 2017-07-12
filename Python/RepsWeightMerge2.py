#This code is run with Hall_Speed_June_26_Directional
import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import MySQLdb

arduino = serial.Serial('COM5', 9600, timeout=.1)

rep_list = []
set_weight_list = []
reps = 0
sets = 0
A = B = C = D = E = F = G = 0
weight_list = [0, 0, 0, 0, 0]
leave = 0
up = 0
reptime = t_up = time.time()
change = 0

def arduino_pin(letter, data_in):
    if letter in data_in:
        data_out = filter(lambda x: x.isdigit(), data)
        data_out = float(data_out)
        return data_out

def check_weight(A, B, C, D, E, weight_list):
    if A == 1 and B == 1 and C == 1 and D == 1 and E == 1:
        weight = 0
    elif B == 1 and C == 1 and D == 1 and E == 1:
        weight = 10
        weight_list[0] += 1
    elif C == 1 and D == 1 and E == 1:
        weight = 20
        weight_list[1] += 1
    elif D == 1 and E == 1:
        weight = 30
        weight_list[2] += 1
    elif E == 1:
        weight = 40
        weight_list[3] += 1
    else:
        weight = 50
        weight_list[4] += 1
    return (weight, weight_list)

def weight_list_max(weight_list):
    weight_order = [10, 20, 30, 40, 50]
    max_loc = weight_list.index(max(weight_list))
    return weight_order[max_loc]

while leave == 0:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        # print data
        A_input = arduino_pin("A", data)
        B_input = arduino_pin("B", data)
        C_input = arduino_pin("C", data)
        D_input = arduino_pin("D", data)
        E_input = arduino_pin("E", data)
        F_input = arduino_pin("F", data)
        G_input = arduino_pin("G", data)
        if A_input == 0 or A_input == 1:
            A = A_input
        if B_input == 0 or B_input == 1:
            B = B_input
        if C_input == 0 or C_input == 1:
            C = C_input
        if D_input == 0 or D_input == 1:
            D = D_input
        if E_input == 0 or E_input == 1:
            E = E_input
        if F_input == 0 or F_input == 1:
            F = F_input
        if G_input == 0 or G_input == 1:
            G = G_input

        if up == 0 and A == 1 and (time.time() - reptime) > 0.2:
            reps = reps + 1
            up = 1
            t_up = time.time()
            change = 1
            if reps == 1:
                weight, weight_list = check_weight(C, D, E, F, G, weight_list)
        else:
            change = 0
        #
        # print "up"
        # print up

        if up == 1 and A == 1 and (time.time() - t_up)> 1:
            up = 0
            reptime = time.time()

        if change == 1:
            print "sets:"
            print sets
            print "reps:"
            print reps
            print weight

        if (time.time() - reptime) >= 10 and reps > 0:
            rep_list.extend([reps])
            reps = 0
            sets = sets + 1
            set_weight_list.extend([weight])
            print set_weight_list
        if (time.time() - reptime) >= 20:
            leave = 1
print "final:"
print sets
print rep_list
print set_weight_list