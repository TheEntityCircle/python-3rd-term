from random import random
import time

# Полностью аналогичный код - умножение матриц, написанное на "чистом Python-е".
# Все операции выполняются "руками", матрицы хранятся в list-ах list-ов.
# Работает, разумеется, сильно медленнее, чем на C++.
# Насколько сильно - стоит измерить.

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
    a = [[0] * N for i in range(N)]
    b = [[0] * N for i in range(N)]
    c = [[0] * N for i in range(N)]

    init_matrix(a)
    init_matrix(b)

    start_time = time.time()
    mult(c, a, b)
    elapsed_time = time.time() - start_time

    print(elapsed_time)
