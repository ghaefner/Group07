import numpy as np
from matplotlib import pyplot as plt

data = np.loadtxt("o_220b.dei", skiprows = 7,usecols = (1,4,9,7,2,8))

transitions = [data[:,1],data[:,2],data[:,3],data[:,0],data[:,4],data[:,5]] #Jf,nf,l,m,Ji,nf

be2 = [[],[],[],[],[]] #Ji ni Jf nf BE2
bm1 = [[],[],[],[],[]] #Ji ni Jf nf BM1

be2_fac = 3.6619 #For W.u. 
#Get BE2
for i in range(len(transitions[0])):
	if transitions[2][i] == 2:
		be2[0].append(transitions[4][i])
		be2[1].append(transitions[5][i])
		be2[2].append(transitions[1][i])
		be2[3].append(transitions[2][i])
		
		BE = round((transitions[3][i]**2)/((2*transitions[4][i]+1)*be2_fac),5)
		
		be2[4].append(BE)
		
	if transitions[2][i] == 1:
		bm1[0].append(transitions[4][i])
		bm1[1].append(transitions[5][i])
		bm1[2].append(transitions[1][i])
		bm1[3].append(transitions[2][i])
		
		BM = round((transitions[3][i]**2)/(2*transitions[4][i]+1),5)		
		
		bm1[4].append(BM)
		
#Write into a file		
f = open("BE2_O22","w")
f2 = open("BM1_O22","w")
#Header
f.write("# J_i  n_i  J_f  n_f     BE2(W.u.)")
f.write("\n")
f2.write("# J_i  n_i  J_f  n_f     BM1(mu_N^2)")
f2.write("\n")

for i in range(len(be2[0])):
	for j in range(len(be2)):
		f.write(" " + str(be2[j][i]) + " ")
	f.write("\n")
	
for i in range(len(bm1[0])):
	for j in range(len(bm1)):
		f2.write(" " + str(bm1[j][i]) + " ")
	f2.write("\n")
	
f.close()
f2.close()

#Plots
be2_large = [[],[]]
be2_small = [[],[]]
for i in range(len(be2[0])):
	if be2[4][i] >= 1.0:
		be2_large[0].append(be2[0][i])
		be2_large[1].append(be2[4][i])
	if be2[4][i] <= 1.0:
		be2_small[0].append(be2[0][i])
		be2_small[1].append(be2[4][i])

bm1_large = [[],[]]
bm1_small = [[],[]]
for i in range(len(bm1[0])):
	if bm1[4][i] >= 0.5:
		bm1_large[0].append(bm1[0][i])
		bm1_large[1].append(bm1[4][i])
	if bm1[4][i] <= 0.5:
		bm1_small[0].append(bm1[0][i])
		bm1_small[1].append(bm1[4][i])



plt.figure(1)
plt.subplot(211)
plt.title('B(E2) and B(M1)-values for O-22')
plt.plot(be2_large[0],be2_large[1],'o',color='red')
plt.plot(be2_small[0],be2_small[1],'+',color='blue')
plt.legend(('BE2 > 1 W.u.','BE2 < 1 W.u.'),loc='upper right')
plt.xlabel('J_i')
plt.ylabel('B(E2) [W.u.]')
plt.subplot(212)
#plt.title('B(M1)-values for O-22')
plt.plot(bm1_large[0],bm1_large[1],'o',color='red')
plt.plot(bm1_small[0],bm1_small[1],'+',color='blue')
plt.legend(('BM1 > 0.5 mu_N^2','BM1 < 0.5 mu_N^2'),loc='upper right')
plt.xlabel('J_i')
plt.ylabel('B(M1) [mu_N^2]')
plt.show()


