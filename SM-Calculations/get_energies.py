import numpy as np
from matplotlib import pyplot as plt

	
Ex = [[],[],[],[]]

#Function to get R42-values, remember it only makes sense for even massnumber nuclei
#Change interaction with j: j=1 means USDA and j=2 means USDB
#def get_R42(k,A_min,A_max):
	
#	if A_min %2 != 0 or A_max %2 != 0:
#		print("Error: Massnumber is not even")
#		exit()
		
#	if k == 1:
#		for j in range(A_min,A_max,2):
				
#			lpt = np.loadtxt("Oxygen/o_%ia.lpt" % j, skiprows=6, usecols=(0,1,2,3,4,5,6))
						
#	elif k == 2:
A_min = 18
A_max = 28
for j in range(A_min,A_max,2):
	lpt = np.loadtxt("Oxygen/o_%ib.lpt" % j, skiprows=6, usecols=(0,1,2,3,4,5,6))
	
		
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



#get_R42(1,18,28)
for i in range(len(Ex[0])):
	
	print("J: " + str(Ex[0][i]) + " R42: " + str(Ex[3][i]) + " E(2_1): " + str(Ex[1][i]))
#Plot					
#plt.xlabel("Massnumber")
#plt.ylabel("R42 - Ratio")	
#plt.plot(Ex[0],Ex[3])
#plt.show()	
	
