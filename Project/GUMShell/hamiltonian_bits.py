import numpy as np
import time

from phase_mod import adadaa

m1 = 0x55555555
m2 = 0x33333333
m4 = 0x0f0f0f0f
m8 = 0x00ff00ff
m16 = 0x0000ffff

def bit_count(x):
    x = (x & m1) + ((x >> 1) & m1)
    x = (x & m2) + ((x >> 2) & m2)
    x = (x & m4) + ((x >> 4) & m4)
    x = (x & m8) + ((x >> 8) & m8)
    x = (x & m16) + ((x >> 16) & m16)
    return x
    

ORBITAL_DIR = "space/"
HAMILTONIAN_DIR = "hamiltonian/"
BASIS_DIR = "basis/"
INTERACTION_DIR = "interaction/"

#def hamiltonian(basisfile, onebodyfile, twobodyfile, orbitals):

#print()
#print("hamiltonian.py: Calculating the Hamiltonian matrix with the following input:")
#print("\torbitals = ", ORBITAL_DIR + orbitals)
#print("\tbasis = ", BASIS_DIR + basisfile)
#print("\tonebody = ", INTERACTION_DIR + oneparticle)
#print("\ttwobody = ", INTERACTION_DIR + twoparticle)
#print()

basisfile = "basis_bit.npy"
onebodyfile = "sd_sp.int"
twobodyfile = "usdb_m.int"

# Basis of Slater determinants
basis = np.load(BASIS_DIR + basisfile)
basis2 = np.loadtxt(BASIS_DIR + "basis.txt")
n_basis_states = np.shape(basis)[0]
n_particles = bit_count(basis[0])
obme = np.loadtxt(INTERACTION_DIR + onebodyfile)
n_obme = np.shape(obme)[0]
tbme = np.loadtxt(INTERACTION_DIR + twobodyfile)
n_tbme = np.shape(tbme)[0]

anni_ob = np.array(2**(obme[:,0] - 1), dtype=np.int32)
anni_tb = np.array(2**(tbme[:,2] - 1) + 2**(tbme[:,3] - 1), dtype=np.int32)
crea = np.array(2**(tbme[:,0] - 1) + 2**(tbme[:,1] - 1), dtype=np.int32)

START = time.time()

H = np.zeros((n_basis_states, n_basis_states))

for i in range(n_basis_states):
    bb = basis[i]
    b2 = basis2[i]
#    print("Alpha =", bin(bb))
    for m in np.arange(n_tbme):
        b = bb
#        print("anni_tbhilator =", bin(anni_tb[m]))
#        if m == 50:
#            break
#        phase, beta2 = adadaa(tbme[m][0],tbme[m][1],tbme[m][2],tbme[m][3], n_particles, b2[0:4])

        if bit_count(b & anni_tb[m]) == 2:
            b -= anni_tb[m]
#            print("Alpha' =", bin(b))
#            print("Creator =", bin(crea[m]))
            if not b & crea[m]:
                b += crea[m]
#                print("Beta =", bin(b), ", ", phase, " * ", beta2)
                for j in range(n_basis_states):
                    if bit_count(b & basis[j]) == n_particles:
#                        print(bin(basis[i]), " --> ", bin(b), " --> ", bin(basis[j]))
                        H[i][j] += tbme[m][4]
#                        print("Added ", tbme[m][4], " at position [", i, ", ", j, "] ", tbme[m][0:4])
                        break

STOP = time.time()

print("Execution took", STOP - START, "seconds")
print(H)

# Convert the basis to integers
# basis = list(map(int, basis))
#basis = np.loadtxt("basis/basis.txt")
#basis_size = np.shape(basis)[0]
#
#for b in basis:
#    
#    H = np.zeros((basis_size, basis_size))
#
#    mass_factor = (18./(16.+n_particles))**(0.3)
#	
#    H = np.zeros((basis_size, basis_size))
#
#    for alpha in range(basis_size):
#        for tb in tbme:
#            if (tb[2] in basis[alpha][:n_particles]) and (tb[3] in basis[alpha][:n_particles]):
#            
#                phi, b = adadaa(tb[0], tb[1], tb[2], tb[3], n_particles, list(basis[alpha][:n_particles]))
#                
#                if phi == 0:
#                    continue
#                else:
#                    for beta in range(0, alpha + 1):
#                        if (basis[beta][:n_particles] == b).all():
#                            H[alpha][beta] += phi*tb[4]*mass_factor
#                            H[beta][alpha] = H[alpha][beta]
#                            break
#
#print(H)

#    for alpha in range(basis_size):
#        spe = 0.
#    
#        for i in range(n_particles):
#            spe += obme[int(basis[alpha][i])-1][4]
#    
#        H[alpha][alpha] += spe
#    spe = 0.
#    
#    np.savetxt(HAMILTONIAN_DIR + "Hamiltonian_bin.txt", H, delimiter = " ")
#
#    print()
#    print("hamiltonian.py: Saved Hamiltonian matrix to '", HAMILTONIAN_DIR, "Hamiltonian.txt'")
#    print()

#hamiltonian("basis_bit.npy", "sd_sp.int", "usdb_m.int", "sd_np.sp")
