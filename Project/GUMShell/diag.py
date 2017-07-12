import numpy as np

def diag(hamiltonian):
    H = np.loadtxt("Hamiltonian")

    eigs, vecs = np.linalg.eig(H)

    for i in range(30):
    	print(np.sort(eigs)[i])


