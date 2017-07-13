import numpy as np

BASIS_DIR = "output/"

def getSlaterEnergy(basisstate, orbitals):
    energy = 0.
    
    for b in basisstate:
        energy += orbitals[int(b) - 1][4]
        
    return energy

def getShellOccupation(basisstate, limits):
    occ = np.zeros(len(limits) - 1)
    
    for b in basisstate:
        flag = False
        for i in range(len(limits) - 1):
            if b >= limits[i] and b < limits[i+1]:
                occ[i] += 1
                flag = True
                break

        if flag == False:
            occ[len(occ) - 1] += 1

    return(occ)

def npnh(basisfile, orbitalfile, n):
    
    print()
    print("truncation.py: Truncating basis of Slater determinants in file'", basisfile, "'")
    print("Truncation mode: ", n, "p", n, "h")
    print()
    
    basis = np.loadtxt(basisfile)
    orbitals = np.loadtxt(orbitalfile)
    
    # Determine the limits of the single nj orbitals
    n_val = orbitals[0][1]
    j_val = orbitals[0][2]
    n_val_n = n_val
    j_val_n = j_val
    
    limits = [0]
    
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
    
    # Compare all the other basis states to the ground state and set up the truncated basis
    trunc = []
    shell_occupation_min = getShellOccupation(bmin[:-1], limits)
    
    for b in basis:
        shell_occupation = getShellOccupation(b[:-1], limits)
#        print(shell_occupation, " - ", shell_occupation_min, " = ", shell_occupation - shell_occupation_min, " (", 0.5*np.sum(np.abs(shell_occupation - shell_occupation_min)), ")")
        if 0.5*np.sum(np.abs(shell_occupation - shell_occupation_min)) <= n:
            trunc.append(b)
    
    np.savetxt("basis_truncated.txt", trunc, delimiter=" ")
    
    print()
    print("truncation.py: Saved truncated basis to '" + BASIS_DIR + "basis_truncated.txt'")
    print("The truncation reduced the basis size from ", np.shape(basis)[0], " to ", np.shape(trunc)[0])
    print()
  
def emax(basisfile, orbitalfile, emax):
    
    print()
    print("truncation.py: Truncating basis of Slater determinants in file'", basisfile, "'")
    print("Truncation mode: Max energy <= ", emax, " MeV (with regard to the ground state)")
    print()
    
    basis = np.loadtxt(basisfile)
    orbitals = np.loadtxt(orbitalfile)
    
    # Find the "ground state" of the Slater determinants, i.e. the one with the lowest sum
    # of single-particle energies
    
    emin = getSlaterEnergy(basis[0,:-1], orbitals)
    energy = emin
    
    for b in basis:
        energy = getSlaterEnergy(b[:-1], orbitals)
        if energy < emin:
            emin = energy
    
    # Compare all the other basis states to the ground state and set up the truncated basis
    trunc = []
    
    for b in basis:
        if getSlaterEnergy(b[:-1], orbitals) - emin <= emax:
            trunc.append(b)
    
    np.savetxt("basis_truncated.txt", trunc, delimiter=" ")
    
    print()
    print("truncation.py: Saved truncated basis to '" + BASIS_DIR + "basis_truncated.txt'")
    print("The truncation reduced the basis size from ", np.shape(basis)[0], " to ", np.shape(trunc)[0])
    print()

def occ(basisfile, orbitalfile, min_occ, max_occ):
    
    print()
    print("truncation.py: Truncating basis of Slater determinants in file'", basisfile, "'")
    print("Truncation mode: Limits for orbital occupation")
    print("\tMinimum occupation: ", min_occ)
    print("\tMaximum occupation: ", max_occ)
    print()
        
    basis = np.loadtxt(basisfile)
    orbitals = np.loadtxt(orbitalfile)

    if np.sum(min_occ) > np.shape(basis)[1]:
        print("Error: truncation.py: The minimum occupation numbers of the single-particle states prevent filling in ", np.shape(basis)[1], " particles")
        exit(0)
    if np.sum(max_occ) < np.shape(basis)[1]:
        print("Error: truncation.py: The maximum occupation numbers of the single-particle states prevent filling in ", np.shape(basis)[1], " particles")
        exit(0)
    
    # Determine the limits of the single nj orbitals
    n_val = orbitals[0][1]
    j_val = orbitals[0][2]
    n_val_n = n_val
    j_val_n = j_val
    
    limits = [0]
    
    for i in range(np.shape(orbitals)[0]):
        n_val_n = orbitals[i][1]
        j_val_n = orbitals[i][2]
        
        if n_val_n != n_val or j_val_n != j_val:
            limits.append(i + 1)
            n_val = n_val_n
            j_val = j_val_n
            
    limits.append(orbitals[-1][0])

    
    # Loop through the basis states, check if they satisfy the given limits, and if this is true, add them to the truncated basis
    trunc = []
    
    flag = True

    for b in basis:
        shell_occupation = getShellOccupation(b[:-1], limits)
#        print(shell_occupation, " - ", shell_occupation_min, " = ", shell_occupation - shell_occupation_min, " (", 0.5*np.sum(np.abs(shell_occupation - shell_occupation_min)), ")")
        for i in range(len(limits) - 1):
            if shell_occupation[i] < min_occ[i] or shell_occupation[i] > max_occ[i]:
                flag = False
                
        if flag == True:
            trunc.append(b)
            print(getShellOccupation(b[:-1], limits))
        flag = True
        
    np.savetxt("basis_truncated.txt", trunc, delimiter=" ")
    
    print()
    print("truncation.py: Saved truncated basis to '" + BASIS_DIR + "basis_truncated.txt'")
    print("The truncation reduced the basis size from ", np.shape(basis)[0], " to ", np.shape(trunc)[0])
    print()
    
def truncate(truncationfile, basisfile, orbitalfile):
    method = np.loadtxt(truncationfile)
    
    print(method)
    
    if method[0] == 0.:
        npnh(basisfile, orbitalfile, method[1])
    
    if method[0] == 1.:
        emax(basisfile, orbitalfile, method[1])
        
    if method[0] == 2.:
        min_occ = []
        max_occ = []
        
        for i in range(1, len(method) - 1, 2):
            min_occ.append(method[i])
            max_occ.append(method[i + 1])
        
        occ(basisfile, orbitalfile, min_occ, max_occ)
        
        
#truncate("truncation/truncation_minmax.txt", "output/basis.txt", "space/sd.sp")