#Program to look for proton decay nuclides
import numpy as np
from matplotlib import pyplot as plt

#Load in data
data = np.loadtxt("aud16.dat")

#Make arrays
z = data[:,0]
a = data[:,1]
bexp = data[:,2] #Binding Energies

#Task 1: Which nuclei are unbound to double proton decay but bound to single proton decay?

isotopes = [[],[],[],[]]

#Look for S_p > 0 and S_2p < 0
for i in range(len(z)):
	for j in range(len(z)):
		if a[j] == a[i]-1 and z[j] == z[i]-1:
			if (bexp[i] - bexp[j]) > 0:
				for k in range(len(z)):
					if a[k] == a[i]-2 and z[k] == z[i]-2:
						if (bexp[i] - bexp[k]) < 0:
							isotopes[0].append(z[i])
							isotopes[1].append(a[i])
							isotopes[2].append(bexp[i]-bexp[j])
							isotopes[3].append(bexp[i]-bexp[k])

#Results
print("Z     A")
for i in range(len(isotopes[0])):
	print isotopes[0][i],isotopes[1][i]

plt.xlabel("Z")
plt.ylabel("N")
plt.title("Proton-decay isotopes")
plt.plot(isotopes[0],isotopes[1],'.')
plt.show()

