#___INITIALIZE___
import MySQLdb
 
db = MySQLdb.connect(host="sql9.freemysqlhosting.net",  # your host, usually localhost
                     user="sql9182609",                 # your username
                     passwd="AN2ffn1RAh",    		# your password
                     db="sql9182609")                   # name of the data base
 
# you must create a Cursor object. It will let
# you execute all the queries you need
cur = db.cursor()

#___INSERT DATA TO LOG TABLE___
#Variables to go in table
exercise = "Exercise Name"          #Name [string] (Max 20 Char)
sets = 4                            #N number of sets
reps = [6, 6, 4, 2]                 #List of length N [int]
weights = [40, 40, 45, 50]          #List of length N [int]
avg_vel = [0.67, 0.56, 0.45, 0.41]  #List of length N [float]
rfid = "0012349093"                 #10 digit code [string]


insert_query = "INSERT INTO log (exercise, sets, reps, weights, avg_vel, rfid, date_added)\
            VALUES (\'"+exercise+"\',"+str(sets)+",\'"+str(reps)+"\',\'"+\
            str(weights)+"\',\'"+str(avg_vel)+"\',\'"+str(rfid)+"\',NOW())"
print insert_query
try:
    cur.execute(insert_query)
    db.commit()
except:
    db.rollback()






#___PRINT RESULTS___
cur.execute("SELECT * FROM log")
 
#print all the first cell of all the rows
for row in cur.fetchall():
    print row[1]
 
db.close()
