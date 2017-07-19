import numpy as np
from phase_mod import J_plus
from phase_mod import J_minus

from config import ORBITAL_DIR
from config import BASIS_DIR
from config import EIGENSPACE_DIR

def JpJm(basisfile, evectorfile, orbitalfile, output_prefix):

    print()
    print("jcoupling.py: Determining J quantum number of eigenvectors in file '", basisfile, "'")
    print()
    
    basis = np.loadtxt(BASIS_DIR + basisfile)
    dim = basis.ndim
    if dim == 1:
        basis_size = 1
        n_particles = np.shape(basis)[0] - 1
        basis = [basis]
    else:
        basis_size = np.shape(basis)[0]
        n_particles = np.shape(basis)[1] - 1
        
    evectors = np.loadtxt(EIGENSPACE_DIR + evectorfile)

    sp = np.loadtxt(ORBITAL_DIR + orbitalfile)
    n_sp = np.shape(sp)[0]
    max_osc = np.max(sp[:,1])
    min_osc = np.min(sp[:,1])
    min_j = np.min(sp[:,2])
    max_m = np.max(sp[:,3])
    min_m = np.min(sp[:,3])

    JpJm_matrix = np.zeros((np.shape(basis)[0], np.shape(basis)[0]))

    # Loop over Slater basis states
    for i in range(basis_size):
        # Calculate the action of all possible J^+
        for osc in np.arange(min_osc, max_osc + 1., 1.):
            for j in np.arange(min_j, max_m + 1., 2.):
                for m in np.arange(min_m, max_m + 1., 2.):

                    phase_plus, beta_plus = J_plus(osc, j, m, n_particles, basis[i][:-1], sp, n_sp)
                    if phase_plus != 0:
                        # Calculate the action of all possible J^-
                        for osc2 in np.arange(min_osc, max_osc + 1., 1.):
                            for j2 in np.arange(min_j, max_m + 1., 2.):
                                for m2 in np.arange(min_m, max_m + 1., 2.):
                                    phase_minus, beta_minus = J_minus(osc2, j2, m2 + 2., n_particles, beta_plus, sp, n_sp)
                                    
                                    if phase_minus != 0:
                                        for k in range(basis_size):
                                            if (basis[k][:-1] == beta_minus).all():
                                                JpJm_matrix[i][k] += phase_plus*phase_minus


    # Calculate the matrix elements of the J^- J^+ operator between the Eigenvectors
    JpJm_evector_matrix = np.zeros((np.shape(basis)[0], np.shape(basis)[0]))
    
    for i in range(basis_size):
        for j in range(basis_size):
            for m in range(basis_size):
                for n in range(basis_size):
                    JpJm_evector_matrix[i][m] += evectors[j][i]*evectors[n][m]*JpJm_matrix[j][n]
    
    JpJm_evector_matrix = np.round(JpJm_evector_matrix)
    
    np.savetxt(EIGENSPACE_DIR + output_prefix + "_jvalues.txt", JpJm_evector_matrix,  fmt='%i', delimiter=" ")
    
    print()
    print("jcoupling.py: Saved J values to '", EIGENSPACE_DIR + output_prefix + "_jvalues.txt'")
    print()
    
#JpJm("output/basis.txt", "eigenspace/eigenvectors.txt", "space/sd.sp")