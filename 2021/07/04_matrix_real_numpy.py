from random import random
import numpy as np
import time

# А теперь используем NumPy до конца.
# И вот теперь правда станет сильно лучше насчёт скорости работы.
# Насколько - можно измерить. Почему - вспоминаем обсуждение.

N = 256

def init_matrix(m):
    size = len(m)
    m[:] = np.random.rand(size, size)


def print_matrix(m):
    for row in m:
        print(row)


def mult(c, a, b):
    np.matmul(a, b, out=c)


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
