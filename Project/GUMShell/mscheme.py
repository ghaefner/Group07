import numpy as np

def mscheme(basisstates, nparticles):
    print()
    print("mscheme.py: Creating basis of Slater determinants for", nparticles, "particles in the orbitals from file'", basisstates, "'")
    print()
	
    N_PARTICLES = nparticles
	
# Give labels to the columns in the input file
#   ID = 0
#   N = 1
#   J = 2
    M = 3
#   T = 4

################################################
# Load file of available single-particle states
################################################
	
    sp = np.loadtxt(basisstates)
	
# Determine number of unique single-particle (SP) states and number of shells (not needed at the moment)
    n_states = np.shape(sp)[0]
    #n_shells = sp[n_states - 1][N]
	
    print("Number of SP states: ", n_states)
    #print("Number of shells: ", n_shells)
    print()
	
########################################
# Initialize the list of basis states
########################################
	
    basis = []
# n_particle_state is a variable to store SP state before they are appended to the basis
    n_particle_state = [0]*N_PARTICLES
# Initialize n_particle_state: The lowest state has the indices [1, 2, 3, 4, ...., N_PARTICLES]
    for i in range(N_PARTICLES):
        n_particle_state[i] = i + 1
# Find the maximum possible state. It has the indices [n_states - N_PARTICLES, n_states - N_PARTICLES + 1, ..., n_states]
    max_state = [0]*N_PARTICLES
    for i in range(N_PARTICLES):
        max_state[N_PARTICLES - i - 1] = n_states - i
	 
####################################################
# Calculate the basis for different numbers of particles. Some numbers have to be treated separately
####################################################
	
# Case N_PARTICLES == 1 has to be treated separately
    if N_PARTICLES == 1:
        for i in range(n_states):
            basis.append([i + 1])
	        
# Case N_PARTICLES == n_states has to be treated separately
    elif N_PARTICLES == n_states:
        basis.append(max_state)
	
	
# Any case with N_PARTICLES > 1 && N_PARTICLES < n_states
# The algorithm works as follows (example with 3 particles)
# 1) Start with the very first state (1,2,3)
# 2) Keep increasing the last index until it is at the value of the maximum state 
#   e.g., if the maximum state is (6,7,8), increase until (1,2,8)
# 3) Increase the next-to-last index, lower the last index, and start from 1)
#   e.g., after (1,2,8), go on with (1,3,4)
# 4) Stop if you reach the maximum state
    else:
        while n_particle_state != max_state:
            basis.append(n_particle_state[:])

            for i in range(N_PARTICLES - 1):
                if n_particle_state[N_PARTICLES - i - 1] != max_state[N_PARTICLES - i - 1]:
                    n_particle_state[N_PARTICLES - i - 1] += 1
                    break
        
                elif n_particle_state[N_PARTICLES - i - 1] == max_state[N_PARTICLES - i -1]:
                    if n_particle_state[N_PARTICLES - i - 2] != max_state[N_PARTICLES - i - 2]:
                        n_particle_state[N_PARTICLES - i - 2] += 1
                        for j in range(i + 1):
                            n_particle_state[N_PARTICLES - (i - j) - 1] = n_particle_state[N_PARTICLES - (i - j) - 2] + 1
                        break
                    else:
                        continue
	
            if n_particle_state == max_state:
                basis.append(n_particle_state[:])
                break
	
#####################################################
# Print basis states with positive M and create a list of allowed J-values
#####################################################

    M_values_positive = []
    M_values = []
	
    print("Listing basis states and their M quantum number (only positive M)")
    print()
    for i in range(N_PARTICLES):
        print("M", i + 1, "\t", end="")
    print()
	
    for b in basis:
        total_M = 0.
        for i in range(N_PARTICLES):
             total_M += sp[b[i] - 1][M]
	    
        M_values.append(total_M)
	    
        if total_M >= 0.:
            for i in range(N_PARTICLES):
                print(b[i], "\t", end='')
	    
            print("2*M =", total_M)
	        
            M_values_positive.append(total_M)
	        
    print()
	
    M_max = np.max(M_values_positive)
    M_min = np.min(M_values_positive)
	
    M_list = np.arange(M_min, M_max + 1., 1.)
	
    print("\tD(J)\td(M)")
	
    for m in M_list:
        print(m, end="")
        print("\t", end="")
        if m < M_max:
            print(M_values_positive.count(m) - M_values_positive.count(m + 2.), end="")
        else:
            print(M_values_positive.count(m), end="")

        print("\t", end="")
        print(M_values_positive.count(m), end="")
        print()
	
#################################
# Write basis states to a file
#################################
	
# Write file header
    f = open("output/basis.txt", 'w')
    f.write("#")
    for i in range(N_PARTICLES):
        f.write("I")
        f.write(str(i + 1))
        f.write("\t")
	    
    f.write("2*M\n")
	
# Write states
    for i in range(np.shape(basis)[0]):
        for bb in basis[i]:
            f.write(str(bb))
            f.write("\t")
	        
        f.write(str(M_values[i]))
        f.write("\n")
	    
    f.close()

    print()
    print("mscheme.py: Saved basis of Slater determinants to '/output/basis.txt'")
    print()
