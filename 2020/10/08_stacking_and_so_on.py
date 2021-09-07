import numpy as np

a = np.array([(1,2,3),(4,5,6)], dtype=np.float64)
b = np.array([(10,20,30),(40,50,60)], dtype=np.float64)

print(np.hstack((a, b)))
print(np.vstack((a, b)))

print(np.hstack((a, b)).ravel())
print(np.vstack((a, b)).ravel())

print("==============")
print(np.tile(a, (2, 3)))

print("==============")
print(np.repeat(a, 2, axis=0))
print(np.repeat(a, 3, axis=1))
