from random import random
import numpy as np
import time

# Возьмём NumPy-ные массивы для хранения данных.
# Все операции выполняются "руками". Это *ОЧЕНЬ* медленно - см. соответственную лекцию.
# Но нам это нужно как пример нагруженного участка кода, который (якобы) не укладывается в NumPy-ные методы.

N = 128

def mult(c, a, b):
    size = len(c)
    print("Matrix size", size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = 0
            for k in range(0, size):
                c[i][j] += a[i][k]*b[k][j]


if __name__ == '__main__':
    a = np.random.rand(N, N)
    b = np.random.rand(N, N)
    c = np.zeros((N, N))

    start_time = time.time()
    mult(c, a, b)
    elapsed_time = time.time() - start_time

    print(elapsed_time)
