# Это функция, принимает аргумент n, возврашает значение n!
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n = 5
print("%d! = %d" % (n, fact(n)))