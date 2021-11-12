import numpy as np
from scipy import linalg

a = np.array([[6, 1, 1],
              [4, -2, 5],
              [2, 8, 7]], dtype=np.float64)

print("A:")
print(a)
b = linalg.inv(a)
print("A^-1:")
print(b)
print("A * A^-1:")
print(a @ b)

eigvals, eigvecs = linalg.eig(a)
for i, eigval in enumerate(eigvals):
    print("================")
    print("eigval:", eigval)
    print("eigvec:", eigvecs[:,i])
    print("delta:", a.dot(eigvecs[:, i]) - eigval * eigvecs[:, i])
