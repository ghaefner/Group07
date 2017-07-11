import numpy as np
from numpy import linalg
# For debugging using python debugger (pdb)
#import pdb
#from phase import bandp
#from phase2 import J_plus
from phase_mod import bandp
from phase_mod import J_plus
from phase_mod import J_minus

# Basis of Slater determinants
basis = np.loadtxt("output/basis_2x2_full.txt")
dim = basis.ndim
if dim == 1:
	basis_size = 1
	n_particles = np.shape(basis)[0] - 1
	basis = [basis]
else:
	basis_size = np.shape(basis)[0]
	n_particles = np.shape(basis)[1] - 1

# One-body matrix elements
spe = np.loadtxt("hamiltonian/pairing_sp.int")
n_spe = np.shape(spe)[0]
# Two-body matrix elements
tbme = np.loadtxt("hamiltonian/pairing_tb.int")
n_tbme = np.shape(spe)[0]
# Single-particle states
sp = np.loadtxt("space/0s1s.txt")
n_sp = np.shape(sp)[0]
max_osc = np.max(sp[:,1])
min_osc = np.min(sp[:,1])
min_j = np.min(sp[:,2])
max_m = np.max(sp[:,3])
min_m = np.min(sp[:,3])

H = np.zeros((basis_size, basis_size))

for alpha in range(basis_size):
    for p in range(1, n_sp + 1):
        for q in range(p + 1, n_sp + 1):
            for r in range(1, n_sp + 1):
                for s in range(r + 1, n_sp + 1):
                    #print(p, ", ", q, ", ", r, ", ", s)
                    for tb in tbme:
                        if (tb[0] == p and tb[1] == q and tb[2] == r and tb[3] == s):
                            if tb[4] == 0.:
                                continue
                            else:
                                phi, b = bandp(p, q, r, s, n_particles, list(basis[alpha][:n_particles]))
                                #print("v_", p, q, r, s, " a_", p, "^+" ,"a_", q, "^+" ,"a_", r,"a_", s,  " |", basis[alpha][:n_particles], "> = ", phi, " * ", tb[4] ," |", b, " >")
                                if phi == 0:
                                    continue
                                else:
                                    for beta in range(basis_size):
                                        if(len(basis[beta][:n_particles]) != len(b)):
                                            print("Error: hamiltonian.py: Vector dimensions not matching")
                                            exit(0)
                                            
                                        #if basis[beta][:n_particles] == b:
                                        if (basis[beta][:n_particles] == b).all():
                                            H[alpha][beta] += phi*tb[4]
                                            H[beta][alpha] = H[alpha][beta]

for alpha in range(basis_size):
    spme = 0.
    
    for i in range(n_particles):
        spme += spe[int(basis[alpha][i])-1][4]
    
    H[alpha][alpha] += spme
    spme = 0.
    
#print(H)
    
evalues, evectors = linalg.eig(H)
    
#print(np.sort(evalues))
#print(evectors)

# Calculate J value of Eigenvectors

J_values = np.zeros((np.shape(basis)[0],1))

J_sum = 0.

# Loop over Eigenvectors
#for k in range(np.shape(evectors)[0]):
#    if k != 333:
#        # Loop over basis Slater determinants in the Eigenvector
#            for i in range(basis_size):
#                print("Basis Slater determinant: ", basis[i,:-1], end="")
#                coeff = evectors[i][k]
#                print(", Coefficient = ", coeff)
#                # Loop over quantum numbers
#                for osc in np.arange(min_osc, max_osc + 1., 1.):
#                    print("n = ", osc)
#                    for j in np.arange(min_j, max_m + 1., 2.):
#                        print("\tj = ", j)
#                        for m in np.arange(min_m, max_m + 1., 2.):
#                            print("\t\tm = ", m)
#    J_values[k] = J_sum
#    J_sum = 0.

# Calculate the matrix elements of the J^- J^+ operator between the Slater basis states

JpJm_matrix = np.zeros((np.shape(basis)[0], np.shape(basis)[0]))

# Loop over Slater basis states
for i in range(basis_size):
    # Calculate the action of all possible J^+
    for osc in np.arange(min_osc, max_osc + 1., 1.):
        for j in np.arange(min_j, max_m + 1., 2.):
            for m in np.arange(min_m, max_m + 1., 2.):

                phase_plus, beta_plus = J_plus(osc, j, m, n_particles, basis[i,:-1], sp, n_sp)
                if phase_plus != 0:
                    # Calculate the action of all possible J^-
                    for osc2 in np.arange(min_osc, max_osc + 1., 1.):
                        for j2 in np.arange(min_j, max_m + 1., 2.):
                            for m2 in np.arange(min_m, max_m + 1., 2.):                    
                                phase_minus, beta_minus = J_minus(osc2, j2, m2 + 2., n_particles, beta_plus, sp, n_sp)

                                if phase_minus != 0:
                                    for k in range(basis_size):
                                        if (basis[k,:-1] == beta_minus).all():
                                            JpJm_matrix[i][k] += phase_plus*phase_minus*(j**2. + m**2. + m)


# Calculate the matrix elements of the J^- J^+ operator between the Eigenvectors
JpJm_evector_matrix = np.zeros((np.shape(basis)[0], np.shape(basis)[0]))

for i in range(basis_size):
    for j in range(basis_size):
        for m in range(basis_size):
            for n in range(basis_size):
                JpJm_evector_matrix[i][m] += evectors[j][i]*evectors[n][m]*JpJm_matrix[j][n]
                
print(JpJm_evector_matrix)

# Find non-diagonal blocks inside the matrix of J^- J^+. These blocks exist, because the
# Eigenvectors in the M-scheme are no Eigenvectors of this operator. The diagonalization
# of the non-diagonal blocks will create state with good J

block_matrix_indices = []
skip = []

# Find off-diagonal matrix elements. The block matrices that are made of the off-diagonal
# matrix elements are the M substates of a certain J. Since the Eigenvectors in the M-scheme
# are no Eigenvectors of the J^- J^+ operator, these blocks matrices exist.
# The code looks so complicated since the blocks may not be obvious "blocks" in the JpJm_evector_matrix
# This is because the ordering of Eigenvectors is arbitrary
for i in range(basis_size):
    if not i in skip:
        # Find block matrices
        for j in range(i + 1, basis_size, 1):
            if JpJm_evector_matrix[i][j] != 0:
                skip.append(i)
                # If a block matrix is found, extract its constituents from the larger matrix ()
                block_matrix_indices.append(i)
                for j in range(i + 1, basis_size, 1):
                    if JpJm_evector_matrix[i][j] != 0:                
                        skip.append(j)
                        block_matrix_indices.append(j)
                # Create block matrix and diagonalize it
                #block_matrix = np.zeros((len(block_matrix_indices), len(block_matrix_indices))

#for i in range(np.shape(basis)[0]):
#    for j in range(np.shape(basis)[0]):
#        if evectors[j][i] != 0. and J_plus_table[j][0] != 0.:
#            beta1 = J_plus_table[j][2]
#            for m in range(np.shape(basis)[0]):
#                for n in range(np.shape(basis)[0]): 
#                    if evectors[n][m] != 0. and J_minus_table[n][0] != 0. and J_minus_table[n][2] == beta1:
#                        JpJm_matrix[i][m] += evectors[j][i]*evectors[n][m]*J_plus_table[j][0]*J_minus_table[n][0]
                        
