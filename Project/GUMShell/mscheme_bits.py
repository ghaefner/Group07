#n1 = 2**3 + 2**4 + 2**5
#n2 = 2**1 + 2**3
#
#print(bin(n1))
#print(bin(n2))
#
#print(bin(n1 & n2))

import numpy as np

orbitalfile = "space/0s1s2s3s_np.txt"

n_protons = 2
n_neutrons = 2

###############################################################################
# Load file of available single-particle states
# It assumes that the file is arranged such that all neutron states are
# listed first, then the proton states
###############################################################################

# Give labels to the columns in the input file
#   ID = 0
#   N = 1
#   J = 2
M = 3
T = 4
    
orbitals = np.loadtxt("space/0s1s2s3s_np.txt")

n_states_tot = np.shape(orbitals)[0]

# Check if the file format is correct (protons after neutrons), calculate the
# number of neutron/proton states and the offset index where the proton
# orbitals start
for i in range(n_states_tot - 1):
    if orbitals[i][T] < orbitals[i+1][T]:
        print("Error: mscheme_bits.py: Wrong format of input file ", orbitalfile + ".\n Neutrons need to be defined before protons. Aborting.")
    if orbitals[i][T] > orbitals[i+1][T]:
        PROTON_OFFSET = i + 1
        
print("PROTON_OFFSET = ", PROTON_OFFSET)

n_states_neutrons = PROTON_OFFSET
n_states_protons = n_states_tot - PROTON_OFFSET

print("n_states_neutrons = ", n_states_neutrons)
print("n_states_protons = ", n_states_protons)


###############################################################################
# 1) Initialize lists of basis states for protons and neutrons separately
# 2) Find the lowest and highest possible states in terms of odometrics (maybe not ...)
###############################################################################

basis_neutrons = []
basis_protons = []

# n_particle_state_np is a variable to store SP state before they are appended to the basis
n_particle_state_neutrons = [0]*n_neutrons
n_particle_state_protons = [0]*n_protons

# Initialize n_particle_state: The lowest state has the indices [1, 2, 3, 4, ...., N_PARTICLES]
for i in range(n_protons):
    n_particle_state_protons[i] = i + 1
# Find the maximum possible state. It has the indices [n_states - N_PARTICLES, n_states - N_PARTICLES + 1, ..., n_states]
max_state_protons = [0]*n_protons
for i in range(n_protons):
    max_state_protons[n_protons - i - 1] = n_states_protons - i
    
####################################################
# Calculate the basis for different numbers of particles. Some numbers have to be treated separately
####################################################
	
## Case N_PARTICLES == 1 has to be treated separately
#    if N_PARTICLES == 1:
#        for i in range(n_states):
#            basis.append([i + 1])
#	        
## Case N_PARTICLES == n_states has to be treated separately
#    elif N_PARTICLES == n_states:
#        basis.append(max_state)
#	
#	
## Any case with N_PARTICLES > 1 && N_PARTICLES < n_states
## The algorithm works as follows (example with 3 particles)
## 1) Start with the very first state (1,2,3)
## 2) Keep increasing the last index until it is at the value of the maximum state 
##   e.g., if the maximum state is (6,7,8), increase until (1,2,8)
## 3) Increase the next-to-last index, lower the last index, and start from 1)
##   e.g., after (1,2,8), go on with (1,3,4)
## 4) Stop if you reach the maximum state
#    else:
#        while n_particle_state != max_state:
#            basis.append(n_particle_state[:])
#
#            for i in range(N_PARTICLES - 1):
#                if n_particle_state[N_PARTICLES - i - 1] != max_state[N_PARTICLES - i - 1]:
#                    n_particle_state[N_PARTICLES - i - 1] += 1
#                    break
#        
#                elif n_particle_state[N_PARTICLES - i - 1] == max_state[N_PARTICLES - i -1]:
#                    if n_particle_state[N_PARTICLES - i - 2] != max_state[N_PARTICLES - i - 2]:
#                        n_particle_state[N_PARTICLES - i - 2] += 1
#                        for j in range(i + 1):
#                            n_particle_state[N_PARTICLES - (i - j) - 1] = n_particle_state[N_PARTICLES - (i - j) - 2] + 1
#                        break
#                    else:
#                        continue
#	
#            if n_particle_state == max_state:
#                basis.append(n_particle_state[:])
#                break