import numpy as np

H = np.loadtxt("Hamiltonian")

eigs, vecs = np.linalg.eig(H)

print(np.sort(eigs))
