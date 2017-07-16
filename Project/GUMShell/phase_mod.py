import numpy as np

def sort(N, a):

    c = a.copy()

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

def getPhase(N, a):

    # Get the phase of the wave function by counting the necessary inversions
    # in the Slater determinant, as you restore it to normal ordering
    n_inv = 0

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            if(a[j] < a[i]):
                n_inv += 1

    phase = (-1)**n_inv

    return(phase)

# The name of this function is to be read as "a dagger a dagger a a"
# It calculates the action of the annihilation and creation operators on a
# Slater determinant
def adadaa(p, q, r, s, N, a):

    c = np.array(a)
    
    # Apply the operators a^+_p a^+_q a_r a_s on the vector a
    for i in range(0, N, 1):
        if r == a[i]:
            c[i] = p
        if s == a[i]:
            c[i] = q
            
    # Check for two or more particles with the same quantum numbers
    # It is more efficient to do it here, than below, since for large values of
    # N, it might be possible to skip the expensive calculation of the phase
    for i in range(0, N-1, 1):
        for j in range(i + 1, N, 1):
            if c[i] == c[j]:
                return(0, c)
    
    # Restore normal ordering and get the phase of the wave function in the
    # process
    phase = getPhase(N, c)
    c = np.sort(c)
    
    # Check for two or more particles with the same quantum numbers
    # This part should be left commented out
#    for i in range(0, N-1, 1):
#        if c[i] == c[i + 1]:
#            return(0, c)
    
    return(phase, c)
    

def bandp(p, q, r, s, N, a):

    point = 0
    c = a.copy()

    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if r == c[i] and s == c[j]:
                point = 1
                c[i] = p
                c[j] = q

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

def J_plus(p, tj, tm, N, a, sp, n_sp):

    point = 0
    c = a.copy()

    for i in range(0, N, 1):
        for j in range(n_sp):
            if (c[i] == sp[j][0] and p == sp[j][1] and tj == sp[j][2] and tm == sp[j][3]):
                for k in range(n_sp):
                    if (p == sp[k][1] and tj == sp[k][2] and tm + 2 == sp[k][3]):
                        point = 1
                        c[i] =  sp[k][0]


    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if c[i] == c[j]:
                point = 0

    if point == 0:
        phase = 0
        b = c[:]
    elif point == 1:
        phi, d = sort(N, c)
        phase = phi * np.sqrt((0.5*tj - 0.5*tm)*(0.5*tj + 0.5*tm + 1. ))
        b = d[:]

    return(phase, b)

def J_minus(p, tj, tm, N, a, sp, n_sp):

    point = 0
    c = a.copy()

    for i in range(0, N, 1):
        for j in range(n_sp):
            if (c[i] == sp[j][0] and p == sp[j][1] and tj == sp[j][2] and tm == sp[j][3]):
                for k in range(n_sp):
                    if (p == sp[k][1] and tj == sp[k][2] and tm - 2 == sp[k][3]):
                        point = 1
                        c[i] =  sp[k][0]


    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if c[i] == c[j]:
                point = 0

    if point == 0:
        phase = 0
        b = c[:]
    elif point == 1:
        phi, d = sort(N, c)
        phase = phi * np.sqrt((0.5*tj + 0.5*tm) * (0.5*tj - 0.5*tm + 1. ))
        b = d[:]

    return(phase, b)
