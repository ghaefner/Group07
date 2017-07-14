import numpy as np
import matplotlib.pyplot as plt

evectors = np.loadtxt("eigenspace/eigenvectors.txt")
evalues = np.loadtxt("eigenspace/eigenvalues.txt")

print(evalues[4])

x = []
y = []

ev = 0
norm = 0.

for i in range(len(evectors[ev])):
    x.append(i)
    y.append(evectors[ev][i]*evectors[ev][i])
    norm += evectors[ev][i]*evectors[ev][i]
    
print(norm)

plt.xlabel(r"ID of Slater determinant $| \Phi_i \rangle$")
plt.ylabel(r"$\langle \Phi_i | 0^+_1 \rangle$")

plt.plot(x,y, color="black")