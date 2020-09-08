"""
Аналогичный comprehension можно использовать и для set-ов
"""

# Попробуйте запустить это и ввести повторные числа
a = set(int(s) for s in input().split())
print(a)