import phase
import numpy as np

sd = np.array([1, 3, 9, 12], order='F')
#sd = np.array([1, 3, 9, 12])
b = phase.bandp(2, 8, 1, 12, 4, sd)

print(b[0])
print(np.shape(b))

for bb in b:
    print(bb, ", ", end="")

print()
