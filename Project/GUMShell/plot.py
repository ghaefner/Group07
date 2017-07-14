import matplotlib.pyplot as plt
import numpy as np

n_basis_states = 924

npnh = [[1, 37, 13.78], [2, 262, 112.18], [3, 662, 328.87], [4, 887, 467.48], [5, 923, 485.45], [6, 924, 488.80]]
npnh_data = []

plt.xlabel("# basis states")
plt.ylabel("time / s")

x = []
y = []
for n in npnh:
    x.append(n[1])
    y.append(n[2])
plt.plot(x, y, "o", color="black")

npnh_values = [1, 2, 3, 4, 5, 6]
for v in npnh_values:
    npnh_calc = np.loadtxt("eigenspace/eigenvalues_npnh_" + str(v) + ".txt")
    npnh_calc = np.sort(np.unique(npnh_calc))
    npnh_calc = npnh_calc - np.min(npnh_calc)
    npnh_data.append(npnh_calc)

#plt.xlabel("# basis states")
#plt.ylabel("energy / MeV")

N_STATES = 30

#for i in range(len(npnh_data)):
#    for j in range(N_STATES):
#        if j > len(npnh_data[i]) - 1:
#            continue
#        plt.scatter([i + 1, i + 1.5], [npnh_data[i][j], npnh_data[i][j]], color="black")

#for i in range(len(npnh_data)):
#    if len(npnh_data[i]) < N_STATES:
#        plt.scatter(np.ones(len(npnh_data))*npnh[i][1], npnh_data[i][0:len(npnh_data)], color="orange")
#    else:
#        plt.scatter(np.ones(N_STATES)*npnh[i][1], npnh_data[i][0:N_STATES], color="orange")
    
emax = [[2., 28, 9.96], [4., 28, 9.86], [6., 28, 9.59], [8., 252., 107.07], [10., 252., 98.75], [15., 672., 346.93], [20., 896., 469.17]]
emax_data = []

emax_values = [2, 4, 6, 8, 10, 15, 20]
for v in emax_values:
    emax_calc = np.loadtxt("eigenspace/eigenvalues_emax_" + str(v) + ".txt")
    emax_calc = np.sort(np.unique(emax_calc))
    emax_calc = emax_calc - np.min(emax_calc)
    emax_data.append(emax_calc)

#for i in range(len(emax_data)):
#    for j in range(N_STATES):
#        if j > len(emax_data[i]) - 1:
#            continue
#        plt.plot([i + 1, i + 1.5],  [emax_data[i][j], emax_data[i][j]], color="black")

#for i in range(len(emax_data)):
#    if len(emax_data[i]) < N_STATES:
#        plt.scatter(np.ones(len(emax_data))*emax[i][1], emax_data[i][0:len(emax_data)], color="green")
#    else:
#        plt.scatter(np.ones(N_STATES)*emax[i][1], emax_data[i][0:N_STATES], color="green")
        
#for i in range(N_STATES):
#    plt.plot([0., n_basis_states], [npnh_data[-1][i], npnh_data[-1][i]], "--", color="black")
    
mcsm = [[0.4, 365, 151.00], [0.5, 433, 185.92], [0.8, 726, 354.62], [0.9, 827, 422.59], [0.95, 875, 480.]]
mcsm_data = []

mcsm_values = [40, 50, 80, 90, 95]
for v in mcsm_values:
    mcsm_calc = np.loadtxt("eigenspace/eigenvalues_mcsm_" + str(v) + ".txt")
    mcsm_calc = np.sort(np.unique(mcsm_calc))
    mcsm_calc = mcsm_calc - np.min(mcsm_calc)
    mcsm_data.append(mcsm_calc)
    
#for i in range(len(mcsm_data)):
#    if len(mcsm_data[i]) < N_STATES:
#        plt.scatter(np.ones(len(mcsm_data))*mcsm[i][1], mcsm_data[i][0:len(mcsm_data)], color="red")
#    else:
#        plt.scatter(np.ones(N_STATES)*mcsm[i][1], mcsm_data[i][0:N_STATES], color="red")