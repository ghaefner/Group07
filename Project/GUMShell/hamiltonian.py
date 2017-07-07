import numpy as np
# For debugging using python debugger (pdb)
#import pdb
from phase import bandp

# Basis of Slater determinants
basis = np.loadtxt("output/basis_2x2.txt")
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

H = np.zeros((basis_size, basis_size))

for alpha in range(basis_size):
    for p in range(1, n_sp + 1):
        for q in range(p + 1, n_sp + 1):
            for r in range(1, n_sp + 1):
                for s in range(r + 1, n_sp + 1):
                    print(p, ", ", q, ", ", r, ", ", s)
                    for tb in tbme:
                        if (tb[0] == p and tb[1] == q and tb[2] == r and tb[3] == s) or (tb[0] == r and tb[1] == s and tb[2] == p and tb[3] == q):
                            if tb[4] == 0.:
                                continue
                            else:
                                print(basis[alpha])
                                phi, b = bandp(p, q, r, s, n_particles, basis[alpha][:n_particles])
                                print(basis[alpha])
                                print("v_", p, q, r, s, " a_", p, "^+" ,"a_", q, "^+" ,"a_", r,"a_", s,  " |", basis[alpha][:n_particles], "> = ", phi, " * ", tb[4] ," |", b, " >")
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
                                            
print(H)