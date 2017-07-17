import numpy as np

data = np.loadtxt("o_220b.dei", skiprows = 7,usecols = (1,4,9,7,2))

transitions = [data[:,1],data[:,2],data[:,3],data[:,0],data[:,4]] #Jf,nf,l,m,Ji

BE2_sum = 0.
BE2_sum_WU = 0.

factor = 3.66196786

for i in range(len(transitions[0])):
	if transitions[0][i] == 2 and transitions[1][i] == 1 and transitions[2][i] == 2:
		BE2_sum += (((transitions[3][i])**2)/(2*transitions[4][i] + 1))

BE2_sum_WU = BE2 / factor	
	
print(str(BE2) + " e^2fm^4")
print(str(BE2_WU) + "  W.u.")
