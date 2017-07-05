import numpy as np

ID = 0
N = 1
J = 2
M = 3
T = 4

N_PARTICLES = 3

sp = np.loadtxt("./space/d5_2.txt")

n_states = np.shape(sp)[0]
n_shells = sp[n_states - 1][N]

print("Number of SP states: ", n_states)
print("Number of shells: ", n_shells)
print()

basis = []
n_particle_state = [0]*N_PARTICLES
for i in range(N_PARTICLES):
    n_particle_state[i] = i + 1
max_state = [0]*N_PARTICLES
for i in range(N_PARTICLES):
    max_state[N_PARTICLES - i - 1] = n_states - i

# Case N_PARTICLES == 1 has to be treated separately
if N_PARTICLES == 1:
    for i in range(n_states):
        basis.append([i + 1])
        
# Case N_PARTICLES == n_states has to be treated separately
elif N_PARTICLES == n_states:
    basis.append(max_state)


# Any case with N_PARTICLES > 1 && N_PARTICLES < n_states
else:
    while n_particle_state != max_state:
        basis.append(n_particle_state[:])
    
#        if n_particle_state[N_PARTICLES - 1] > 20:
#            break

        for i in range(N_PARTICLES - 1):
            if n_particle_state[N_PARTICLES - i - 1] != max_state[N_PARTICLES - i - 1]:
                n_particle_state[N_PARTICLES - i - 1] += 1
                break
        
            elif n_particle_state[N_PARTICLES - i - 1] == max_state[N_PARTICLES - i -1]:
                if n_particle_state[N_PARTICLES - i - 2] != max_state[N_PARTICLES - i - 2]:
                    n_particle_state[N_PARTICLES - i - 2] += 1
                    for j in range(i + 1):
                        n_particle_state[N_PARTICLES - (i - j) - 1] = n_particle_state[N_PARTICLES - (i - j) - 2] + 1
                    break
                else:
                    continue

        if n_particle_state == max_state:
            basis.append(n_particle_state[:])
            break

# Print basis states with positive M and create a list of M-values
M_values = []

for b in basis:
    MJ = 0.
    for i in range(N_PARTICLES):
        MJ += sp[b[i] - 1][M]
    
    if MJ >= 0.:
        for i in range(N_PARTICLES):
            print(b[i], "\t", end='')
    
        print("M = ", MJ)
        
        M_values.append(MJ)
        
print(M_values)
print(M_values.count(5.))

