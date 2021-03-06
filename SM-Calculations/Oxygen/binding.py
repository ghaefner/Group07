# Program to plot Bindingenergies and Separation energies

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#Load in data
data = np.loadtxt("bindingenergies.dat")

#Make arrays for x-axis and binding energies 
zet = data[:,0]
x = data[:,2] # Massnumber
bexpt = data[:,3]
liquid_drop = data[:,4]
diff_be = data[:,5]
n = [data[:,2] - [data[:,0]]] # Neutron number

'''
#Plot the Differences in BE
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xlabel("Neutron number")
ax.set_ylabel("Proton number")
ax.grid(True,linestyle='-',color='0.75')
#plt.zscale('log')
ax.set_xlim([0,20])
ax.set_ylim([0,20])
ax.scatter(n,zet,c=diff_be,marker='o',cmap = cm.jet)
plt.show()

#Plot for binding energies
plt.plot(x,bexpt, 'o', x, liquid_drop, 'o')
plt.axis([0,20,-1,10.0])
plt.xlabel(r'A')
plt.ylabel(r'Binding energies per nucleon [MeV]')
plt.legend(('Experiment','Liquid Drop'),loc='upper right')
plt.title('Binding energies per nucleon vs. liquid drop model')
plt.show()
'''
#Functions for liquid drop model
a = [ 15.49, 17.23, 0.697, 22.6 ] # Konstanten in MeV

def BE(A,Z):
	N = A - Z
	#if A%2 == 1:
	return a[0] * A - a[1] * A**(2./3.) - a[2] * Z * (Z-1) * A **(-1./3.) - a[3] * ((N-Z)**2./A)
	
def S_n(A,Z):
	return BE(A,Z) - BE(A-1,Z)
	
#Seperation energie from data file
#def SepNeutron(Z0):
bindings = [[],[],[]]
separation = [[],[],[]]
Z0 = 8
for i in range(len(zet)):
	if zet[i] == Z0 and x[i] >= 18:
		bindings[0].append(x[i])
		bindings[1].append(bexpt[i])
		bindings[2].append((BE(x[i],Z0)/x[i]))

for j in range(len(bindings[0])-1):
	separation[0].append(bindings[0][j+1])
	separation[1].append((bindings[0][j+1])*bindings[1][j+1]-(bindings[0][j])*bindings[1][j])
	separation[2].append(S_n(separation[0][j],Z0))

#Load in USDA/USDB data

usd = np.loadtxt("be_usd")
mass = usd[:,0]
usda = usd[:,1]/usd[:,0]
usdb = usd[:,2]/usd[:,0]

f = open("binding_usd","w")

#Header
f.write("# N(Z=8)   Binding energies: Exp. | Liquid drop | USDA | USDB")
f.write("\n")
for i in range(len(bindings[0])):			
	f.write(str(mass[i+1]) + " " + str(bindings[1][i]) + " " + str(bindings[2][i]) + " " + str(usda[i+1]) + " " + str(usdb[i+1]))
	f.write("\n")
f.close()

print "mass: " + str((mass))
print "binding: " + str((bindings[0]))
'''	
#Plot everything	
#plt.figure(1)
#plt.subplot(211)
#plt.title('Separation and binding energies for Z= %d isotopes' % Z0)
#plt.plot(separation[0],separation[1],'b-', separation[0],separation[2], 'r-')
#plt.legend(('Experiment','Liquid Drop'),loc='upper right')
#plt.xlabel('A')
#plt.ylabel('Separation energies [MeV]')
#plt.subplot(212)
plt.plot(bindings[0],bindings[1],'r-', bindings[0], bindings[2], 'b-', mass, usda, 'o', mass, usdb, '+')
plt.axis([17.8,24.2,7.,7.9])
plt.yscale('log')
plt.legend(('Experiment','Liquid Drop','USDA','USDB'),loc='upper right')
plt.xlabel('A')
plt.ylabel('Binding energies [MeV]')
plt.show()
'''
