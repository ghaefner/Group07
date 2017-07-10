import numpy as np
from matplotlib import pyplot as plt

#Read the data
data = np.loadtxt('toiee.dat',usecols=(0,1,2,3,4,5,6))

a = data[:,1]
z = data[:,2]
J = data[:,3]
p = data[:,4]
n = data[:,5]
Ex = data[:,6]

ratio = [[],[],[],[]]

#Look for J=8 and J=6 for each isotopes
for i in range(len(a)):
	if J[i] == 8 and p[i] == 1 and n[i] == 1:
		for j in range(len(a)):
			if a[j] == a[i] and z[j] == z[i] and J[j] == 6 and p[j] == 1 and n[j] == 1:
				ratio[0].append(z[j])
				ratio[1].append(a[j])
				ratio[2].append(Ex[i]/Ex[j])
				ratio[3].append(a[j]-z[j])


#Plot results
rot = 1.7142857
x_values = np.linspace(0,250,500)
y_values = np.linspace(rot,rot,500)

plt.title('R8/6 Ratio')
plt.xlabel('Neutron')
plt.ylabel('Ex(8+)/Ex(6+)')
plt.axis([0,150, 0.75,2.5])
plt.legend(('Data','Rigid Rotor'))		
plt.plot(ratio[3],ratio[2],'ro', x_values,y_values,'b-')
plt.show()	
