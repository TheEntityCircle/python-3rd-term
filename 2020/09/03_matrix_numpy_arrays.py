from random import random
import numpy as np
import time

# А теперь возьмём NumPy-ные массивы для хранения данных. Они же должны быть быстрые.
# Все операции всё ещё выполняются "руками", так что чудес насчёт скорости не ждём.
# Но всё-таки должно же стать лучше.
# (Спойлер: не станет. Будет хуже, причём сильно. Насколько и почему - или тестировать и думать, или смотреть стрим.)

N = 256

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