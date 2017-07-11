import numpy as np
from numpy import linalg
# For debugging using python debugger (pdb)
#import pdb
#from phase import bandp
#from phase2 import Jcalc
from phase_mod import bandp
from phase_mod import Jcalc

# Basis of Slater determinants
basis = np.loadtxt("output/basis.txt")
dim = basis.ndim
if dim == 1:
	basis_size = 1
	n_particles = np.shape(basis)[0] - 1
	basis = [basis]
else:
	basis_size = np.shape(basis)[0]
	n_particles = np.shape(basis)[1] - 1

# One-body matrix elements
spe = np.loadtxt("hamiltonian/sd_sp.int")
n_spe = np.shape(spe)[0]
# Two-body matrix elements
tbme = np.loadtxt("hamiltonian/usdb_m.int")
n_tbme = np.shape(spe)[0]
# Single-particle states
sp = np.loadtxt("space/sd.sp")
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
                                            #print("Error: hamiltonian.py: Vector dimensions not matching")
                                            exit(0)
                                            
                                        #if basis[beta][:n_particles] == b:
                                        if (basis[beta][:n_particles] == b).all():
                                            print("Phase = ", phi, " TBME = ", tb[4])
                                            H[alpha][beta] += phi*tb[4]
                                            H[beta][alpha] = H[alpha][beta]
                                            print("alpha =  ", alpha, " beta =  ", beta)

for alpha in range(basis_size):
    spme = 0.
    
    for i in range(n_particles):
        spme += spe[int(basis[alpha][i])-1][4]
    
    H[alpha][alpha] += spme
    spme = 0.
    
print(H)
np.savetxt('Hamiltonian',H, delimiter=" ")
    
#evalues, evectors = linalg.eig(H)
    
#print(np.sort(evalues))
#print(evectors)
'''
# Calculate J value of Eigenvectors

J_value = 0.
for i in range(basis_size):
    for osc in np.arange(min_osc, max_osc, 1.):
        for j in np.arange(min_j, max_m + 1., 2.):
            for m in np.arange(min_m, max_m + 1., 2.):
                coeff = evectors[i][0]
                print("coeff = ", coeff)
                print("a_{n = ", osc, " 2*j = ", j, " 2*m = ", m, "} | ", end="")
                for bb in basis[i,:-1]:
                    print(bb, " ", end="")
                print("> = | ", end="")
                phase, beta = Jcalc(osc, j, m, n_particles, basis[i,:-1], sp, n_sp)
                for bb in beta:
                    print(bb, " ", end="")
                print(">")
                print("phase = ", phase)
                J_value += (0.5*j - 0.5*m)*(0.5*j + 0.5*m + 1.)*phase*coeff
                print("J_value = ", J_value)
                print()
    J_value = 0.
'''
