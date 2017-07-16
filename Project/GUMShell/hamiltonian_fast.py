import numpy as np
#from phase import bandp
#from phase2 import Jcalc
from phase_mod import bandp
from phase_mod import adadaa
import time

START = time.time()

HAMILTONIAN_DIR = "hamiltonian/"

orbitals = "space/sd.sp"
basisfile = "output/basis.txt"
oneparticle = "interaction/sd_sp.int"
twoparticle = "interaction/usdb_m.int"

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
	
CALC_START = time.time()

H = np.zeros((basis_size, basis_size))

for alpha in range(basis_size):
    for tb in tbme:
        if (tb[2] in basis[alpha][:n_particles]) and (tb[3] in basis[alpha][:n_particles]):
        
            phi, b = bandp(tb[0], tb[1], tb[2], tb[3], n_particles, list(basis[alpha][:n_particles]))
            phi2, b2 = adadaa(tb[0], tb[1], tb[2], tb[3], n_particles, list(basis[alpha][:n_particles]))
           
            print("a^+_p a^+_q a_r a_s | Psi > = ", tb[0], " ", tb[1], " ", tb[2], " ", tb[3], " * ", basis[alpha][:n_particles])
            print("Old result = new result ? -> ", phi, " == ", phi2, "?\t", b, " == ", b2, "?")

            if phi != phi2:
                print("Failure!: phi != phi2!")
                break
                
            if (b != b2).all():
                print("Failure!: b != b2!")
                break
            
            if phi == 0:
                continue
            else:
                for beta in range(basis_size):                    
                    if (basis[beta][:n_particles] == b).all():
                        H[alpha][beta] += phi*tb[4]*mass_factor
                        H[beta][alpha] = H[alpha][beta]
                        break

for alpha in range(basis_size):
    spme = 0.

    for i in range(n_particles):
        spme += obme[int(basis[alpha][i])-1][4]

    H[alpha][alpha] += spme
spme = 0.

CALC_STOP = time.time()

print("Calculation of Hamiltonian took ", CALC_STOP - CALC_START, "seconds")

np.savetxt(HAMILTONIAN_DIR + "Hamiltonian.txt", H, delimiter = " ")

print()
print("hamiltonian.py: Saved Hamiltonian matrix to '", HAMILTONIAN_DIR, "Hamiltonian.txt'")
print()

STOP = time.time()

print("Total execution time: ", STOP - START, " seconds")

