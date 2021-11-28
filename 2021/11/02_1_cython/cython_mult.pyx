import numpy as np
cimport numpy as np

DTYPE = np.float64

def mult(np.ndarray c, np.ndarray a, np.ndarray b):
    assert a.dtype == DTYPE and b.dtype == DTYPE and c.dtype == DTYPE
    # TODO: assert dims also

    cdef int size = a.shape[0]
    cdef int i, j, k

    print("Matrix size: ", size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = 0
            for k in range(0, size):
                c[i][j] += a[i][k]*b[k][j]

