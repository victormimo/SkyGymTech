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
way = 0
reps = 0
oldway = 0
reptime = time.time()
sets = 0
A = 0
B = 0
leave = 0

def arduino_pin(letter, data_in):
    if letter in data_in:
        data_out = filter(lambda x: x.isdigit(), data)
        data_out = float(data_out)
        return data_out

def rising_edge(prev, pres):
    cur_t = time.clock()
    return cur_t

while leave == 0:
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

        if (time.time() - reptime) >= 4 and reps > 0:
            rep_list.extend([reps])
            reps = 0
            sets = sets + 1
        if (time.time() - reptime) >= 10:
            print "done"
            leave = 1

db = MySQLdb.connect(host="sql9.freemysqlhosting.net",  # your host, usually localhost
                     user="sql9182609",  # your username
                     passwd="AN2ffn1RAh",  # your password
                     db="sql9182609")  # name of the data base

# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

# ___INSERT DATA TO LOG TABLE___
# Variables to go in table
exercise = "Exercise Name"  # Name [string] (Max 20 Char)
sets = sets  # N number of sets
reps = rep_list  # List of length N [int]
weights = [20, 20, 2, 20]  # List of length N [int]
avg_vel = [0.67, 0.56, 0.45, 0.41]  # List of length N [float]
rfid = "0012349093"  # 10 digit code [string]

insert_query = "INSERT INTO log (exercise, sets, reps, weights, avg_vel, rfid, date_added)\
            VALUES (\'" + exercise + "\'," + str(sets) + ",\'" + str(reps) + "\',\'" + \
               str(weights) + "\',\'" + str(avg_vel) + "\',\'" + str(rfid) + "\',NOW())"
print insert_query
try:
    cur.execute(insert_query)
    db.commit()
except:
    db.rollback()

# ___PRINT RESULTS___
cur.execute("SELECT * FROM log")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[1]

db.close()
