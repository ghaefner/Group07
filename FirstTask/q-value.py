#Program to calculate the Q-value
import numpy as np
from matplotlib import pyplot as plt

#Load in data
data = np.loadtxt("aud16.dat")

#Make arrays
z = data[:,0]
a = data[:,1]
bexp = data[:,2] #Binding energies

#Task 5: Q-Value
#Get the essential binding energies
for i in range(len(a)):
	if z[i] == 88 and a[i] == 223:
		BE_Ra223 = bexp[i]
	if z[i] == 82 and a[i] == 209:
		BE_Pb209 = bexp[i]
	if z[i] == 6 and a[i] == 14:
		BE_C14 = bexp[i]
	if z[i] == 2 and a[i] == 4:
		BE_alpha = bexp[i]
	if z[i] == 86 and a[i] == 219:
		BE_Rn219 = bexp[i]

#Calculate the q-value from the binding energies [MeV]	
Q_cluster = (- BE_Ra223 + BE_Pb209 + BE_C14)/1000
Q_cluster_lit = 31.828

if Q_cluster <= Q_cluster_lit * 1.05 and Q_cluster >= Q_cluster_lit * 0.95:
	print "Q-value " + str(Q_cluster) + " MeV"
else:
	print("Error: wrong Q-value")
	exit(0) 


t12_alpha = 11.43 # [d]
Q_alpha = 5.589 # [MeV]


#Half-Lifes using the universal decay law
def t12(Q,Z):
	#coeff = t12_alpha * np.sqrt(Q_alpha) /(Z)
	coeff = 1
	return coeff * Z /(np.sqrt(Q))
	
print "Half-Life " + str(t12(Q_cluster,223)) + " d"

#Calculating the branching ratio
b = t12_alpha / t12(Q_cluster,223)

print "Branching Ratio " + str(b)
