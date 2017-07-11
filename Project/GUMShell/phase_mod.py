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



def Jcalc(p, tj, tm, N, a, sp, n_sp):

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
        phase, d = sort(N, c)
        b = d[:]

    return(phase, b)
