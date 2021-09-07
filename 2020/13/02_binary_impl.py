from random import random
import numpy as np
import time

import cython_mult
import cpp_mult

# Возьмём NumPy-ные массивы для хранения данных.
# Все операции выполняются "руками".
# Но теперь они написаны с использованием Cython или C++.

N = 128

def init_matrix(m):
    size = len(m)
    for i in range(0, size):
        for j in range(0, size):
            m[i][j] = random()


def print_matrix(m):
    for row in m:
        print(row)


if __name__ == '__main__':
    a = np.zeros((N, N))
    b = np.zeros((N, N))
    c = np.zeros((N, N))

    init_matrix(a)
    init_matrix(b)

    start_time = time.time()
    cython_mult.mult(c, a, b)
    elapsed_time = time.time() - start_time

    print("Cython:", elapsed_time)

    start_time = time.time()
    cpp_mult.mult(c, a, b)
    elapsed_time = time.time() - start_time

    print("C++:", elapsed_time)
