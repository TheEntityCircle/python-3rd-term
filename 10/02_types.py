import numpy as np

a = np.array([(1,2,3),(4,5,6)])

print(a)
print(a.dtype)
print(a.itemsize)

a = np.array([(1,2,3),(4,5,6)], dtype=np.float64)

print(a)
print(a.dtype)
print(a.itemsize)