import serial

weight_old = 5
A = B = C = D = E = 0
arduino = serial.Serial('COM8', 9600, timeout=.1)

print ("1")

def arduino_pin(letter, data_in):
    if letter in data_in:
        data_out = filter(lambda x: x.isdigit(), data)
        data_out = float(data_out)
        return data_out

def check_weight(A, B, C, D, E):
    if A == 1 and B == 1 and C == 1 and D == 1 and E == 1:
        weight = 0
    elif B == 1 and C == 1 and D == 1 and E == 1:
        weight = 10
    elif C == 1 and D == 1 and E == 1:
        weight = 20
    elif D == 1 and E == 1:
        weight = 30
    elif E == 1:
        weight = 40
    else:
        weight = 50
    return weight

while True:
    data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
    if data:
        print "3"
        A_input = arduino_pin("A", data)
        B_input = arduino_pin("B", data)
        C_input = arduino_pin("C", data)
        D_input = arduino_pin("D", data)
        E_input = arduino_pin("E", data)
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

        weight = check_weight(A, B, C, D, E)

        if weight != weight_old:
            print weight
        weight_old = weight
