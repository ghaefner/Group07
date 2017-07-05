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
#Define Separation Functions
def s_p(Z,A):
	for i in range(len(z)):
		if a[i] == A and z[i] == Z:
			for j in range(len(z)):
				if a[j] == A-1 and z[j] == Z-1:
					return bexp[i] - bexp[j]
		
def s_2p(Z,A):
	for i in range(len(z)):
		if a[i] == A and z[i] == Z:
			for j in range(len(z)):
				if a[j] == A-2 and z[j] == Z-2:
					return bexp[i] - bexp[j]
					
#Look for isotopes on the given condition
isotopes = [[],[]]
for i in range(len(z)):
	if s_p(z[i],a[i]) > 0 and s_2p(z[i],a[i]) < 0:
		isotopes[0].append(z[i])
		isotopes[1].append(a[i]-z[i])

plt.xlabel("Z")
plt.ylabel("N")
plt.title("Proton-decay isotopes")
plt.plot(isotopes[0],isotopes[1],'.')
plt.show()


''' Comment on the Results
Task 1:	According to our calculation there are 165 nuclei which are unbound to double-proton decay but bound to
		single-proton decay. Those are plottet in an N-Z-plot
'''
		

