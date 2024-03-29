"""
Есть в Python-е такая фундаментальная штука - tuples
"""

# На первый взгляд почти не отличается от списка, только скобочки круглые
# На них работает всё то, что было выше для списков
t = (1, 2, 3)
print(t)
print(t[0])
# Только писать в него нельзя, элементы тапла неизменяемые, так что закомментированная строка ниже упадёт
# t[0] = -1

# Присвоить повторно при этом можно, но только целиком
t = ('a', 'b', 'c')
print(t)

# Присовить один тапл другому тоже, конечно, можно
t2 = t
print(t2)

# Ещё можно пропускать скобки. Вот так тоже будет тапл:
tt = 1, 2, 3
print(tt)

# Дальше начинается лёгкая магия

# Можно распаковать содержимое тапла в несколько переменных
# Это часто удобно, но это ладно
a, b, c = tt
print(a, b)

# Но дальше можно написать такое:
b, a = a, b
# И они правда поменяются местами:
print(a, b)

"""
Последний пример работает на самом деле так:
- то, что справа от равно запаковывается во временный тапл,
- этот тапл присваивается таплу слева от равно,
- тапл слева от равно распаковыывается в именованные переменные.
А синтаксис выглядит лёгкой магией, потому что скобочки у таплов можно не писать.
"""