# Program to plot differences in charge radii for N and N-1 for each Isotopes

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

'''
# plot sqrt(<r^2>(A,N)) - sqrt(<r^2>(A-1,N-1)) [fm]
# Load in data
data = np.loadtxt("BK_dN=1.dat")
n_data = np.shape(data)[0]

Z = data[:,0]
N = data[:,1]
#A = data[:,2]
dRMS = data[:,3]

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Z')
ax.set_ylabel('N')
ax.set_zlabel('delta RMS(Z,N_N-1) [fm]')

ax.set_xlim(60, 65)
ax.set_ylim(70, 110)

ax.plot(Z,N,dRMS,"o")
plt.show()
'''


'''
# plot sqrt(<r^2>(A,N)) - sqrt(<r^2>(A-2,N-2)) [fm]
# Load in data
data = np.loadtxt("BK_dN=2.dat")
n_data = np.shape(data)[0]

Z = data[:,0]
N = data[:,1]
#A = data[:,2]
dRMS = data[:,3]

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Z')
ax.set_ylabel('N')
ax.set_zlabel('delta RMS(Z,N_N-2) [fm]')

ax.set_xlim(60, 65)
ax.set_ylim(70, 110)

ax.plot(Z,N,dRMS,"o")
plt.show()
'''


# plot (<r^2>(A,N) - <r^2>(A-2,N-2))/(<r^2(LD;A)> - <r^2(LD;A-2)>)
# <r^2>(LD;A) = 3/5 (1.2 * A**(1/3))**2 : assume homogenious spherical symmetric charge density
# https://people.nscl.msu.edu/~brown/brown-all-papers/065-1984-jpg.10.1683-rms-charge-radii.pdf
# Load in data
data = np.loadtxt("BK_Alex.dat")
n_data = np.shape(data)[0]

Z = data[:,0]
N = data[:,1]
#A = data[:,2]
dRMS = data[:,3]

# 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('Z')
ax.set_ylabel('N')
ax.set_zlabel('delta MS(Z,N_N-2) / delta LD(A_A-2)  [fm]')

ax.set_xlim(60, 65)
ax.set_ylim(70, 110)

ax.plot(Z,N,dRMS,"o")
plt.show()
