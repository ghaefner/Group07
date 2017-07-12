import numpy as np

EIGENSPACE_DIR = "eigenspace/"

def diag(hamiltonian):
    H = np.loadtxt(hamiltonian)
    
    print()
    print("diag.py: Diagonalizing the Hamiltonian matrix from file '" + hamiltonian)
    print()

    eigs, vecs = np.linalg.eig(H)
    eigs = np.sort(eigs)
#    for i in range(30):
#    	print(np.sort(eigs)[i])
        
    np.savetxt(EIGENSPACE_DIR + "eigenvalues.txt", eigs, delimiter=" ")
    np.savetxt(EIGENSPACE_DIR + "eigenvectors.txt", vecs, delimiter=" ")

    print()
    print("diag.py: Saved Eigenvalues to '" + EIGENSPACE_DIR + "eigenvalues.txt")
    print("diag.py: Saved Eigenvectors to '" + EIGENSPACE_DIR + "eigenvectors.txt")
    print()