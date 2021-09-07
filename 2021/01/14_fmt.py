# Данные
name = "Alice"
age = 18

# Старый стиль
print("%s is %d" % (name, age))

# Новый стиль
print("{n} is {a}".format(n = name, a = age))

# Новейший стиль (f-strings, Python 3.6+)
print(f'{name} is {age}')

# Можно не только подстановку переменных, но и вычисление
a = 2
b = 3
print(f'{a} + {b} = {a + b}')