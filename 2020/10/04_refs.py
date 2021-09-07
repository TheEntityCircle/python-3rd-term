import numpy as np

a = np.array([(1,2,3),(4,5,6)], dtype=np.float64)

b = a[1,1:]
b[0] = 42

print(a)