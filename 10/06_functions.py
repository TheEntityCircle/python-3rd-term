import numpy as np

a = np.array([(3,2,1),(4,5,6)], dtype=np.float64)

print(a)
#print("min:", a.min())
#print("max:", a.max())
#print("sum:", a.sum())
#print("mean:", a.mean())
#print("axis sum:", a.sum(axis=1))
#print("axis mean:", a.mean(axis=1, keepdims=True))

print("==============")
print(a.T)
col_one = a.T[:,0]
col_two = a.T[:,1]

print(col_one + col_two)
print(col_one * col_two)
print(np.dot(col_one, col_two))
print(col_one @ col_two)
