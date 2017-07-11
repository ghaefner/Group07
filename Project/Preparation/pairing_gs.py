import numpy as np
from matplotlib import pyplot as plt

g = np.linspace(-1,1,500)

omega = 2

n_1 = 12
n_2 = 16

def E_0(strength,deg,n_p):
	return - float(strength) / 4 * n_p * (deg - n_p +2)
	

y_values1 = [E_0(x,omega,n_1) for x in g]
y_values2 = [E_0(x,omega,n_2) for x in g]

plt.xlabel("Strength g")
plt.ylabel("Ground-state energy E_0")
#plt.legend(['p=6'],['p=8'], loc=1)
plt.legend(('Experiment','Liquid Drop'),loc='upper right')
plt.plot(g,y_values1,'b-',g,y_values2,'r-')
plt.show()
