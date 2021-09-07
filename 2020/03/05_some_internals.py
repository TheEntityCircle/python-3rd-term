# Немного изнанки и служебных методов

class A:
    def __init__(self, v=42, t="asd"):
        self.data = v
        self.tag = t

    # Это позволяет задать, как будет виден объект глазами, например, в отладчике и консоли
    def __repr__(self):
        return "class A: %d" % self.data

    # А это - во что превратится объект при явном кастовании в строку
    # Если не задать __str__, для этой цели тоже будет использоваться __repr__
    def __str__(self):
        return "Instance of class A with %d inside" % self.data

    # Как проверять экземпляры на равенство
    # Это примерно перегрузка оператора ==
    def __eq__(self, other):
        return self.data == other.data and self.tag == other.tag

    # Ещё есть перегрузка
    # __ne__(self, other)
    # __lt__(self, other)
    # __le__(self, other)
    # __gt__(self, other)
    # __ge__(self, other)

    # И математику при большом желании тоже можно перегружать
    # __add__(self, other)
    # __mul__(self, other)
    # __sub__(self, other)
    # __mod__(self, other)
    # __truediv__(self, other)

    # Есть ещё более нишевые служебные методы в духе индексации, получения размера и т.д.

    # Немного особняком стоит __hash__
    # Он вычисляет хэш для экземпляра класса.
    # А этот хэш используется, когда класс должен быть сложен в set или оказаться ключом в dict-е.
    # (Под капотом set и dict реализованы как хэш-таблицы. Так что нужен хэш для объекта, чтобы его туда сложить.)
    def __hash__(self):
        # Здесь сейчас сказано, что хэш считается по таплу, в который включены два поля.
        # То есть хэши для двух экземпляров класса будут разные, если значение хотя бы одно из полей у них разное.
        # Хэши совпадут, если значения обоих полей совпадёт.
        # Логически это как будто очень близко к __eq__, но технически используется для совсем других целей.
        return hash((self.data, self.tag))


# Попробуйте запускать, меняя __repr__ и __str__
a = A()
print(a)

# А это попробуйте запускать, меняя __eq__ и значения полей классов
b = A(42, "zxc")
print(a == b)