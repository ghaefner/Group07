import numpy as np
from phase_mod import adadaa
import time

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
    obme = np.loadtxt(oneparticle)
    # Two-body matrix elements
    tbme = np.loadtxt(twoparticle)

    mass_factor = (18./(16.+n_particles))**(0.3)
	
    START = time.time()
    
    H = np.zeros((basis_size, basis_size))

    for alpha in range(basis_size):
        for tb in tbme:
            if (tb[2] in basis[alpha][:n_particles]) and (tb[3] in basis[alpha][:n_particles]):
            
                phi, b = adadaa(tb[0], tb[1], tb[2], tb[3], n_particles, list(basis[alpha][:n_particles]))
                
                if phi == 0:
                    continue
                else:
                    for beta in range(0, alpha + 1):
                        if (basis[beta][:n_particles] == b).all():
                            H[alpha][beta] += phi*tb[4]*mass_factor
                            H[beta][alpha] = H[alpha][beta]
                            break

    for alpha in range(basis_size):
        spe = 0.
    
        for i in range(n_particles):
            spe += obme[int(basis[alpha][i])-1][4]
    
        H[alpha][alpha] += spe
    spe = 0.
    
    STOP = time.time()
    
    print("Calculation of Hamiltonian took ", STOP - START, "seconds")
    
    np.savetxt(HAMILTONIAN_DIR + "Hamiltonian.txt", H, delimiter = " ")

    print()
    print("hamiltonian.py: Saved Hamiltonian matrix to '", HAMILTONIAN_DIR, "Hamiltonian.txt'")
    print()

#hamiltonian("output/basis.txt", "interaction/sd_sp.int", "interaction/usdb_m.int", "space/sd.sp")