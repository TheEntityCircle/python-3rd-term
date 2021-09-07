# Были у нас переменные
a = 1
b = -1
c = 0

# Сделаем из них массив
data = [a, b, c]

# Поиспользуем немного встроенных функций
print("Max: %d" % max(data))
print("Min: %d" % min(data))

print("Sorted data:")
print(sorted(data))

print("Reverse sorted data:")
print(sorted(data, reverse=True))