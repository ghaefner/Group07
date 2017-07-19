# This script creates a "music" sample
# Notation as in B. A. Brown's MIDI script
# The "music" imitates the energy dependence of the nuclear level density in 
# the time-pattern of the notes
# The level density is approximated by the constant temperature model
# [1] A. Gilbert, A.G.W. Cameron, Can. Journal Phys. 43 (1965) 1446-1496

#import matplotlib.pyplot as plt
import numpy as np

# Calculates the total time
def total_time(music):
    tot_time = 0.
    
    for m in music:
        tot_time += m[0]
        
    return tot_time

# Determines the density of notes
def dens(u, e0, t, c):
    return c*np.exp((u - e0)/t)

# Time in seconds
tstart = 0.
tstop = 20.

# Pitch over 4 octaves
amin = 16.
amax = 64.
middlec = 40.

pitch_range = amax - amin
pitch_offset = amin

signal_duration = 0.2
initial_break = 0.8

pitch = [0.]
time = [0.]
delta_t_list = [signal_duration]

tot_t = 0.

i = 0.
while tot_t < 20.:
    delta_t = 1./dens(tot_t, 0., 15., 1./initial_break)
    delta_t_list.append(delta_t)
    time.append(tot_t + delta_t)
    pitch.append(i + 1)
    tot_t += delta_t
    time.append(tot_t + signal_duration)
    tot_t += signal_duration
    delta_t_list.append(signal_duration)
    pitch.append(0.)
    i += 1
    
# Adapt time of last element in delta_t_list to match exactly 20 seconds
delta_t_list[-1] -= time[-1] - 20.

pitch = np.array(pitch)

# Adapt pitch to fit the given minimum and maximum pitch
for i in range(np.shape(pitch)[0]):
    if pitch[i] != 0:
        pitch[i] = pitch[i]/33.*48. + 16.

# Write the "music", i.e. a list of [delta_t, pitch] tuples, to file
f = open("music.txt", 'w')

# Write choice of the instrument to file header.
f.write("i = 14\t!Xylophone\n") # 14 == Xylophone
f.write("\n")
for i in range(np.shape(time)[0]):
    f.write(str(delta_t_list[i]) + " " + str(pitch[i]) + "\n")
    
f.close()