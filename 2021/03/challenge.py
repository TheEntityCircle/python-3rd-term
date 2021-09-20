# Есть у нас вот такой класс
class MyClass:
    def __init__(self, a=0, b=0, c=0):
        self.a, self.b, self.c = a, b, c

    def __repr__(self):
        return "MyClass instance with values (%d; %d; %d)" % (self.a, self.b, self.c)

    # Хэш считается только по полю a
    def __hash__(self):
        return hash(self.a)


# То есть хэши вот этих объектов совпадут
z = MyClass(1, 2, 3)
q = MyClass(1, 8, 42)

# Попробуем сложить эти объекты в set (хэши совпадают)
s = set()
s.add(z)
s.add(q)

# Обойдём set и напечатаем его содержимое
for v in s:
    print(v)

# Запустите, посмотрите на вывод, объясните результат
