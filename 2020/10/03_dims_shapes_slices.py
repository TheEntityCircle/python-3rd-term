import numpy as np

a = np.array([(1,2,3),(4,5,6)], dtype=np.float64)

print(a)
print("Dims:", a.ndim)
print("Shape:", a.shape)

a = a.reshape(3, 2)

print(a)
print("Dims:", a.ndim)
print("Shape:", a.shape)

print("Slice 1: ", a[0:,0])
print("Slice 2: ", a[1,:])
print("Slice 3: ", a.reshape(1,6)[0,4:])
