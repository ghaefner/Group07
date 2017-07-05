import numpy as np

import ex
import vec

print(ex.ex(3,4))
print(vec.vec(10, 3))
d = vec.vec(10,3)

for dd in d:
    print(dd)

print("The size of the array is ", np.shape(d))
