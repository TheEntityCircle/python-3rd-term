"""
Исключения в Python-е есть, как же без них
"""

# Например, если этой попытке чтения входа скормить на вход не int-ы, а строки, то она упадёт
# Ошибка будет в духе: ValueError: invalid literal for int() ...
a = [int(s) for s in input().split()]

# Хотелось бы в таких случаях не умирать на месте, а иметь шанс обработать ошибку.
# Для этого нужен try и ловля исключений, как и в других языках.
# Если попробовать скормить на вход строки вместо int-ов вот такой конструкции, то она не упадёт,
# а попадёт в блок except, в котором можно написать свою логику.
try:
    a = [int(s) for s in input().split()]
except:
    pass # pass - служебная конструкция со смыслом "этот блок пустой, и это так задумано"
