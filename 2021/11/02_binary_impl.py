from random import random
import numpy as np
import time

import cython_mult
import cpp_mult

# Возьмём NumPy-ные массивы для хранения данных.
# Все операции выполняются "руками".
# Но теперь они написаны с использованием Cython или C++.

N = 128

if __name__ == '__main__':
    a = np.random.rand(N, N)
    b = np.random.rand(N, N)
    c = np.zeros((N, N))

    start_time = time.time()
    cython_mult.mult(c, a, b)
    elapsed_time = time.time() - start_time

    print("Cython:", elapsed_time)

    start_time = time.time()
    cpp_mult.mult(c, a, b)
    elapsed_time = time.time() - start_time

    print("C++:", elapsed_time)
