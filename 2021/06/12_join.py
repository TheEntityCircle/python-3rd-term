import pandas as pd

# У нас есть данные из разных источников, которые хочется склеить по ключу
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})

print("=== left #1")
print(left)

print("=== right #1")
print(right)

# Это можно сделать вот так
print("=== merged #1")
m = pd.merge(left, right, on='key')
print(m)


# А если ключи не совпадают?
right2 = pd.DataFrame({'key': ['foo', 'baz'], 'rval': [4, 5]})
print("=== left #2")
print(left)

print("=== right #2")
print(right2)

print("=== merged #2")
print(pd.merge(left, right2, on='key'))


# А если в ключах сплошные повторы?
left3 = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right3 = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print("=== left #3")
print(left3)

print("=== right #3")
print(right3)

print("=== merged #3")
print(pd.merge(left3, right3, on='key'))


# Это примерно как join в базах данных.
# И у него есть примерно столь же много вариаций и ключей разной степени полезности.
