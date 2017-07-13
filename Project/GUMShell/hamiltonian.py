import numpy as np
#from phase import bandp
#from phase2 import Jcalc
from phase_mod import bandp

HAMILTONIAN_DIR = "hamiltonian/"

def hamiltonian(basisfile, oneparticle, twoparticle, orbitals):

    print()
    print("hamiltonian.py: Calculating the Hamiltonian matrix with the following input:")
    print("\torbitals = ", orbitals)
    print("\tbasis = ", basisfile)
    print("\toneparticle = ", oneparticle)
    print("\ttwoparticle = ", twoparticle)
    print()
    
    # Basis of Slater determinants
    basis = np.loadtxt(basisfile)
    dim = basis.ndim
    if dim == 1:
        basis_size = 1
        n_particles = np.shape(basis)[0] - 1
        basis = [basis]
    else:
        basis_size = np.shape(basis)[0]
        n_particles = np.shape(basis)[1] - 1

    # One-body matrix elements
    spe = np.loadtxt(oneparticle)
#   n_spe = np.shape(spe)[0]
    # Two-body matrix elements
    tbme = np.loadtxt(twoparticle)
#   n_tbme = np.shape(spe)[0]
    # Single-particle states
    sp = np.loadtxt(orbitals)
    n_sp = np.shape(sp)[0]
#   max_osc = np.max(sp[:,1])
#   min_osc = np.min(sp[:,1])
#   min_j = np.min(sp[:,2])
#   max_m = np.max(sp[:,3])
#   min_m = np.min(sp[:,3])

    mass_factor = (18./(16.+n_particles))**(1./3.)
	
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
                                                print("Error: hamiltonian.py: Vector dimensions not matching")
                                                exit(0)
                                            
                                            #if basis[beta][:n_particles] == b:
                                            if (basis[beta][:n_particles] == b).all():
                                                H[alpha][beta] += phi*tb[4]*mass_factor
                                                H[beta][alpha] = H[alpha][beta]

    for alpha in range(basis_size):
        spme = 0.
    
        for i in range(n_particles):
            spme += spe[int(basis[alpha][i])-1][4]
    
        H[alpha][alpha] += spme
    spme = 0.
    
    np.savetxt(HAMILTONIAN_DIR + "Hamiltonian.txt", H, delimiter = " ")

    print()
    print("hamiltonian.py: Saved Hamiltonian matrix to '", HAMILTONIAN_DIR, "Hamiltonian.txt'")
    print()
