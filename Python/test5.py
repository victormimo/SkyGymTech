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

A = 1
B = 1
C = 0
D = 1
E = 1

weight = check_weight(A, B, C, D, E)

print weight