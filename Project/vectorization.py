import numpy as np
import matplotlib.pyplot as plt
import time

x = range(8)
y1 = []
y2 = []
y3 = []

for i in range(8):
    
    ARRAY_SIZE = 10**i
    
    print(ARRAY_SIZE)

    array = np.random.rand(ARRAY_SIZE)
    array2 = np.copy(array)
    
    squaresum = 0.
    
    START1 = time.time()
    ###########################################################################
    # Method using for loop
    ###########################################################################

    for a in range(ARRAY_SIZE):
        squaresum += array2[a]*array2[a]
       
    ###########################################################################

    STOP1 = time.time()
    
    print("\tConventional loop:", STOP1 - START1, "seconds, result = ", squaresum)
    y1.append(STOP1 - START1)
    
    array2 = np.copy(array)
    
    START2 = time.time()
    
    ###########################################################################
    # Method using numpy vectors
    ###########################################################################

    squaresum = np.sum(array2*array2)

    ###########################################################################

    
    STOP2 = time.time()
    
    print("\tNumpy:", STOP2 - START2, "seconds, result = ", squaresum)
    y2.append(STOP2 - START2)
    print()
    
    array2 = np.copy(array)
    
    squaresum = 0.
    
    START3 = time.time()
    
    ###########################################################################
    # Method using for loop and general exponential function
    ###########################################################################

    for a in range(ARRAY_SIZE):
        squaresum += array2[a]**2

    ###########################################################################
    
    STOP3 = time.time()
    
    print("\tExponential:", STOP3 - START3, "seconds, result = ", squaresum)
    y3.append(STOP3 - START3)
    print()


plt.xlabel(r"Exponent $10^n$")
plt.ylabel("Time / s")
plt.semilogy(x, y1, label="for")
plt.semilogy(x, y2, label="numpy")
plt.semilogy(x, y3, label="for with exponential")

plt.legend()