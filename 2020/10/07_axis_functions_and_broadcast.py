import numpy as np

a = np.array([(3,2,4),(4,1,6)], dtype=np.float64)

print(a)
print(a - a.min())
print("==============")
print(a.min(axis=0))
print(a.min(axis=1))
print(a.min(axis=1, keepdims=True))
print("==============")
print(a - a.min(axis=1, keepdims=True))
