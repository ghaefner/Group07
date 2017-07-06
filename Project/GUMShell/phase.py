def sort(N, a):
    number = 0
    p = 0

    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if(a[j] < a[i]):
                number += 1
                p = a[i]
                a[i] = a[j]
                a[j] = p

    phase = (-1)**number

    return phase

def bandp(p, q, r, s, N, a):

    point = 0
    c = a

    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if r == a[i] and s == a[j]:
                point = 1
                a[i] = p
                a[j] = q

    for i in range(0, N - 1, 1):
        for j in range(i + 1, N, 1):
            if a[i] == a[j]:
                point = 0

    if point == 0:
        phase = 0
        b = c
    elif point == 1:
        phase = sort(N, a)
        b = a

    return phase, b
