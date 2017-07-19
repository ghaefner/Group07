# Program to plot differences in charge radii for N and N-1 for each Isotopes

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


# plot sqrt(<r^2>(A,N)) - sqrt(<r^2>(A-1,N-1)) [fm]
# Load in data
data = np.loadtxt("BK_dN=1.dat")
n_data = np.shape(data)[0]

Z = data[:,0]
N = data[:,1]
#A = data[:,2]
dRMS = data[:,3]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot range
Z_min = 60
Z_max = 75

# 2D bar plot
for i in range (Z_min, Z_max+1, 1):
    n = 0
    for j in range(n_data):
        if ( i == Z[j] ):
            n += 1
            ij_max = j
    ij_min = ij_max-n+1
    if ( ij_min <= ij_max ):
        ax.bar(N[ij_min:ij_max+1], dRMS[ij_min:ij_max+1], zs=i, zdir='y', alpha=0.8)

ax.set_xlabel('N')
ax.set_ylabel('Z')
ax.set_zlabel('delta RMS(Z,N_N-1) [fm]')

plt.show()



# # plot sqrt(<r^2>(A,N)) - sqrt(<r^2>(A-2,N-2)) [fm]
# # Load in data
# data = np.loadtxt("BK_dN=2.dat")
# n_data = np.shape(data)[0]
#
# Z = data[:,0]
# N = data[:,1]
# #A = data[:,2]
# dRMS = data[:,3]
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # plot range
# Z_min = 60
# Z_max = 75
#
# # 2D bar plot
# for i in range (Z_min, Z_max+1, 1):
#     n = 0
#     for j in range(n_data):
#         if ( i == Z[j] ):
#             n += 1
#             ij_max = j
#     ij_min = ij_max-n+1
#     if ( ij_min <= ij_max ):
#         ax.bar(N[ij_min:ij_max+1], dRMS[ij_min:ij_max+1], zs=i, zdir='y', alpha=0.8)
#
# ax.set_xlabel('N')
# ax.set_ylabel('Z')
# ax.set_zlabel('delta RMS(Z,N_N-2) [fm]')
#
# plt.show()



# # plot (<r^2>(A,N) - <r^2>(A-2,N-2))/(<r^2(LD;A)> - <r^2(LD;A-2)>)
# # <r^2>(LD;A) = 3/5 (1.2 * A**(1/3))**2 : assume homogenious spherical symmetric charge density
# # https://people.nscl.msu.edu/~brown/brown-all-papers/065-1984-jpg.10.1683-rms-charge-radii.pdf
# # Load in data
# data = np.loadtxt("BK_Alex.dat")
# n_data = np.shape(data)[0]
#
# Z = data[:,0]
# N = data[:,1]
# #A = data[:,2]
# dRMS = data[:,3]
#
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # plot range
# Z_min = 60
# Z_max = 75
#
# # 2D bar plot
# for i in range (Z_min, Z_max+1, 1):
#     n = 0
#     for j in range(n_data):
#         if ( i == Z[j] ):
#             n += 1
#             ij_max = j
#     ij_min = ij_max-n+1
#     if ( ij_min <= ij_max ):
#         ax.bar(N[ij_min:ij_max+1], dRMS[ij_min:ij_max+1], zs=i, zdir='y', alpha=0.8)
#
# ax.set_xlabel('N')
# ax.set_ylabel('Z')
# ax.set_zlabel('delta MS(Z,N_N-2) / delta LD(A_A-2)')
#
# plt.show()
