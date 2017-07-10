import numpy as np

def sort(N, a):

    c = a[:]

    number = 0
    p = 0

    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if(c[j] < c[i]):
                number += 1
                p = c[i]
                c[i] = c[j]
                c[j] = p

    phase = (-1)**number

    return(phase, c)

def Jcalc(p, tj, tm, N, a):

    point = 0
    c = a[:]

    basis = np.loadtxt("0s1s.txt")
    basis_size = np.shape(basis)[0]

    for i in range(0, N, 1):
        for j in range(basis_size):
            if (c[i] == basis[j][0] and p == basis[j][1] and tj == basis[j][2] and tm == basis[j][3]):
                for k in range(basis_size):
                    if (p == basis[k][1] and tj == basis[k][2] and tm + 2 == basis[k][3]):
                        point = 1
                        c[i] =  basis[k][0]


    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if c[i] == c[j]:
                point = 0

    if point == 0:
        phase = 0
        b = c[:]
    elif point == 1:
        phase, d = sort(N, c)
        b = d[:]

    return(phase, b)

#print(bandp(7, 8, 1, 2, 4, [1, 2, 3, 4]))
