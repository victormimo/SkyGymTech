#This code is run with Hall_Speed_June_26_Directional
import serial
import time
import numpy as np
import matplotlib.pyplot as plt
import MySQLdb

arduino = serial.Serial('COM5', 9600, timeout=.1)

prev_A = 0
prev_B = 0

t_A = -0.0001
t_B = -0.0001
t_B_old = -0.0001
radius = 0.04
rep_list = []
set_weight_list = []
way = 0
reps = 0
oldway = 0
reptime = time.time()
sets = 0
A = B = C = D = E = F = G = 0
weight_list = [0, 0, 0, 0, 0]
leave = 0

def arduino_pin(letter, data_in):
    if letter in data_in:
        data_out = filter(lambda x: x.isdigit(), data)
        data_out = float(data_out)
        return data_out

def rising_edge(prev, pres):
    cur_t = time.clock()
    return cur_t

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



            # print "letters"
            # print C, D, E, F, G
            weight, weight_list = check_weight(C, D, E, F, G, weight_list)

            print "weight:"
            print weight

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

        if (time.time() - reptime) >= 10 and reps > 0:
            rep_list.extend([reps])
            reps = 0
            sets = sets + 1
            set_weight = weight_list_max(weight_list)
            set_weight_list.extend([set_weight])
            print set_weight_list
        if (time.time() - reptime) >= 20:
            leave = 1
print "final:"
print sets
print rep_list
print set_weight_list

# db = MySQLdb.connect(host="sql9.freemysqlhosting.net",  # your host, usually localhost
#                      user="sql9182609",  # your username
#                      passwd="AN2ffn1RAh",  # your password
#                      db="sql9182609")  # name of the data base
#
# # you must create a Cursor object. It will let
# # you execute all the queries you need
# cur = db.cursor()
#
# # ___INSERT DATA TO LOG TABLE___
# # Variables to go in table
# exercise = "Exercise Name"  # Name [string] (Max 20 Char)
# sets = sets  # N number of sets
# reps = rep_list  # List of length N [int]
# weights = [20, 20, 2, 20]  # List of length N [int]
# avg_vel = [0.67, 0.56, 0.45, 0.41]  # List of length N [float]
# rfid = "0012349093"  # 10 digit code [string]
#
# insert_query = "INSERT INTO log (exercise, sets, reps, weights, avg_vel, rfid, date_added)\
#             VALUES (\'" + exercise + "\'," + str(sets) + ",\'" + str(reps) + "\',\'" + \
#                str(weights) + "\',\'" + str(avg_vel) + "\',\'" + str(rfid) + "\',NOW())"
# print insert_query
# try:
#     cur.execute(insert_query)
#     db.commit()
# except:
#     db.rollback()
#
# # ___PRINT RESULTS___
# cur.execute("SELECT * FROM log")
#
# # print all the first cell of all the rows
# for row in cur.fetchall():
#     print row[1]
#
# db.close()
