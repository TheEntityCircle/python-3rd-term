import numpy as np
cimport numpy as np

DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

cimport cython

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
def mult(np.ndarray[DTYPE_t, ndim=2] c, np.ndarray[DTYPE_t, ndim=2] a, np.ndarray[DTYPE_t, ndim=2] b):
    assert a.dtype == DTYPE and b.dtype == DTYPE and c.dtype == DTYPE
    # TODO: assert dims also

    cdef int size = a.shape[0]
    cdef int i, j, k

    print("Matrix size: ", size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = 0
            for k in range(0, size):
                c[i][j] += a[i][k] * b[k][j]

