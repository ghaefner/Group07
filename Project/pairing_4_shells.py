import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

H_DIM = 6 # Dimension of hamilton operator

# Parameter g from 2-body interaction between nucleon pairs
# < p + p - | V | q + q - > = -g
g_min = -2.
g_max = 2.
g_steps = 50

g_values = np.linspace(g_min, g_max, g_steps)
H = np.zeros((H_DIM, H_DIM))
level = np.zeros((H_DIM, g_steps))
counter = 0

for g in g_values:
    for i in range(H_DIM):
        for j in range(H_DIM):
            # Set all matrix elements to -g
            H[i][j] = -g
            
    # Add the single-particle energies in the diagonal matrix elements
    H[0][0] += 2.
    H[1][1] += 4.
    H[2][2] += 6.
    H[3][3] += 6.
    H[4][4] += 8.
    H[5][5] += 10.
    
    # Set certain two-body matrix elements to zero, since the two-body
    # interaction cannot link the basis states
    
    H[5][0] = 0.
    H[4][1] = 0.
    H[3][2] = 0.
    H[2][3] = 0.
    H[1][4] = 0.
    H[0][5] = 0.

    # Calculate eigensystem    
    evalues, evectors = np.linalg.eig(H)
    # Sort the eigenvalues. Apparently, np.linalg.eig imposes some random ordering. Try running without this line and be surprised
    evalues = np.sort(evalues)
    
    # Fill the array for plotting
    level[0][counter] = evalues[0]
    level[1][counter] = evalues[1]
    level[2][counter] = evalues[2]
    level[3][counter] = evalues[3]
    level[4][counter] = evalues[4]
    level[5][counter] = evalues[5]
   
    counter += 1
    
# Plot the resulting level scheme in dependence on g

plt.xlabel("g")
plt.ylabel("Energy levels")

for i in range(H_DIM):
    plt.plot(g_values, level[i,:])

print(H)

plt.show()
