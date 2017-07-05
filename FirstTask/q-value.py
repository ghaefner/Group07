#Program to calculate the Q-value
import numpy as np
from matplotlib import pyplot as plt

#Load in data
data = np.loadtxt("aud16.dat")

#Make arrays
z = data[:,0]
a = data[:,1]
bexp = data[:,2] #Binding Energies

#Task 5: Q-Value
#Q-Value
for i in range(len(a)):
	if z[i] == 88 and a[i] == 223:
		BE_Ra226 = bexp[i]
	if z[i] == 82 and a[i] == 209:
		BE_Hg209 = bexp[i]
	if z[i] == 6 and a[i] == 14:
		BE_C14 = bexp[i]
	if z[i] == 2 and a[i] == 4:
		BE_alpha = bexp[i]
	if z[i] == 86 and a[i] == 219:
		BE_Rn219 = bexp[i]
		
Q_cluster = - BE_Ra226 + BE_Hg209 + BE_C14
Q_alpha = -BE_Ra226 + BE_alpha + BE_Rn219


#Half-Lifes
coeffs = [1.6070,-0.9467,-30.912]

def T_12(Q,A,Z):
	return 10**(a[0]*Z*Q**(-1./2.)+a[1]*Z**(-1./2.)*A**(-1./6.)+a[2]) 
	#Returns Half-Life for alpha decay in seconds

print "Half-life: " + str((T_12(Q_alpha,223,88)/(3600.*24))) + " in days" #Half-life for alpha decay in days
print "Q-value: " + str(Q_alpha)
