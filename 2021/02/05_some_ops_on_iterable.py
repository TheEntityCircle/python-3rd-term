"""
Разумеется, над iterable сущностями можно много всего выполнить.
Здесь некоторые характерные примеры.
"""

# Создадим set из символов строки.
# Просто потому что можем. Ну и для ещё одного примера кастов, конечно.
s = set("abcd")

# Просто for-ы уже были (примерно аналоги range for-ов в C++).
# А если iterable хочется обойти, имея не только значение, но и индекс, то можно использовать enumerate.
# (Ещё раз напомним, что set и dict в Python не упорядоченные!)
for index, value in enumerate(s):
    print(f'Value {index}: {value}')

# Если нужно проверить, есть ли элемент в коллекции (контейнер в терминах C++), то для этого используется in.
# Реализация этого in-а будет разная для разных коллекций. Время работы соответственное.
if 'q' in s:
    print("Set contains q")
else:
    print("Set does not contain q")

# Ещё раз проверим вхождение нескольких элементов в коллекцию.
# Просто ради ещё одной демки синтаксиса.
for v in list("az"):
    print(f'{v} in set: {v in s}')

