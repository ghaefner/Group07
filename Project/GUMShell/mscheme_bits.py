import numpy as np
from config import ORBITAL_DIR
from config import BASIS_DIR

WRITE_TEXT = True
WRITE_BINARY = True
WRITE_BINARY_AS_TEXT = True
VERBOSE = True

def mscheme(orbitalfile, n_neutrons, n_protons, output_prefix):

    print()
    print("mscheme.py: Creating basis of Slater determinants for", n_protons, "proton(s) and ", n_neutrons," neutron(s) in the orbitals from file'", ORBITAL_DIR + orbitalfile, "'")
    print()
    
    n_nucleons = n_neutrons + n_protons
    
    ###############################################################################
    # Load file of available single-particle states
    # It assumes that the file is arranged such that all neutron states are
    # listed first, then the proton states
    ###############################################################################
    
    # Give labels to the columns in the input file
    ID = 0
    #   N = 1
    #   J = 2
    M = 3
    T = 4
        
    orbitals = np.loadtxt(ORBITAL_DIR + orbitalfile)
    
    n_states_tot = np.shape(orbitals)[0]
    
    # Check if the file format is correct (protons after neutrons), calculate the
    # number of neutron/proton states and the offset index where the proton
    # orbitals start
    PROTON_OFFSET = n_states_tot
    for i in range(n_states_tot - 1):
        if orbitals[i][T] < orbitals[i+1][T]:
            print("Error: mscheme_bits.py: Wrong format of input file ", orbitalfile + ".\n Neutrons need to be defined before protons. Aborting.")
        if orbitals[i][T] > orbitals[i+1][T]:
            PROTON_OFFSET = i + 1
    
    n_states_neutrons = PROTON_OFFSET
    n_states_protons = n_states_tot - PROTON_OFFSET
    
    ###############################################################################
    # 1) Initialize lists of basis states for protons and neutrons separately
    # 2) Find the lowest and highest possible states in odometric measure
    ###############################################################################
    
    basis_neutrons = []
    basis_protons = []
    
    # n_particle_state_np is a variable to store SP state before they are appended to the basis
    n_particle_state_neutrons = [0]*n_neutrons
    n_particle_state_protons = [0]*n_protons
    
    # Initialize n_particle_state: The lowest state has the indices [1, 2, 3, 4, ...., N_PARTICLES]
    for i in range(n_neutrons):
        n_particle_state_neutrons[i] = i + 1
    # Find the maximum possible state. It has the indices [n_states - N_PARTICLES, n_states - N_PARTICLES + 1, ..., n_states]
    max_state_neutrons = [0]*n_neutrons
    for i in range(n_neutrons):
        max_state_neutrons[n_neutrons - i - 1] = n_states_neutrons - i
    
    # Initialize n_particle_state: The lowest state has the indices [1, 2, 3, 4, ...., N_PARTICLES]
    for i in range(n_protons):
        n_particle_state_protons[i] = i + 1 + PROTON_OFFSET
    # Find the maximum possible state. It has the indices [n_states - N_PARTICLES, n_states - N_PARTICLES + 1, ..., n_states]
    max_state_protons = [0]*n_protons
    for i in range(n_protons):
        max_state_protons[n_protons - i - 1] = n_states_protons - i + PROTON_OFFSET
        
    ###############################################################################
    # Calculate the basis for different numbers of neutrons. Some cases have to be treated separately
    ###############################################################################
    	
    # Case n_neutrons == 1 has to be treated separately
    if n_neutrons == 1:
        for i in range(n_states_neutrons):
            basis_neutrons.append([i + 1])
    	        
    # Case N_PARTICLES == n_states has to be treated separately
    elif n_neutrons == n_states_neutrons:
        basis_neutrons.append(max_state_neutrons)
    	
    # Any case with N_PARTICLES > 1 && N_PARTICLES < n_states
    # The algorithm works as follows (example with 3 particles)
    # 1) Start with the very first state (1,2,3)
    # 2) Keep increasing the last index until it is at the value of the maximum state 
    #   e.g., if the maximum state is (6,7,8), increase until (1,2,8)
    # 3) Increase the next-to-last index, lower the last index, and start from 1)
    #   e.g., after (1,2,8), go on with (1,3,4)
    # 4) Stop if you reach the maximum state
    else:
        while n_particle_state_neutrons != max_state_neutrons:
            basis_neutrons.append(n_particle_state_neutrons[:])
    
            for i in range(n_neutrons - 1):
                if n_particle_state_neutrons[n_neutrons - i - 1] != max_state_neutrons[n_neutrons - i - 1]:
                    n_particle_state_neutrons[n_neutrons - i - 1] += 1
                    break
        
                elif n_particle_state_neutrons[n_neutrons - i - 1] == max_state_neutrons[n_neutrons - i -1]:
                    if n_particle_state_neutrons[n_neutrons - i - 2] != max_state_neutrons[n_neutrons - i - 2]:
                        n_particle_state_neutrons[n_neutrons - i - 2] += 1
                        for j in range(i + 1):
                            n_particle_state_neutrons[n_neutrons - (i - j) - 1] = n_particle_state_neutrons[n_neutrons - (i - j) - 2] + 1
                        break
                    else:
                        continue
    	
            if n_particle_state_neutrons == max_state_neutrons:
                basis_neutrons.append(n_particle_state_neutrons[:])
                break     
    
    ###############################################################################
    # Calculate the basis for different numbers of protons. Some cases have to be treated separately
    ###############################################################################
    
    # Case n_protons == 1 has to be treated separately
    if n_protons == 1:
        for i in range(n_states_protons):
            basis_protons.append([i + 1 + PROTON_OFFSET])
    
    # Case N_PARTICLES == n_states has to be treated separately
    elif n_protons == n_states_protons:
        basis_protons.append(max_state_protons)
    
    # Any case with N_PARTICLES > 1 && N_PARTICLES < n_states
    # The algorithm works as follows (example with 3 particles)
    # 1) Start with the very first state (1,2,3)
    # 2) Keep increasing the last index until it is at the value of the maximum state
    #   e.g., if the maximum state is (6,7,8), increase until (1,2,8)
    # 3) Increase the next-to-last index, lower the last index, and start from 1)
    #   e.g., after (1,2,8), go on with (1,3,4)
    # 4) Stop if you reach the maximum state
    else:
        while n_particle_state_protons != max_state_protons:
            basis_protons.append(n_particle_state_protons[:])
    
            for i in range(n_protons - 1):
                if n_particle_state_protons[n_protons - i - 1] != max_state_protons[n_protons - i - 1]:
                    n_particle_state_protons[n_protons - i - 1] += 1
                    break
    
                elif n_particle_state_protons[n_protons - i - 1] == max_state_protons[n_protons - i -1]:
                    if n_particle_state_protons[n_protons - i - 2] != max_state_protons[n_protons - i - 2]:
                        n_particle_state_protons[n_protons - i - 2] += 1
                        for j in range(i + 1):
                            n_particle_state_protons[n_protons - (i - j) - 1] = n_particle_state_protons[n_protons - (i - j) - 2] + 1
                        break
                    else:
                        continue
    
            if n_particle_state_protons == max_state_protons:
                basis_protons.append(n_particle_state_protons[:])
                break
    
    ###############################################################################
    # Loop over basis states of neutrons and protons and do the following:
    # 1) Concatenate the neutron- and protons states
    # 2) Determine their M quantum numbers
    # 3) Convert them to bit-representation
    ###############################################################################
    	
    basis_np = []
    
    if n_protons == 0:
        basis_np = basis_neutrons
        
    elif n_neutrons == 0:
        basis_np = basis_protons
    
    else:
        for n in basis_neutrons:
            for p in basis_protons:
                basis_np.append(n + p)
                
    # Create arrays to store bit representations and total M quantum numbers
    basis_np_bit = np.zeros(np.shape(basis_np)[0], dtype=np.int32)
    M_values = np.zeros(np.shape(basis_np)[0], dtype=np.int32)

    if VERBOSE:    
        print("Listing basis states and their 2*M quantum number")
        print()
        for i in range(n_neutrons):
            print("2*M", i + 1, "(n)\t", end="")
        for i in range(n_neutrons):
            print("2*M", i + 1, "(p)\t", end="")
        print("2*M")
        print()
        
    for i in range(np.shape(basis_np)[0]):
        for j in range(n_nucleons):
            M_values[i] += orbitals[basis_np[i][j] - 1][M]
            basis_np_bit[i] += 2**(orbitals[basis_np[i][j] - 1][ID] - 1)
            if VERBOSE:
                print(basis_np[i][j], "\t", end="")
        if VERBOSE:
            print(M_values[i])
            print("Bit representation:", bin(int(basis_np_bit[i])))
        
    ###############################################################################
    # Calculate the number of allowed J-values and print them
    ###############################################################################

    if VERBOSE:
        print()
        print("2*M\tD(2*J)\td(2*M)")
    
        M_values_unique, M_values_frequency = np.unique(M_values, return_counts=True)
        	        
        for i in range(np.shape(M_values_unique)[0]):
            if M_values_unique[i] >= 0:
                if i == np.shape(M_values_unique)[0] - 1:
                    print(M_values_unique[i], "\t", M_values_frequency[i], "\t", M_values_frequency[i])
                    break
                print(M_values_unique[i], "\t", end="")
                print(M_values_frequency[i] - M_values_frequency[i + 1], "\t", end="")
                print(M_values_frequency[i])
            
    ###############################################################################
    # Write basis states in odometric representation to a file
    ###############################################################################
   
    if WRITE_TEXT: 	
        # Write file header
        f = open(BASIS_DIR + output_prefix + "_basis.txt", 'w')
        f.write("#")
        for i in range(n_neutrons):
            f.write("n(")
            f.write(str(i + 1))
            f.write(")\t")
        for i in range(n_protons):
            f.write("p(")
            f.write(str(i + 1))
            f.write(")\t")
        
        f.write("2*M\n")
        
        # Write states
        for i in range(np.shape(basis_np)[0]):
            for bb in basis_np[i]:
                f.write(str(bb))
                f.write("\t")
        	        
            f.write(str(M_values[i]))
            f.write("\n")
        	    
        f.close()
        
        print()
        print("mscheme_bits.py: Saved basis of Slater in odometric representation determinants to '" + BASIS_DIR + output_prefix + "_basis.txt'")
    
            
    ###############################################################################
    # Write basis states in bit representation to a file
    ###############################################################################
    
    # The verbose way, where the output is still human-readable	
    
    # Write file header
    if WRITE_BINARY:
        if WRITE_BINARY_AS_TEXT:
            f = open(BASIS_DIR  + output_prefix + "_basis_bit.txt", 'w')
            f.write("#")
            for i in range(n_states_neutrons):
                f.write("n(")
                f.write(str(i + 1))
                f.write(")\t")
            for i in range(n_states_protons):
                f.write("p(")
                f.write(str(i + 1))
                f.write(")\t")
            	    
            f.write("2*M\n")
            	
            # Write states
            for i in range(np.shape(basis_np_bit)[0]):
                f.write(str(bin(int(basis_np_bit[i]))))
            #    f.write(str(int(basis_np_bit[i])))
                f.write("\t")
                f.write(str(M_values[i]))
                f.write("\n")
            	    
            f.close()
        
            print()
            print("mscheme_bits.py: Saved basis of Slater determinants in bit representation to '" + BASIS_DIR + output_prefix + "_basis_bit.txt'")
            print()
        
        # Output as a true binary file
        
#        basis_np_bit.tofile(BASIS_DIR + "basis_bit.bin")
        np.save(BASIS_DIR + output_prefix + "_basis_bit", basis_np_bit)
        
        print("mscheme_bits.py: Saved basis of Slater determinants in bit representation to '" + BASIS_DIR + output_prefix + "_basis_bit.npy'")
        print()
    
# For testing uncomment the following lines:
#orbitalfile = "sd_np.txt"
#mscheme(orbitalfile, 4, 0, "basis")