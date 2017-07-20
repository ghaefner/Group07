import numpy as np
import matplotlib.pyplot as plt
import time

x = range(8)
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

N_ITERATIONS = 20

times = np.zeros((N_ITERATIONS, 5))

#for i in range(8):
i = 7

for j in range(N_ITERATIONS):
    print("Iteration:", j)

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
    
    print("\tExponential with int:", STOP3 - START3, "seconds, result = ", squaresum)
    y3.append(STOP3 - START3)

    array2 = np.copy(array)
    
    squaresum = 0.
    
    START4 = time.time()
    
    ###########################################################################
    # Method using for loop and general exponential function
    ###########################################################################

    for a in range(ARRAY_SIZE):
        squaresum += array2[a]**2.

    ###########################################################################
    
    STOP4 = time.time()
    
    print("\tExponential with float:", STOP4 - START4, "seconds, result = ", squaresum)
    y4.append(STOP4 - START4)

    array2 = np.copy(array)
    
    squaresum = 0.
    
    START5 = time.time()
    
    ###########################################################################
    # Method using for loop and general exponential function
    ###########################################################################

    for a in array:
        squaresum += a*a

    ###########################################################################
    
    STOP5 = time.time()
    
    print("\tPython-style for:", STOP5 - START5, "seconds, result = ", squaresum)
    y5.append(STOP5 - START5)
    print()
    
    times[j][0] = STOP1 - START1
    times[j][1] = STOP2 - START2
    times[j][2] = STOP3 - START3
    times[j][3] = STOP4 - START4
    times[j][4] = STOP5 - START5

print("Conventional loop: ", np.mean(times[:,0]), " +- ", np.std(times[:,0]))
print("Numpy : ", np.mean(times[:,1]), " +- ", np.std(times[:,1]))
print("Exponential with int: ", np.mean(times[:,2]), " +- ", np.std(times[:,2]))
print("Exponential with float: ", np.mean(times[:,3]), " +- ", np.std(times[:,3]))
print("Python-style for: ", np.mean(times[:,4]), " +- ", np.std(times[:,4]))


#plt.xlabel(r"Exponent $10^n$")
#plt.ylabel("Time / s")
#plt.semilogy(x, y1, label="for")
#plt.semilogy(x, y2, label="numpy")
#plt.semilogy(x, y3, label="for with exponential and int")
#plt.semilogy(x, y4, label="for with exponential and float")
#plt.semilogy(x, y5, label="python-style for")
#
#plt.legend()