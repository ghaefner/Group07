#Program to look for proton decay nuclides
import numpy as np
from matplotlib import pyplot as plt

#Load in data
data = np.loadtxt("aud16.dat")

#Make arrays
z = data[:,0]
a = data[:,1]
bexp = data[:,2] #Binding Energies

plt.plot(a,bexp/a,'r-')
plt.show()
