import numpy as np

H = np.loadtxt("Hamiltonian")

eigs, vecs = np.linalg.eig(H)

for i in range(30):
	print(np.sort(eigs)[i])


