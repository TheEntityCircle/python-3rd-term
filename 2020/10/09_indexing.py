import numpy as np

a = np.array([(1,2,3),(4,5,6)], dtype=np.float64)

print(a)
print(a[1][1])
print(a[[0, 1],[0, 2]])

a[[0, 1],[0, 1]] += 100
print(a)

mask = (a > 100)
print(mask)
print(a[mask])
print(a[mask].sum())
