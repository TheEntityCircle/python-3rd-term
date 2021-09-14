"""
Аналогичный comprehension можно использовать и для set-ов и dict-ов
# ВНИМАНИЕ! Контейнеры set и dict в Python не упорядоченные! Здесь можно получить некоторые сюрпризы.
"""

# Попробуйте запустить это и ввести повторные числа
a = set(int(s) for s in input().split())
print(a)

# Этот пример довольно искусственный. Но это dict comprehension.
d = {i: i**3 for i in range(5)}
print(d)