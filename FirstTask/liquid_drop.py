# Question set 1 - 2

import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# For debugging only
#import pdb
#pdb.set_trace()

# Using the notation from B.A. Brown, Lecture Notes in Nuclear Structure Physics, NSCL, Michigan State University (2017)

# Parameters for liquid drop model, all units are in MeV
LD_PARAMS = np.array([15.49, 17.23, 0.697, 22.6])

# Liquid drop model for the binding energy of a nucleus
def LD(A,Z):
    return LD_PARAMS[0]*A - LD_PARAMS[1]*A**(0.6666667) - LD_PARAMS[2]*Z**2./(A**0.33333333) - LD_PARAMS[3]*(A - 2.*Z)**2/A

# Set range of N and Z, and create a meshgrid of N and Z values
N_MIN = 1
N_MAX = 200
Z_MIN = 1
Z_MAX = 200

n = np.arange(N_MIN, N_MAX + 1, 1.)
z = np.arange(Z_MIN, Z_MAX + 1, 1.)

N, Z = np.meshgrid(n, z)

# Calculate binding energy per nucleon (BEA) in liquid drop model
# and visualize it in a 2D color plot
BEA = np.zeros((np.shape(N)[0], np.shape(N)[1]))

for i in range(np.shape(N)[0]):
    for j in range(np.shape(N)[1]):
        be = LD(N[i][j] + Z[i][j], Z[i][j])
        
        # To get a nice plot, set all binding energies < 0 (== unbound) to zero
        if(be > 0):
            BEA[i][j] = LD(N[i][j] + Z[i][j], Z[i][j])
        else:
            BEA[i][j] = 0.
        
plt.imshow(BEA, origin='lower', interpolation='none')

# Get driplines from the list of binding energies
# i.e. at a given Z, loop over N and find the transitions
# BEA <= 0. -> BEA > 0. (proton dripline)
# BEA > 0. -> BEA < 0. (neutron dripline)

proton_dripline = N[0, 0]
proton_dripline_flag = False
neutron_dripline = N[0, np.shape(BEA)[1] - 1]

driplines = np.zeros((np.shape(BEA)[1], 2))

for i in range(np.shape(BEA)[0]):
    for j in range(np.shape(BEA)[1]):
        
        if proton_dripline_flag == False and BEA[i][j] > 0.:
            proton_dripline = N[i][j]
            proton_dripline_flag = True
        if proton_dripline_flag == True and BEA[i][j] <= 0.:
            neutron_dripline = N[i][j - 1]
            break
       
    driplines[i][0] = proton_dripline
    driplines[i][1] = neutron_dripline
    
    proton_dripline = N[0, 0]
    neutron_dripline = N[0, np.shape(BEA)[1] - 1]
    proton_dripline_flag = False

# Plot driplines
plt.xlabel("Neutron number N")
plt.ylabel("Proton number Z")
plt.plot(driplines[:,0], z, color="red")   
plt.plot(driplines[:,1], z, color="red")    
plt.show()
