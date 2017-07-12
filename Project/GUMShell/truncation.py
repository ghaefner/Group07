import numpy as np

def getSlaterEnergy(basisstate, orbitals):
    energy = 0.
    
    for b in basisstate:
        energy += orbitals[int(b) - 1][4]
        
    return energy

def getShellOccupation(basisstate, limits):
    occ = np.zeros(len(limits))
    
    print(limits)
    
    for b in basisstate:
        flag = False
        print(b)
        for i in range(len(limits)):
            print(b, ", ", limits[i])
            if b >= limits[i]:
                occ[i] += 1
                flag = True
                break
            
        if flag == False:
            occ[i] += 1
    
    return(occ)

def npnh(basisfile, orbitalfile, n):
    basis = np.loadtxt(basisfile)
    orbitals = np.loadtxt(orbitalfile)
    
    # Determine the limits of the single nj orbitals
    n_val = orbitals[0][1]
    j_val = orbitals[0][2]
    n_val_n = n_val
    j_val_n = j_val
    
    limits = []
    
    for i in range(np.shape(orbitals)[0]):
        n_val_n = orbitals[i][1]
        j_val_n = orbitals[i][2]
        
        if n_val_n != n_val or j_val_n != j_val:
            limits.append(i + 1)
            n_val = n_val_n
            j_val = j_val_n
            
    limits.append(orbitals[-1][0])
    
    # Find the "ground state" of the Slater determinants, i.e. the one with the lowest sum
    # of single-particle energies
    
    emin = getSlaterEnergy(basis[0,:-1], orbitals)
    energy = emin
    bmin = basis[0]
    
    for b in basis:
        energy = getSlaterEnergy(b[:-1], orbitals)
        if energy < emin:
            emin = energy
            bmin = b
    
#    print(emin)
#    print(bmin)
#    print(limits)
    
    print(getShellOccupation(bmin[:-1], limits))
    
    # Compare all the other basis states to the ground state and set up the truncated basis
    trunc = []
#    shell_occupation_min = getShellOccupation()
    shell_occupation = 1
    
    
    
basisfile = "output/basis.txt"
orbitalfile = "space/sd.sp"

orbitals = npnh(basisfile, orbitalfile, 1)