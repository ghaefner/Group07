import numpy as np

from config import EIGENSPACE_DIR
from config import HAMILTONIAN_DIR

def diag(hamiltonian):
    
    print()
    print("diag.py: Diagonalizing the Hamiltonian matrix from file '" + HAMILTONIAN_DIR + hamiltonian)
    print()
    
    H = np.loadtxt(HAMILTONIAN_DIR + hamiltonian)

    eigs, vecs = np.linalg.eig(H)
    eigs = np.sort(eigs)
        
    np.savetxt(EIGENSPACE_DIR + "eigenvalues.txt", eigs, delimiter=" ")
    np.savetxt(EIGENSPACE_DIR + "eigenvectors.txt", vecs, delimiter=" ")
    
    print(eigs)

    print()
    print("diag.py: Saved Eigenvalues to '" + EIGENSPACE_DIR + "eigenvalues.txt")
    print("diag.py: Saved Eigenvectors to '" + EIGENSPACE_DIR + "eigenvectors.txt")
    print()

diag(HAMILTONIAN_DIR + "Hamiltonian.txt")
diag(HAMILTONIAN_DIR + "Hamiltonian_bit.txt")