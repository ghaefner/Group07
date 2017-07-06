import numpy as np
from phase import bandp

# Basis of Slater determinants
basis = np.loadtxt("output/basis_paired.txt")
basis_size = np.shape(basis)[0]
n_particles = np.shape(basis)[1] - 1
# One-body matrix elements
spe = np.loadtxt("hamiltonian/pairing_sp.int")
n_spe = np.shape(spe)[0]
# Two-body matrix elements
tbme = np.loadtxt("hamiltonian/pairing_tb.int")
n_tbme = np.shape(spe)[0]
# Single-particle states
sp = np.loadtxt("space/0s1s2s3s.txt")
n_sp = np.shape(sp)[0]

H = np.zeros((basis_size, basis_size))

for alpha in range(basis_size):
    for p in range(n_sp):
        for q in range(p, n_sp):
            for r in range(n_sp):
                for s in range(r, n_sp):
                    for tb in tbme:
                        if tb[0] == p and tb[1] == q and tb[2] == r and tb[3] == s:
                            if tb[4] == 0.:
                                continue
                            else:
                                print([p, q, r, s])
                                bandp(p, q, r, s, n_particles, basis[alpha][:n_particles])
#                                if phi == 0:
#                                    continue
#                                else:
#                                    for beta in range(basis_size):
#                                        if(len(basis[beta][:n_particles]) != len(b)):
#                                            print("Error: hamiltonian.py: Vector dimensions not matching")
#                                            exit(0)
#                                            
#                                        if basis[beta][:n_particles] == b:
#                                            H[alpha][beta] += phi*tb[4]
#                                            
#print(H)