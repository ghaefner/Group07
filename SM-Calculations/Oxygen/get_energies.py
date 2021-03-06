import numpy as np
from matplotlib import pyplot as plt
	
A = range(18,30,2)

Ex = [[],[],[],[]]

for j in A:
	lpt = np.loadtxt("Flourine/f_%ia.lpt" % j, skiprows=6, usecols=(0,1,2,3,4,5,6))
	J = lpt[:,4]
	NJ = lpt[:,1]
	energy = lpt[:,2]
	ex = lpt[:,3]
	for k in range(len(J)):
		if J[k] == 2 and NJ[k] == 1:
			Ex[0].append(j)
			Ex[1].append(ex[k])
		if J[k] == 4 and NJ[k] == 1:
			Ex[2].append(ex[k])			
			
for i in range(len(Ex[0])):
	R42 = Ex[2][i]/Ex[1][i]
	
	Ex[3].append(R42)
	
	
plt.plot(Ex[0],Ex[3])
plt.show()
	
