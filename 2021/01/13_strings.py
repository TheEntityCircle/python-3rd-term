# Строки - это массивы символов
s = "abcdf"
print(s, type(s))

# Но отдельные символы - это тоже строки, просто длины 1
s0 = s[0]
print(s0, type(s0))

# Если нужен аналог char-а, есть отдельные функции
c = ord(s0)
print(c, type(c), chr(c))

# Для строк есть много полезных функций (здесь только малая часть)
data = "abc def gh"
print("String:", data)
print("Len:", len(data))
print("Upper:", data.upper())
print("Lower:", data.lower())
words = data.split(' ')
print(words)