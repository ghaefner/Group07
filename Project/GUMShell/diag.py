import numpy as np

from config import EIGENSPACE_DIR
from config import HAMILTONIAN_DIR

SORT_EIGENVALUES = False

def diag(hamiltonian, output_prefix):
    
    print()
    print("diag.py: Diagonalizing the Hamiltonian matrix from file '" + HAMILTONIAN_DIR + hamiltonian)
    print()
    
    H = np.loadtxt(HAMILTONIAN_DIR + hamiltonian)

    eigs, vecs = np.linalg.eig(H)
    if SORT_EIGENVALUES:
       eigs = np.sort(eigs)
        
    np.savetxt(EIGENSPACE_DIR + output_prefix + "_eigenvalues.txt", eigs, delimiter=" ")
    np.savetxt(EIGENSPACE_DIR + output_prefix + "_eigenvectors.txt", vecs, delimiter=" ")

    print()
    print("diag.py: Saved Eigenvalues to '" + EIGENSPACE_DIR + output_prefix + "_eigenvalues.txt")
    print("diag.py: Saved Eigenvectors to '" + EIGENSPACE_DIR + output_prefix + "_eigenvectors.txt")
    print()

#diag(HAMILTONIAN_DIR + "Hamiltonian.txt")
#diag(HAMILTONIAN_DIR + "Hamiltonian_bit.txt")