import numpy as np

energies = np.loadtxt("eigenspace/eigenvalues.txt")

f = open("eigenspace/O-18.txt","w")

f.write(" Energy levels for oxygen 18 ")
f.write("\n")
f.write("Index Energy   Ex [MeV]")
f.write("\n")

E0 = min(energies)

for i in range(len(energies)):
	f.write(str(i) + "     " + str(round(energies[i],4)) + "   " + str(round((energies[i]-E0),4)))
	f.write("\n")
	
f.close()
