from random import random
import numpy as np
import time

# Возьмём NumPy-ные массивы для хранения данных.
# Все операции выполняются "руками". Это *ОЧЕНЬ* медленно - см. стрим 09.
# Но нам это нужно как пример нагруженного участка кода, который (якобы) не укладывается в NumPy-ные методы.

N = 128

def init_matrix(m):
    size = len(m)
    for i in range(0, size):
        for j in range(0, size):
            m[i][j] = random()


def print_matrix(m):
    for row in m:
        print(row)


def mult(c, a, b):
    size = len(c)
    print("Matrix size", size)
    for i in range(0, size):
        for j in range(0, size):
            c[i][j] = 0
            for k in range(0, size):
                c[i][j] += a[i][k]*b[k][j]


if __name__ == '__main__':
    a = np.zeros((N, N))
    b = np.zeros((N, N))
    c = np.zeros((N, N))

    init_matrix(a)
    init_matrix(b)

    start_time = time.time()
    mult(c, a, b)
    elapsed_time = time.time() - start_time

    print(elapsed_time)
