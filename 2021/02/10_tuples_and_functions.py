"""
Ещё на tuples работает такая особенность функций в Python-е
"""

# У нас есть функция, она принимает пару параметров (это ок),
# а потом она внезапно возвращает два значения через запятую (это как?)
def func(a, b):
    return a + b, a - b


# На самом деле функция возвращает тапл, который можно принять и распаковать
x, y = func(1, 2)
print(x)
print(y)

# Ну или не распаковать, а так и оставить таплом
q = func(1, 2)
print(q)

# Но если уж начали распаковывать, то делать это надо с умом
# Строчка ниже упадёт - нельзя распаковать 2 значения в 3
# i, j, k = func(1, 2)